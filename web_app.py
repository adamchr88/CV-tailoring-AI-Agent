import streamlit as st
from file_utils import read_file
from templates import generate_summary, generate_bullets, generate_cover_letter

st.title("CV Tailoring AI Agent")

cv_file = st.file_uploader("Upload your CV", type=["txt", "pdf"])
job_text = st.text_area("Paste Job Description")

if cv_file and job_text:
    cv_text = cv_file.read().decode("utf-8")
    st.subheader("📊 Summary")
    st.write(generate_summary(cv_text, job_text))

    st.subheader("📌 Bullet Points")
    for bullet in generate_bullets(cv_text, job_text):
        st.write("- " + bullet)

    st.subheader("✉️ Cover Letter")
    st.write(generate_cover_letter(cv_text, job_text))
