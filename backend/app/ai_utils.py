import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)

def ask_gemini(question: str, text: str) -> str:
    try:
        prompt = f"""
Policy text:

{text}

Question:
{question}

Answer clearly and concisely.
"""

        response = client.text_generation(
            prompt,
            model="mistralai/Mistral-7B-Instruct-v0.2",
            max_new_tokens=200
        )

        return response

    except Exception as e:
        return f"ERROR: {str(e)}"