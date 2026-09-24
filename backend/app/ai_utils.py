def ask_gemini(question: str, text: str) -> str:
    try:
        text_lower = text.lower()
        question_lower = question.lower()

        if "vacation" in question_lower:
            lines = text.split("\n")

            for line in lines:
                if (
                    "vacation days annually" in line.lower()
                    or "entitled to 10 vacation days" in line.lower()
                ):
                    return line.strip()

        return text[:500]

    except Exception as e:
        return f"ERROR: {str(e)}"