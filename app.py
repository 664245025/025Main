import streamlit as st

st.set_page_config(
    page_title="ML Hub - Tourism",
    page_icon="📍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Enhanced CSS with Professional Design
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&family=Orbitron:wght@700;800;900&display=swap');

/* Animated Background */
.stApp {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    font-family: 'Prompt', sans-serif;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Hero Section with Glassmorphism */
.hero-section {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    border-radius: 30px;
    padding: 60px 40px;
    text-align: center;
    margin-bottom: 50px;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
    border: 2px solid rgba(255, 255, 255, 0.3);
    animation: slideDown 0.8s ease;
}

@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 3.2rem;
    font-weight: 900;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 20px;
    letter-spacing: 2px;
}

.hero-subtitle {
    font-size: 1.3rem;
    color: #4a5568;
    font-weight: 500;
    letter-spacing: 1px;
}

/* Card Grid */
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 35px;
    margin: 40px 0;
}

/* Enhanced Cards */
.card {
    background: white;
    border-radius: 25px;
    padding: 40px;
    min-height: 420px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
    animation: slideUp 0.8s ease;
    animation-fill-mode: both;
}

.card:nth-child(1) { animation-delay: 0.1s; }
.card:nth-child(2) { animation-delay: 0.2s; }
.card:nth-child(3) { animation-delay: 0.3s; }

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    transform: scaleX(0);
    transition: transform 0.4s ease;
}

.card:hover::before {
    transform: scaleX(1);
}

.card:hover {
    transform: translateY(-15px) scale(1.02);
    box-shadow: 0 30px 80px rgba(0, 0, 0, 0.3);
}

.card-icon {
    font-size: 4rem;
    margin-bottom: 25px;
    display: inline-block;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-10px); }
    60% { transform: translateY(-5px); }
}

.card-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #2d3748;
    margin-bottom: 15px;
    line-height: 1.4;
}

.card-description {
    font-size: 1.05rem;
    color: #718096;
    line-height: 1.7;
    flex-grow: 1;
    margin-bottom: 25px;
}

/* Button with Ripple Effect */
.button-wrapper {
    margin-top: auto;
    padding-top: 20px;
}

.card-button {
    display: block;
    width: 100%;
    padding: 18px 30px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white !important;
    text-decoration: none !important;
    border-radius: 15px;
    font-weight: 700;
    font-size: 1.15rem;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    position: relative;
    overflow: hidden;
    border: none;
}

.card-button::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

.card-button:hover::before {
    width: 300px;
    height: 300px;
}

.card-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(20px);
    border-right: 2px solid rgba(255, 255, 255, 0.5);
    box-shadow: 5px 0 30px rgba(0, 0, 0, 0.1);
}

.sidebar-header {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.3rem;
    font-weight: 900;
    background: linear-gradient(135deg, #667eea 0%, #f093fb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding: 25px 16px;
    text-align: center;
    border-bottom: 3px solid rgba(102, 126, 234, 0.3);
    margin-bottom: 20px;
    letter-spacing: 2px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 40px 20px;
    color: white;
    font-size: 1.1rem;
    font-weight: 500;
    margin-top: 60px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

/* Hide Streamlit elements */
#MainMenu, footer {
    visibility: hidden;
}

/* Responsive */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2rem;
    }
    .hero-subtitle {
        font-size: 1rem;
    }
    .card-grid {
        grid-template-columns: 1fr;
        gap: 25px;
    }
    .card {
        min-height: 380px;
        padding: 30px;
    }
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">แนะนำสถานที่ท่องเที่ยว</h1>
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

# Create Cards using HTML Grid
cards_html = '<div class="card-grid">'
for icon, title, desc, url in APPS:
    cards_html += f"""
    <div class="card">
        <div>
            <span class="card-icon">{icon}</span>
            <h3 class="card-title">{title}</h3>
            <p class="card-description">{desc}</p>
        </div>
        <div class="button-wrapper">
            <a href="{url}" target="_blank" class="card-button">
                เปิดแอปพลิเคชัน →
            </a>
        </div>
    </div>
    """
cards_html += '</div>'

st.markdown(cards_html, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Made with ❤️ using Streamlit · Machine Learning Projects</p>
    <p style="margin-top: 10px; font-size: 0.95rem;">© 2026 Tourism ML Hub</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-header">MACHINE LEARNING HUB</div>', unsafe_allow_html=True)
    st.markdown("")
    st.info("🎓 โครงการ Machine Learning\n\n📍 ระบบแนะนำการท่องเที่ยว\n\nPowered by Streamlit")