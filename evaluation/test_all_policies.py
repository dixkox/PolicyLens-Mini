from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
DATA = ROOT / "data" / "raw"

sys.path.insert(0, str(BACKEND))
from app.retrieval import retrieve_answer, UNSUPPORTED_QUESTION_RESPONSE

POLICIES = [
    ("anti_harassment_policy", "Anti-Harassment Policy"),
    ("attendance_policy", "Attendance Policy"),
    ("benefits_policy", "Benefits Policy"),
    ("code_of_conduct", "Code of Conduct"),
    ("data_protection_policy", "Data Protection Policy"),
    ("expense_policy", "Expense Reimbursement Policy"),
    ("holiday_policy", "Company Holiday Policy"),
    ("hr_general_policy", "HR General Policy"),
    ("it_usage_policy", "IT Usage Policy"),
    ("parental_leave_policy", "Parental Leave Policy"),
    ("pto_policy", "Paid Time Off (PTO) Policy"),
    ("reimbursement_policy", "Reimbursement Policy"),
    ("remote_work_policy", "Remote Work Policy"),
    ("security_policy", "Information Security Policy"),
    ("travel_policy", "Travel Policy"),
    ("workplace_behavior_policy", "Workplace Behavior Policy"),
]

FACT_TESTS = [
    ("anti_harassment_policy", "Where should employees report harassment?", "report"),
    ("attendance_policy", "When should an absence be reported?", "one hour"),
    ("benefits_policy", "When do health benefits begin?", "90 days"),
    ("code_of_conduct", "Must employees disclose external employment?", "external employment"),
    ("data_protection_policy", "Where must confidential information be stored?", "approved systems"),
    ("expense_policy", "When must expense reports be submitted?", "30 days"),
    ("holiday_policy", "How many paid holidays are observed each year?", "10 paid holidays"),
    ("hr_general_policy", "Who should employees contact about workplace concerns?", "HR"),
    ("it_usage_policy", "Can employees install unauthorized software?", "unauthorized software"),
    ("parental_leave_policy", "How much parental leave is available?", "12 weeks"),
    ("pto_policy", "How much PTO do employees accrue each month?", "1.5 days"),
    ("reimbursement_policy", "When must reimbursement requests be submitted?", "14 days"),
    ("remote_work_policy", "How many days per week may employees work remotely?", "3 days"),
    ("security_policy", "When must security incidents be reported?", "24 hours"),
    ("travel_policy", "When must travel receipts be submitted?", "14 days"),
    ("workplace_behavior_policy", "Is bullying tolerated?", "Bullying"),
]

def load_all_policy_text():
    parts = []
    missing = []
    for stem, _ in POLICIES:
        path = DATA / f"{stem}.md"
        if not path.exists():
            missing.append(str(path))
        else:
            parts.append(path.read_text(encoding="utf-8"))
    if missing:
        raise FileNotFoundError("Missing policy files:\n" + "\n".join(missing))
    return "\n\n".join(parts)


def check(label, condition, answer):
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {label}")
    if not condition:
        print(f"       answer: {answer}")
    return condition


def main():
    text = load_all_policy_text()
    passed = 0
    total = 0

    print("\n=== 16 POLICY-NAME TESTS ===")
    for _, title in POLICIES:
        question = f"What is {title}?"
        result = retrieve_answer(question, text)
        ok = result["matched"] and result["answer"] != UNSUPPORTED_QUESTION_RESPONSE
        total += 1
        passed += check(question, ok, result["answer"])

    print("\n=== 16 FACT TESTS ===")
    for _, question, expected in FACT_TESTS:
        result = retrieve_answer(question, text)
        ok = (
            result["matched"]
            and result["answer"] != UNSUPPORTED_QUESTION_RESPONSE
            and expected.lower() in result["answer"].lower()
        )
        total += 1
        passed += check(question, ok, result["answer"])

    print("\n=== UNSUPPORTED TESTS ===")
    unsupported = [
        "What is the cook policy?",
        "What does the policy say about company pets?",
        "What is the policy for cryptocurrency trading?",
    ]
    for question in unsupported:
        result = retrieve_answer(question, text)
        ok = (
            not result["matched"]
            and result["answer"] == UNSUPPORTED_QUESTION_RESPONSE
        )
        total += 1
        passed += check(question, ok, result["answer"])

    print(f"\nRESULT: {passed}/{total} tests passed")
    if passed != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
