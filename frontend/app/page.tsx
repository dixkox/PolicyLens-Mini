"use client";

import { useState } from "react";

  export default function Home() {
    const [file, setFile] = useState<File | null>(null);
    const [policyText, setPolicyText] = useState("");
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");

    const uploadPdf = async () => {
      if (!file) {
        alert("Please select a PDF file.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(
      "https://policylens-mini.onrender.com/upload",
      {
        method: "POST",
        body: formData,
      }
    );

    const data = await response.json();
    setPolicyText(data.text);
  };

  const askQuestion = async () => {
    const response = await fetch(
      `https://policylens-mini.onrender.com/ask?question=${encodeURIComponent(question
      )}&text=${encodeURIComponent(policyText)}`,
      {
        method: "POST",
      }
    );

    const data = await response.json();
    setAnswer(data.answer);
  };

  return (
    <main style={{ maxWidth: "900px", margin: "auto", padding: "40px" }}>
      <h1>PolicyLens</h1>

      <h2>Upload Policy PDF</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) =>
          setFile(e.target.files ? e.target.files[0] : null)
        }
        />

        <button onClick={uploadPdf}>
          Upload PDF
        </button>

        <h2>Extracted Policy Text</h2>

        <textarea
          value={policyText}
          readOnly
          rows={12}
          style={{ width: "100%" }}
        />

        <h2>Ask a Question</h2>

        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="How many vacation days are employees entitled to?"
          style={{
            width: "100%",
            padding: "10px",
          }}
        />



        <br />
        <br />

        <button onClick={askQuestion}>
          Ask Question
        </button>

        <h2>Answer</h2>

        <div
          style={{
          padding: "15px",
          border: "1px solid #ccc",
          borderRadius: "8px",
        }}
      >
        {answer}
      </div>
    </main>
  );
}