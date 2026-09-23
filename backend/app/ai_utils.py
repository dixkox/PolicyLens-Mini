def ask_gemini(question: str, text: str) -> str:
        try:
            question = question.lower()

            if "vacation" in question:
                for line in text.split("."):
                 if "vacation" in line.lower():
                     return line.strip()

            return text[:500]

        except Exception as e:
            return f"ERROR: {str(e)}"