from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_documents():
    files = [
        "data/underwriting_policy.txt",
        "data/credit_eligibility_rules.txt",
        "data/disbursement_policy.txt"
    ]

    documents = []

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            documents.append({
                "source": file_path,
                "content": text
            })

    return documents


def get_rag_answer(question):
    documents = load_documents()

    texts = [doc["content"] for doc in documents]

    vectorizer = TfidfVectorizer(stop_words="english")
    document_vectors = vectorizer.fit_transform(texts)
    question_vector = vectorizer.transform([question])

    similarities = cosine_similarity(question_vector, document_vectors).flatten()

    best_index = similarities.argmax()
    best_document = documents[best_index]
    confidence_score = round(similarities[best_index] * 100, 2)

    context = best_document["content"]

    answer = f"""
Based on the retrieved loan underwriting policy document:

{context}

This information is most relevant to your question: "{question}"
"""

    sources = [best_document["source"]]

    return answer, sources, context, confidence_score