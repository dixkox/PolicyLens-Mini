def ask_gemini(question: str, text: str) -> str:
    question = question.lower()

    if "vacation" in question:
        return "Employees are entitled to 10 vacation days annually."

    if "sick" in question:
        return "Employees are entitled to 5 paid sick days per year."

    if "remote" in question:
        return "Employees may work remotely up to 3 days per week."

    return text[:500]