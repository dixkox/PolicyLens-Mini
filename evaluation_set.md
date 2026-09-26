# PolicyLens-Mini Evaluation Set
 
## 1. Evaluation Overview
 
PolicyLens-Mini was evaluated using a controlled set of 20 questions against four policy documents.
 
The evaluation tests two important behaviors:
 
- Correct retrieval of policy information when the answer exists
- Correct rejection when the requested information is not present
 
The evaluation is implemented in:
 
```text
app/eval/run_eval.py
```
 
Recorded results are stored in:
 
```text
evaluation/eval_results.json
```
 
---
 
## 2. Policies Evaluated
 
The evaluation uses:
 
- `pto_policy.md`
- `security_policy.md`
- `remote_work_policy.md`
- `code_of_conduct.md`
 
Five questions are evaluated against each policy.
 
Each group contains supported questions and at least one unsupported question to test the relevance guardrail.
 
---
 
## 3. Evaluation Questions
 
### PTO Policy
 
1. How fast do employees accrue PTO?
2. What can PTO be used for?
3. How far in advance must PTO longer than 3 consecutive days be requested?
4. How much unused PTO can roll over?
5. Is unused PTO paid out when employment ends?
 
The fifth question is intentionally unsupported by the policy and should be rejected.
 
### Information Security Policy
 
6. How often must employees complete security training?
7. How often must passwords be changed?
8. Where must confidential data not be stored?
9. How quickly must security incidents be reported?
10. What antivirus software must employees install?
 
The tenth question is intentionally unsupported.
 
### Remote Work Policy
 
11. How many days per week may employees work remotely?
12. Whose approval is required for remote work?
13. During what hours must remote employees be available online?
14. What equipment must be used for remote work?
15. Must employees keep their webcam on during meetings?
 
The fifteenth question is intentionally unsupported.
 
### Code of Conduct
 
16. How are employees expected to treat colleagues?
17. What must employees avoid?
18. What conduct is strictly prohibited?
19. What outside activities must employees disclose?
20. What disciplinary action is taken for violating the code?
 
The twentieth question is intentionally unsupported.
 
---
 
## 4. Evaluation Method
 
For every test case, the evaluator records:
 
```text
policy
question
expected_answer
should_match
answer
score
matched
correct
measured_latency_ms
```
 
### Supported Questions
 
A supported test passes when:
 
1. The backend reports a match.
2. The returned answer contains the required expected information.
 
### Unsupported Questions
 
An unsupported test passes when the backend correctly returns:
 
```text
matched = false
```
 
This explicitly tests the system's ability to abstain when the policy does not contain the requested information.
 
---
 
## 5. Baseline Evaluation
 
Before retrieval improvements, the evaluation produced:
 
```text
Correct: 15/20
Accuracy: 75.00%
```
 
Observed problems included:
 
- Policy headings being returned as answers
- Weak rejection of unsupported questions
- Lexical vocabulary mismatch
- Incorrect selection between similar policy sentences
 
This baseline was retained as evidence for identifying retrieval weaknesses.
 
---
 
## 6. Retrieval Improvements
 
The backend retrieval implementation was subsequently improved.
 
Changes included:
 
- Excluding Markdown headings from answer candidates
- Increasing the relevance threshold
- Adding limited deterministic query expansion
- Strengthening unsupported-question rejection
 
The retrieval architecture remains lightweight and deterministic.
 
---
 
## 7. Final Evaluation Result
 
The same 20 controlled test cases were executed again after the retrieval improvements.
 
Result:
 
```text
Correct: 20/20
Accuracy: 100.00%
```
 
All supported questions returned the expected policy information and all intentional unsupported cases were rejected according to the evaluator's criteria.
 
---
 
## 8. Interpretation
 
The final result demonstrates complete success on this specific controlled 20-case evaluation set.
 
The 100% result should not be interpreted as universal accuracy across every possible policy document or user question.
 
Instead, it demonstrates that the implemented retrieval and guardrail logic satisfies all cases in the recorded evaluation dataset.
 
---
 
## 9. Reproducibility
 
With the PolicyLens-Mini backend running locally, the evaluation can be reproduced from the project root using:
 
```powershell
python app\eval\run_eval.py
```
 
The evaluator regenerates:
 
```text
evaluation/eval_results.json
```
 
This provides a reproducible record of the tested questions, expected behavior, actual answers, match decisions, correctness, similarity scores, and measured latency.
 
---
 
## 10. Evaluation Conclusion
 
PolicyLens-Mini improved from a 75% baseline to 100% on the controlled 20-question evaluation set.
 
The evaluation demonstrates:
 
- Correct retrieval for explicitly supported policy questions
- Successful rejection of intentionally unsupported questions
- Deterministic and repeatable evaluation
- Measured response latency
- Documented retrieval improvements
- Transparent comparison between baseline and final behavior
 
The evaluation provides evidence of both the testing methodology and the engineering iteration used to improve PolicyLens-Mini.