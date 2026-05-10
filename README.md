# Loan Underwriting RAG Assistant

This project is a loan underwriting assistant built with Python and Streamlit. It helps answer questions about loan approval rules, credit eligibility, risk review, and disbursement policies.

The project uses local text documents as the knowledge base and retrieves the most relevant policy section using TF-IDF vector search. It also includes a loan application lookup and a small KPI dashboard for underwriting analysis.

## Why I built this

I wanted to create a project close to a real business analyst workflow in a loan processing environment. The goal was to connect policy rules with application data and make it easier to understand why a loan is approved, rejected, or sent for manual review.

## Features

- Ask questions about loan underwriting policies
- Retrieve relevant policy context from local documents
- Search a loan application by application ID
- Explain approval, rejection, or manual review decisions
- View approval, rejection, and manual review rates
- Analyze risk category and loan lifecycle stage distribution
- Work with 250,000 synthetic loan application records

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- TF-IDF Vector Search
- Cosine Similarity
- Plotly

## Project Structure

loan-underwriting-rag-assistant/
├── data/
├── docs/
├── src/
├── app.py
├── requirements.txt
└── README.md

## How to Run

Create and activate a virtual environment:

python -m venv .venv

.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Generate the loan data:

python src\generate_loan_data.py

Run the app:

streamlit run app.py

## Sample Questions

- What is the minimum credit score for approval?
- Can an applicant with DTI above 50 percent be approved?
- Can rejected applications move to disbursement?
- Which applications require manual underwriting review?
- What documents are required before disbursement?

## Notes

This project uses synthetic data only. It does not contain real customer or financial data.
