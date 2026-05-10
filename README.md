\# Loan Underwriting Policy RAG Assistant



Loan Underwriting Policy RAG Assistant is a corporate-style RAG project that answers loan underwriting, credit eligibility, approval, rejection, and disbursement policy questions using local policy documents and synthetic loan application data.



\## Project Overview



This project simulates a financial loan processing workflow. It uses TF-IDF vector search and cosine similarity to retrieve relevant policy context from underwriting, credit eligibility, and disbursement documents. It also includes application lookup, approval decision explanation, KPI dashboard, and synthetic loan lifecycle data.



\## Business Context



Loan processing teams need to validate applicant eligibility, underwriting rules, risk scoring, approval decisions, and disbursement readiness. This project simulates that workflow using structured loan application records and unstructured policy documents.



\## Features



\- Local RAG-style policy assistant

\- 250,000 synthetic loan application records

\- Underwriting policy retrieval

\- Credit eligibility rule retrieval

\- Disbursement policy retrieval

\- Loan application lookup

\- Approval and rejection explanation

\- KPI dashboard

\- Approval rate, rejection rate, and manual review rate

\- Risk category distribution

\- Loan lifecycle stage tracking

\- Business rules documentation

\- UAT test cases



\## Tech Stack



Python, Streamlit, Pandas, Scikit-learn, TF-IDF Vector Search, Cosine Similarity, Plotly



\## Project Structure



loan-underwriting-rag-assistant/

├── data/

│   ├── loan\_applications.csv

│   ├── underwriting\_policy.txt

│   ├── credit\_eligibility\_rules.txt

│   └── disbursement\_policy.txt

├── docs/

│   ├── business\_rules.md

│   └── uat\_test\_cases.csv

├── src/

│   ├── generate\_loan\_data.py

│   ├── rag\_pipeline.py

│   └── loan\_analysis.py

├── app.py

├── requirements.txt

├── README.md

└── .gitignore



\## How to Run



1\. Create virtual environment



python -m venv .venv



2\. Activate virtual environment



.venv\\Scripts\\Activate.ps1



3\. Install dependencies



pip install -r requirements.txt



4\. Generate loan data



python src\\generate\_loan\_data.py



5\. Run Streamlit app



streamlit run app.py



\## Sample Questions



\- Can an applicant with DTI above 50 percent be approved?

\- What is the minimum credit score for approval?

\- Can rejected applications move to disbursement?

\- What documents are required before disbursement?

\- Which applicants require manual underwriting review?



\## Resume Summary



Built a corporate-style loan underwriting RAG assistant using Python, Streamlit, Pandas, Scikit-learn, and TF-IDF vector search to answer policy questions, explain loan decisions, track lifecycle stages, and monitor underwriting KPIs across 250K synthetic loan applications.

