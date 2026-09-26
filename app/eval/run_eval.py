import json
import statistics
import time
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"
OUTPUT_FILE = ROOT / "evaluation" / "eval_results.json"

API_URL = "http://127.0.0.1:8000/ask"
TIMEOUT = 30


TEST_CASES = [
    {
        "policy": "pto_policy.md",
        "question": "How fast do employees accrue PTO?",
        "expected_answer": "1.5 days per month",
        "expected_terms": ["1.5 days per month"],
        "should_match": True,
    },
    {
        "policy": "pto_policy.md",
        "question": "What can PTO be used for?",
        "expected_answer": "vacation, personal time, or illness",
        "expected_terms": ["vacation", "personal time", "illness"],
        "should_match": True,
    },
    {
        "policy": "pto_policy.md",
        "question": "How far in advance must PTO longer than 3 consecutive days be requested?",
        "expected_answer": "at least 2 weeks in advance",
        "expected_terms": ["2 weeks"],
        "should_match": True,
    },
    {
        "policy": "pto_policy.md",
        "question": "How much unused PTO can roll over?",
        "expected_answer": "up to 5 days per calendar year",
        "expected_terms": ["5 days"],
        "should_match": True,
    },
    {
        "policy": "pto_policy.md",
        "question": "Is unused PTO paid out when employment ends?",
        "expected_answer": None,
        "expected_terms": [],
        "should_match": False,
    },
    {
        "policy": "security_policy.md",
        "question": "How often must employees complete security training?",
        "expected_answer": "annually",
        "expected_terms": ["annual security training"],
        "should_match": True,
    },
    {
        "policy": "security_policy.md",
        "question": "How often must passwords be changed?",
        "expected_answer": "every 90 days",
        "expected_terms": ["90 days"],
        "should_match": True,
    },
    {
        "policy": "security_policy.md",
        "question": "Where must confidential data not be stored?",
        "expected_answer": "on personal devices",
        "expected_terms": ["personal devices"],
        "should_match": True,
    },
    {
        "policy": "security_policy.md",
        "question": "How quickly must security incidents be reported?",
        "expected_answer": "within 24 hours",
        "expected_terms": ["24 hours"],
        "should_match": True,
    },
    {
        "policy": "security_policy.md",
        "question": "What antivirus software must employees install?",
        "expected_answer": None,
        "expected_terms": [],
        "should_match": False,
    },
    {
        "policy": "remote_work_policy.md",
        "question": "How many days per week may employees work remotely?",
        "expected_answer": "up to 3 days per week",
        "expected_terms": ["3 days per week"],
        "should_match": True,
    },
    {
        "policy": "remote_work_policy.md",
        "question": "Whose approval is required for remote work?",
        "expected_answer": "manager approval",
        "expected_terms": ["manager approval"],
        "should_match": True,
    },
    {
        "policy": "remote_work_policy.md",
        "question": "During what hours must remote employees be available online?",
        "expected_answer": "between 9 AM and 3 PM EST",
        "expected_terms": ["9 am", "3 pm", "est"],
        "should_match": True,
    },
    {
        "policy": "remote_work_policy.md",
        "question": "What equipment must be used for remote work?",
        "expected_answer": "company equipment",
        "expected_terms": ["company equipment"],
        "should_match": True,
    },
    {
        "policy": "remote_work_policy.md",
        "question": "Must employees keep their webcam on during meetings?",
        "expected_answer": None,
        "expected_terms": [],
        "should_match": False,
    },
    {
        "policy": "code_of_conduct.md",
        "question": "How are employees expected to treat colleagues?",
        "expected_answer": "respect colleagues",
        "expected_terms": ["respect colleagues"],
        "should_match": True,
    },
    {
        "policy": "code_of_conduct.md",
        "question": "What must employees avoid?",
        "expected_answer": "conflicts of interest",
        "expected_terms": ["conflicts of interest"],
        "should_match": True,
    },
    {
        "policy": "code_of_conduct.md",
        "question": "What conduct is strictly prohibited?",
        "expected_answer": "harassment or discrimination",
        "expected_terms": ["harassment", "discrimination"],
        "should_match": True,
    },
    {
        "policy": "code_of_conduct.md",
        "question": "What outside activities must employees disclose?",
        "expected_answer": "external employment or consulting activities",
        "expected_terms": ["external employment", "consulting activities"],
        "should_match": True,
    },
    {
        "policy": "code_of_conduct.md",
        "question": "What disciplinary action is taken for violating the code?",
        "expected_answer": None,
        "expected_terms": [],
        "should_match": False,
    },
]


def contains_expected_terms(answer, terms):
    answer_lower = (answer or "").lower()
    return all(term.lower() in answer_lower for term in terms)


def evaluate_case(case, response_data):
    answer = response_data.get("answer", "")
    matched = bool(response_data.get("matched", False))

    if case["should_match"]:
        return matched and contains_expected_terms(
            answer,
            case["expected_terms"],
        )
    return not matched


def percentile(values, percentile_value):
    if not values:
        return 0.0

    values = sorted(values)
    position = (len(values) - 1) * percentile_value
    lower = int(position)
    upper = min(lower + 1, len(values) - 1)
    fraction = position - lower

    return values[lower] + (values[upper] - values[lower]) * fraction


def main():
    print("Running PolicyLens-Mini evaluation...\n")

    results = []
    latencies = []

    for index, case in enumerate(TEST_CASES, start=1):
        policy_path = DATA_DIR / case["policy"]

        if not policy_path.exists():
            raise FileNotFoundError(f"Policy file not found: {policy_path}")

        policy_text = policy_path.read_text(encoding="utf-8")
        print(f"[{index}/{len(TEST_CASES)}] {case['question']}")

        started = time.perf_counter()
        data = {}
        error = None

        try:
            response = requests.post(
                API_URL,
                params={
                    "question": case["question"],
                    "text": policy_text,
                },
                timeout=TIMEOUT,
            )
            response.raise_for_status()
            data = response.json()
        except (requests.RequestException, ValueError) as exc:
            error = str(exc)

        measured_latency_ms = (time.perf_counter() - started) * 1000
        correct = False if error else evaluate_case(case, data)

        result = {
            "policy": case["policy"],
            "question": case["question"],
            "expected_answer": case["expected_answer"],
            "should_match": case["should_match"],
            "answer": data.get("answer") if isinstance(data, dict) else None,
            "score": data.get("score") if isinstance(data, dict) else None,
            "matched": data.get("matched") if isinstance(data, dict) else False,
            "correct": correct,
            "measured_latency_ms": round(measured_latency_ms, 3),
        }
        if error:
            result["error"] = error

        results.append(result)

        if error is None:
            latencies.append(measured_latency_ms)

    successful = sum(1 for result in results if result["correct"])
    total = len(results)
    accuracy = (successful / total * 100) if total else 0.0

    summary = {
        "total_cases": total,
        "correct_cases": successful,
        "incorrect_cases": total - successful,
        "accuracy_percent": round(accuracy, 2),
        "latency_ms": {
            "mean": round(statistics.mean(latencies), 3) if latencies else 0.0,
            "median": round(statistics.median(latencies), 3) if latencies else 0.0,
            "p95": round(percentile(latencies, 0.95), 3) if latencies else 0.0,
            "minimum": round(min(latencies), 3) if latencies else 0.0,
            "maximum": round(max(latencies), 3) if latencies else 0.0,
        },
    }

    output = {
        "system": "PolicyLens-Mini",
        "summary": summary,
        "results": results,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print("\nEvaluation complete.")
    print(f"Correct: {successful}/{total}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
