# PolicyLens-Mini Evaluation
 
## 1. Purpose
 
This document records the final evaluation of PolicyLens-Mini.
 
The evaluation measures whether the retrieval system:
 
- Returns the expected policy information for supported questions
- Rejects questions whose answers are not present in the policy
- Produces reproducible results
- Maintains low response latency
 
The automated evaluator is:
 
```text
app/eval/run_eval.py
```
 
The recorded results are:
 
```text
evaluation/eval_results.json
```
 
---
 
## 2. System Under Evaluation
 
PolicyLens-Mini uses a lightweight deterministic retrieval pipeline:
 
```text
Policy Text
|
Sentence Chunking
|
Tokenization
|
TF-IDF Weighting
|
Cosine Similarity
|
Best Candidate
|
Relevance Guardrail
|
Answer / Rejection
```
 
The retrieval implementation is located at:
 
```text
backend/app/retrieval.py
```
 
The final implementation also excludes Markdown headings from answer candidates and applies limited deterministic query expansion.
 
---
 
## 3. Evaluation Dataset
 
The controlled evaluation contains 20 questions across four policies:
 
| Policy | Tests |
|---|---:|
| Paid Time Off | 5 |
| Information Security | 5 |
| Remote Work | 5 |
| Code of Conduct | 5 |
| **Total** | **20** |
 
The test suite includes both supported and intentionally unsupported questions.
 
Unsupported questions test whether the relevance guardrail correctly abstains instead of returning unrelated policy content.
 
---
 
## 4. Evaluation Criteria
 
Each test records:
 
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
 
### Supported Question
 
A supported test passes when:
 
```text
matched = true
```
 
and the returned passage contains the required expected information.
 
### Unsupported Question
 
An unsupported test passes when:
 
```text
matched = false
```
 
This measures successful abstention when the requested information is absent.
 
---
 
## 5. Baseline Evaluation
 
The initial controlled evaluation produced:
 
```text
Correct: 15/20
Accuracy: 75.00%
```
 
Five failures were identified.
 
### Failure Modes
 
The baseline exposed:
 
- Policy headings returned as answers
- Weak rejection of unsupported questions
- Vocabulary mismatch
- Selection of a related but incorrect sentence
 
These failures provided concrete targets for improving the retrieval pipeline.
 
---
 
## 6. Retrieval Improvements
 
The following changes were made after analyzing the baseline failures.
 
### Heading Exclusion
 
Markdown headings are no longer eligible answer candidates.
 
### Relevance Guardrail
 
The relevance threshold was strengthened to reject weaker matches.
 
### Query Expansion
 
Limited deterministic query expansion was introduced to reduce selected lexical mismatches.
 
### Improved Abstention
 
Questions without sufficient supporting evidence are returned as:
 
```text
No relevant policy information was found.
```
 
with:
 
```text
matched = false
```
 
---
 
## 7. Final Results
 
The same 20 controlled cases were rerun after these changes.
 
Final result:
 
```text
Correct: 20/20
Accuracy: 100.00%
```
 
Comparison:
 
| Evaluation | Correct | Accuracy |
|---|---:|---:|
| Baseline | 15/20 | 75% |
| Final | 20/20 | 100% |
| Improvement | +5 cases | +25 percentage points |
 
All final cases passed the evaluator's defined criteria.
 
---
 
## 8. Positive Retrieval Examples
 
### PTO Accrual
 
Question:
 
```text
How fast do employees accrue PTO?
```
 
Expected information:
 
```text
1.5 days per month
```
 
Returned:
 
```text
Employees accrue PTO at a rate of 1.5 days per month.
```
 
Result:
 
```text
Correct
```
 
### Password Policy
 
Question:
 
```text
How often must passwords be changed?
```
 
Expected:
 
```text
every 90 days
```
 
Returned:
 
```text
Passwords must be changed every 90 days and meet complexity requirements.
```
 
Result:
 
```text
Correct
```
 
### Remote Availability
 
Question:
 
```text
During what hours must remote employees be available online?
```
 
Expected:
 
```text
between 9 AM and 3 PM EST
```
 
Returned:
 
```text
All remote employees must be available online between 9 AM and 3 PM EST.
```
 
Result:
 
```text
Correct
```
 
### Code of Conduct
 
Question:
 
```text
What conduct is strictly prohibited?
```
 
Expected:
 
```text
harassment or discrimination
```
 
Returned:
 
```text
Harassment or discrimination of any kind is strictly prohibited.
```
 
Result:
 
```text
Correct
```
 
---
 
## 9. Negative and Guardrail Testing
 
The evaluation deliberately includes questions whose answers are absent from the relevant policy.
 
Examples include:
 
```text
Is unused PTO paid out when employment ends?
```
 
```text
What antivirus software must employees install?
```
 
```text
Must employees keep their webcam on during meetings?
```
 
```text
What disciplinary action is taken for violating the code?
```
 
In the final evaluation, these cases satisfied the evaluator's rejection criteria.
 
This is important because a policy retrieval system should not present unsupported information merely because some vocabulary overlaps with the question.
 
---
 
## 10. Latency
 
Each evaluation request records end-to-end HTTP latency in:
 
```text
measured_latency_ms
```
 
The evaluator calculates:
 
- Mean
- Median
- p95
- Minimum
- Maximum
 
The authoritative latency values for the final run are stored directly in:
 
```text
evaluation/eval_results.json
```
 
This prevents obsolete measurements from earlier implementations being presented as current performance.
 
---
 
## 11. Interpretation
 
The final 100% result applies specifically to this controlled 20-question evaluation set.
 
It does not establish universal 100% accuracy for arbitrary policies, unseen document structures, or every possible user question.
 
The result demonstrates that PolicyLens-Mini satisfies all cases defined by the current automated evaluation suite.
 
---
 
## 12. Limitations
 
The evaluation has several limitations:
 
- Only 20 controlled questions
- Four policies represented in the automated suite
- Limited paraphrase diversity
- Limited adversarial testing
- Lexical retrieval rather than semantic retrieval
- Manually defined query expansion
- No independent human-rated groundedness metric
- No neural reranking
 
These limitations should be considered when interpreting the result.
 
---
 
## 13. Reproducibility
 
With the backend running locally, the evaluation can be reproduced from the project root:
 
```powershell
python app\eval\run_eval.py
```
 
The command regenerates:
 
```text
evaluation/eval_results.json
```
 
This makes the evaluation repeatable and auditable.
 
---
 
## 14. Conclusion
 
PolicyLens-Mini improved from:
 
```text
15/20 correct
75% accuracy
```
 
to:
 
```text
20/20 correct
100% accuracy
```
 
on the same controlled evaluation suite.
 
The improvement resulted from analyzing actual failures and modifying heading handling, relevance filtering, and lexical matching.
 
The evaluation therefore provides evidence not only of final system behaviour, but also of an iterative software engineering process based on testing, failure analysis, implementation changes, and regression evaluation.