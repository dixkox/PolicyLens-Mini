import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)

def ask_gemini(question: str, text: str) -> str:
        try:

            sentences = text.split(".")
            for sentence in sentences:
                if "vacation" in sentence.lower():
                    return sentence.strip()

            return text[:500]

        except Exception as e:
            return f"ERROR: {str(e)}"