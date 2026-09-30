AI Tooling Usage - PolicyLens-Mini
1. Overview
This document describes how AI-assisted tools were used during the development of PolicyLens-Mini.

PolicyLens-Mini is a lightweight policy analysis application built with a Next.js frontend and FastAPI backend. It supports PDF policy upload, text extraction, natural-language questions, deterministic lexical retrieval, similarity scoring, policy-section retrieval, and relevance guardrails.

AI tools were used as engineering assistants for:

Development
Debugging
Architecture exploration
Evaluation
Documentation
Repository organization
AI-generated suggestions were reviewed, tested, modified, or rejected before inclusion in the final project.

2. AI Tools Used
2.1 Microsoft Copilot
Microsoft Copilot assisted with:

FastAPI debugging
Frontend-backend integration
Retrieval debugging
Evaluation analysis
Guardrail improvements
Git and repository cleanup
Architecture review
Documentation review
Capstone preparation
Copilot was particularly useful for comparing implementation behavior with evaluation results and identifying inconsistencies between older project documentation and the final PolicyLens-Mini implementation.

2.2 Cursor IDE
Cursor was used as an AI-assisted development environment for:

Project scaffolding
Python development
TypeScript development
Refactoring
File creation and modification
Import and path debugging
Backend integration
Frontend development
Repository reconstruction
Code cleanup
AI-generated code changes were reviewed and tested before being retained.

2.3 Gemini
Gemini was used during earlier development and experimentation for:

Architecture exploration
Retrieval design discussions
Policy dataset generation
Evaluation-question development
Documentation drafting
Exploring potential RAG improvements
Some proposed approaches were intentionally not used in the final implementation because they introduced unnecessary complexity for the lightweight PolicyLens-Mini architecture.

3. AI-Assisted Architecture Development
AI tools assisted with evaluating architectural alternatives.

The final architecture uses:

Next.js Frontend
      |
      v
FastAPI Backend
      |
      +--> PDF Extraction
      |
      +--> Deterministic Retrieval
              |
              v
      TF-IDF-Style Weighting
              |
              v
      Cosine Similarity
              |
              v
      Relevance Guardrail
           /       \
          v         v
       Answer     Reject
The final architecture was selected and refined through implementation, testing, and evaluation rather than being accepted solely from AI-generated recommendations.

4. AI-Assisted Debugging
AI assistance was used to investigate:

FastAPI routing
API request formatting
CORS configuration
Frontend fetch behavior
Python environments
Next.js integration
Retrieval failures
Similarity scoring
Git cleanup
Repository organization
AI debugging suggestions were treated as hypotheses and verified against actual application behavior.

5. AI-Assisted Evaluation
AI tools assisted with developing and reviewing the automated evaluation workflow.

The evaluation runner is located at:

app/eval/run_eval.py
Results are stored in:

evaluation/eval_results.json
The controlled evaluation includes:

20 test cases
4 policy categories
Supported policy questions
Intentionally unsupported questions
Expected-answer checks
Match-status checks
Similarity scores
Performance measurements
The evaluation artifacts were retained in the repository to make the testing process reproducible.

6. Evaluation-Driven Engineering
The initial controlled evaluation produced:

Correct: 15/20
Accuracy: 75.00%
AI assistance helped analyze the unsuccessful cases.

Identified problems included:

Markdown headings becoming answer candidates
Weak rejection of unsupported questions
Vocabulary mismatch
Incorrect selection between related policy sentences
These findings were reviewed and used to guide backend improvements.

7. Retrieval Improvements
Evaluation findings resulted in several retrieval improvements.

Heading Exclusion
Markdown headings were removed from eligible factual-answer candidates.

Stronger Relevance Guardrail
The relevance threshold was increased from:

0.10
to:

0.20
to reduce weak matches.

Deterministic Query Expansion
Limited deterministic query expansion was introduced to address selected vocabulary mismatches.

Improved Abstention
Questions without sufficient supporting evidence are rejected instead of returning weakly related policy information.

Policy-Name Detection
Explicit policy-name questions receive specialized handling so that valid policy sections can be distinguished from unsupported policy names.

Policy-Section Retrieval
When a requested policy exists, PolicyLens-Mini can return the associated policy-section content rather than only a single candidate sentence.

8. Final Evaluation
The same controlled 20-case evaluation suite was rerun following the retrieval improvements.

Final result:

Correct: 20/20
Accuracy: 100.00%
Measured improvement:

Baseline: 15/20 (75%)
Final:    20/20 (100%)
Change:   +25 percentage points
The 100% result applies specifically to the controlled 20-case evaluation suite. It is not presented as universal accuracy across every possible policy document or question.

9. AI-Assisted Documentation
AI tools assisted with reviewing and improving project documentation, including:

README.md
backend/README.md
ai-tooling.md
design-and-evaluation.md
evaluation_set.md
evaluation/evaluation.md
evaluation/evaluation_summary.md
demo/demo_script.md
demo/demo_steps.md
One important documentation activity involved removing obsolete material from earlier implementation work and ensuring that the final repository accurately described PolicyLens-Mini.

10. Limitations of AI Assistance
AI assistance introduced several challenges that required human review.

Overly Complex Suggestions
Some recommendations involved technologies or architectures that were unnecessary for the final lightweight implementation.

These suggestions were evaluated and rejected when they did not provide sufficient benefit.

Incorrect Debugging Suggestions
AI-generated diagnoses were not always correct.

Potential fixes therefore required testing against the actual application before being retained.

Documentation Drift
Earlier documentation could become inconsistent with the implementation as the project evolved.

Documentation therefore required comparison against the final source code, evaluation results, and deployed behavior.

Overgeneralization
Evaluation results required careful interpretation.

For example:

20/20 on the controlled evaluation suite
does not mean:

100% accurate for every possible policy document and question
Human review was necessary to maintain this distinction.

11. Human Oversight
AI-generated material was treated as engineering assistance rather than authoritative output.

Human oversight included:

Reviewing generated code
Running the application
Testing API behavior
Inspecting retrieval results
Reviewing similarity scores
Running automated evaluations
Comparing baseline and final results
Verifying Git changes
Reviewing documentation
Correcting inaccurate suggestions
Rejecting unnecessary architectural complexity
AI-assisted tools supported the engineering process, but final technical decisions, testing, verification, repository content, and submission responsibility remained with the project author.

12. Academic Integrity
AI-assisted tools were used transparently during software-engineering activities including:

Brainstorming
Code development
Debugging
Refactoring
Testing
Evaluation analysis
Architecture exploration
Documentation
AI-generated material was reviewed and adapted rather than assumed to be correct.

The project documentation records the role of AI assistance while maintaining human responsibility for implementation, validation, and the final submitted work.

13. Engineering Lessons
One of the most important lessons from the project was that AI assistance itself requires verification.

PolicyLens-Mini followed an iterative engineering process:

Implement
    |
    v
Test
    |
    v
Evaluate
    |
    v
Identify Failures
    |
    v
Improve
    |
    v
Retest
    |
    v
Document
The measured improvement from:

15/20
to:

20/20
provides a concrete example of evaluation-driven development.

The project also demonstrated that AI assistance is most useful when combined with engineering judgment, reproducible testing, source control, and measurable evaluation.

14. Conclusion
AI-assisted engineering contributed to PolicyLens-Mini through:

Development support
Debugging
Architecture exploration
Retrieval analysis
Evaluation development
Documentation
Repository cleanup
AI-generated recommendations were not automatically accepted. They were reviewed against the application, source code, evaluation results, and project requirements.

The final PolicyLens-Mini implementation therefore represents human-directed software engineering supported by AI-assisted development tools.