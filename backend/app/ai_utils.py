import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)

def ask_gemini(question: str, text: str) -> str:
    try:
        messages = [
            {
                "role": "user",
                "content": f"""
Policy text:

{text}

Question:
{question}

Answer clearly and concisely.
"""
            }
        ]

        response = client.chat_completion(
            messages=messages,
            model="HuggingFaceH4/zephyr-7b-beta",
            max_tokens=200,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"ERROR: {str(e)}"