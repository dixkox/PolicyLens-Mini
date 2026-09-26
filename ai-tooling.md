# AI Tooling Usage - PolicyLens-Mini
 
## 1. Overview
 
This document describes the use of AI-assisted development tools during the design, implementation, debugging, testing, documentation, and refinement of PolicyLens-Mini.
 
PolicyLens-Mini is a lightweight policy analysis application built with a Next.js frontend and FastAPI backend. The application supports PDF policy upload, document processing, natural-language questions, deterministic retrieval, similarity scoring, and relevance guardrails.
 
AI tools were used as engineering assistants. Generated suggestions and code were reviewed, tested, modified, or rejected as necessary before inclusion in the project.
 
---
 
## 2. AI Tools Used
 
### 2.1 Microsoft Copilot
 
Microsoft Copilot was used throughout development for:
 
- Debugging FastAPI errors
- Investigating frontend-backend integration issues
- Reviewing retrieval logic
- Improving guardrails
- Troubleshooting Git and repository structure
- Reviewing evaluation results
- Improving project documentation
- Reviewing Capstone deliverables
 
A particularly useful role was identifying inconsistencies between documentation and the actual PolicyLens-Mini implementation.
 
### 2.2 Cursor
 
Cursor was used as an AI-assisted development environment for:
 
- Project scaffolding
- Python development
- Refactoring
- Creating and modifying project files
- Troubleshooting imports and paths
- Backend integration
- Frontend development
- Repository reconstruction and cleanup
 
AI-generated changes were reviewed and tested before being retained.
 
### 2.3 Gemini
 
Gemini was used during earlier stages of development for:
 
- Architecture exploration
- Retrieval and RAG experimentation
- Policy dataset generation
- Evaluation-question development
- Documentation drafts
- Exploring possible system improvements
 
Some suggested approaches were intentionally not included in the final implementation because they added unnecessary complexity.
 
---
 
## 3. How AI Assisted Development
 
### Architecture
 
AI tools helped compare architectural alternatives and reason about frontend-backend separation, PDF processing, retrieval, scoring, and guardrails.
 
The final architecture was selected and refined based on implementation requirements and observed system behaviour.
 
### Development and Debugging
 
AI assistance was particularly useful for:
 
- FastAPI routing problems
- API requests and responses
- CORS and frontend-backend communication
- Python dependency issues
- Next.js integration
- Git repository cleanup
- Environment configuration
- Retrieval debugging
 
### Documentation
 
AI tools assisted with drafts and reviews of:
 
- `README.md`
- `design-and-evaluation.md`
- `evaluation/evaluation.md`
- `evaluation/evaluation_summary.md`
- `demo/demo_script.md`
- `demo/demo_steps.md`
- `ai-tooling.md`
 
Documentation was reviewed against the actual implementation because AI-generated documentation occasionally reflected older versions of the project.
 
### Evaluation
 
AI assistance was used to:
 
- Review evaluation outputs
- Identify incorrect and unsupported answers
- Examine retrieval failure modes
- Review latency measurements
- Distinguish retrieval relevance from final-answer correctness
- Suggest improvements to the evaluation methodology
 
Unsuccessful evaluation cases are retained as engineering evidence rather than being removed merely to improve reported performance.
 
---
 
## 4. Benefits
 
AI-assisted development improved productivity in several areas:
 
- Faster debugging
- Faster implementation and refactoring
- Improved code review
- Architecture exploration
- Documentation development
- Evaluation analysis
- Repository cleanup
 
AI assistance was especially useful during troubleshooting because multiple possible causes could be examined quickly before testing a solution.
 
---
 
## 5. Limitations Observed
 
### Overly Complex Suggestions
 
AI tools sometimes proposed solutions that were more complex than required, including semantic retrieval, vector databases, reranking, and additional frameworks.
 
These suggestions were evaluated rather than automatically implemented.
 
### Incorrect Diagnoses
 
AI-generated debugging suggestions were not always correct. Proposed solutions therefore required testing against the actual application.
 
### Documentation Drift
 
A significant limitation was documentation drift.
 
Earlier AI-generated documentation continued to describe the previous Policy-RAG-App architecture after PolicyLens-Mini had evolved.
 
This required a final repository audit to ensure that documentation, architecture diagrams, demo materials, evaluation artifacts, and implementation accurately represented the same system.
 
### Evaluation Interpretation
 
AI-generated evaluation summaries could overstate system performance if outputs were not independently checked.
 
For this reason, PolicyLens-Mini evaluation results are reviewed against the underlying recorded outputs.
 
---
 
## 6. Human Oversight
 
AI-generated output was treated as a development aid rather than authoritative project output.
 
Engineering oversight included:
 
- Reviewing generated code
- Running and testing the application
- Verifying API behaviour
- Reviewing architecture changes
- Inspecting Git changes
- Reviewing evaluation results
- Correcting inaccurate documentation
- Rejecting inappropriate technical suggestions
 
Final responsibility for the submitted PolicyLens-Mini project remains with the project author.
 
---
 
## 7. Academic Integrity
 
AI tools were used to assist software engineering activities such as brainstorming, debugging, code development, documentation, and analysis.
 
AI assistance is documented transparently in this file.
 
Generated material was reviewed and adapted to the project rather than assumed to be correct. Project evaluation also records identified limitations and unsuccessful cases instead of presenting only successful results.
 
---
 
## 8. Conclusion
 
AI-assisted engineering contributed substantially to the development of PolicyLens-Mini, particularly in debugging, implementation support, architecture exploration, documentation, and evaluation analysis.
 
The development process also demonstrated an important engineering lesson: AI-generated code, documentation, and analysis require verification.
 
PolicyLens-Mini therefore combines AI-assisted development with testing, human review, source control, evaluation, and iterative engineering.