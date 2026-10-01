import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="ผู้พัฒนา | ML Hub",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;500;700&family=Orbitron:wght@700&display=swap');

/* Main App Layout */
.stApp {
    background: #ffffff;
    background-image:
        radial-gradient(circle at 20% 20%, rgba(255,102,153,0.08) 0%, transparent 40%),
        radial-gradient(circle at 80% 70%, rgba(255,182,193,0.12) 0%, transparent 40%),
        linear-gradient(rgba(255,102,153,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,102,153,0.04) 1px, transparent 1px);
    background-size: auto, auto, 40px 40px, 40px 40px;
}
html, body, [class*="css"] { font-family: 'Prompt', sans-serif; }

/* Hero Section */
.hero { text-align: center; padding: 30px 10px 10px 10px; }
.hero h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.6rem;
    background: linear-gradient(90deg, #e6005c, #ff4081, #ff6699);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}
.hero p { color: #8c5a6f; letter-spacing: 1px; margin-top: 6px; }

/* Profile Photo Wrapper */
.profile-photo-wrap {
    display: flex;
    justify-content: center;
    margin-top: 10px;
}
.profile-photo-wrap img {
    width: 220px;
    height: 220px;
    border-radius: 50%;
    border: 3px solid transparent;
    background:
        linear-gradient(#ffffff, #ffffff) padding-box,
        linear-gradient(135deg, #e6005c, #ff4081, #ff6699) border-box;
    box-shadow: 0 0 30px rgba(255, 102, 153, 0.25);
    object-fit: cover;
}

/* Profile Card */
.profile-card {
    max-width: 420px;
    margin: 24px auto 0 auto;
    background: #fffafc;
    border: 1px solid #ffd1e1;
    border-radius: 18px;
    padding: 26px 30px;
    text-align: center;
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 20px rgba(255, 102, 153, 0.08);
}
.profile-card h2 {
    color: #4a2b38;
    font-family: 'Orbitron', sans-serif;
    font-size: 1.4rem;
    margin: 4px 0 14px 0;
}
.info-row {
    display: flex;
    justify-content: space-between;
    padding: 10px 4px;
    border-top: 1px solid #ffe6f0;
    color: #4a2b38;
    font-size: 0.95rem;
}
.info-row:first-of-type { border-top: none; }
.info-row span.label { color: #8c5a6f; }
.info-row span.value { font-weight: 600; color: #d8006f; }

footer, #MainMenu { visibility: hidden; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: #fffafc;
    border-right: 1px solid #ffd1e1;
}
[data-testid="stSidebarNav"] {
    padding-top: 6px;
}
[data-testid="stSidebarNav"]::before {
    content: "MACHINE LEARNING HUB";
    display: block;
    margin: 14px 16px 12px 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid #ffd1e1;
    font-family: 'Orbitron', sans-serif;
    font-size: 0.78rem;
    letter-spacing: 1.5px;
    background: linear-gradient(90deg, #e6005c, #ff4081, #ff6699);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
[data-testid="stSidebarNav"] a {
    margin: 2px 10px;
    padding: 10px 14px !important;
    border-radius: 10px;
    color: #8c5a6f !important;
    font-family: 'Prompt', sans-serif;
    font-weight: 500;
    transition: all .2s ease;
}
[data-testid="stSidebarNav"] a:hover {
    background: #ffe6f0;
    color: #d8006f !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, #fff0f5, #ffe6f0);
    color: #d8006f !important;
    box-shadow: inset 3px 0 0 #ff4081;
}

/* เปลี่ยนข้อความเมนู: app -> หน้าหลัก, about -> ผู้พัฒนา */
[data-testid="stSidebarNav"] li:nth-child(1) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(1) a::after { content: "หน้าหลัก"; font-size: 1rem !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a::after { content: "ผู้พัฒนา"; font-size: 1rem !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>ผู้พัฒนา</h1>
    <p>ข้อมูลผู้จัดทำโปรเจค Machine Learning Hub</p>
</div>
""", unsafe_allow_html=True)

photo_path = Path(__file__).resolve().parent.parent / "assets" / "1.jpg"
photo_b64 = base64.b64encode(photo_path.read_bytes()).decode()
st.markdown(
    f'<div class="profile-photo-wrap"><img src="data:image/jpeg;base64,{photo_b64}"></div>',
    unsafe_allow_html=True,
)

st.markdown("""
<div class="profile-card">
    <h2>พีรพัฒน์ กองบุตร</h2>
    <div class="info-row"><span class="label">รหัสนักศึกษา</span><span class="value">664245025</span></div>
    <div class="info-row"><span class="label">หมู่เรียน</span><span class="value">Sec. 66/43</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center;color:#5a6b8c;margin-top:30px;'>Made with Streamlit · Machine Learning Projects</p>", unsafe_allow_html=True)
