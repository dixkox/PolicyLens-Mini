# PolicyLens-Mini
 
## MSSE Capstone Project
 
**PolicyLens-Mini** is a lightweight policy analysis web application developed for the Quantic Master of Science in Software Engineering Capstone Project.
 
The application allows users to upload a PDF policy document and ask natural-language questions about its contents.
 
PolicyLens-Mini uses deterministic lexical retrieval, TF-IDF-style weighting, cosine similarity, deterministic query expansion, policy-section retrieval, and relevance guardrails to retrieve supporting policy information or reject unsupported questions.
 
---
 
## Live Demo
 
**Application:**
https://policylens-mini.vercel.app
 
**Sample Policy Handbook:**
demo/PolicyLens_Mini_Complete_Policy_Handbook.pdf
 
### Quick Demo
 
1. Download the sample policy handbook above.
2. Open the live PolicyLens-Mini application.
3. Select the downloaded PDF.
4. Click **Upload**.
5. Ask a supported question, for example:
- `What is Attendance Policy?`
- `What is Remote Work Policy?`
- `How quickly must security incidents be reported?`
6. Try an unsupported policy question:
- `What is Cook Policy?`
7. PolicyLens-Mini returns policy information when relevant evidence exists and rejects unsupported policy questions.
 
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
- Policy-section retrieval
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
 
The FastAPI backend extracts text from the uploaded document and makes the extracted content available for policy questioning.
 
### Policy Question Answering
 
Users can ask natural-language questions about the uploaded policy.
 
For factual questions, the backend retrieves relevant policy information using deterministic lexical similarity.
 
For explicit policy-name questions, PolicyLens-Mini can retrieve the complete content associated with the matching policy section.
 
For example:
 
```text
What is Attendance Policy?
```
 
returns the content of the Attendance Policy section.
 
### Unsupported Policy Detection
 
PolicyLens-Mini includes a guardrail for policy questions that are not supported by the uploaded document.
 
For example:
 
```text
What is Cook Policy?
```
 
returns:
 
```text
This question is not covered by the uploaded policy document.
```
 
This prevents unrelated policy names from being incorrectly matched to existing policy content.
 
---
## Deterministic Retrieval
 
The core factual retrieval pipeline performs:
 
```text
Policy Text
|
v
Sentence Chunking
|
v
Tokenization
|
v
TF-IDF-Style Weighting
|
v
Cosine Similarity
|
v
Best Candidate
|
v
Relevance Guardrail
|
+---- Match ----> Policy Answer
|
+-- No Match ---> Rejection
```
 
Explicit policy-name questions additionally use policy-section detection so that complete matching policy sections can be returned.
 
This approach provides:
 
- Reproducible results
- Transparent scoring
- Lightweight execution
- No external LLM dependency for core retrieval
- Predictable behavior
- Easier debugging and evaluation
 
---

## Relevance Guardrail
 
PolicyLens-Mini applies a factual retrieval relevance threshold of:
 
```text
0.20
```
 
When sufficient supporting information is found, an API response can contain:
 
```json
{
"answer": "Employees accrue PTO at a rate of 1.5 days per month.",
"score": 0.446,
"matched": true
}
```
 
When sufficient evidence is not found:
 
```json
{
"answer": "No relevant policy information was found.",
"score": 0.0,
"matched": false
}
```
 
For an explicit policy name that does not exist in the uploaded document:
 
```json
{
"answer": "This question is not covered by the uploaded policy document.",
"score": 0.0,
"matched": false
}
```
 
Markdown headings are excluded from normal factual answer candidates.
 
The retrieval system also uses limited deterministic query expansion to reduce selected vocabulary mismatches.
 
---

- Python
- FastAPI
- Uvicorn
- PyPDF
- Python Multipart
 
### Retrieval
 
- Sentence-level chunking
- Policy-section extraction
- Tokenization
- TF-IDF-style weighting
- Cosine similarity
- Deterministic query expansion
- Relevance guardrails
 
### Engineering and Deployment
 
- Git
- GitHub
- GitHub Actions
- Render
- Vercel
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
 
Example response:
 
```json
{
"status": "ok"
}
```
 
### Upload
 
```text
POST /upload
```
 
Accepts a PDF document and returns the filename and extracted text.
 
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
+--> Policy Section Detection
|
+--> Sentence Chunking
|
+--> TF-IDF-Style Retrieval
|
+--> Cosine Similarity
|
+--> Relevance Guardrail
|
+------ Match ------> Policy Answer
|
+---- No Match -----> Rejection
```
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
| |-- PolicyLens_Mini_Complete_Policy_Handbook.pdf
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

The evaluated policy categories are:
 
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
 
Observed failure categories included:
 
- Policy headings returned as answers
- Unsupported questions incorrectly matched
- Vocabulary mismatch
- Incorrect selection between related policy sentences
 
---
## Retrieval Improvements
 
Evaluation findings led to several backend improvements:
 
- Markdown headings excluded from factual answers
- Relevance threshold increased from `0.10` to `0.20`
- Limited deterministic query expansion added
- Unsupported-question rejection improved
- Explicit unsupported policy-name detection added
- Complete policy-section retrieval added for matching policy-name questions
 
---
 
## Final Evaluation
 
The same controlled 20-case evaluation suite was rerun after the retrieval improvements.
 
Final result:
 
```text
Correct: 20/20
Accuracy: 100.00%
```
The complete machine-readable results are available at:
 
```text
evaluation/eval_results.json
```
 
---
 
## Deployment
 
PolicyLens-Mini uses a separated cloud deployment architecture:
 
```text
Browser
|
v
Vercel
Next.js Frontend
|
v
Render
FastAPI Backend
```
 
### Production Application
 
https://policylens-mini.vercel.app
 
---
 
## Examiner Testing

For reproducible testing:
 
1. Open this repository.
2. Download:
`demo/PolicyLens_Mini_Complete_Policy_Handbook.pdf`
3. Open:
https://policylens-mini.vercel.app
4. Upload the handbook.
5. Ask:
`What is Attendance Policy?`
6. Confirm that PolicyLens returns the Attendance Policy content.
7. Ask:
`What is Cook Policy?`
8. Confirm that PolicyLens rejects the unsupported policy question.
 
---
 
## Supporting Documentation
 
Additional project documentation includes:
 
- `ai-tooling.md`
- `design-and-evaluation.md`
- `evaluation_set.md`
- `evaluation/evaluation.md`
- `evaluation/evaluation_summary.md`
- `demo/demo_script.md`
- `demo/demo_steps.md`
- `architecture/architecture_diagram.png`
 
---
 
## Conclusion
 
PolicyLens-Mini demonstrates an end-to-end software engineering workflow for deterministic policy-document retrieval.
 
The project integrates PDF ingestion, structured text processing, deterministic retrieval, relevance guardrails, automated evaluation, frontend-backend integration, Git-based development, and cloud deployment into a reproducible capstone application.