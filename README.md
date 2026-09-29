PolicyLens-Mini
MSSE Capstone Project
PolicyLens-Mini is a lightweight policy-document analysis web application developed for the Quantic Master of Science in Software Engineering Capstone Project.

The application allows users to upload a PDF policy document and ask natural-language questions about its contents.

PolicyLens-Mini uses deterministic lexical retrieval, TF-IDF-style weighting, cosine similarity, deterministic query expansion, policy-section retrieval, and relevance guardrails to retrieve supporting policy information or reject unsupported questions.

Live Application
Production Application:
https://policylens-mini.vercel.app

Sample Policy Handbook:
demo/PolicyLens_Mini_Complete_Policy_Handbook.pdf

Quick Demo
Download the sample policy handbook.
Open the production application.
Select the downloaded PDF.
Click Upload.
Ask supported questions such as:
What is Attendance Policy?
What is Remote Work Policy?
How quickly must security incidents be reported?
Ask an unsupported question:
What is Cook Policy?
Observe that PolicyLens-Mini retrieves relevant policy information when supporting evidence exists and rejects unsupported policy questions.
Project Objectives
PolicyLens-Mini demonstrates:

Full-stack software engineering
PDF document ingestion and text extraction
Natural-language policy retrieval
Deterministic information retrieval
TF-IDF-style weighting
Cosine similarity scoring
Policy-section retrieval
Unsupported-question guardrails
REST API development
Frontend-backend integration
Automated evaluation and regression testing
Git-based version control
CI/CD practices
Cloud deployment
Agile software development
Reproducible software testing
Software architecture and technical documentation
Core Features
PDF Policy Upload
Users can upload PDF policy documents.

The FastAPI backend extracts text from the uploaded document and makes the extracted content available for policy questioning.

Policy Question Answering
Users can ask natural-language questions about uploaded policy documents.

For factual questions, the backend retrieves relevant policy information using deterministic lexical similarity.

For explicit policy-name questions, PolicyLens-Mini can retrieve the complete content associated with the matching policy section.

Example:

What is Attendance Policy?
PolicyLens-Mini returns the corresponding Attendance Policy content.

Unsupported Policy Detection
PolicyLens-Mini includes a relevance guardrail for policy questions that are not supported by the uploaded document.

Example:

What is Cook Policy?
Response:

This question is not covered by the uploaded policy document.
This prevents unrelated policy names from being incorrectly matched to existing policy content.

Deterministic Retrieval Pipeline
The core factual retrieval pipeline performs:

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
Explicit policy-name questions additionally use policy-section detection so that complete matching policy sections can be returned.

This approach provides:

Reproducible results
Transparent scoring
Lightweight execution
No external LLM dependency for core retrieval
Predictable behavior
Easier debugging and evaluation
Relevance Guardrail
PolicyLens-Mini applies a factual retrieval relevance threshold of:

0.20
When sufficient supporting information is found, an API response can contain:

{
  "answer": "Employees accrue PTO at a rate of 1.5 days per month.",
  "score": 0.446,
  "matched": true
}
When sufficient evidence is not found:

{
  "answer": "No relevant policy information was found.",
  "score": 0.0,
  "matched": false
}
For an explicit policy name that does not exist in the uploaded document:

{
  "answer": "This question is not covered by the uploaded policy document.",
  "score": 0.0,
  "matched": false
}
Markdown headings are excluded from normal factual-answer candidates.

The retrieval system also uses limited deterministic query expansion to reduce selected vocabulary mismatches.

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
PolicyLens-Mini was developed using an iterative Agile software engineering approach across three development sprints.

The project used GitHub Projects to document development activities, sprint work, implementation tasks, and completion status.

Sprint 1: Core Architecture and Application
Sprint 1 established the initial full-stack application.

Activities included:

Defining the PolicyLens-Mini architecture
Building the FastAPI backend
Building the Next.js frontend
Establishing the core application structure
Implementing the initial document-processing workflow
Sprint 2: Retrieval Quality and Evaluation
Sprint 2 focused on retrieval quality, testing, and systematic evaluation.

Activities included:

Developing the automated evaluation workflow
Establishing controlled evaluation cases
Identifying retrieval failures
Improving heading exclusion
Refining relevance filtering
Adding deterministic query expansion
Improving unsupported-question handling
The baseline evaluation produced:

Correct: 15/20
Accuracy: 75.00%
Sprint 3: Production Readiness and Final Validation
Sprint 3 focused on completing and validating the production-ready system.

Activities included:

Adding explicit policy-name detection
Adding complete policy-section retrieval
Strengthening unsupported-question guardrails
Running regression evaluation
Finalizing cloud deployment
Finalizing architecture documentation
Finalizing testing and evaluation documentation
Preparing examiner demonstration resources
Final controlled evaluation:

Correct: 20/20
Accuracy: 100.00%
Agile Task Board
The project backlog, sprint activities, implementation tasks, and completion status are documented through the PolicyLens-Mini GitHub Projects board.

Agile Task Board:
https://github.com/users/dixkox/projects/1/views/2

Final board status:

Todo:        0
In Progress: 0
Done:        18
API
The FastAPI backend exposes:

GET  /health
POST /upload
POST /ask
Health Check
GET /health
Example:

{
  "status": "ok"
}
Upload
POST /upload
Accepts a PDF document and returns the filename and extracted text.

Ask
POST /ask
Receives:

question
text
and returns:

answer
score
matched
Architecture
PolicyLens-Mini follows a separated frontend/backend architecture.

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
Separating the presentation layer from document processing and retrieval logic supports maintainability, independent deployment, testing, and separation of concerns.

Additional architecture and design documentation:

architecture/architecture_diagram.png
design-and-evaluation.md
Repository Structure
PolicyLens-Mini/
|
|-- app/
|   `-- eval/
|       `-- run_eval.py
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
|   `-- evaluation_summary.md
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
Local Development
Clone Repository
git clone https://github.com/dixkox/PolicyLens-Mini.git
cd PolicyLens-Mini
Backend
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
Health check:

http://127.0.0.1:8000/health
Interactive FastAPI documentation:

http://127.0.0.1:8000/docs
Frontend
Open another terminal:

cd frontend
npm install
npm run dev
Frontend:

http://localhost:3000
Testing and Evaluation
PolicyLens-Mini includes a reproducible automated evaluation suite.

Evaluator:

app/eval/run_eval.py
Authoritative machine-readable results:

evaluation/eval_results.json
The controlled evaluation contains:

20 test cases
4 policy documents
Evaluated policy categories include:

Paid Time Off
Information Security
Remote Work
Code of Conduct
The evaluation contains supported questions as well as intentionally unsupported questions.

Baseline Evaluation
Initial result:

Correct: 15/20
Accuracy: 75.00%
Observed failure categories included:

Policy headings returned as answers
Unsupported questions incorrectly matched
Vocabulary mismatch
Incorrect selection between related policy sentences
Evaluation-Driven Improvements
Evaluation findings led to several retrieval improvements:

Markdown headings excluded from factual answers
Relevance threshold increased from 0.10 to 0.20
Limited deterministic query expansion added
Unsupported-question rejection improved
Explicit unsupported policy-name detection added
Complete policy-section retrieval added
Final Evaluation
The controlled 20-case evaluation suite was rerun following the retrieval improvements.

Correct: 20/20
Accuracy: 100.00%
Full results:

evaluation/eval_results.json
CI/CD and Deployment
PolicyLens-Mini uses Git-based version control and cloud deployment as part of its software engineering workflow.

The project uses:

Git and GitHub for source control
GitHub Actions for automated workflow support
Vercel for frontend deployment
Render for backend deployment
Automated evaluation for regression validation
Production architecture:

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
Production Application
https://policylens-mini.vercel.app

Deployment architecture choices, testing decisions, and evaluation evidence are documented further in:

design-and-evaluation.md
Reproducibility and Examiner Testing
An examiner can reproduce the primary PolicyLens-Mini workflow without constructing a separate test document.

Open this repository.
Download: demo/PolicyLens_Mini_Complete_Policy_Handbook.pdf
Open: https://policylens-mini.vercel.app
Upload the supplied handbook.
Ask: What is Attendance Policy?
Confirm that PolicyLens-Mini returns the corresponding policy content.
Ask: What is Remote Work Policy?
Confirm that PolicyLens-Mini retrieves the corresponding policy section.
Ask: What is Cook Policy?
Confirm that PolicyLens-Mini rejects the unsupported policy question.
Engineering Documentation
Supporting project documentation includes:

Document	Purpose
design-and-evaluation.md	Architecture, design decisions, testing and evaluation
architecture/architecture_diagram.png	System architecture
evaluation_set.md	Controlled evaluation cases
evaluation/eval_results.json	Machine-readable evaluation results
evaluation/evaluation.md	Evaluation documentation
evaluation/evaluation_summary.md	Evaluation summary
ai-tooling.md	AI tooling documentation
demo/demo_script.md	Demonstration guidance
demo/demo_steps.md	Reproducible demonstration procedure
demo/PolicyLens_Mini_Complete_Policy_Handbook.pdf	Examiner demonstration document
Evidence of Engineering Initiative
PolicyLens-Mini extends beyond basic PDF upload and keyword search by incorporating:

Deterministic TF-IDF-style retrieval
Cosine-similarity ranking
Relevance guardrails
Explicit unsupported-policy detection
Full policy-section retrieval
Deterministic query expansion
Reproducible automated evaluation
Evaluation-driven retrieval refinement
Regression validation
Production frontend/backend deployment
Examiner-ready reproducibility resources
The controlled evaluation improved from:

15/20 (75%)
to:

20/20 (100%)
following systematic retrieval improvements.

Conclusion
PolicyLens-Mini demonstrates an end-to-end software engineering lifecycle covering requirements-driven development, Agile iteration, architecture, implementation, testing, evaluation, CI/CD practices, documentation, and production deployment.

The final system integrates PDF ingestion, structured text processing, deterministic retrieval, policy-section detection, relevance guardrails, automated evaluation, frontend-backend integration, Git-based development, and cloud deployment into a reproducible policy-document analysis application.