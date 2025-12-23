import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import extract_text_from_pdf, clean_text

def rank_resumes(folder_path, job_description):

    resume_texts = []
    resume_names = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            text = extract_text_from_pdf(path)
            resume_texts.append(clean_text(text))
            resume_names.append(file)

    job_desc_cleaned = clean_text(job_description)

    documents = [job_desc_cleaned] + resume_texts

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_scores = cosine_similarity(
        tfidf_matrix[0:1], tfidf_matrix[1:]
    )[0]

    results = sorted(
        zip(resume_names, similarity_scores),
        key=lambda x: x[1],
        reverse=True
    )

    return results
