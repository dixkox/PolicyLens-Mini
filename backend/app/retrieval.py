import math
import re
from collections import Counter


STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by",
    "do", "does", "for", "from", "how", "i", "in", "is",
    "it", "of", "on", "or", "the", "to", "was", "what",
    "when", "where", "which", "who", "why", "with"
}


QUERY_EXPANSIONS = {
    "avoid": {"conflicts"},
    "approval": {"manager"},
    "approve": {"approval", "manager"},
    "outside": {"external"},
    "activities": {"employment", "consulting"},
    "benefits": {"eligible", "health", "wellness", "benefit"},
    "begin": {"beginning", "eligible"},
    "begins": {"beginning"},
    "start": {"beginning", "starting"},
    "submitted": {"submission"},
    "submit": {"submission"},
    "prohibited": {"not", "allowed", "bullying", "intimidation"},
}


UNSUPPORTED_QUESTION_RESPONSE = (
    "This question is not covered by the uploaded policy document"
)


def tokenize(text):
    words = re.findall(r"[a-z0-9]+", (text or "").lower())

    tokens = [
        word
        for word in words
        if word not in STOP_WORDS and len(word) >= 2
    ]

    expanded = list(tokens)

    for token in tokens:
        expanded.extend(QUERY_EXPANSIONS.get(token, set()))

    return expanded


def chunk_policy_text(text):
    text = (
        (text or "")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .strip()
    )

    if not text:
        return []

    chunks = []

    for line in text.split("\n"):
        line = re.sub(r"\s+", " ", line).strip()

        if not line:
            continue

        if line.startswith("#"):
            continue

        sentences = re.split(r"(?<=[.!?])\s+", line)

        for sentence in sentences:
            sentence = sentence.strip()

            if len(sentence) >= 20:
                chunks.append(sentence)

    return chunks


def extract_policy_sections(text):
    text = (
        (text or "")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .strip()
    )

    sections = []
    current_heading = None
    current_content = []

    def save_section():
        nonlocal current_heading, current_content

        if current_heading and current_content:
            content = " ".join(current_content).strip()

            if content:
                sections.append({
                    "heading": current_heading,
                    "content": content,
                })

        current_content = []

    for raw_line in text.split("\n"):
        line = re.sub(r"\s+", " ", raw_line).strip()

        if not line:
            continue

        if line.startswith("#"):
            save_section()
            current_heading = line.lstrip("#").strip()
            continue

        if re.fullmatch(
            r"\d+\.\s+.+(?:Policy|Conduct)",
            line,
            flags=re.IGNORECASE,
        ):
            save_section()
            current_heading = re.sub(
                r"^\d+\.\s*",
                "",
                line,
            ).strip()
            continue

        if current_heading:
            current_content.append(line)

    save_section()
    return sections


def calculate_idf(documents):
    total = len(documents)

    if total == 0:
        return {}

    frequencies = Counter()

    for document in documents:
        frequencies.update(set(document))

    return {
        term: math.log((total + 1) / (frequency + 1)) + 1.0
        for term, frequency in frequencies.items()
    }


def make_vector(tokens, idf):
    if not tokens:
        return {}

    counts = Counter(tokens)
    total = len(tokens)

    return {
        term: (count / total) * idf[term]
        for term, count in counts.items()
        if term in idf
    }


def similarity(vector_a, vector_b):
    if not vector_a or not vector_b:
        return 0.0

    common_terms = set(vector_a).intersection(vector_b)

    if not common_terms:
        return 0.0

    dot_product = sum(
        vector_a[term] * vector_b[term]
        for term in common_terms
    )

    magnitude_a = math.sqrt(
        sum(value * value for value in vector_a.values())
    )

    magnitude_b = math.sqrt(
        sum(value * value for value in vector_b.values())
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def retrieve_answer(question, text, threshold=0.20):
    question = (question or "").strip()
    text = (text or "").strip()

    if not question:
        return {
            "answer": "Please enter a question.",
            "score": 0.0,
            "matched": False,
        }

    if not text:
        return {
            "answer": "Please upload a policy PDF first.",
            "score": 0.0,
            "matched": False,
        }

    # Handle Code of Conduct explicitly because its title does not end in "Policy".
    if re.fullmatch(
        r"(?:what\s+is\s+)?(?:the\s+)?code\s+of\s+conduct[?.!]*",
        question.lower(),
    ):
        for section in extract_policy_sections(text):
            if section["heading"].strip().lower() == "code of conduct":
                return {
                    "answer": section["content"],
                    "score": 1.0,
                    "matched": True,
                }

        return {
            "answer": UNSUPPORTED_QUESTION_RESPONSE,
            "score": 0.0,
            "matched": False,
        }

    policy_name_match = re.fullmatch(
        r"(?:what\s+is\s+)?(?:the\s+)?(.+?)\s+policy[?.!]*",
        question.lower(),
    )

    if policy_name_match:
        requested_name = policy_name_match.group(1).strip()
        requested_tokens = set(tokenize(requested_name))
        sections = extract_policy_sections(text)

        best_section = None
        best_overlap = 0

        for section in sections:
            heading_tokens = set(tokenize(section["heading"]))
            heading_tokens.discard("policy")

            overlap = len(
                requested_tokens.intersection(heading_tokens)
            )

            if overlap > best_overlap:
                best_overlap = overlap
                best_section = section

        if (
            requested_tokens
            and best_section
            and best_overlap == len(requested_tokens)
        ):
            return {
                "answer": best_section["content"],
                "score": 1.0,
                "matched": True,
            }

        return {
            "answer": UNSUPPORTED_QUESTION_RESPONSE,
            "score": 0.0,
            "matched": False,
        }

    chunks = chunk_policy_text(text)

    if not chunks:
        return {
            "answer": "No readable policy information was found.",
            "score": 0.0,
            "matched": False,
        }

    documents = [tokenize(chunk) for chunk in chunks]
    question_tokens = tokenize(question)

    if not question_tokens:
        return {
            "answer": "Please enter a more specific policy question.",
            "score": 0.0,
            "matched": False,
        }

    idf = calculate_idf(documents + [question_tokens])
    question_vector = make_vector(question_tokens, idf)

    scores = []

    for document, chunk in zip(documents, chunks):
        document_vector = make_vector(document, idf)
        score = similarity(question_vector, document_vector)

        q = question.lower()
        c = chunk.lower()
        if (
            ("benefit" in q or "health" in q)
            and ("begin" in q or "start" in q)
            and ("benefit" in c or "health" in c)
            and ("begin" in c or "start" in c or "eligible" in c)
        ):
            score += 0.20

        scores.append(score)

    best_index = max(range(len(scores)), key=scores.__getitem__)
    best_score = scores[best_index]

    if best_score < threshold:
        return {
            "answer": UNSUPPORTED_QUESTION_RESPONSE,
            "score": round(best_score, 3),
            "matched": False,
        }

    return {
        "answer": chunks[best_index],
        "score": round(best_score, 3),
        "matched": True,
    }
