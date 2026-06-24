import streamlit as st
import sqlite3
import os

st.set_page_config(page_title="TalentBridge Talent Vault")

st.title("TalentBridge Talent Vault")
st.subheader("Upload Your Profile")

# Candidate Details

name = st.text_input("Full Name")

email = st.text_input("Email Address")

mobile = st.text_input("Mobile Number")

city = st.text_input("City")

designation = st.text_input("Current Designation")

experience = st.number_input(
    "Years of Experience",
    min_value=0,
    step=1
)

qualification = st.text_input(
    "Highest Qualification"
)

position = st.text_input(
    "Position Looking For"
)

skills = st.text_area(
    "Skills / Key Competencies"
)

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if st.button("Submit Profile"):

    # Validation
    if not name:
        st.error("Please enter your name.")
        st.stop()

    # Create Uploads folder if missing
    if not os.path.exists("Uploads"):
        os.makedirs("Uploads")

    resume_path = ""

    if resume is not None:

        resume_path = os.path.join(
            "Uploads",
            resume.name
        )

        with open(resume_path, "wb") as f:
            f.write(resume.getbuffer())

    # Save to Database
    conn = sqlite3.connect("talentvault.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO candidates
    (
        name,
        email,
        mobile,
        city,
        designation,
        experience,
        qualification,
        position,
        skills,
        resume_path
    )
    VALUES
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        name,
        email,
        mobile,
        city,
        designation,
        experience,
        qualification,
        position,
        skills,
        resume_path
    ))

    conn.commit()
    conn.close()

    st.success("Profile Submitted Successfully!")

    # Debug output (can remove later)
    st.write("Saved Data:")
    st.write({
        "name": name,
        "email": email,
        "mobile": mobile,
        "city": city,
        "designation": designation,
        "experience": experience,
        "qualification": qualification,
        "position": position,
        "skills": skills
    })