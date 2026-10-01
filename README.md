PolicyLens-Mini
MSSE Capstone Project
PolicyLens-Mini is a lightweight policy-document analysis web application developed for the Quantic Master of Science in Software Engineering Capstone Project.
The application allows users to upload a PDF policy document and ask natural-language questions about its contents. It uses deterministic lexical retrieval, TF-IDF-style weighting, cosine similarity, deterministic query expansion, policy-section retrieval, and relevance guardrails to retrieve supporting policy information or reject unsupported questions.
Live Application
Production application: https://policylens-mini.vercel.app
Sample policy handbook: `demo/PolicyLens_Mini_Complete_Policy_Handbook.pdf`
Quick Demo
Download `demo/PolicyLens_Mini_Complete_Policy_Handbook.pdf`.
Open the production application.
Select the downloaded PDF and upload it.
Ask supported questions such as:
`What is Attendance Policy?`
`What is Remote Work Policy?`
`How quickly must security incidents be reported?`
Ask an unsupported question:
`What is Cook Policy?`
Observe that PolicyLens-Mini returns policy information when supporting evidence exists and rejects unsupported policy questions.
Project Objectives
PolicyLens-Mini demonstrates:
Full-stack software engineering
PDF ingestion and text extraction
Natural-language policy retrieval
Deterministic information retrieval
TF-IDF-style weighting and cosine similarity
Policy-section retrieval
Unsupported-question guardrails
REST API development
Frontend-backend integration
Automated evaluation and regression testing
Git-based version control
CI/CD practices
Cloud deployment
Agile development across three sprints
Reproducible testing and technical documentation
Core Features
PDF Policy Upload
Users can upload PDF policy documents. The FastAPI backend extracts the document text and makes it available for policy questioning.
Policy Question Answering
For factual questions, the backend retrieves relevant policy information using deterministic lexical similarity. Explicit policy-name questions use policy-section detection so complete matching policy sections can be returned.
Example:
```text
What is Attendance Policy?
```
Unsupported Policy Detection
When an explicit policy question is not supported by the uploaded document, PolicyLens-Mini returns:
```text
This question is not covered by the uploaded policy document
```
This guardrail prevents unrelated or nonexistent policy names from being incorrectly matched to existing policy content.
Retrieval Pipeline
```text
Policy Text
    |
    v
Sentence Chunking / Policy Section Detection
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
The approach provides reproducible results, transparent scoring, lightweight execution, predictable behavior, and no external LLM dependency for core retrieval.
Relevance Guardrail
Factual retrieval uses a relevance threshold of `0.20`.
Example matched response:
```json
{
  "answer": "Employees accrue PTO at a rate of 1.5 days per month.",
  "score": 0.446,
  "matched": true
}
```
Example unsupported explicit policy response:
```json
{
  "answer": "This question is not covered by the uploaded policy document",
  "score": 0.0,
  "matched": false
}
```
Markdown headings are excluded from normal factual-answer candidates. Limited deterministic query expansion is used to reduce selected vocabulary mismatches.
Technology Stack
Frontend
Next.js
React
TypeScript
Vercel
Backend
Python
FastAPI
Uvicorn
PyPDF
Python Multipart
Render
Retrieval
Sentence-level chunking
Policy-section extraction
Tokenization
TF-IDF-style weighting
Cosine similarity
Deterministic query expansion
Relevance guardrails
Engineering and DevOps
Git
GitHub
GitHub Projects
GitHub Actions
Automated evaluation
Vercel deployment
Render deployment
Agile development practices
Agile Software Development
PolicyLens-Mini was developed iteratively across three development sprints.
Sprint 1: Core Architecture and Application
Defined the application architecture
Built the FastAPI backend
Built the Next.js frontend
Established the project structure
Implemented the initial document-processing workflow
Sprint 2: Retrieval Quality and Evaluation
Developed the automated evaluation workflow
Established controlled evaluation cases
Identified retrieval failures
Improved heading exclusion
Refined relevance filtering
Added deterministic query expansion
Improved unsupported-question handling
Controlled baseline evaluation:
```text
Correct: 15/20
Accuracy: 75.00%
```
Sprint 3: Production Readiness and Final Validation
Added explicit policy-name detection
Added complete policy-section retrieval
Strengthened unsupported-question guardrails
Performed regression validation
Finalized cloud deployment
Finalized architecture, testing, and evaluation documentation
Prepared examiner demonstration resources
Controlled final evaluation:
```text
Correct: 20/20
Accuracy: 100.00%
```
Final Regression Validation
Following final retrieval refinements, the comprehensive regression suite produced:
```text
Policy-name tests:          16/16 passed
Policy fact tests:          16/16 passed
Unsupported-question tests:  3/3 passed
Total:                      35/35 passed
```
Regression test:
`evaluation/test_all_policies.py`
Agile Task Board
Development activities, sprint work, implementation tasks, and completion status are documented in the PolicyLens-Mini GitHub Projects board.
Agile task board: https://github.com/users/dixkox/projects/1/views/2
Final board status:
```text
Todo:        0
In Progress: 0
Done:       18
```
API
The FastAPI backend exposes:
```text
GET  /health
POST /upload
POST /ask
```
Health Check
```text
GET /health
```
Example:
```json
{
  "status": "ok"
}
```
Upload
`POST /upload` accepts a PDF document and returns the filename and extracted text.
Ask
`POST /ask` receives:
`question`
`text`
and returns:
`answer`
`score`
`matched`
Architecture
PolicyLens-Mini follows a separated frontend/backend architecture.
```text
User
 |
 v
Next.js / React Frontend
 |
 | HTTP API
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
Separating the presentation layer from document processing and retrieval logic supports maintainability, independent deployment, testing, and separation of concerns.
Additional documentation:
`architecture/architecture_diagram.png`
`design-and-evaluation.md`
Repository Structure
```text
PolicyLens-Mini/
|
|-- backend/
|   |-- app/
|   |   |-- main.py
|   |   |-- routes.py
|   |   |-- retrieval.py
|   |   `-- pdf_utils.py
|   |-- requirements.txt
|   |-- render.yaml
|   `-- README.md
|
|-- frontend/
|   |-- app/
|   |   |-- page.tsx
|   |   |-- layout.tsx
|   |   `-- globals.css
|   |-- public/
|   `-- package.json
|
|-- architecture/
|   `-- architecture_diagram.png
|
|-- evaluation/
|   |-- eval_results.json
|   |-- evaluation.md
|   |-- evaluation_summary.md
|   `-- test_all_policies.py
|
|-- demo/
|   |-- PolicyLens_Mini_Complete_Policy_Handbook.pdf
|   |-- screenshots/
|   |-- demo_script.md
|   `-- demo_steps.md
|
|-- data/
|   |-- policies/
|   `-- raw/
|
|-- ai-tooling.md
|-- design-and-evaluation.md
|-- evaluation_set.md
`-- README.md
```
Local Development
Clone Repository
```powershell
git clone https://github.com/dixkox/PolicyLens-Mini.git
cd PolicyLens-Mini
```
Backend
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
Health check: http://127.0.0.1:8000/health
Interactive FastAPI documentation: http://127.0.0.1:8000/docs
Frontend
Open another terminal:
```powershell
cd frontend
npm install
npm run dev
```
Frontend: http://localhost:3000
Testing and Evaluation
PolicyLens-Mini includes reproducible automated evaluation and regression validation.
Controlled Evaluation
Authoritative machine-readable results:
`evaluation/eval_results.json`
The controlled evaluation contains 20 test cases across four policy categories:
Paid Time Off
Information Security
Remote Work
Code of Conduct
Baseline:
```text
15/20 correct
75.00% accuracy
```
After evaluation-driven retrieval improvements:
```text
20/20 correct
100.00% accuracy
```
Comprehensive Regression Suite
The final regression suite validates all policy names, factual retrieval, and unsupported-question behavior:
```powershell
python .\evaluation	est_all_policies.py
```
Final result:
```text
RESULT: 35/35 tests passed
```
CI/CD and Deployment
PolicyLens-Mini uses Git-based source control and cloud deployment.
Git and GitHub for source control
GitHub Actions for automated workflow support
Vercel for frontend deployment
Render for backend deployment
Automated evaluation for regression validation
Production architecture:
```text
Browser
   |
   v
Vercel
Next.js Frontend
   |
   | HTTP API
   v
Render
FastAPI Backend
```
Production application: https://policylens-mini.vercel.app
Deployment architecture choices, testing decisions, and evaluation evidence are documented in `design-and-evaluation.md`.
Reproducibility and Examiner Testing
An examiner can reproduce the primary workflow without constructing a separate test document:
Open this repository.
Download `demo/PolicyLens_Mini_Complete_Policy_Handbook.pdf`.
Open https://policylens-mini.vercel.app.
Upload the supplied handbook.
Ask `What is Attendance Policy?`.
Ask `What is Reimbursement Policy?` and confirm the 14-day Reimbursement Policy is returned rather than the Expense Reimbursement Policy.
Ask `What is Remote Work Policy?`.
Ask `What is Cook Policy?` and confirm the unsupported question is rejected.
Engineering Documentation
Document	Purpose
`design-and-evaluation.md`	Architecture, design decisions, testing, and evaluation
`architecture/architecture_diagram.png`	System architecture
`evaluation_set.md`	Controlled evaluation cases
`evaluation/eval_results.json`	Machine-readable controlled evaluation results

`evaluation/evaluation.md`	Evaluation documentation
`evaluation/evaluation_summary.md`	Evaluation summary
`evaluation/test_all_policies.py`	Comprehensive regression suite
`ai-tooling.md`	AI tooling documentation
`demo/demo_script.md`	Demonstration guidance
`demo/demo_steps.md`	Reproducible demonstration procedure
`demo/PolicyLens_Mini_Complete_Policy_Handbook.pdf`	Examiner demonstration document
Final Demonstration
A recorded final Capstone demonstration will be linked here before submission.
Demonstration video:(https://drive.google.com/file/d/1O7O84Wea0Z9PHPckucxOqYdBieSMItXG/view?usp=sharing)
Evidence of Engineering Initiative
PolicyLens-Mini extends beyond basic PDF upload and keyword search through:
Deterministic TF-IDF-style retrieval
Cosine-similarity ranking
Relevance guardrails
Explicit unsupported-policy detection
Full policy-section retrieval
Deterministic query expansion
Reproducible automated evaluation
Evaluation-driven retrieval refinement
Comprehensive regression validation
Production frontend/backend deployment
Examiner-ready reproducibility resources
Conclusion
PolicyLens-Mini demonstrates an end-to-end software engineering lifecycle covering requirements-driven development, Agile iteration, architecture, implementation, testing, evaluation, CI/CD practices, documentation, and production deployment.
The final system integrates PDF ingestion, structured text processing, deterministic retrieval, policy-section detection, relevance guardrails, automated evaluation, frontend-backend integration, Git-based development, and cloud deployment into a reproducible policy-document analysis application.