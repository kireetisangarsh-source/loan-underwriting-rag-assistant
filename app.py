import plotly.express as px
import streamlit as st

from src.loan_analysis import (
    calculate_kpis,
    get_application_details,
    get_risk_summary,
    get_stage_summary,
    get_status_summary,
    load_loan_data
)
from src.rag_pipeline import get_rag_answer


st.set_page_config(
    page_title="Loan Underwriting RAG Assistant",
    layout="wide"
)

st.title("Loan Underwriting Policy RAG Assistant")

st.write(
    "Corporate-style loan underwriting assistant for policy questions, "
    "credit eligibility rules, risk scoring, approval decisions, and disbursement workflows."
)

tab1, tab2, tab3, tab4 = st.tabs(
    ["RAG Assistant", "Application Lookup", "KPI Dashboard", "Loan Data"]
)

with tab1:
    st.subheader("Ask a Loan Underwriting Policy Question")

    question = st.text_input(
        "Example: Can an applicant with DTI above 50 percent be approved?"
    )

    if st.button("Get Answer"):
        if question:
            answer, sources, context, confidence_score = get_rag_answer(question)

            st.subheader("AI Answer")
            st.write(answer)

            st.subheader("Confidence Score")
            st.write(f"{confidence_score}%")

            st.subheader("Sources Used")
            for source in sources:
                st.write(source)

            with st.expander("View Retrieved Policy Context"):
                st.write(context)
        else:
            st.warning("Please enter a question.")

with tab2:
    st.subheader("Loan Application Lookup")

    application_id = st.text_input(
        "Enter Application ID",
        placeholder="Example: LN0001000"
    )

    if st.button("Search Application"):
        if application_id:
            application = get_application_details(application_id)

            if application:
                st.success("Application found.")
                st.json(application)

                st.subheader("Decision Explanation")

                if application["approval_status"] == "Approved":
                    st.write(
                        "This application is approved because the applicant meets the policy criteria for credit score, income, debt-to-income ratio, and employment status."
                    )
                elif application["approval_status"] == "Rejected":
                    st.write(
                        f"This application is rejected because: {application['rejection_reason']}."
                    )
                else:
                    st.write(
                        f"This application requires manual review because: {application['rejection_reason']}."
                    )
            else:
                st.error("Application not found.")
        else:
            st.warning("Please enter an application ID.")

with tab3:
    st.subheader("Loan Underwriting KPI Dashboard")

    kpis = calculate_kpis()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Applications", f"{kpis['total_applications']:,}")
    col2.metric("Approval Rate", f"{kpis['approval_rate']}%")
    col3.metric("Rejection Rate", f"{kpis['rejection_rate']}%")
    col4.metric("Manual Review Rate", f"{kpis['manual_review_rate']}%")

    col5, col6, col7 = st.columns(3)

    col5.metric("Avg Credit Score", kpis["avg_credit_score"])
    col6.metric("Avg DTI Ratio", f"{kpis['avg_dti']}%")
    col7.metric("Avg Processing Days", kpis["avg_processing_days"])

    status_summary = get_status_summary()
    risk_summary = get_risk_summary()
    stage_summary = get_stage_summary()

    fig_status = px.bar(
        status_summary,
        x="approval_status",
        y="count",
        title="Applications by Approval Status"
    )
    st.plotly_chart(fig_status, use_container_width=True)

    fig_risk = px.bar(
        risk_summary,
        x="risk_category",
        y="count",
        title="Applications by Risk Category"
    )
    st.plotly_chart(fig_risk, use_container_width=True)

    fig_stage = px.bar(
        stage_summary,
        x="current_stage",
        y="count",
        title="Applications by Loan Lifecycle Stage"
    )
    st.plotly_chart(fig_stage, use_container_width=True)

with tab4:
    st.subheader("Synthetic Loan Application Data")
    df = load_loan_data()
    st.dataframe(df)