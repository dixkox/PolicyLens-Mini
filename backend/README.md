# PolicyLens-Mini Backend
 
The backend service for **PolicyLens-Mini**, a lightweight policy analysis application built with FastAPI.
 
## Features
 
- PDF upload and text extraction
- Natural-language policy questions
- Deterministic lexical retrieval
- TF-IDF weighting
- Cosine similarity scoring
- Relevance guardrails
- Unsupported-question rejection
- REST API endpoints
- FastAPI interactive API documentation
 
## Technology Stack
 
- Python
- FastAPI
- Uvicorn
- PyPDF
- TF-IDF-style lexical retrieval
- Cosine similarity
 
## API Endpoints
 
### Health Check
 
```text
GET /health
```
 
Example response:
 
```json
{
"status": "ok"
}
```
 
### Upload Policy PDF
 
```text
POST /upload
```
 
The endpoint accepts a PDF file, extracts its text, and returns:
 
```json
{
"filename": "policy.pdf",
"text": "Extracted policy text..."
}
```
 
### Ask a Policy Question
 
```text
POST /ask
```
 
The endpoint accepts:
 
```text
question
text
```
 
and returns:
 
```json
{
"answer": "Relevant policy information...",
"score": 0.5,
"matched": true
}
```
 
If sufficient supporting information is not found:
 
```json
{
"answer": "No relevant policy information was found.",
"score": 0.0,
"matched": false
}
```
 
## Retrieval Pipeline
 
```text
Policy Text
|
Sentence Chunking
|
Tokenization
|
TF-IDF Weighting
|
Cosine Similarity
|
Best Candidate
|
Relevance Guardrail
|
Answer or Rejection
```
 
Markdown headings are excluded from answer candidates.
 
The final retrieval implementation also uses limited deterministic query expansion to reduce selected vocabulary mismatches.
 
## Local Development
 
From the `backend` directory:
 
```powershell
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```
 
Health endpoint:
 
```text
http://127.0.0.1:8000/health
```
 
Interactive API documentation