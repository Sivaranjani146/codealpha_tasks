
import streamlit as st
import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# Load FAQ data
with open('faq_data.json', 'r') as f:
    faqs = json.load(f)

questions = [faq['question'] for faq in faqs]
answers = [faq['answer'] for faq in faqs]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
question_vectors = vectorizer.fit_transform(questions)

st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")
st.title("🤖 AI FAQ Chatbot")
st.write("Ask a question related to CodeAlpha internship")

user_question = st.text_input("Your Question")

if st.button("Ask"):
    if user_question.strip() == "":
        st.warning("Please enter a question")
    else:
        user_vector = vectorizer.transform([user_question])
        similarities = cosine_similarity(user_vector, question_vectors)
        best_match = similarities.argmax()

        if similarities[0][best_match] < 0.2:
            st.error("Sorry, I don't understand your question.")
        else:
            st.success("Answer:")
            st.write(answers[best_match])
