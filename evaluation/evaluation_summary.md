# Evaluation Summary - PolicyLens-Mini
 
## Overview
 
PolicyLens-Mini was evaluated using a reproducible automated test suite covering supported policy questions and intentionally unsupported questions.
 
The final evaluation contains:
 
- 20 test cases
- 4 policy documents
- Positive retrieval tests
- Negative guardrail tests
- Similarity scoring
- Correctness checks
- End-to-end latency measurement
 
The authoritative results are stored in:
 
```text
evaluation/eval_results.json
```
 
---
 
## Evaluation Method
 
The evaluator tests four policies:
 
1. Paid Time Off
2. Information Security
3. Remote Work
4. Code of Conduct
 
Each policy is tested with five questions.
 
For supported questions, the retrieved answer must contain the expected policy information.
 
For intentionally unsupported questions, the system must reject the query by returning:
 
```text
matched = false
```
 
---
 
## Baseline Result
 
Before retrieval improvements:
 
```text
Correct: 15/20
Accuracy: 75.00%
```
 
The baseline exposed:
 
- Heading-dominance errors
- Unsupported questions incorrectly matching policy content
- Vocabulary mismatch
- Incorrect selection between related passages
 
---
 
## Improvements Implemented
 
The retrieval pipeline was improved by:
 
- Excluding Markdown headings from answer candidates
- Strengthening the relevance threshold
- Adding limited deterministic query expansion
- Improving rejection of unsupported questions
 
The same evaluation suite was then rerun.
 
---
 
## Final Result
 
```text
Correct: 20/20
Accuracy: 100.00%
```
 
| Result | Baseline | Final |
|---|---:|---:|
| Correct cases | 15/20 | 20/20 |
| Accuracy | 75% | 100% |
| Improvement | | +25 percentage points |
 
All 20 final cases passed the evaluator's defined criteria.
 
---
 
## Guardrail Testing
 
The evaluation includes questions whose answers are deliberately absent from the relevant policy.
 
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
 
The final system correctly rejected these cases according to the automated evaluation criteria.
 
---
 
## Performance
 
Each request records:
 
```text
measured_latency_ms
```
 
The evaluator calculates:
 
- Mean latency
- Median latency
- p95 latency
- Minimum latency
- Maximum latency
 
Exact measurements for the final run are preserved in `eval_results.json`.
 
---
 
## Limitations
 
The 100% result applies only to this controlled 20-case evaluation suite.
 
It should not be interpreted as universal 100% accuracy for arbitrary documents or questions.
 
Current limitations include:
 
- Small evaluation dataset
- Four policies represented
- Lexical retrieval
- Limited query expansion
- Limited paraphrase testing
- No semantic embeddings or reranking
 
---
 
## Conclusion
 
PolicyLens-Mini improved from:
 
```text
15/20 (75%)
```
 
to:
 
```text
20/20 (100%)
```
 
on the same controlled evaluation suite.
 
The result provides reproducible evidence that evaluation-driven engineering improvements corrected the failures identified in the baseline implementation.