PolicyLens-Mini: Design and Evaluation
1. Purpose and Scope
PolicyLens-Mini is a full-stack policy-document analysis application developed for the MSSE Capstone Project.

The system allows a user to upload a PDF policy document and ask natural-language questions about its contents.

The primary engineering objectives were to create a system that is:

Lightweight
Deterministic
Reproducible
Testable
Explainable
Deployable as a web application
The core retrieval functionality does not depend on an external large language model. Instead, PolicyLens-Mini uses deterministic lexical retrieval and relevance controls.

2. System Requirements
The primary functional requirements were:

Accept PDF policy documents.
Extract textual content from uploaded PDFs.
Accept natural-language questions.
Retrieve relevant policy information.
Support complete policy-section retrieval.
Reject questions not supported by the uploaded document.
Provide a browser-based user interface.
Provide a backend API for document processing and retrieval.
Support reproducible testing and evaluation.
Operate as a deployed web application.
The principal non-functional requirements were:

Maintainability
Reproducibility
Transparency
Testability
Separation of concerns
Deployment flexibility
Predictable retrieval behavior
3. Architecture Overview
PolicyLens-Mini uses a separated frontend and backend architecture.

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
 +--> Tokenization
 |
 +--> TF-IDF-Style Weighting
 |
 +--> Cosine Similarity
 |
 +--> Relevance Guardrail
 |
 +------ Match ------> Policy Answer
 |
 +---- No Match -----> Rejection
The frontend is responsible for user interaction.

The backend is responsible for PDF processing, retrieval, relevance evaluation, and API responses.

This separation allows presentation concerns and document-processing concerns to evolve independently.

4. Architecture Decisions
Separated Frontend and Backend
The application uses independent frontend and backend components.

This decision provides:

Separation of concerns
Independent deployment
Modular development
Easier backend testing
Easier replacement or modification of the user interface
The frontend communicates with the backend through HTTP endpoints rather than directly executing retrieval logic.

Deterministic Retrieval
The core retrieval pipeline was intentionally implemented without requiring an external LLM.

This decision was made to provide:

Reproducible behavior
Transparent similarity scoring
Predictable testing
Lower runtime complexity
Easier debugging
Reduced dependency on external inference services
5. Technology Selection and Rationale
Next.js, React, and TypeScript
Next.js and React were selected for the frontend because they provide a modular component-based approach to web application development.

TypeScript provides additional type checking for frontend implementation.

FastAPI
FastAPI was selected for the backend API.

It provides a clear separation between HTTP routes and retrieval/document-processing functionality.

The backend exposes:

GET  /health
POST /upload
POST /ask
Python
Python was selected for document processing and retrieval because it provides straightforward support for text processing, PDF extraction, mathematical calculations, and automated evaluation.

PyPDF
PyPDF is used for extracting textual content from uploaded PDF files.

Git and GitHub
Git and GitHub provide version control, repository management, and project history.

GitHub Projects
GitHub Projects is used to maintain the Agile task board and document implementation work across development sprints.

6. Frontend Design
The frontend provides the primary user interaction layer.

Its responsibilities include:

PDF selection
PDF upload
Question entry
API communication
Displaying retrieved answers
Displaying unsupported-question responses
Retrieval logic is not implemented in the frontend.

Keeping retrieval logic within the backend avoids duplicating document-processing behavior across application layers.

7. Backend Design
The FastAPI backend provides the application's processing and retrieval services.

Major backend responsibilities include:

Receiving PDF uploads
Extracting PDF text
Receiving natural-language questions
Detecting explicit policy-name requests
Generating retrieval candidates
Calculating similarity
Applying relevance rules
Returning supported answers
Rejecting unsupported questions
The backend implementation is separated into modules responsible for routes, retrieval, application configuration, and PDF processing.

This modular organization improves maintainability and testability.

8. PDF Processing
Uploaded PDF documents are processed by the backend.

The processing workflow is:

PDF Upload
 |
 v
PDF Text Extraction
 |
 v
Extracted Policy Text
 |
 v
Retrieval Pipeline
The extracted text becomes the source corpus used for answering questions.

For reproducible examiner testing, the repository includes a demonstration policy handbook.

9. Retrieval Architecture
The factual retrieval pipeline follows this sequence:

Question
 |
 v
Tokenization
 |
 v
Candidate Policy Content
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
Relevance Threshold
 |
 +--> Relevant ----> Return Answer
 |
 +--> Insufficient -> Reject
The objective is to determine which candidate policy content is most lexically relevant to the user's question.

TF-IDF-Style Weighting
Term weighting reduces the influence of common terms while increasing the relative importance of more informative terms.

Cosine Similarity
Cosine similarity provides a deterministic measure of similarity between the user question and candidate policy content.

The use of deterministic scoring makes evaluation repeatable.

10. Software and Architectural Patterns
Several software-engineering patterns are reflected in PolicyLens-Mini.

Separation of Concerns
The frontend handles presentation and interaction.

The backend handles document extraction and retrieval.

This prevents retrieval behavior from becoming coupled to the user interface.

Layered Processing
The retrieval pipeline is divided into distinct stages:

Extraction
    ↓
Processing
    ↓
Retrieval
    ↓
Relevance Evaluation
    ↓
Response
This allows individual stages to be analyzed and improved independently.

API-Based Client/Server Architecture
The frontend communicates with the backend using HTTP requests.

This allows the frontend and backend to be hosted independently.

Guardrail Pattern
Retrieval does not automatically mean that an answer should be returned.

A relevance decision is applied before the final response.

This separates candidate retrieval from answer acceptance.

11. Relevance Guardrails
One important engineering objective was preventing plausible but unsupported answers.

PolicyLens-Mini applies a relevance threshold to factual retrieval.

The final threshold used by the system is:

0.20
If sufficient supporting evidence exists, the system can return:

{
  "answer": "Relevant policy information",
  "score": 0.446,
  "matched": true
}
If supporting evidence is insufficient:

{
  "answer": "No relevant policy information was found.",
  "score": 0.0,
  "matched": false
}
Explicit unsupported policy-name questions use an additional guardrail.

For example:

What is Cook Policy?
is rejected when no corresponding policy exists in the uploaded document.

This distinction reduces inappropriate matching between unrelated policy names and document content.

12. Testing Strategy
Testing was approached as an iterative engineering activity rather than a final verification step.

The testing strategy included:

Functional testing
Retrieval testing
Supported-question testing
Unsupported-question testing
Regression evaluation
Deployment verification
API behavior verification
Automated evaluation was particularly important because retrieval behavior can appear reasonable during isolated manual testing while still failing across a broader question set.

A controlled evaluation set therefore provided repeatable evidence of system behavior.

13. Automated Evaluation
PolicyLens-Mini includes a reproducible automated evaluation workflow.

The controlled evaluation contains:

20 test cases
4 policy categories
The policy categories include:

Paid Time Off
Information Security
Remote Work
Code of Conduct
The evaluation set includes both supported and intentionally unsupported questions.

Machine-readable evaluation results are retained in:

evaluation/eval_results.json
Keeping the evaluation set and results within the repository provides reproducible evidence and allows identical tests to be rerun following retrieval changes.

14. Baseline Evaluation
The initial controlled evaluation produced:

Correct: 15/20
Accuracy: 75.00%
The baseline was retained rather than reporting only the final result.

This made it possible to measure whether retrieval changes actually improved system behavior.

15. Failure Analysis
Analysis of the five unsuccessful baseline cases identified multiple retrieval problems.

The observed failure categories included:

Policy headings being returned as factual answers
Unsupported questions receiving inappropriate matches
Vocabulary mismatch between questions and source text
Incorrect selection between closely related policy statements
This demonstrated that selecting lexically related content does not necessarily guarantee a correct or appropriately grounded answer.

The baseline evaluation therefore became an input to the next development iteration.

16. Retrieval Improvements
The failure analysis resulted in several retrieval changes.

Heading Exclusion
Markdown headings were excluded from normal factual-answer candidates.

This reduced cases where a heading was selected instead of substantive policy content.

Relevance Threshold Refinement
The relevance threshold was increased from:

0.10
to:

0.20
The objective was to reduce weak matches.

Deterministic Query Expansion
Limited deterministic query expansion was introduced to reduce specific vocabulary mismatches between natural-language questions and policy wording.

Unsupported-Question Handling
Guardrail behavior was strengthened so unsupported queries could be rejected rather than forced into an existing policy match.

Explicit Policy-Name Detection
Questions explicitly requesting named policies received specialized handling.

Complete Policy-Section Retrieval
When a valid policy is explicitly requested, PolicyLens-Mini can return the associated policy-section content instead of only one candidate sentence.

17. Final Evaluation
Following retrieval improvements, the same controlled evaluation was rerun.

The final result was:

Correct: 20/20
Accuracy: 100.00%
This represents an improvement from:

15/20
75.00%
to:

20/20
100.00%
The same controlled test set was used for baseline and final comparison, allowing the effect of retrieval changes to be evaluated consistently.

The 100% result refers specifically to this controlled 20-case evaluation set and should not be interpreted as proof of perfect performance for every possible policy document or question.

18. CI/CD and Deployment
PolicyLens-Mini uses Git-based source control and cloud deployment practices.

The engineering workflow incorporates:

Git
GitHub
GitHub Actions
Automated evaluation
Vercel frontend deployment
Render backend deployment
The deployed architecture is:

Browser
 |
 v
Vercel
Next.js Frontend
 |
 | HTTPS / HTTP API
 v
Render
FastAPI Backend
Separating frontend and backend deployment allows the web interface and retrieval service to be managed separately.

The production application is available at:

https://policylens-mini.vercel.app
19. Deployment Strategy and Cost Implications
PolicyLens-Mini uses a cloud-based deployment model with the Next.js frontend hosted through Vercel and the FastAPI backend hosted through Render.

Cloud deployment was selected because the Capstone application needs to be accessible to an examiner without requiring local environment configuration.

The separated deployment model also maintains the architectural boundary between the frontend and backend.

Current Deployment Approach
The project uses hosting tiers appropriate for its Capstone demonstration workload.

This approach minimizes infrastructure requirements while maintaining a publicly accessible application.

Alternative: Paid Cloud Hosting
A production system with increased traffic or reliability requirements could move to paid cloud infrastructure.

Potential benefits include:

Increased compute resources
Higher service limits
Additional scalability options
Additional operational capabilities
The trade-off is recurring infrastructure expenditure.

The exact cost would depend on the selected provider, traffic, compute consumption, storage, bandwidth, and availability requirements.

Alternative: Self-Hosted Infrastructure
The application could also be deployed to self-managed infrastructure.

This could provide additional operational control, but cost considerations could include:

Server hardware or virtual-machine costs
Network infrastructure
Electricity
Maintenance
Monitoring
Security administration
Backup management
Engineering/administrative time
Cost Decision
For the current PolicyLens-Mini Capstone workload, the existing Vercel and Render deployment provides an appropriate balance between:

Accessibility
Deployment simplicity
Separation of concerns
Infrastructure requirements
Cost
If usage increased significantly, the hosting strategy would need to be reconsidered based on measurable workload, reliability, capacity, and operating-cost requirements.

No fixed future hosting cost is specified because actual costs would depend on the selected infrastructure and workload.

20. Engineering Lessons
The baseline evaluation demonstrated that retrieval relevance and answer correctness are separate concerns.

Retrieval relevance
!=
Answer correctness
!=
Groundedness
The project also demonstrated the value of iterative testing.

The development sequence was:

Implement
 |
 v
Evaluate
 |
 v
Identify Failures
 |
 v
Improve Retrieval
 |
 v
Rerun Identical Tests
 |
 v
Compare Results
The measured improvement from:

15/20
to:

20/20
provides concrete evidence of this iterative engineering process.

Another important lesson was that retrieval systems require explicit handling of unsupported queries.

Returning the highest-scoring candidate alone does not establish that the candidate is sufficiently relevant.

The relevance guardrail therefore became an important system-level control separating retrieval from answer acceptance.

21. Conclusion
PolicyLens-Mini implements an end-to-end policy-document question-answering workflow using:

Next.js
React
TypeScript
Python
FastAPI
PDF ingestion
Text extraction
Deterministic lexical retrieval
TF-IDF-style weighting
Cosine similarity
Deterministic query expansion
Policy-section detection
Relevance guardrails
Automated evaluation
Git-based version control
CI/CD practices
Cloud deployment
The controlled baseline evaluation initially produced:

15/20 correct
75.00% accuracy
Analysis of the five unsuccessful cases led to improvements in heading handling, relevance thresholds, query expansion, unsupported-question rejection, policy-name detection, and policy-section retrieval.

After those changes, the same controlled evaluation produced:

20/20 correct
100.00% evaluation accuracy
This baseline-to-final comparison provides reproducible evidence that testing directly informed improvements to the PolicyLens-Mini implementation.

The project demonstrates the complete engineering lifecycle from architecture and implementation through testing, iterative improvement, deployment, documentation, and reproducible evaluation.