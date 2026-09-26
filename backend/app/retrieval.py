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

        # Headings identify sections but should never become answers.
        if line.startswith("#"):
            continue

        sentences = re.split(r"(?<=[.!?])\s+", line)

        for sentence in sentences:
            sentence = sentence.strip()

            if len(sentence) >= 20:
                chunks.append(sentence)

    return chunks


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

    for document in documents:
        document_vector = make_vector(document, idf)
        scores.append(
            similarity(question_vector, document_vector)
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
        "answer": chunks[best_index],
        "score": round(best_score, 3),
        "matched": True,
    }
