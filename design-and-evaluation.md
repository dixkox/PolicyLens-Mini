This would enable more detailed analysis than a single overall accuracy measurement.
 
---
 
# 20. Engineering Lessons
 
The baseline evaluation demonstrated that retrieval relevance and answer correctness are separate concerns.
 
```text
Retrieval relevance
!=
Answer correctness
!=
Groundedness
```
 
The project also demonstrated the value of iterative testing.
 
The development sequence was:
 
```text
Implement
|
Evaluate
|
Identify failures
|
Improve retrieval
|
Rerun identical tests
|
Compare results
```
 
The measured improvement from 15/20 to 20/20 provides concrete evidence of this engineering process.
 
---
 
# 21. Conclusion
 
PolicyLens-Mini implements an end-to-end policy question-answering workflow using:
 
- Next.js
- FastAPI
- PDF ingestion
- Text extraction
- Deterministic lexical retrieval
- TF-IDF weighting
- Cosine similarity
- Relevance guardrails
- Automated evaluation
- Performance measurement
 
The controlled evaluation initially produced 75% accuracy.
 
Analysis of the five failures led to improvements in heading handling, relevance thresholds, query expansion, and unsupported-question rejection.
 
After those changes, the same evaluation produced:
 
```text
20/20 correct
100.00% evaluation accuracy
```
 
This baseline-to-final comparison provides reproducible evidence that testing directly informed improvements to the final PolicyLens-Mini implementation.