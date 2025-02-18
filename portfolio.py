import streamlit as st
from PIL import Image

# ---- PAGE CONFIG ----
st.set_page_config(page_title="My Portfolio", page_icon="📌", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #0d1117;
            color: #c9d1d9;
        }
        .main-title {
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            color: #58a6ff;
        }
        .sub-title {
            text-align: center;
            font-size: 1.5rem;
            color: #8b949e;
        }
        .section-title {
            font-size: 2rem;
            margin-top: 20px;
            border-bottom: 2px solid #58a6ff;
            padding-bottom: 5px;
        }
        .card {
            background-color: #161b22;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        a {
            color: #58a6ff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER SECTION ----
st.markdown("<h1 class='main-title'>👋 Hello, I'm Mirshoir!</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>A Passionate Developer & AI Enthusiast</p>", unsafe_allow_html=True)

profile_pic = "IMG_4049 copy.jpg"  # Replace with your image filename
st.image(profile_pic, width=200, use_container_width=False)
st.markdown("> I specialize in LLMs, AI applications, and full-stack development.")

# ---- PROJECTS SECTION ----
st.markdown("<h2 class='section-title'>🚀 Projects</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='card'>
    <h3>1️⃣ Chatbot</h3>
    <p>A chatbot powered by AI and Rumi's wisdom.</p>
    <a href='https://github.com/Mirshoir/chatbot' target='_blank'>GitHub Repo</a>
</div>
<div class='card'>
    <h3>2️⃣ AI Chatbot for Student Guidance</h3>
    <p>An AI chatbot that helps students manage stress & focus.</p>
    <a href='https://github.com/Mirshoir/Capstone_design_project' target='_blank'>GitHub Repo</a>
</div>
""", unsafe_allow_html=True)

# ---- SKILLS SECTION ----
st.markdown("<h2 class='section-title'>🛠️ Skills</h2>", unsafe_allow_html=True)
skills = ["Python", "Streamlit", "FAISS", "Flask", "Machine Learning", "Kotlin"]
st.markdown(f"<p>{' | '.join(skills)}</p>", unsafe_allow_html=True)

# ---- CONTACT SECTION ----
st.markdown("<h2 class='section-title'>📬 Contact Me</h2>", unsafe_allow_html=True)
st.markdown("""
<p>📧 Email: <a href='mailto:mirshoir29@gmail.com'>mirshoir29@gmail.com</a></p>
<p>💼 LinkedIn: <a href='https://linkedin.com/in/mirshoir' target='_blank'>linkedin.com/in/mirshoir</a></p>
<p>🐙 GitHub: <a href='https://github.com/Mirshoir' target='_blank'>github.com/Mirshoir</a></p>
""", unsafe_allow_html=True)
