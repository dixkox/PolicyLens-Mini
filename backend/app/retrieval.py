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
    "outside": {"external"},
    "activities": {"employment", "consulting"},
}


def normalize_text(text):
    return re.sub(r"\s+", " ", text or "").strip()


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


def is_policy_heading(line):
    line = normalize_text(line)

    if not line:
        return False

    # Markdown heading
    if line.startswith("#"):
        return True

    # PDF headings such as:
    # 1. Anti-Harassment Policy
    # 14. Information Security Policy
    if re.fullmatch(
        r"\d+\.\s+.+(?:Policy|Conduct)",
        line,
        flags=re.IGNORECASE,
    ):
        return True

    return False


def extract_sections(text):
    """
    Returns:
    [
    {
    "heading": "Anti-Harassment Policy",
    "sentences": [...]
    }
    ]
    """

    text = (
        (text or "")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .strip()
    )

    sections = []
    current_heading = ""
    current_sentences = []

    def save_section():
        nonlocal current_heading, current_sentences

        if current_sentences:
            sections.append({
                "heading": current_heading,
                "sentences": current_sentences.copy(),
            })

        current_sentences = []

    for raw_line in text.split("\n"):
        line = normalize_text(raw_line)

        if not line:
            continue

        if is_policy_heading(line):
            save_section()
            current_heading = re.sub(
                r"^\d+\.\s*",
                "",
                line.lstrip("#").strip(),
            )
            continue

        sentences = re.split(r"(?<=[.!?])\s+", line)

        for sentence in sentences:
            sentence = normalize_text(sentence)

            if len(sentence) >= 20:
                current_sentences.append(sentence)

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
    question = normalize_text(question)
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

    sections = extract_sections(text)

    if not sections:
        return {
            "answer": "No readable policy information was found.",
            "score": 0.0,
            "matched": False,
        }

    question_tokens = tokenize(question)

    if not question_tokens:
        return {
            "answer": "Please enter a more specific policy question.",
            "score": 0.0,
            "matched": False,
        }

    # ---------------------------------------------------------
    # POLICY-LEVEL QUESTION
    # Example:
    # "What is Anti-Harassment Policy?"
    #
    # Match the policy heading, but RETURN CONTENT UNDER IT.
    # ---------------------------------------------------------

    heading_documents = [
        tokenize(section["heading"])
        for section in sections
        if section["heading"]
    ]

    heading_sections = [
        section
        for section in sections
        if section["heading"]
    ]

    if heading_documents:
        heading_idf = calculate_idf(
            heading_documents + [question_tokens]
        )

        question_vector = make_vector(
            question_tokens,
            heading_idf,
        )

        heading_scores = []

        for document in heading_documents:
            heading_vector = make_vector(
                document,
                heading_idf,
            )

            heading_scores.append(
                similarity(
                    question_vector,
                    heading_vector,
                )
            )

        best_heading_index = max(
            range(len(heading_scores)),
            key=heading_scores.__getitem__,
        )

        best_heading_score = heading_scores[best_heading_index]
        selected_section = heading_sections[best_heading_index]

        # Strong heading match means the user is asking
        # about a particular policy.
        if (
            best_heading_score >= 0.60
            and selected_section["sentences"]
        ):
            answer = " ".join(selected_section["sentences"])
            return {
                "answer": answer,
                "score": round(best_heading_score, 3),
                "matched": True,
            }

    # ---------------------------------------------------------
    # FACT-LEVEL RETRIEVAL
    # ---------------------------------------------------------

    candidates = []

    for section in sections:
        for sentence in section["sentences"]:
            candidates.append(sentence)

    if not candidates:
        return {
            "answer": "No readable policy information was found.",
            "score": 0.0,
            "matched": False,
        }

    documents = [
        tokenize(candidate)
        for candidate in candidates
    ]

    idf = calculate_idf(
        documents + [question_tokens]
    )

    question_vector = make_vector(
        question_tokens,
        idf,
    )

    scores = []

    for document in documents:
        document_vector = make_vector(
            document,
            idf,
        )

        scores.append(
            similarity(
                question_vector,
                document_vector,
            )
        )

    best_index = max(
        range(len(scores)),
        key=scores.__getitem__,
    )

    best_score = scores[best_index]

    if best_score < threshold:
        return {
            "answer": "No relevant policy information was found.",
            "score": round(best_score, 3),
            "matched": False,
        }

    return {
        "answer": candidates[best_index],
        "score": round(best_score, 3),
        "matched": True,
    }
