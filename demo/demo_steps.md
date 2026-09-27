# PolicyLens-Mini Capstone Demo Steps
 
## Pre-Demo Checklist
 
Before recording:
 
- Start the FastAPI backend.
- Start the Next.js frontend.
- Confirm `/health` returns successfully.
- Confirm the frontend loads.
- Have the complete PolicyLens-Mini policy handbook ready.
- Have the architecture diagram ready.
- Have the evaluation terminal/results ready.
- Have GitHub, Render, Vercel, GitHub Actions, and the agile board ready in browser tabs.
- Close unrelated applications and browser tabs.
- Use a readable browser zoom level.
 
---
 
## Step 1 - Introduction
 
### Show
PolicyLens-Mini frontend.
 
### Explain
PolicyLens-Mini is an MSSE Capstone policy analysis application that allows users to upload PDF policies and ask natural-language questions.
 
---
 
## Step 2 - Problem and Solution
 
### Explain
 
The system simplifies policy lookup:
 
```text
Upload PDF
|
Extract Text
|
Ask Question
|
Retrieve Evidence
|
Answer or Reject
```
 
Emphasize that the final retrieval implementation is deterministic.
 
---
 
## Step 3 - Architecture
 
### Show
 
```text
architecture/architecture_diagram.png
```
 
### Explain
 
Identify:
 
- Next.js frontend
- TypeScript
- FastAPI backend
- PDF extraction
- TF-IDF-style retrieval
- Cosine similarity
- Relevance guardrail
- Automated evaluation
 
---
 
## Step 4 - Upload Complete Policy Handbook
 
### Show
The application before upload.
 
### Action
Select:
 
```text
PolicyLens_Mini_Complete_Policy_Handbook.pdf
```
 
Select **Upload PDF**.
 
### Verify
 
The Extracted Policy Text area contains text from the uploaded handbook.
 
### Screenshot
 
```text
01-policy-upload.png
```
 
---
 
## Step 5 - General Policy Retrieval
 
### Ask
 
```text
What is the Attendance Policy?
```
 
### Verify
 
The result returns substantive Attendance Policy content rather than only the heading.
 
### Explain
 
This demonstrates section-level policy retrieval.
 
### Screenshot
 
```text
02-attendance-policy-answer.png
```
 
---
 
## Step 6 - PTO Fact Retrieval
 
### Ask
 
```text
How fast do employees accrue PTO?
```
 
### Expected
 
```text
Employees accrue PTO at a rate of 1.5 days per month.
```
 
### Screenshot
 
```text
03-pto-answer.png
```
 
---
 
## Step 7 - Security Retrieval
 
### Ask
 
```text
How often must passwords be changed?
```
 
### Expected
 
The answer identifies the 90-day password-change requirement.
 
### Screenshot
 
```text
04-security-answer.png
```
 
---
 
## Step 8 - Remote Work Retrieval
 
### Ask
 
```text
During what hours must remote employees be available online?
```
 
### Expected
 
The result identifies:
 
```text
9 AM to 3 PM EST
```
 
---
 
## Step 9 - Guardrail Demonstration
 
### Ask
 
```text
What antivirus software must employees install?
```
 
### Expected
 
```text
No relevant policy information was found.
```
 
### Explain
 
The policy does not identify a specific antivirus product, so PolicyLens-Mini abstains instead of inventing an answer.
 
### Screenshot
 
```text
05-guardrail-rejection.png
```
 
---
 
## Step 10 - FastAPI
 
### Show
 
```text
http://127.0.0.1:8000/docs
```
 
### Highlight
 
```text
GET /health
POST /upload
POST /ask
```
 
Then show a successful `/health` response.
 
### Screenshot
 
```text
06-fastapi-api.png
```
 
---
 
## Step 11 - Automated Evaluation
 
### Show
 
Run:
 
```powershell
python app\eval\run_eval.py
```
 
### Highlight
 
```text
Correct: 20/20
Accuracy: 100.00%
```
 
### Explain
 
Baseline:
 
```text
15/20
75%
```
 
Final controlled evaluation:
 
```text
20/20
100%
```
 
Improvement:
 
```text
+5 correct cases
+25 percentage points
```
 
State clearly that 100% refers specifically to the controlled 20-case evaluation suite.
 
### Screenshot
 
```text
07-evaluation-20-of-20.png
```
 
---
 
## Step 12 - Evaluation-Driven Improvements
 
### Explain
 
The evaluation resulted in improvements including:
 
- Heading handling
- 0.20 relevance threshold
- Limited deterministic query expansion
- Unsupported-question rejection
- Policy-section retrieval
- Substantive answers instead of heading-only responses
 
Explain that regression testing remained:
 
```text
20/20
100%
```
 
---
 
## Step 13 - GitHub Repository
 
### Show
 
PolicyLens-Mini GitHub repository.
 
### Highlight
 
```text
app/
architecture/
backend/
data/
demo/
evaluation/
frontend/
README.md
design-and-evaluation.md
evaluation_set.md
ai-tooling.md
```
 
### Screenshot
 
```text
08-github-repository.png
```
 
---
 
## Step 14 - CI/CD
 
### Show
 
GitHub Actions.
 
### Explain
 
Show the automated workflow and successful execution evidence.
 
### Screenshot
 
```text
09-github-actions.png
```
 
---
 
## Step 15 - Backend Deployment
 
### Show
 
Render dashboard for PolicyLens-Mini.
 
### Highlight
 
Successful backend deployment.
 
### Screenshot
 
```text
10-render-deployment.png
```
 
---
 
## Step 16 - Frontend Deployment
 
### Show
 
Vercel PolicyLens-Mini project.
 
### Highlight
 
Frontend deployment and connection to the project repository.
 
### Screenshot
 
```text
11-vercel-deployment.png
```
 
---
 
## Step 17 - Agile Development
 
### Show
 
Project task board.
 
### Highlight
 
- Backlog
- User stories
- Sprint work
- Completed tasks
- Testing
- Deployment activities
 
### Screenshot
 
```text
12-agile-board.png
```
 
---
 
## Step 18 - Limitations
 
### Explain
 
PolicyLens-Mini uses lightweight deterministic retrieval.
 
Retrieval quality can depend on:
 
- PDF extraction quality
- Policy structure
- User question wording
- Vocabulary overlap
- Similarity threshold
- Query expansion rules
 
The controlled benchmark does not represent universal accuracy.
 
---
 
## Step 19 - Future Improvements
 
Briefly mention:
 
- Larger evaluation dataset
- Improved section detection
- Semantic retrieval
- Additional integration testing
- Improved frontend feedback
- Deployment monitoring
 
---
 
## Step 20 - Conclusion
 
### Explain
 
PolicyLens-Mini demonstrates:
 
- PDF ingestion
- Text extraction
- Policy question answering
- Deterministic retrieval
- TF-IDF-style weighting
- Cosine similarity
- Relevance guardrails
- Full-stack integration
- Automated evaluation
- Regression testing
- CI/CD
- Deployment
- Agile development
 
Finish with:
 
```text
Baseline: 15/20 (75%)
Final: 20/20 (100%)
```
 
Thank the viewer and conclude the demonstration.
 
---
 
# Final Screenshot Checklist
 
```text
01-policy-upload.png
02-attendance-policy-answer.png
03-pto-answer.png
04-security-answer.png
05-guardrail-rejection.png
06-fastapi-api.png
07-evaluation-20-of-20.png
08-github-repository.png
09-github-actions.png
10-render-deployment.png
11-vercel-deployment.png
12-agile-board.png
```
 
Store the final images in:
 
```text
demo/screenshots/
```