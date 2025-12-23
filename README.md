# AI_Resume_Ranker
🤖 AI-Powered Resume Ranker

An intelligent web application that ranks resumes based on their relevance to a given job description using Natural Language Processing (NLP) and Machine Learning techniques.

📌 Project Overview

Hiring teams often receive hundreds of resumes for a single job role. Manually screening them is time-consuming and inefficient.
This project automates the resume screening process by analyzing resume content and ranking candidates based on how well their skills and experience match a provided job description.

The system uses TF-IDF vectorization and cosine similarity to compute relevance scores and presents the results through an interactive web interface.

🚀 Features

Upload multiple resume PDFs

Paste job description text

Automatic resume ranking

Individual resume match score out of 100%

Best-matching resume scaled to 100%

Interactive results table and bar chart

Simple and user-friendly UI built with Streamlit

Downloadable ranking results (CSV)

🧠 How It Works

Resume PDFs are uploaded and converted into plain text.

Job description text is cleaned and preprocessed using NLP techniques.

TF-IDF is used to convert text into numerical vectors.

Cosine similarity measures how closely each resume matches the job description.

Scores are normalized so the best resume gets 100%.

Ranked results are displayed visually in the web app.

🛠️ Technologies Used

Python

Streamlit – Frontend UI

SpaCy – NLP preprocessing

Scikit-learn – TF-IDF & similarity

PyPDF2 – PDF text extraction

Pandas & NumPy – Data handling

📂 Project Structure
AI_Resume_Ranker/
│
├── app.py                 # Streamlit web application
├── resume_ranker.py       # Resume ranking logic
├── utils.py               # PDF extraction & text preprocessing
├── uploaded_resumes/      # Uploaded resume PDFs
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/AI-Resume-Ranker.git
cd AI-Resume-Ranker

2️⃣ Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

3️⃣ Run the application
streamlit run app.py

📊 Sample Job Descriptions

Python Developer

Machine Learning Engineer

Data Analyst

AI / NLP Engineer

These can be used to test and validate the ranking system.

📈 Use Cases

Resume screening automation

HR recruitment support tools

Internship & fresher hiring

Applicant Tracking Systems (ATS)

🧪 Future Enhancements

Skill-wise match percentage

Resume preview in UI

Keyword highlighting

Threshold-based filtering

Cloud deployment

Role-based login system

🎯 Learning Outcomes

Practical implementation of NLP concepts

Understanding TF-IDF and cosine similarity

Building real-world ML applications

Developing interactive web apps using Streamlit

End-to-end ML project workflow
