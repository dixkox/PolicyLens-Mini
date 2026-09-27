# PolicyLens-Mini Capstone Demonstration Script
 
## 1. Introduction
 
Hello, my name is Tinubu Damilola, and this is my MSSE Capstone demonstration of PolicyLens-Mini.
 
PolicyLens-Mini is a lightweight policy analysis web application that allows users to upload policy documents in PDF format and ask natural-language questions about their contents.
 
The system combines a Next.js frontend with a FastAPI backend and deterministic information retrieval.
 
During this demonstration, I will show the application workflow, architecture, retrieval approach, guardrails, automated evaluation, deployment, CI/CD, agile development evidence, and project repository.
 
---
## 2. Problem and Solution
 
Organizations often maintain workplace policies as documents that employees must manually search.
 
PolicyLens-Mini provides a simpler workflow:
 
1. Upload a policy PDF.
2. Extract the policy text.
3. Ask a natural-language question.
4. Search the policy using deterministic retrieval.
5. Return relevant policy information when sufficient evidence exists.
6. Reject unsupported questions when the evidence is insufficient.
 
The goal is to provide a lightweight and explainable policy retrieval system without requiring an external language model for the core retrieval process.
 
---
## 3. System Architecture
 
PolicyLens-Mini uses a separated frontend and backend architecture.
 
The major components are:
 
- Next.js frontend
- TypeScript
- FastAPI backend
- PDF text extraction
- Policy section and sentence processing
- Deterministic lexical retrieval
- TF-IDF-style weighting
- Cosine similarity
- Relevance guardrails
- Automated evaluation
 
I will briefly show:
 
```text
architecture/architecture_diagram.png
```
 
The frontend communicates with the FastAPI backend through HTTP endpoints.
 
---
## 4. Application Overview
 
I will now open the PolicyLens-Mini frontend.
 
The interface provides three primary areas:
 
- PDF upload
- Extracted policy text
- Natural-language question answering
 
For this demonstration, I will use a PDF containing the PolicyLens-Mini sample workplace policies.
 
The handbook includes policies covering areas such as:
 
- Anti-harassment
- Attendance
- Employee benefits
- Code of conduct
- Data protection
- Expenses
- Holidays
- Human resources
- IT usage
- Parental leave
- Paid time off
- Reimbursement
- Remote work
- Information security
- Business travel
- Workplace behavior
 
---
## 5. PDF Upload Demonstration
 
I will select the PolicyLens-Mini policy handbook and upload it.
 
After the upload completes, the backend extracts the PDF text and returns it to the frontend.
 
The extracted policy information is displayed in the application.
 
This demonstrates the PDF ingestion and text-extraction components of the system.
 
---
 
## 6. General Policy Question
 
I will first demonstrate a general policy-level question.
 
Example:
 
```text
What is the Attendance Policy?
```
 
PolicyLens-Mini identifies the Attendance Policy section and returns the substantive content of that policy.
 
The returned information explains attendance expectations, schedule requirements, absence reporting, unexcused absences, and tardiness.
 
This test also demonstrates an important retrieval improvement.
 
Earlier versions could return only a matching section heading.
 
The final implementation identifies the section but returns the actual policy content instead of merely returning the heading.
 
---
## 7. Specific Policy Question
 
Next, I will demonstrate a more specific factual question.
 
Example:
 
```text
How fast do employees accrue PTO?
```
 
The relevant policy states:
 
```text
Employees accrue PTO at a rate of 1.5 days per month.
```
 
PolicyLens-Mini retrieves this policy information and returns it to the user.
 
---
## 8. Additional Supported Questions
 
I can also demonstrate questions across different policy areas.
 
### Paid Time Off
 
```text
How much unused PTO can roll over?
```
 
Expected information:
 
```text
Unused PTO rolls over up to 5 days per calendar year.
```
 
### Information Security
 
```text
How often must passwords be changed?
```
 
Expected information:
 
```text
Passwords must be changed every 90 days.
```
 
### Remote Work
 
```text
During what hours must remote employees be available online?
```
 
Expected information:
 
```text
9 AM to 3 PM EST.
```
 
### Code of Conduct
 
```text
What conduct is strictly prohibited?
```
 
The system retrieves the relevant prohibition from the Code of Conduct.
 
These examples demonstrate retrieval across different policy topics.
 
---
## 9. Unsupported-Question Guardrail
 
PolicyLens-Mini should not return an unrelated sentence simply because some words overlap with the question.
 
I will demonstrate this with a question whose answer is not contained in the relevant policy.
 
Example:
 
```text
What antivirus software must employees install?
```
 
The Information Security Policy does not specify an antivirus product.
 
PolicyLens-Mini should therefore return:
 
```text
No relevant policy information was found.
```
 
The response should indicate:
 
```text
matched = false
```
 
This demonstrates the system's relevance guardrail.
 
---
## 10. Retrieval Design
 
PolicyLens-Mini uses deterministic retrieval rather than generative answer creation.
 
The retrieval process includes:
 
```text
Question
|
Tokenization
|
Query Expansion
|
TF-IDF-Style Weighting
|
Cosine Similarity
|
Best Candidate
|
Relevance Guardrail
|
Answer or Rejection
```
 
A relevance threshold of:
 
```text
0.20
```
 
is used as part of the match decision.
 
The implementation also contains logic for policy headings and section-level questions.
 
---
## 11. FastAPI Demonstration
 
I will now show the FastAPI interactive documentation.
 
The application exposes three main endpoints:
 
```text
GET /health
POST /upload
POST /ask
```
 
The `/health` endpoint confirms that the backend service is operational.
 
The `/upload` endpoint accepts the policy PDF and extracts its text.
 
The `/ask` endpoint processes natural-language policy questions using the retrieval system.
 
---
 
## 12. Automated Evaluation
 
Automated evaluation is an important part of PolicyLens-Mini.
 
The evaluation script is located at:
 
```text
app/eval/run_eval.py
```
 
Evaluation results are stored in:
 
```text
evaluation/eval_results.json
```
 
The controlled evaluation contains:
 
```text
20 test cases
4 policy documents
```
 
The four evaluated policy areas are:
 
- Paid Time Off
- Information Security
- Remote Work
- Code of Conduct
 
---
## 13. Baseline Evaluation
 
The baseline retrieval implementation achieved:
 
```text
Correct: 15/20
Accuracy: 75.00%
```
 
The evaluation exposed retrieval weaknesses involving:
 
- Policy headings
- Vocabulary mismatch
- Unsupported questions
- Selection between related policy sentences
 
These failures were used to guide engineering improvements.
 
---
 
## 14. Retrieval Improvements
 
Based on the evaluation findings, I improved the retrieval implementation.
 
The improvements included:
 
- Excluding Markdown headings from normal answer candidates
- Increasing the relevance threshold from 0.10 to 0.20
- Adding limited deterministic query expansion
- Improving unsupported-question rejection
- Improving handling of policy-level questions
- Returning policy content rather than only matching headings
 
The same controlled evaluation was then executed again.
 
---
## 15. Final Evaluation
 
The final automated evaluation produced:
 
```text
Correct: 20/20
Accuracy: 100.00%
```
 
This represents an improvement from:
 
```text
15/20 = 75%
```
 
to:
 
```text
20/20 = 100%
```
 
The improvement is:
 
```text
+5 correctly handled cases
+25 percentage points
```
 
The 100% result applies specifically to the controlled 20-case evaluation suite and should not be interpreted as universal accuracy across arbitrary policy documents and questions.
 
---
## 16. Iterative Engineering Process
 
PolicyLens-Mini demonstrates an evaluation-driven engineering workflow:
 
```text
Implement
|
Test
|
Evaluate
|
Identify Failure
|
Improve
|
Regression Test
|
Validate
```
 
After implementing additional policy-section handling, I reran the complete evaluation suite.
 
The result remained:
 
```text
20/20
100%
```
 
This regression test confirmed that the additional retrieval capability did not break the previously validated evaluation cases.
 
---
 
## 17. Software Engineering Design
 
The project separates responsibilities across several components:
 
- Frontend presentation
- API routing
- PDF processing
- Retrieval
- Similarity scoring
- Guardrail logic
- Automated evaluation
- Deployment configuration
 
This separation supports maintainability, debugging, testing, and independent deployment of the frontend and backend.
 
---
## 18. GitHub Repository
 
I will now show the PolicyLens-Mini GitHub repository.
 
The repository contains:
 
```text
app/
architecture/
backend/
data/
demo/
evaluation/
frontend/
```
 
It also contains key project documentation including:
 
```text
README.md
design-and-evaluation.md
evaluation_set.md
ai-tooling.md
```
 
Git is used throughout development to track implementation and documentation changes.
 
---
 
## 19. CI/CD and Deployment
 
PolicyLens-Mini uses separate deployment platforms for its frontend and backend.
 
The backend deployment is configured for Render.
 
The frontend deployment is configured for Vercel.
 
I will show the deployment dashboards and successful deployment evidence.
 
I will also show the GitHub Actions and repository configuration used as part of the project's CI/CD workflow.
 
---
## 20. Agile Development
 
PolicyLens-Mini was developed iteratively using agile software engineering practices.
 
Development activities included:
 
- Backlog management
- User stories
- Sprint planning
- Implementation tasks
- Testing
- Debugging
- Evaluation
- Documentation
- Deployment activities
 
I will show the project task board as evidence of this development process.
 
---
 
## 21. Limitations
 
PolicyLens-Mini intentionally uses lightweight deterministic retrieval.
 
As a result, the system has limitations.
 
The quality of retrieval depends on:
 
- Extracted PDF text quality
- Vocabulary overlap
- Query formulation
- Policy structure
- Similarity threshold
- Available deterministic query expansions
 
The controlled evaluation demonstrates performance on the defined benchmark but does not establish universal accuracy.
 
These limitations provide opportunities for future improvement.
 
---
## 22. Future Improvements
 
Potential future improvements include:
 
- Expanded evaluation datasets
- Additional policy document formats
- Improved section detection
- More sophisticated lexical normalization
- Semantic retrieval
- Improved frontend feedback
- Additional automated integration tests
- Deployment monitoring
 
Any future retrieval enhancement should be evaluated against the existing controlled benchmark to prevent regression.
 
---
 
## 23. Conclusion
 
PolicyLens-Mini demonstrates an end-to-end software engineering solution involving:
 
- PDF ingestion
- Text extraction
- Natural-language policy questions
- Deterministic information retrieval
- TF-IDF-style weighting
- Cosine similarity
- Policy-section retrieval
- Relevance guardrails
- Frontend-backend integration
- Automated evaluation
- Regression testing
- CI/CD
- Deployment
- Agile development
- Technical documentation
 
The project improved from a baseline evaluation of:
 
```text
15/20
75%
```
 
to a final controlled evaluation of:
 
```text
20/20
100%
```
 
The final system also successfully handles broader policy-level questions by returning substantive policy content rather than only section headings.
 
Thank you for viewing my PolicyLens-Mini MSSE Capstone demonstration.