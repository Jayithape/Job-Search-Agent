import streamlit as st
from agent import ask_ai, analyze_resume, extract_skills
from scraper import search_jobs
from pypdf import PdfReader

# PDF TEXT EXTRACTION FUNCTION
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# ==========================================
# SIDEBAR MENU
# ==========================================
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio(
    "Go to",
    ["Job Search", "Resume Analyzer"],
    index=0
)

st.title("💼 AI Career Agent")


# ==========================================
# 1) JOB SEARCH PAGE
# ==========================================
if menu == "Job Search":
    st.header("🔍 Job Search")

    qualification = st.text_input("Enter your qualification or role:")

    if st.button("Search Jobs"):
        if qualification.strip() == "":
            st.warning("Please enter your qualification.")
        else:
            st.subheader("🎯 AI Recommended Job Roles")

            job_roles = ask_ai(
                f"Suggest 5 fresher software job roles for: {qualification}. Return short bullet points only."
            )
            st.write(job_roles)

            st.subheader("🔗 Job Openings (Company + Apply Link)")

            results = search_jobs(qualification)

            for job in results:
                st.markdown(f"**Company:** {job['company']}")
                st.markdown(f"**Role:** {job.get('title','')}")
                st.markdown(f"[Apply Here]({job['link']})")
                st.write("---")


# ==========================================
# 2) RESUME ANALYZER PAGE
# ==========================================
elif menu == "Resume Analyzer":
    st.header("📄 Resume Analyzer")

    uploaded_file = st.file_uploader("Upload your Resume (PDF only):", type=["pdf"])

    if uploaded_file:
        st.success("Resume uploaded successfully!")

        # Extract text
        resume_text = extract_text_from_pdf(uploaded_file)

        st.subheader("📘 Resume Analysis (AI Powered)")
        analysis = analyze_resume(resume_text)
        st.write(analysis)

        # ----------------------------
        # JOBS BASED ON SKILLS
        # ----------------------------
        st.subheader("🔗 Job Apply Links Based on Resume Skills")

        skills_raw = extract_skills(resume_text)
        skills = [s.strip() for s in skills_raw.split(",")]

        for skill in skills:
            if skill:
                st.markdown(f"### 🛠 Skill: **{skill}**")

                results = search_jobs(skill)

                for job in results:
                    st.markdown(f"**Company:** {job['company']}")
                    st.markdown(f"**Role:** {job.get('title', '')}")
                    st.markdown(f"[Apply Here]({job['link']})")
                    st.write("---")
