PolicyLens-Mini Capstone Demonstration Script
1. Introduction
Hello, my name is Tinubu Damilola, and this is my MSSE Capstone demonstration of PolicyLens-Mini.

PolicyLens-Mini is a lightweight policy analysis web application that allows users to upload a PDF policy document and ask natural-language questions about its contents.

In this demonstration, I will show the application, architecture, major user workflows, retrieval pipeline, guardrails, evaluation, deployment, CI/CD, and repository.

2. Problem and Solution
Organizations may maintain important policies in documents that require users to manually search for relevant information.

PolicyLens-Mini provides a simpler workflow:

Upload a policy PDF.
Extract the policy text.
Ask a natural-language question.
Retrieve the most relevant policy information.
Reject questions when sufficient supporting information cannot be identified.
3. Architecture
PolicyLens-Mini consists of:

Next.js and TypeScript frontend
FastAPI backend
PDF text extraction
Sentence-level document segmentation
Deterministic lexical retrieval
TF-IDF weighting
Cosine similarity
Relevance guardrails
I will show:

architecture/architecture_diagram.png

The frontend communicates with the backend through the /upload and /ask endpoints.

4. Application Demonstration

I will now open PolicyLens-Mini.

First, I will upload a sample policy PDF.

After upload, PolicyLens-Mini extracts the policy text and displays it in the application.

5. Supported Question

I will now ask a question whose answer exists in the uploaded policy.

For example, using the PTO policy:

Plain Text
How fast do employees accrue PTO?
Show more lines

The expected policy information is:

Plain Text
1.5 days per month
Show more lines

PolicyLens-Mini retrieves the relevant policy sentence and returns it to the frontend.

6. Additional Supported Questions

I will demonstrate several additional question types.

Examples include:

Plain Text
How much unused PTO can roll over?
Show more lines
Plain Text
How often must passwords be changed?
Show more lines
Plain Text
During what hours must remote employees be available online?
Show more lines
Plain Text
What conduct is strictly prohibited?
``
Show more lines

These demonstrate retrieval across different policy topics.

7. Guardrail Demonstration

Next, I will demonstrate an intentionally unsupported question.

Example:

Plain Text
What disciplinary action is taken for violating the code?
Show more lines

The Code of Conduct used by the evaluation does not contain that information.

PolicyLens-Mini should therefore return:

Plain Text
No relevant policy information was found.
Show more lines

with:

Plain Text
matched = false
Show more lines

This demonstrates the relevance guardrail and abstention behavior.

8. API Demonstration

I will briefly show the FastAPI interactive documentation.

The main endpoints are:

Plain Text
GET /health
POST /upload
POST /ask
Show more lines

The API separates policy processing and retrieval from the Next.js presentation layer.

9. Evaluation

I will now show the automated evaluation.

The evaluator is located at:

Plain Text
app/eval/run_eval.py
Show more lines

The recorded results are stored in:

Plain Text
evaluation/eval_results.json
Show more lines

The controlled evaluation contains 20 cases covering:

Paid Time Off
Information Security
Remote Work
Code of Conduct

The initial evaluation produced:

Plain Text
15/20 correct
75% accuracy
Show more lines

The failures identified weaknesses involving headings, weak lexical matches, and unsupported questions.

After improving the retrieval implementation, the same evaluation produced:

Plain Text
20/20 correct
100% accuracy
Show more lines

The 100% result applies specifically to this controlled 20-case evaluation suite.

10. Engineering Improvement

The evaluation directly informed changes to the retrieval system.

Improvements included:

Removing Markdown headings from answer candidates
Strengthening the relevance threshold
Adding limited deterministic query expansion
Improving unsupported-question rejection

This demonstrates an iterative engineering process:

Plain Text
Implement
Evaluate
Identify failures
Improve
Retest
Compare
Show more lines
11. Software Engineering Design

The project separates responsibilities between:

Frontend presentation
REST API routing
PDF processing
Retrieval
Similarity scoring
Guardrail logic
Automated evaluation

This separation improves maintainability and testability.

12. CI/CD and Deployment

I will show the project's deployment and CI/CD artifacts.

Git and GitHub are used for source control.

I will also demonstrate the deployed application and supporting configuration included in the repository.

13. Agile Development

I will show the project task board and explain how user stories and engineering work were tracked during development.

14. Repository

Finally, I will show the PolicyLens-Mini repository.

The repository includes:

Backend source code
Frontend source code
Architecture artifacts
Evaluation artifacts
Deployment configuration
Demo documentation
Design and testing documentation
AI tooling documentation
15. Conclusion

PolicyLens-Mini demonstrates an end-to-end policy analysis workflow involving:

PDF ingestion
Text extraction
Deterministic information retrieval
Similarity scoring
Relevance guardrails
Frontend-backend integration
Automated evaluation
Deployment
Software engineering documentation

The evaluation-driven improvement from 15/20 to 20/20 demonstrates how testing was used to identify and correct weaknesses in the implementation.

Thank you for viewing my PolicyLens-Mini MSSE Capstone demonstration.


### Improvements
Removed the `Â` corruption, fixed spacing, replaced obsolete Policy-RAG examples, and synchronized the script with the final **20-case evaluation and 20/20 result**.