"use client";

import { useState } from "react";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

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

    try {
      const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Upload failed: ${response.status}`);
      }

      const data = await response.json();
      setPolicyText(data.text);
      setAnswer("");
    } catch (error) {
      console.error(error);
      setAnswer("Unable to upload the policy PDF.");
    }
  };

  const askQuestion = async () => {
    if (!question.trim()) {
      setAnswer("Please enter a question.");
      return;
    }

    if (!policyText.trim()) {
      setAnswer("Please upload a policy PDF first.");
      return;
    }

    try {
      const url =
        `${API_URL}/ask?question=${encodeURIComponent(question)}` +
        `&text=${encodeURIComponent(policyText)}`;

      const response = await fetch(url, {
        method: "POST",
      });

      if (!response.ok) {
        throw new Error(`Question request failed: ${response.status}`);
      }

      const data = await response.json();
      setAnswer(data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Unable to retrieve policy information.");
    }
  };

  return (
    <main
      style={{
        maxWidth: "900px",
        margin: "auto",
        padding: "40px",
      }}
    >
      <h1>PolicyLens</h1>

      <section style={{ marginBottom: "24px" }}>
        <h2>Upload Policy PDF</h2>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files ? e.target.files[0] : null)}
        />

        <button onClick={uploadPdf} style={{ marginLeft: "12px" }}>
          Upload
        </button>
      </section>

      <section style={{ marginBottom: "24px" }}>
        <h2>Ask a Question</h2>

        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask about the uploaded policy..."
          rows={4}
          style={{ width: "100%", boxSizing: "border-box", marginBottom: "12px" }}
        />

        <div>
          <button onClick={askQuestion}>Ask</button>
        </div>
      </section>

      {answer && (
        <section>
          <h2>Answer</h2>
          <p style={{ whiteSpace: "pre-wrap" }}>{answer}</p>
        </section>
      )}
    </main>
  );
}
