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

:root {
    --primary-color: #ff6b6b;
    --secondary-color: #f093fb;
    --text-dark: #2d3748;
    --text-light: #718096;
}

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

.hero-section {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 30px;
    padding: 50px 40px;
    text-align: center;
    margin-bottom: 40px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(10px);
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
    color: var(--text-light);
    font-weight: 400;
}

.card-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 30px;
    margin: 40px 0;
}

.card {
    background: white;
    border-radius: 20px;
    padding: 35px;
    height: 320px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
    border: 2px solid rgba(255, 255, 255, 0.5);
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.25);
}

.card-icon {
    font-size: 3rem;
    margin-bottom: 15px;
}

.card-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-dark);
    margin-bottom: 12px;
}

.card-description {
    font-size: 1rem;
    color: var(--text-light);
    line-height: 1.6;
    flex-grow: 1;
}

.card-button {
    display: inline-block;
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
    margin-top: 20px;
}

.card-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(102, 126, 234, 0.5);
}

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

.footer {
    text-align: center;
    padding: 30px;
    color: white;
    font-size: 1rem;
    margin-top: 50px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

#MainMenu, footer {
    visibility: hidden;
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
                <div class="card-icon">{icon}</div>
                <h3 class="card-title">{title}</h3>
                <p class="card-description">{desc}</p>
            </div>
            <a href="{url}" target="_blank" class="card-button">
                เปิดแอปพลิเคชัน →
            </a>
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