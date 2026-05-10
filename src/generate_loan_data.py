import random
from pathlib import Path

import pandas as pd


random.seed(42)

NUM_RECORDS = 250000
OUTPUT_PATH = Path("data/loan_applications.csv")

loan_purposes = [
    "Home Improvement",
    "Debt Consolidation",
    "Auto Loan",
    "Education",
    "Medical Expense",
    "Small Business",
    "Personal Loan"
]

employment_statuses = [
    "Full-time",
    "Part-time",
    "Self-employed",
    "Unemployed"
]

stages = [
    "Application Intake",
    "Document Verification",
    "Underwriting Review",
    "Approval Decision",
    "Disbursement"
]

records = []

for i in range(1, NUM_RECORDS + 1):
    application_id = f"LN{i:07d}"
    applicant_id = f"APP{random.randint(100000, 999999)}"

    credit_score = random.randint(520, 820)
    annual_income = random.randint(30000, 180000)
    requested_loan_amount = random.randint(5000, 100000)
    debt_to_income_ratio = round(random.uniform(15, 65), 2)
    employment_status = random.choice(employment_statuses)
    loan_purpose = random.choice(loan_purposes)

    processing_days = random.randint(2, 30)
    current_stage = random.choice(stages)

    if credit_score < 600:
        risk_category = "High"
        approval_status = "Rejected"
        rejection_reason = "Credit score below minimum threshold"
    elif debt_to_income_ratio > 50:
        risk_category = "High"
        approval_status = "Rejected"
        rejection_reason = "Debt-to-income ratio exceeds policy limit"
    elif employment_status == "Unemployed":
        risk_category = "High"
        approval_status = "Rejected"
        rejection_reason = "Applicant employment status is not eligible"
    elif requested_loan_amount > annual_income * 0.8:
        risk_category = "Medium"
        approval_status = "Manual Review"
        rejection_reason = "Requested amount requires additional underwriting review"
    elif credit_score >= 700 and debt_to_income_ratio <= 40:
        risk_category = "Low"
        approval_status = "Approved"
        rejection_reason = "None"
    else:
        risk_category = "Medium"
        approval_status = "Manual Review"
        rejection_reason = "Requires additional risk review"

    records.append({
        "application_id": application_id,
        "applicant_id": applicant_id,
        "credit_score": credit_score,
        "annual_income": annual_income,
        "requested_loan_amount": requested_loan_amount,
        "debt_to_income_ratio": debt_to_income_ratio,
        "employment_status": employment_status,
        "loan_purpose": loan_purpose,
        "risk_category": risk_category,
        "approval_status": approval_status,
        "rejection_reason": rejection_reason,
        "current_stage": current_stage,
        "processing_days": processing_days
    })

df = pd.DataFrame(records)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated {len(df)} loan application records.")
print(f"Saved to {OUTPUT_PATH}")