# Demo Steps - PolicyLens-Mini
 
## 1. Prepare the Demonstration
 
Before recording:
 
- Verify the deployed frontend is working.
- Verify the deployed FastAPI backend is working.
- Prepare a sample policy PDF.
- Open the GitHub repository.
- Open the agile task board.
- Open the architecture diagram.
- Open the final evaluation results.
- Prepare the required identification and recording setup.
 
---
 
## 2. Introduce PolicyLens-Mini
 
Explain:
 
PolicyLens-Mini is a lightweight policy analysis web application that allows users to upload a PDF policy document and ask natural-language questions about its contents.
 
Explain the core workflow:
 
```text
Upload PDF
|
Extract Text
|
Ask Question
|
Retrieve Policy Information
|
Apply Relevance Guardrail
|
Answer or Reject
```
 
---
 
## 3. Show the Architecture
 
Open:
 
```text
architecture/architecture_diagram.png
```
 
Explain the main components:
 
- Next.js frontend
- FastAPI backend
- PDF text extraction
- Sentence-level chunking
- TF-IDF weighting
- Cosine similarity
- Relevance guardrail
 
---
 
## 4. Demonstrate PDF Upload
 
Open the deployed PolicyLens-Mini application.
 
1. Select a policy PDF.
2. Click the upload button.
3. Confirm that the extracted policy text appears.
4. Explain that the extracted text is used by the retrieval pipeline.
 
---
 
## 5. Demonstrate a Supported Question
 
Using the PTO policy, ask:
 
```text
How fast do employees accrue PTO?
```
 
Expected information:
 
```text
1.5 days per month
```
 
Confirm that PolicyLens-Mini returns the relevant policy sentence.
 
---
 
## 6. Demonstrate Additional Questions
 
Examples:
 
```text
How much unused PTO can roll over?
```
 
```text
How often must passwords be changed?
```
 
```text
During what hours must remote employees be available online?
```
 
```text
What conduct is strictly prohibited?
```
 
Explain that these demonstrate retrieval across different policy topics.
 
---
 
## 7. Demonstrate the Guardrail
 
Ask an intentionally unsupported question:
 
```text
What disciplinary action is taken for violating the code?
```
 
Expected behavior:
 
```text
No relevant policy information was found.
```
 
The response should indicate:
 
```text
matched = false
```
 
Explain that PolicyLens-Mini rejects the question because the requested information is not contained in the evaluated policy.
 
---
 
## 8. Show the FastAPI API
 
Open the FastAPI interactive documentation.
 
Show:
 
```text
GET /health
POST /upload
POST /ask
```
 
Briefly explain how the frontend communicates with the backend.
 
---
 
## 9. Show the Automated Evaluation
 
Open:
 
```text
app/eval/run_eval.py
```
 
Then show:
 
```text
evaluation/eval_results.json
```
 
Explain the baseline result:
 
```text
15/20 correct
75% accuracy
```
 
Then explain the final result after retrieval improvements:
 
```text
20/20 correct
100% accuracy
```
 
Clarify that 100% refers specifically to the controlled 20-case evaluation suite.
 
---
 
## 10. Explain the Improvements
 
Show:
 
```text
backend/app/retrieval.py
```
 
Explain the main improvements:
 
- Markdown headings excluded from answer candidates
- Stronger relevance threshold
- Limited deterministic query expansion
- Improved unsupported-question rejection
 
Explain the engineering cycle:
 
```text
Implement
Evaluate
Identify Failures
Improve
Retest
Compare
```
 
---
 
## 11. Show Design and Testing Documentation
 
Open:
 
```text
design-and-evaluation.md
```
 
Show:
 
```text
evaluation_set.md
evaluation/evaluation.md
evaluation/evaluation_summary.md
```
 
Explain that these document:
 
- Architecture decisions
- Testing methods
- Evaluation methodology
- Baseline failures
- Retrieval improvements
- Final evaluation results
- Known limitations
 
---
 
## 12. Show CI/CD and Deployment
 
Show the repository's CI/CD and deployment configuration.
 
Demonstrate the deployed frontend and backend if available during recording.
 
---
 
## 13. Show the Agile Task Board
 
Show the project task board.
 
Demonstrate the completed user stories and engineering tasks associated with the Capstone project.
 
---
 
## 14. Show the GitHub Repository
 
Show the final repository structure, including:
 
```text
backend/
frontend/
app/eval/
architecture/
evaluation/
demo/
data/
```
 
Highlight:
 
- Source code
- Architecture
- Testing
- Evaluation
- Deployment configuration
- Documentation
 
---
 
## 15. Final Demonstration Check
 
Before finishing, verify that the demonstration has shown:
 
- Working deployed application
- PDF upload
- Successful question
- Unsupported question
- FastAPI endpoints
- Architecture
- Automated evaluation
- Baseline versus final results
- CI/CD and deployment
- Agile task board
- GitHub repository
 
---
 
## 16. Conclusion
 
Summarize PolicyLens-Mini as an end-to-end policy analysis system combining:
 
- PDF ingestion
- Next.js frontend
- FastAPI backend
- Deterministic retrieval
- Similarity scoring
- Relevance guardrails
- Automated testing
- Evaluation-driven improvement
- Deployment and software engineering documentation
 
Conclude by highlighting the measured improvement:
 
```text
Baseline: 15/20 (75%)
Final: 20/20 (100%)
```
 
State clearly that the final result represents performance on the controlled 20-case evaluation suite.