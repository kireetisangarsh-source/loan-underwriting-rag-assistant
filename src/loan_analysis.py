import pandas as pd


DATA_PATH = "data/loan_applications.csv"


def load_loan_data():
    return pd.read_csv(DATA_PATH)


def get_application_details(application_id):
    df = load_loan_data()

    application = df[df["application_id"].str.upper() == application_id.upper()]

    if application.empty:
        return None

    return application.to_dict(orient="records")[0]


def calculate_kpis():
    df = load_loan_data()

    total_applications = len(df)
    approved = len(df[df["approval_status"] == "Approved"])
    rejected = len(df[df["approval_status"] == "Rejected"])
    manual_review = len(df[df["approval_status"] == "Manual Review"])

    approval_rate = round((approved / total_applications) * 100, 2)
    rejection_rate = round((rejected / total_applications) * 100, 2)
    manual_review_rate = round((manual_review / total_applications) * 100, 2)

    high_risk = len(df[df["risk_category"] == "High"])
    medium_risk = len(df[df["risk_category"] == "Medium"])
    low_risk = len(df[df["risk_category"] == "Low"])

    avg_processing_days = round(df["processing_days"].mean(), 2)
    avg_credit_score = round(df["credit_score"].mean(), 2)
    avg_dti = round(df["debt_to_income_ratio"].mean(), 2)

    return {
        "total_applications": total_applications,
        "approved": approved,
        "rejected": rejected,
        "manual_review": manual_review,
        "approval_rate": approval_rate,
        "rejection_rate": rejection_rate,
        "manual_review_rate": manual_review_rate,
        "high_risk": high_risk,
        "medium_risk": medium_risk,
        "low_risk": low_risk,
        "avg_processing_days": avg_processing_days,
        "avg_credit_score": avg_credit_score,
        "avg_dti": avg_dti
    }


def get_status_summary():
    df = load_loan_data()
    return df.groupby("approval_status").size().reset_index(name="count")


def get_risk_summary():
    df = load_loan_data()
    return df.groupby("risk_category").size().reset_index(name="count")


def get_stage_summary():
    df = load_loan_data()
    return df.groupby("current_stage").size().reset_index(name="count")