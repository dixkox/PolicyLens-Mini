PolicyLens-Mini Evaluation Set
1. Evaluation Overview
PolicyLens-Mini was evaluated using a controlled set of 20 questions across four policy documents.

The evaluation tests two primary behaviors:

Correct retrieval when supporting policy information exists
Correct rejection when requested information is unsupported
The evaluation runner is located at:

app/eval/run_eval.py
Recorded results are stored in:

evaluation/eval_results.json
2. Policies Evaluated
The evaluation uses:

pto_policy.md
security_policy.md
remote_work_policy.md
code_of_conduct.md
Five questions are evaluated against each policy.

Each group contains supported questions and at least one intentionally unsupported question to test the relevance guardrail.

3. Evaluation Questions
PTO Policy
How fast do employees accrue PTO?
What can PTO be used for?
How far in advance must PTO longer than 3 consecutive days be requested?
How much unused PTO can roll over?
Is unused PTO paid out when employment ends?
Question 5 is intentionally unsupported and should be rejected.

Information Security Policy
How often must employees complete security training?
How often must passwords be changed?
Where must confidential data not be stored?
How quickly must security incidents be reported?
What antivirus software must employees install?
Question 10 is intentionally unsupported and should be rejected.

Remote Work Policy
How many days per week may employees work remotely?
Whose approval is required for remote work?
During what hours must remote employees be available online?
What equipment must be used for remote work?
Must employees keep their webcam on during meetings?
Question 15 is intentionally unsupported and should be rejected.

Code of Conduct
How are employees expected to treat colleagues?
What must employees avoid?
What conduct is strictly prohibited?
What outside activities must employees disclose?
What disciplinary action is taken for violating the code?
Question 20 is intentionally unsupported and should be rejected.

4. Evaluation Method
For every test case, the evaluator records:

policy
question
expected_answer
should_match
answer
score
matched
correct
measured_latency_ms
Supported Questions
A supported test passes when:

The backend reports a match.
The returned answer contains the required expected information.
Unsupported Questions
An unsupported test passes when:

matched = false
This tests the system's ability to abstain when sufficient supporting policy information does not exist.

5. Baseline Evaluation
Before retrieval improvements, the controlled evaluation produced:

Correct: 15/20
Accuracy: 75.00%
Observed failure categories included:

Policy headings being returned as answers
Weak rejection of unsupported questions
Vocabulary mismatch
Incorrect selection between related policy sentences
The baseline was retained to provide measurable evidence of retrieval weaknesses and subsequent improvement.

6. Retrieval Improvements
Analysis of the baseline failures resulted in several backend improvements:

Excluding Markdown headings from factual-answer candidates
Increasing the relevance threshold from 0.10 to 0.20
Adding limited deterministic query expansion
Strengthening unsupported-question rejection
Adding explicit policy-name detection
Adding complete policy-section retrieval
The core retrieval architecture remains lightweight and deterministic.

7. Final Evaluation Result
The same 20 controlled test cases were executed following the retrieval improvements.

Final result:

Correct: 20/20
Accuracy: 100.00%
Measured improvement:

Baseline: 15/20 (75%)
Final:    20/20 (100%)
Change:   +25 percentage points
All supported questions satisfied the evaluator's expected-answer criteria, and all intentionally unsupported cases were rejected according to the evaluator's match criteria.

8. Interpretation
The final result represents complete success on this specific controlled 20-case evaluation set.

The result:

20/20
100.00%
should not be interpreted as universal accuracy across every possible policy document or user question.

Instead, it demonstrates that the final retrieval and guardrail implementation satisfies all cases contained within the recorded controlled evaluation dataset.

9. Reproducibility
With the required project environment configured, the evaluation can be reproduced from the project root using:

python app\eval\run_eval.py
The evaluator generates:

evaluation/eval_results.json
The same controlled evaluation set is used for baseline-to-final comparison so that retrieval changes can be evaluated consistently.

The resulting evaluation data provides a reproducible record of:

Tested questions
Expected behavior
Actual answers
Match decisions
Correctness
Similarity scores
Measured latency
10. Evaluation Conclusion
PolicyLens-Mini improved from:

15/20 correct
75.00%
to:

20/20 correct
100.00%
on the controlled 20-question evaluation set.

The evaluation provides evidence of:

Correct retrieval for supported policy questions
Rejection of intentionally unsupported questions
Deterministic and repeatable evaluation
Measured response latency
Documented retrieval improvements
Regression validation using the same evaluation set
Transparent comparison between baseline and final behavior
The results demonstrate how systematic testing and failure analysis directly informed improvements to the final PolicyLens-Mini retrieval implementation.