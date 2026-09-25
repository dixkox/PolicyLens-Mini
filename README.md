# PolicyLens-Mini
 
## MSSE Capstone Project
 
**PolicyLens-Mini** is a lightweight policy analysis web application developed for the Quantic Master of Science in Software Engineering Capstone Project.
 
The application allows users to upload a PDF policy document and ask natural-language questions about its contents. The backend extracts the document text and uses deterministic text retrieval to identify relevant policy information while applying a similarity threshold to reject questions that are not sufficiently supported by the document.
 
---
 
## Project Objectives
 
PolicyLens-Mini was designed to demonstrate:
 
- Full-stack software engineering
- Document ingestion and PDF text extraction
- Natural-language information retrieval
- Deterministic retrieval and relevance scoring
- Guardrails for unsupported questions
- REST API development
- Frontend-backend integration
- Automated testing and evaluation
- Git-based version control
- CI/CD practices
- Cloud deployment
- Agile software development
 
---
 
## Core Features
 
### PDF Policy Upload
 
Users can upload PDF policy documents. The FastAPI backend extracts the document text for subsequent analysis.
 
### Policy Question Answering
 
Users can ask questions about an uploaded policy document through the `/ask` API.
 
### Deterministic Retrieval
 
The current retrieval pipeline performs text normalization, tokenization, TF-IDF-style weighting and similarity scoring using a deterministic implementation.
 
This design provides:
 
- Reproducible results
- No external LLM dependency for core retrieval
- Low operating cost
- Explainable similarity scores
- Reduced risk of unsupported generated answers
 
### Relevance Guardrail
 
Retrieved results include a relevance assessment so the application can distinguish supported questions from questions that do not sufficiently match the supplied policy.
 
Example response:
 
```json
{
"answer": "Employees are entitled to 10 vacation days annually.",
"score": 0.559,
"matched": true
}
```
 
### REST API
 
The backend exposes endpoints including:
 
```text
POST /upload
POST /ask
GET /health
```
 
Interactive API documentation is available through FastAPI's API documentation interface when the backend is running.
 
---
 
## Technology Stack
 
### Backend
 
- Python
- FastAPI
- Uvicorn
- PyPDF
- Python Multipart
 
### Frontend
 
- Next.js
- React
- TypeScript
- CSS
 
### Engineering and Deployment
 
- Git
- GitHub
- GitHub Actions
- Render
- Automated evaluation
- Agile development practices
 
---
 
## Repository Structure
 
```text
PolicyLens-Mini/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── routes.py
│ │ ├── retrieval.py
│ │ ├── pdf_utils.py
│ │ └── ai_utils.py
│ ├── requirements.txt
│ ├── render.yaml
│ └── runtime.txt
│
├── frontend/
│ ├── app/
│ │ ├── page.tsx
│ │ ├── layout.tsx
│ │ └── globals.css
│ ├── public/
│ ├── package.json
│ └── next.config.ts
│
├── architecture/
│ └── architecture_diagram.png
│
├── evaluation/
│ ├── eval_results.json
│ ├── evaluation.md
│ └── evaluation_summary.md
│
├── demo/
│ ├── screenshots/
│ ├── demo_script.md
│ └── demo_steps.md
│
├── data/
│ ├── policies/
│ └── raw/
│
├── scripts/
│ └── generate_policies.py
│
├── design-and-evaluation.md
├── ai-tooling.md
└── README.md
```
 
---
 
# Architecture
 
PolicyLens-Mini follows a separated frontend/backend web architecture.
 
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
+--> Text Processing
|
+--> Deterministic Retrieval
|
+--> Similarity Scoring
|
+--> Match Guardrail
|
v
Grounded Policy Answer
```
 
The separation of concerns keeps the user interface, API layer, document processing and retrieval logic independently maintainable.
 
Additional architecture material is available in:
 
```text
architecture/architecture_diagram.png
design-and-evaluation.md
```
 
---
 
# Local Development
 
## Clone the Repository
 
```powershell
git clone https://github.com/dixkox/PolicyLens-Mini.git
cd PolicyLens-Mini
```
 
## Backend
 
Create and activate a Python virtual environment and install the backend dependencies.
 
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
 
Start FastAPI:
 
```powershell
python -m uvicorn app.main:app --reload
```
 
Backend:
 
```text
http://127.0.0.1:8000
```
 
API documentation:
 
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
 
PolicyLens-Mini is tested at multiple levels, including:
 
- Retrieval behaviour
- Relevant policy questions
- Unsupported questions
- Similarity scoring
- Guardrail behaviour
- API health
- PDF processing
- Frontend-backend integration
- Production behaviour
 
Evaluation artifacts are maintained under:
 
```text
evaluation/
```
 
Detailed testing and engineering decisions are documented in:
 
```text
design-and-evaluation.md
```
 
---
 
# CI/CD
 
The project uses Git and GitHub for source control and incorporates automated CI/CD practices.
 
The CI workflow is stored in:
 
```text
.github/workflows/
```
 
The application is also configured for cloud deployment.
 
---
 
# Deployment
 
PolicyLens-Mini is designed to operate as a deployed web application in addition to local development.
 
**Production application:**
Add final deployed frontend URL here.
 
**Production backend:**
Add final Render backend URL here.
 
The final deployed URLs will remain linked from this repository for Capstone evaluation.
 
---
 
# Agile Engineering
 
PolicyLens-Mini was developed iteratively using agile engineering practices.
 
The Capstone development record includes:
 
- Product backlog
- User stories
- Sprint planning
- At least three development sprints
- Implementation tasks
- Testing activities
- Sprint completion evidence
- Deployment activities
 
**Agile Task Board:**
Add final accessible task-board URL here.
 
---
 
# Design and Testing Documentation
 
The Capstone design and testing documentation covers:
 
- System architecture
- Major engineering decisions
- Technology choices and rationale
- Software and architectural patterns
- Retrieval architecture
- Testing strategy
- Automated and manual testing
- Evaluation results
- Deployment strategy
- Hosting considerations
- Cost considerations
- Limitations and future improvements
 
See:
 
```text
design-and-evaluation.md
```
 
---
 
# AI-Assisted Engineering
 
AI development tools were used to support activities including debugging, architecture reasoning, code development, documentation and engineering analysis.
 
Usage is documented in:
 
```text
ai-tooling.md
```
 
Engineering decisions, integration, validation and final project responsibility remain with the project author.
 
---
 
# Capstone Demonstration
 
The final Quantic demonstration will show the deployed PolicyLens-Mini system operating across multiple representative user inputs, including:
 
1. Application overview
2. PDF policy upload
3. Successful policy question
4. Retrieval result
5. Similarity score
6. Unsupported-question guardrail
7. Architecture
8. Testing and evaluation
9. GitHub repository
10. CI/CD and deployment
11. Agile development evidence
 
The final Capstone recording will follow the required **15 to 20 minute** presentation duration.
 
---
 
# Capstone Deliverables
 
- [x] GitHub repository
- [x] Backend implementation
- [x] Frontend implementation
- [x] PDF document processing
- [x] Policy question answering
- [x] Deterministic retrieval
- [x] Similarity scoring
- [x] Unsupported-question guardrail
- [x] Architecture artifacts
- [x] Evaluation artifacts
- [x] Git version control
- [x] CI/CD artifacts
- [ ] Final deployed URLs verified
- [ ] Agile task board finalized
- [ ] Design and testing document final audit
- [ ] Quantic grader repository access verified
- [ ] Final 15–20 minute demonstration recorded
- [ ] Final submission links verified
 
---
 
# Repository
 
GitHub:
 
https://github.com/dixkox/PolicyLens-Mini
 
---
 
## Author
 
**Tinubu Damilola**
Master of Science in Software Engineering
Quantic School of Business and Technology
 
---
 
## Academic Integrity
 
PolicyLens-Mini was developed as an academic software engineering project. External tools, libraries and AI-assisted development tools used during development are documented where appropriate.
 
Synthetic policy data is used for demonstration and evaluation purposes.
 
---
 
## License
 
See the applicable repository license files for licensing information.