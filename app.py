import streamlit as st

st.set_page_config(
    page_title="ML Hub - Tourism",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Enhanced CSS with modern design
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Orbitron:wght@700;800;900&display=swap');

/* Root Variables */
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --pink-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --purple-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --gold-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    --text-dark: #2d3748;
    --text-light: #718096;
    --bg-primary: #fafbfc;
    --card-bg: rgba(255, 255, 255, 0.95);
}

/* Main App Background with Animation */
.stApp {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    font-family: 'Prompt', sans-serif;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Main Container */
.main-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 20px;
}

/* Hero Section with Glassmorphism */
.hero-section {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(20px);
    border-radius: 30px;
    padding: 60px 40px;
    text-align: center;
    margin-bottom: 50px;
    border: 2px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
    animation: fadeInDown 1s ease;
}

@keyframes fadeInDown {
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
    font-size: 3.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #ffffff 0%, #ffd700 50%, #ff6b6b 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 15px;
    text-shadow: 0 4px 15px rgba(0,0,0,0.1);
    letter-spacing: 2px;
}

.hero-subtitle {
    font-size: 1.3rem;
    color: rgba(255, 255, 255, 0.95);
    font-weight: 500;
    letter-spacing: 1px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

/* Card Container */
.cards-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 30px;
    margin: 40px 0;
}

/* Enhanced Cards */
.card {
    background: var(--card-bg);
    border-radius: 25px;
    padding: 35px;
    height: 320px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(15px);
    border: 2px solid rgba(255, 255, 255, 0.5);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.8s ease;
    animation-fill-mode: both;
}

.card:nth-child(1) { animation-delay: 0.1s; }
.card:nth-child(2) { animation-delay: 0.2s; }
.card:nth-child(3) { animation-delay: 0.3s; }

@keyframes fadeInUp {
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
    height: 5px;
    background: var(--pink-gradient);
    transform: scaleX(0);
    transition: transform 0.4s ease;
}

.card:hover::before {
    transform: scaleX(1);
}

.card:hover {
    transform: translateY(-15px) scale(1.02);
    box-shadow: 0 30px 80px rgba(0, 0, 0, 0.25);
    border-color: rgba(255, 107, 107, 0.5);
}

.card-icon {
    font-size: 3.5rem;
    margin-bottom: 20px;
    display: inline-block;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-10px); }
    60% { transform: translateY(-5px); }
}

.card-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-dark);
    margin-bottom: 12px;
    line-height: 1.3;
}

.card-description {
    font-size: 1rem;
    color: var(--text-light);
    line-height: 1.6;
    flex-grow: 1;
}

/* Enhanced Buttons */
.card-button {
    display: inline-block;
    width: 100%;
    padding: 16px 24px;
    background: var(--pink-gradient);
    color: white !important;
    text-decoration: none !important;
    border-radius: 15px;
    font-weight: 600;
    font-size: 1.1rem;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4);
    border: none;
    margin-top: 20px;
    position: relative;
    overflow: hidden;
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
    box-shadow: 0 15px 40px rgba(245, 87, 108, 0.5);
}

.card-button:active {
    transform: translateY(-1px);
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(255,255,255,0.98) 0%, rgba(255,255,255,0.95) 100%);
    backdrop-filter: blur(20px);
    border-right: 2px solid rgba(255, 255, 255, 0.5);
    box-shadow: 5px 0 30px rgba(0, 0, 0, 0.1);
}

.sidebar-header {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.1rem;
    font-weight: 800;
    background: var(--pink-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    padding: 20px 16px;
    border-bottom: 3px solid rgba(245, 87, 108, 0.3);
    margin-bottom: 10px;
    letter-spacing: 2px;
    text-align: center;
}

/* Navigation Links */
[data-testid="stSidebarNav"] a {
    margin: 8px 12px !important;
    padding: 14px 18px !important;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
    border: 2px solid transparent;
}

[data-testid="stSidebarNav"] a:hover {
    background: linear-gradient(135deg, rgba(245, 87, 108, 0.1) 0%, rgba(240, 147, 251, 0.1) 100%);
    border-color: rgba(245, 87, 108, 0.3);
    transform: translateX(5px);
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: var(--pink-gradient);
    color: white !important;
    box-shadow: 0 8px 20px rgba(245, 87, 108, 0.3);
    transform: translateX(5px);
}

/* Footer */
.footer {
    text-align: center;
    padding: 40px 20px;
    color: rgba(255, 255, 255, 0.9);
    font-size: 1rem;
    font-weight: 500;
    margin-top: 50px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.footer a {
    color: #ffd700;
    text-decoration: none;
    font-weight: 600;
}

/* Hide Streamlit Branding */
#MainMenu, footer {
    visibility: hidden;
}

/* Responsive Design */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2.2rem;
    }
    .hero-subtitle {
        font-size: 1rem;
    }
    .cards-container {
        grid-template-columns: 1fr;
        gap: 20px;
    }
    .card {
        height: auto;
        min-height: 300px;
    }
}

/* Loading Animation */
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}

.loading {
    animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
</style>
""", unsafe_allow_html=True)

# Main Content
st.markdown("""
<div class="main-container">
    <div class="hero-section">
        <h1 class="hero-title"> แนะนำสถานที่ท่องเที่ยว</h1>
        <p class="hero-subtitle">ศูนย์รวมเว็บแอปพลิเคชัน Machine Learning สำหรับการท่องเที่ยว</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Apps Data
APPS = [
    ("📍", "โครงสร้างข้อมูลท่องเที่ยว", 
     "นำสถานที่ท่องเที่ยวที่น่าสนใจมาจัดระบบและวิเคราะห์ด้วยเทคนิค Machine Learning", 
     "https://colab.research.google.com/drive/1ZmBJEQh-4eOANw2rbN9O-rx08Qo6DiSQ?usp=sharing"),
    
    ("📊", "วิเคราะห์ข้อมูลท่องเที่ยว", 
     "วิเคราะห์ข้อมูลและความสัมพันธ์ของสถานที่ท่องเที่ยวด้วยโมเดลขั้นสูง", 
     "https://colab.research.google.com/drive/12YK3jnjWNXlemkG97EKQmmonLxFx8Cmi?usp=sharing"),
    
    ("🎯", "ระบบแนะนำสถานที่ท่องเที่ยว", 
     "แนะนำสถานที่ท่องเที่ยวที่เหมาะสมจากข้อมูลด้วย AI Recommendation System", 
     "https://mzvpqrmpmmrw4htsbjr7tt.streamlit.app/"),
]

# Create Cards
cards_html = '<div class="cards-container">'
for icon, title, desc, url in APPS:
    cards_html += f"""
    <div class="card">
        <div>
            <div class="card-icon">{icon}</div>
            <h3 class="card-title">{title}</h3>
            <p class="card-description">{desc}</p>
        </div>
        <a class="card-button" href="{url}" target="_blank">
            เปิดแอปพลิเคชัน →
        </a>
    </div>
    """
cards_html += '</div>'

st.markdown(cards_html, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Made with ❤️ using Streamlit · Machine Learning Projects</p>
    <p style="margin-top: 10px; font-size: 0.9rem;">© 2026 Tourism ML Hub</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Content
with st.sidebar:
    st.markdown('<div class="sidebar-header">MACHINE LEARNING HUB</div>', unsafe_allow_html=True)
    st.markdown("")
    
    # Add some info in sidebar
    st.info("🎓 โครงการ Machine Learning\n\n📍 ระบบแนะนำการท่องเที่ยว\n\n Powered by Streamlit")