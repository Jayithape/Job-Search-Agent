import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Load API Key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Client
client = genai.Client(api_key=api_key)


# 1) GENERAL AI (Job roles, questions)
def ask_ai(prompt):
    response = client.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=prompt
    )
    return response.text


# 2) RESUME ANALYZER
def analyze_resume(resume_text):
    prompt = f"""
    You are an expert HR + ATS Resume Analyzer.

    Analyze the resume and provide:
    1. Summary
    2. Strengths
    3. Weaknesses
    4. ATS Score (0–100)
    5. Best Job Roles
    6. Missing Skills
    7. Resume Improvement Suggestions
    8. ATS Keywords

    Resume:
    {resume_text}
    """

    response = client.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=prompt
    )
    return response.text


# 3) SKILL EXTRACTION
def extract_skills(resume_text):
    prompt = f"""
    Extract ONLY technical skills from this resume.
    Return comma-separated list (python, sql, java, flutter).

    Resume:
    {resume_text}
    """

    response = client.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=prompt
    )
    return response.text
