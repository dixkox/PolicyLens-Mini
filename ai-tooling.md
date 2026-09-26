# AI Tooling Usage - PolicyLens-Mini
 
## 1. Overview
 
This document describes how AI-assisted tools were used during the development of PolicyLens-Mini.
 
PolicyLens-Mini is a lightweight policy analysis application built with a Next.js frontend and FastAPI backend. It supports PDF policy upload, text extraction, natural-language questions, deterministic lexical retrieval, similarity scoring, and relevance guardrails.
 
AI tools were used as engineering assistants for development, debugging, architecture exploration, evaluation, and documentation.
 
Generated suggestions were reviewed, tested, modified, or rejected before inclusion in the final project.
 
---
 
## 2. AI Tools Used
 
### 2.1 Microsoft Copilot
 
Microsoft Copilot assisted with:
 
- FastAPI debugging
- Frontend-backend integration
- Retrieval debugging
- Evaluation analysis
- Guardrail improvements
- Git and repository cleanup
- Architecture review
- Documentation review
- Capstone preparation
 
Copilot was particularly useful for comparing implementation behavior against evaluation results and identifying inconsistencies between older project documentation and the current PolicyLens-Mini implementation.
 
---
 
### 2.2 Cursor IDE
 
Cursor was used as an AI-assisted development environment for:
 
- Project scaffolding
- Python development
- TypeScript development
- Refactoring
- File creation and modification
- Import and path debugging
- Backend integration
- Frontend development
- Repository reconstruction
- Code cleanup
 
AI-generated code changes were reviewed and tested before being retained.
 
---
 
### 2.3 Gemini
 
Gemini was used during earlier development and experimentation for:
 
- Architecture exploration
- Retrieval design discussions
- Policy dataset generation
- Evaluation-question development
- Documentation drafting
- Exploring potential RAG improvements
 
Some proposed approaches were intentionally not used in the final implementation because they introduced unnecessary complexity for PolicyLens-Mini.
 
---
 
## 3. AI-Assisted Architecture Development
 
AI tools assisted with evaluating architectural alternatives.
 
The final PolicyLens-Mini architecture uses:
 
```text
Next.js Frontend
|
v
FastAPI Backend
|
+---- PDF Extraction
|
+---- Deterministic Retrieval
|
v
TF-IDF Weighting
|
v
Cosine Similarity
|
v
Relevance Guardrail
|
+----+----+
| |
Answer Reject
```
 
The final architecture was selected and refined through implementation, testing, and evaluation.
 
---
 
## 4. AI-Assisted Debugging
 
AI assistance was used to investigate:
 
- FastAPI routing
- API request formatting
- CORS configuration
- Frontend fetch behavior
- Python environments
- Next.js integration
- Retrieval failures
- Similarity scoring
- Git cleanup
- Repository organization
 
AI debugging suggestions were treated as hypotheses and verified against actual system behavior.
 
---
 
## 5. AI-Assisted Evaluation
 
AI tools assisted with developing and reviewing the automated evaluation workflow.
 
The final controlled evaluation uses:
 
```text
app/eval/run_eval.py
```
 
Results are written to:
 
```text
evaluation/eval_results.json
```
 
The evaluation contains:
 
- 20 controlled test cases
- 4 policy documents
- Supported policy questions
- Intentionally unsupported questions
- Expected-answer checks
- Match-status checks
- Similarity scores
- Latency measurements
 
---
 
## 6. Evaluation-Driven Engineering
 
The initial controlled evaluation produced:
 
```text
Correct: 15/20
Accuracy: 75.00%
```
 
AI assistance helped analyze the five failures.
 
Identified issues included:
 
- Markdown headings becoming answer candidates
- Weak rejection of unsupported questions
- Vocabulary mismatch
- Incorrect selection between related policy sentences
 
The findings were then used to guide backend improvements.
 
---
 
## 7. Retrieval Improvements
 
The retrieval implementation was improved by:
 
### Heading Exclusion
 
Markdown headings were removed from eligible answer candidates.
 
### Stronger Relevance Guardrail
 
The relevance threshold was increased from:
 
```text
0.10
```
 
to:
 
```text
0.20
```
 
to reduce weak matches.
 
### Deterministic Query Expansion
 
A limited query-expansion mapping was introduced for selected vocabulary mismatches.
 
### Improved Abstention
 
Unsupported questions with insufficient evidence are rejected rather than returning weakly related policy content.
 
---
 
## 8. Final Evaluation
 
The same 20 controlled test cases were rerun after the backend improvements.
 
Final result:
 
```text
Correct: 20/20
Accuracy: 100.00%
```
 
The measured improvement was:
 
```text
Baseline: 15/20 (75%)
Final: 20/20 (100%)
Change: +25 percentage points
```
 
The 100% result applies specifically to the controlled 20-case evaluation suite and is not presented as universal system accuracy.
 
---
 
## 9. AI-Assisted Documentation
 
AI tools assisted in reviewing and improving:
 
```text
README.md
backend/README.md
ai-tooling.md
design-and-evaluation.md
evaluation_set.md
evaluation/evaluation.md
evaluation/evaluation_summary.md
demo/demo_script.md
demo/demo_steps.md
```
 
A major documentation task involved removing obsolete material from the earlier Policy-RAG-App implementation and aligning the repository with PolicyLens-Mini.
 
---
 
## 10. Limitations of AI Assistance
 
AI assistance introduced several challenges.
 
### Overly Complex Suggestions
 
Some suggestions involved technologies or architectures that were unnecessary for the final lightweight implementation.
 
### Incorrect Debugging Suggestions
 
AI-generated diagnoses were not always correct and required verification.
 
### Documentation Drift
 
Earlier generated documentation continued to describe previous project architecture and evaluation results after the implementation had changed.
 
### Overgeneralization
 
Evaluation results require careful wording.
 
For example:
 
```text
20/20 on the controlled evaluation suite
```
 
does not mean:
 
```text
100% accurate for every possible policy and question
```
 
Human review was necessary to maintain this distinction.
 
---
 
## 11. Human Oversight
 
AI-generated material was treated as engineering assistance rather than authoritative output.
 
Human oversight included:
 
- Reviewing code
- Running the application
- Testing APIs
- Inspecting retrieval results
- Reviewing similarity scores
- Running automated evaluation
- Comparing baseline and final results
- Verifying Git changes
- Correcting documentation
- Rejecting unsuitable suggestions
 
Final responsibility for the PolicyLens-Mini implementation and submission remains with the project author.
 
---
 
## 12. Academic Integrity
 
AI-assisted tools were used transparently during software engineering activities including:
 
- Brainstorming
- Code development
- Debugging
- Refactoring
- Testing
- Evaluation analysis
- Documentation
 
AI-generated material was reviewed and adapted rather than assumed to be correct.
 
The project documentation records the use of AI assistance and the engineering verification performed afterward.
 
---
 
## 13. Engineering Lesson
 
One of the most important lessons from the project was that AI assistance itself requires verification.
 
PolicyLens-Mini followed an iterative process:
 
```text
Implement
|
Test
|
Evaluate
|
Identify Failures
|
Improve
|
Retest
|
Document
```
 
The improvement from 15/20 to 20/20 provides a concrete example of evaluation-driven development.
 
---
 
## 14. Conclusion
 
AI-assisted engineering contributed significantly to PolicyLens-Mini through:
 
- Development support
- Debugging
- Architecture exploration
- Retrieval analysis
- Evaluation development
- Documentation
- Repository cleanup
 
The project also demonstrated the importance of combining AI assistance with testing, engineering judgment, source control, evaluation, and human verification.
 
The final PolicyLens-Mini implementation therefore represents human-directed software engineering supported by AI-assisted development tools.