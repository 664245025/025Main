import streamlit as st

st.set_page_config(
    page_title="ML Hub - Tourism",
    page_icon="📍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Orbitron:wght@700;800&display=swap');

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    background-size: 200% 200%;
    animation: gradientAnimation 15s ease infinite;
    font-family: 'Prompt', sans-serif;
}

@keyframes gradientAnimation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Hero Section */
.hero-section {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 30px;
    padding: 50px 40px;
    text-align: center;
    margin-bottom: 40px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
}

.hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #f093fb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 15px;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: #718096;
    font-weight: 400;
}

/* Card Styling */
.card {
    background: white;
    border-radius: 20px;
    padding: 35px;
    height: 380px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
    margin-bottom: 20px;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.25);
}

.card-icon {
    font-size: 3.5rem;
    margin-bottom: 20px;
    display: block;
}

.card-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #2d3748;
    margin-bottom: 15px;
    line-height: 1.3;
}

.card-description {
    font-size: 1rem;
    color: #718096;
    line-height: 1.6;
    flex-grow: 1;
}

/* Button Container */
.button-container {
    margin-top: 25px;
    padding-top: 20px;
    border-top: 2px solid #f0f0f0;
}

.card-button {
    display: block;
    width: 100%;
    padding: 15px 24px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white !important;
    text-decoration: none !important;
    border-radius: 12px;
    font-weight: 600;
    font-size: 1.1rem;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    border: none;
}

.card-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(102, 126, 234, 0.5);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(10px);
}

.sidebar-header {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #f093fb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding: 20px 16px;
    text-align: center;
    border-bottom: 2px solid rgba(102, 126, 234, 0.3);
    margin-bottom: 15px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 30px;
    color: white;
    font-size: 1rem;
    margin-top: 50px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

/* Hide Streamlit elements */
#MainMenu, footer {
    visibility: hidden;
}

/* Fix for Streamlit containers */
.stColumn {
    display: flex;
    flex-direction: column;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title"> แนะนำสถานที่ท่องเที่ยว</h1>
    <p class="hero-subtitle">ศูนย์รวมเว็บแอปพลิเคชัน Machine Learning สำหรับการท่องเที่ยว</p>
</div>
""", unsafe_allow_html=True)

# Apps Data
APPS = [
    ("", "โครงสร้างข้อมูลท่องเที่ยว", 
     "นำสถานที่ท่องเที่ยวที่น่าสนใจมาจัดระบบและวิเคราะห์ด้วยเทคนิค Machine Learning", 
     "https://colab.research.google.com/drive/1ZmBJEQh-4eOANw2rbN9O-rx08Qo6DiSQ?usp=sharing"),
    
    ("📊", "วิเคราะห์ข้อมูลท่องเที่ยว", 
     "วิเคราะห์ข้อมูลและความสัมพันธ์ของสถานที่ท่องเที่ยวด้วยโมเดลขั้นสูง", 
     "https://colab.research.google.com/drive/12YK3jnjWNXlemkG97EKQmmonLxFx8Cmi?usp=sharing"),
    
    ("🎯", "ระบบแนะนำสถานที่ท่องเที่ยว", 
     "แนะนำสถานที่ท่องเที่ยวที่เหมาะสมจากข้อมูลด้วย AI Recommendation System", 
     "https://mzvpqrmpmmrw4htsbjr7tt.streamlit.app/"),
]

# Create Cards using Streamlit columns
cols = st.columns(3)

for i, (icon, title, desc, url) in enumerate(APPS):
    with cols[i]:
        st.markdown(f"""
        <div class="card">
            <div>
                <span class="card-icon">{icon}</span>
                <h3 class="card-title">{title}</h3>
                <p class="card-description">{desc}</p>
            </div>
            <div class="button-container">
                <a href="{url}" target="_blank" class="card-button">
                    เปิดแอปพลิเคชัน →
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Made with ❤️ using Streamlit · Machine Learning Projects</p>
    <p style="margin-top: 10px; font-size: 0.9rem;">© 2026 Tourism ML Hub</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-header">MACHINE LEARNING HUB</div>', unsafe_allow_html=True)
    st.markdown("")
    st.info("🎓 โครงการ Machine Learning\n\n📍 ระบบแนะนำการท่องเที่ยว\n\nPowered by Streamlit")