import streamlit as st

st.set_page_config(
    page_title="ML Hub",
    page_icon="📌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS Styling - ตรงตามต้นฉบับ
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Orbitron:wght@700;800&display=swap');

/* Main App Background with Grid Pattern */
.stApp {
    background: #ffffff;
    background-image:
        radial-gradient(circle at 20% 20%, rgba(255,102,153,0.08) 0%, transparent 40%),
        radial-gradient(circle at 80% 70%, rgba(255,182,193,0.12) 0%, transparent 40%),
        linear-gradient(rgba(255,102,153,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,102,153,0.04) 1px, transparent 1px);
    background-size: auto, auto, 40px 40px, 40px 40px;
    font-family: 'Prompt', sans-serif;
}

html, body, [class*="css"] {
    font-family: 'Prompt', sans-serif !important;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 40px 20px 20px 20px;
}
.hero h1 {
    font-family: 'Prompt', sans-serif;
    font-size: 3rem;
    font-weight: 700;
    color: #e6005c;
    margin-bottom: 10px;
    letter-spacing: 1px;
}
.hero p {
    color: #8c5a6f;
    font-size: 1.05rem;
    letter-spacing: 0.5px;
    margin-top: 8px;
}

/* Card Grid */
.card-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 25px;
    margin: 40px auto;
    max-width: 1200px;
    padding: 0 20px;
}

/* Cards */
.card {
    background: #fffafc;
    border: 1.5px solid #ffd1e1;
    border-radius: 18px;
    padding: 28px;
    min-height: 240px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(255, 102, 153, 0.06);
}
.card:hover {
    transform: translateY(-6px);
    border-color: #ff6699;
    box-shadow: 0 8px 25px rgba(255, 64, 129, 0.2);
}
.card-icon {
    font-size: 2.2rem;
    margin-bottom: 10px;
    display: block;
}
.card-title {
    color: #4a2b38;
    font-size: 1.15rem;
    font-weight: 700;
    margin: 8px 0 10px 0;
    line-height: 1.4;
}
.card-desc {
    color: #8c5a6f;
    font-size: 0.9rem;
    line-height: 1.5;
    flex-grow: 1;
    margin-bottom: 18px;
}

/* Buttons */
.btn {
    display: block;
    width: 100%;
    text-align: center;
    text-decoration: none !important;
    padding: 12px;
    border-radius: 10px;
    font-weight: 600;
    font-size: 1rem;
    color: #ffffff !important;
    background: linear-gradient(90deg, #ff4081, #ff6699);
    transition: all 0.2s;
    box-shadow: 0 4px 12px rgba(255, 64, 129, 0.25);
    border: none;
}
.btn:hover {
    filter: brightness(1.08);
    box-shadow: 0 6px 18px rgba(255, 64, 129, 0.35);
    transform: translateY(-1px);
}

/* Footer */
.footer-text {
    text-align: center;
    color: #5a6b8c;
    margin-top: 40px;
    padding-bottom: 30px;
    font-size: 0.95rem;
}

/* Hide Streamlit elements */
footer, #MainMenu {
    visibility: hidden;
}

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
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #e6005c;
}

[data-testid="stSidebarNav"] a {
    margin: 2px 10px;
    padding: 10px 14px !important;
    border-radius: 10px;
    color: #8c5a6f !important;
    font-family: 'Prompt', sans-serif;
    font-weight: 500;
    transition: all 0.2s ease;
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

/* Rename sidebar menu items */
[data-testid="stSidebarNav"] li:nth-child(1) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(1) a::after { content: "หน้าหลัก"; font-size: 1rem !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a::after { content: "ผู้พัฒนา"; font-size: 1rem !important; }

/* Responsive */
@media (max-width: 900px) {
    .card-grid {
        grid-template-columns: 1fr;
    }
    .hero h1 {
        font-size: 2rem;
    }
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>แนะนำสถานที่ท่องเที่ยว</h1>
    <p>ศูนย์รวมเว็บแอปพลิเคชัน สถานที่ท่องเที่ยว</p>
</div>
""", unsafe_allow_html=True)

# Apps Data
APPS = [
    ("📌", "โครงสร้างข้อมูลท่องเที่ยว", "นำสถานที่ท่องเที่ยว", 
     "https://colab.research.google.com/drive/1ZmBJEQh-4eOANw2rbN9O-rx08Qo6DiSQ?usp=sharing"),
    ("📌", "วิเคราะห์ข้อมูลท่องเที่ยว", "วิเคราะห์ข้อมูลและความสัมพันธ์ของสถานที่ท่องเที่ยว", 
     "https://colab.research.google.com/drive/12YK3jnjWNXlemkG97EKQmmonLxFx8Cmi?usp=sharing"),
    ("", "ระบบแนะนำสถานที่ท่องเที่ยว", "แนะนำสถานที่ท่องเที่ยวจากข้อมูล", 
     "https://mzvpqrmpmmrw4htsbjr7tt.streamlit.app/"),
]

# Create Cards
cards_html = '<div class="card-grid">'
for icon, title, desc, url in APPS:
    cards_html += f"""
    <div class="card">
        <div>
            <span class="card-icon">{icon}</span>
            <h3 class="card-title">{title}</h3>
            <p class="card-desc">{desc}</p>
        </div>
        <a class="btn" href="{url}" target="_blank">เปิดแอป →</a>
    </div>
    """
cards_html += '</div>'

st.markdown(cards_html, unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer-text">Made with Streamlit · Machine Learning Projects</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("")
    # Sidebar navigation will be handled by Streamlit pages