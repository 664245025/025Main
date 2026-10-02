import streamlit as st

st.set_page_config(
    page_title="ML Hub",
    page_icon="🏝️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;500;700&family=Orbitron:wght@700&display=swap');

/* Main App Layout */
.stApp {
    background: #05070f;
    background-image:
        radial-gradient(circle at 20% 20%, rgba(0,160,255,0.14) 0%, transparent 40%),
        radial-gradient(circle at 80% 70%, rgba(0,90,200,0.18) 0%, transparent 40%),
        linear-gradient(rgba(0,160,255,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,160,255,0.05) 1px, transparent 1px);
    background-size: auto, auto, 40px 40px, 40px 40px;
    color: #e6f1ff;
}
[data-testid="stHeader"] { background: transparent; }
html, body, [class*="css"] { font-family: 'Prompt', sans-serif; }

/* Hero Section */
.hero {
    text-align: center;
    padding: 30px 10px 10px 10px;
}
.hero h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 3rem;
    background: linear-gradient(90deg, #00b4ff, #38d0ff, #7fe3ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}
.hero p { color: #8fa8c8; letter-spacing: 1px; margin-top: 6px; }

/* Cards */
.card {
    background: #0b1220;
    border: 1px solid #1b3a63;
    border-radius: 18px;
    padding: 22px;
    height: 250px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(8px);
    transition: all .3s ease;
    margin-bottom: 18px;
    box-shadow: 0 4px 15px rgba(0, 120, 255, 0.10);
}
.card:hover {
    transform: translateY(-6px);
    border-color: #00b4ff;
    box-shadow: 0 8px 25px rgba(0, 180, 255, 0.30);
}
.card .icon { font-size: 2.2rem; }
.card h3 { color: #e6f1ff; margin: 8px 0 4px 0; font-size: 1.15rem; font-weight: 700; }
.card p { color: #8fa8c8; font-size: 0.85rem; line-height: 1.4; }

/* Buttons */
.btn {
    display: block;
    text-align: center;
    text-decoration: none !important;
    padding: 10px;
    border-radius: 10px;
    font-weight: 600;
    color: #ffffff !important;
    background: linear-gradient(90deg, #0066ff, #00b4ff);
    transition: all .2s;
    box-shadow: 0 4px 12px rgba(0, 140, 255, 0.35);
}
.btn:hover {
    filter: brightness(1.1);
    box-shadow: 0 6px 18px rgba(0, 180, 255, 0.5);
}

footer, #MainMenu { visibility: hidden; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: #070c18;
    border-right: 1px solid #1b3a63;
}
[data-testid="stSidebarNav"] {
    padding-top: 6px;
}
[data-testid="stSidebarNav"]::before {
    content: "MACHINE LEARNING HUB";
    display: block;
    margin: 14px 16px 12px 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid #1b3a63;
    font-family: 'Orbitron', sans-serif;
    font-size: 0.78rem;
    letter-spacing: 1.5px;
    background: linear-gradient(90deg, #00b4ff, #38d0ff, #7fe3ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
[data-testid="stSidebarNav"] a {
    margin: 2px 10px;
    padding: 10px 14px !important;
    border-radius: 10px;
    color: #8fa8c8 !important;
    font-family: 'Prompt', sans-serif;
    font-weight: 500;
    transition: all .2s ease;
}
[data-testid="stSidebarNav"] a:hover {
    background: #0f1d36;
    color: #38d0ff !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, #0a1a33, #0f2548);
    color: #38d0ff !important;
    box-shadow: inset 3px 0 0 #00b4ff;
}

/* เปลี่ยนข้อความเมนู: app -> หน้าหลัก, about -> ผู้พัฒนา */
[data-testid="stSidebarNav"] li:nth-child(1) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(1) a::after { content: "หน้าหลัก"; font-size: 1rem !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a::after { content: "ผู้พัฒนา"; font-size: 1rem !important; }
</style>

<div class="hero">
    <h1>แนะนำสถานที่ท่องเที่ยว</h1>
    <p>ศูนย์รวมเว็บแอปพลิเคชัน สถานที่ท่องเที่ยว</p>
</div>
""", unsafe_allow_html=True)

st.write("")

APPS = [
    ("🏝️", "โครงสร้างข้อมูลทีท่องเที่ยว", "นำสถานที่ท่องเที่ยว", "https://colab.research.google.com/drive/1ZmBJEQh-4eOANw2rbN9O-rx08Qo6DiSQ?usp=sharing"),
    ("⛰️", "วิเคราะข้อมูลท่องเที่ยว", "วิเคราะข้อมูลและความสัมพันธ์ของสถานที่ท่องเที่ยว", "https://colab.research.google.com/drive/12YK3jnjWNXlemkG97EKQmmonLxFx8Cmi?usp=sharing"),
    ("🛕", "ระบบแนะนำสถานที่ท่องเที่ยว", "แนะนำสถานที่ท่องเที่ยวจากข้อมูล", "https://mzvpqrmpmmrw4htsbjr7tt.streamlit.app/"),
    ("🎨", "สไลด์นำเสนอโปรเจกต์", "สรุปภาพรวมและผลงานของโปรเจกต์แนะนำสถานที่ท่องเที่ยว", "https://canva.link/6sdssxnz2wcjzi4"),
]

cols = st.columns(3)
for i, (icon, title, desc, url) in enumerate(APPS):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
            <div>
                <div class="icon">{icon}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            <a class="btn" href="{url}" target="_blank">เปิดแอป →</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center;color:#8fa8c8;margin-top:30px;'>Made with Streamlit · Recommend_Projects</p>", unsafe_allow_html=True)
