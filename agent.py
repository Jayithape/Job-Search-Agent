import google.genai as genai
import streamlit as st

# Load API Key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

# FIX: Disable VertexAI
client = genai.Client(
    api_key=api_key,
    vertexai=False
)


def ask_ai(prompt):
    response = client.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=prompt
    )
    return response.text


def analyze_resume(resume_text):
    prompt = f"""
    You are an expert HR + ATS Resume Analyzer.

    Analyze the resume and provide:
    1. Summary
    2. Strengths
    3. Weaknesses
    4. ATS Score (0-100)
    5. Best Job Roles
    6. Missing Skills
    7. Resume Improvements
    8. ATS Keywords

    Resume:
    {resume_text}
    """

    response = client.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=prompt
    )
    return response.text


def extract_skills(resume_text):
    prompt = f"""
    Extract ONLY technical skills from this resume.
    Return comma-separated skill names.

    Resume:
    {resume_text}
    """

    response = client.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=prompt
    )
    return response.text
