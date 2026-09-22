import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(question: str, text: str) -> str:
    try:
        prompt = f"""
You are an AI policy assistant.

Here is the policy text:

{text}

Question: {question}

Provide a clear, concise answer.
"""

        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"ERROR: {str(e)}"