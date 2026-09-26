# PolicyLens-Mini
 
## MSSE Capstone Project
 
**PolicyLens-Mini** is a lightweight policy analysis web application developed for the Quantic Master of Science in Software Engineering Capstone Project.
 
The application allows users to upload a PDF policy document and ask natural-language questions about its contents.
 
PolicyLens-Mini uses deterministic lexical retrieval, TF-IDF-style weighting, cosine similarity, and a relevance guardrail to retrieve supporting policy information or reject questions when sufficient evidence is not available.
 
---
 
## Project Objectives
 
PolicyLens-Mini demonstrates:
 
- Full-stack software engineering
- PDF document ingestion
- Text extraction
- Natural-language policy retrieval
- Deterministic retrieval
- TF-IDF-style weighting
- Cosine similarity scoring
- Unsupported-question guardrails
- REST API development
- Frontend-backend integration
- Automated evaluation
- Git-based version control
- CI/CD practices
- Cloud deployment
- Agile software development
 
---
 
## Core Features
 
### PDF Policy Upload
 
Users can upload PDF policy documents.
 
The FastAPI backend extracts the document text and makes it available for policy questioning.
 
### Policy Question Answering
 
Users can ask natural-language questions about the uploaded policy.
 
The backend retrieves the policy sentence with the strongest lexical similarity to the question.
 
### Deterministic Retrieval
 
The retrieval pipeline performs:
 
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
 
This approach provides:
 
- Reproducible results
- Transparent scoring
- Lightweight execution
- No external LLM dependency for core retrieval
- Easier debugging and evaluation
 
### Relevance Guardrail
 
PolicyLens-Mini applies a relevance threshold of:
 
```text
0.20
```
 
If sufficient supporting information is found:
 
```json
{
"answer": "Employees accrue PTO at a rate of 1.5 days per month.",
"score": 0.446,
"matched": true
}
```
 
If sufficient evidence is not found:
 
```json
{
"answer": "No relevant policy information was found.",
"score": 0.0,
"matched": false
}
```
 
Markdown headings are excluded from answer candidates.
 
The retrieval system also uses limited deterministic query expansion to reduce selected vocabulary mismatches.
 
---
 
## Technology Stack
 
### Frontend
 
- Next.js
- React
- TypeScript
- CSS
 
### Backend
 
- Python
- FastAPI
- Uvicorn
- PyPDF
- Python Multipart
 
### Retrieval
 
- Sentence-level chunking
- Tokenization
- TF-IDF-style weighting
- Cosine similarity
- Deterministic query expansion
- Relevance guardrail
 
### Engineering and Deployment
 
- Git
- GitHub
- GitHub Actions
- Render
- Automated evaluation
- Agile development practices
 
---
 
## API
 
The FastAPI backend exposes:
 
```text
GET /health
POST /upload
POST /ask
```
 
### Health Check
 
```text
GET /health
```
 
Example:
 
```json
{
"status": "ok"
}
```
 
### Upload
 
```text
POST /upload
```
 
Accepts a PDF and returns the filename and extracted text.
 
### Ask
 
```text
POST /ask
```
 
Receives:
 
```text
question
text
```
 
and returns:
 
```text
answer
score
matched
```
 
---
 
## Architecture
 
PolicyLens-Mini follows a separated frontend/backend architecture.
 
```text
User
|
v
Next.js Frontend
|
| HTTP
v
FastAPI Backend
|
+--> PDF Extraction
|
+--> Sentence Chunking
|
+--> TF-IDF Retrieval
|
+--> Cosine Similarity
|
+--> Relevance Guardrail
|
+------ Match ------> Policy Answer
|
+---- No Match -----> Rejection
```
 
This separation keeps presentation, API routing, document processing, retrieval, and evaluation independently maintainable.
 
Additional architecture documentation:
 
```text
architecture/architecture_diagram.png
design-and-evaluation.md
```
 
---
 
## Repository Structure
 
```text
PolicyLens-Mini/
|
|-- app/
| `-- eval/
| `-- run_eval.py
|
|-- backend/
| |-- app/
| | |-- main.py
| | |-- routes.py
| | |-- retrieval.py
| | `-- pdf_utils.py
| |-- requirements.txt
| |-- render.yaml
| `-- README.md
|
|-- frontend/
| |-- app/
| | |-- page.tsx
| | |-- layout.tsx
| | `-- globals.css
| |-- public/
| `-- package.json
|
|-- architecture/
| `-- architecture_diagram.png
|
|-- evaluation/
| |-- eval_results.json
| |-- evaluation.md
| `-- evaluation_summary.md
|
|-- demo/
| |-- screenshots/
| |-- demo_script.md
| `-- demo_steps.md
|
|-- data/
| |-- policies/
| `-- raw/
|
|-- ai-tooling.md
|-- design-and-evaluation.md
|-- evaluation_set.md
`-- README.md
```
 
---
 
# Local Development
 
## Clone the Repository
 
```powershell
git clone https://github.com/dixkox/PolicyLens-Mini.git
cd PolicyLens-Mini
```
 
## Backend
 
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
 
Health check:
 
```text
http://127.0.0.1:8000/health
```
 
Interactive API documentation:
 
```text
http://127.0.0.1:8000/docs
```
 
## Frontend
 
Open another terminal:
 
```powershell
cd frontend
npm install
npm run dev
```
 
Frontend:
 
```text
http://localhost:3000
```
 
---
 
# Testing and Evaluation
 
PolicyLens-Mini includes a reproducible automated evaluation suite.
 
The evaluator is located at:
 
```text
app/eval/run_eval.py
```
 
The authoritative results are stored in:
 
```text
evaluation/eval_results.json
```
 
The controlled evaluation contains:
 
```text
20 test cases
4 policy documents
```
 
The policies used are:
 
- Paid Time Off
- Information Security
- Remote Work
- Code of Conduct
 
The evaluation contains both supported questions and intentionally unsupported questions.
 
---
 
## Baseline Evaluation
 
The initial evaluation produced:
 
```text
Correct: 15/20
Accuracy: 75.00%
```
 
Failures included:
 
- Policy headings returned as answers
- Unsupported questions incorrectly matched
- Vocabulary mismatch
- Incorrect selection between related policy sentences
 
---
 
## Retrieval Improvements
 
Evaluation findings led to several backend improvements:
 
- Markdown headings excluded from answers
- Relevance threshold increased from `0.10` to `0.20`
- Limited deterministic query expansion added
- Unsupported-question rejection improved
 
The same 20 cases were