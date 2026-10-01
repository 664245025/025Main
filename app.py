import streamlit as st

st.set_page_config(
    page_title="ML Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Orbitron:wght@500;700&display=swap');

/* =========================
   GLOBAL
========================= */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(0, 229, 255, 0.12), transparent 35%),
        radial-gradient(circle at 90% 80%, rgba(124, 58, 237, 0.14), transparent 40%),
        linear-gradient(135deg, #050816 0%, #0a1025 50%, #080b18 100%);
    
    min-height: 100vh;
}

html, body, [class*="css"] {
    font-family: 'Prompt', sans-serif;
}

/* =========================
   HERO
========================= */

.hero {
    text-align: center;
    padding: 45px 10px 25px 10px;
}

.hero .badge {
    display: inline-block;
    padding: 6px 16px;
    border: 1px solid rgba(0, 229, 255, 0.35);
    border-radius: 50px;
    color: #67e8f9;
    background: rgba(0, 229, 255, 0.06);
    font-size: 0.8rem;
    letter-spacing: 2px;
    margin-bottom: 18px;
}

.hero h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 3.2rem;
    font-weight: 700;
    letter-spacing: 2px;
    background: linear-gradient(
        90deg,
        #22d3ee,
        #60a5fa,
        #a78bfa,
        #22d3ee
    );
    background-size: 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientMove 6s ease infinite;
    margin: 0;
}

.hero p {
    color: #94a3b8;
    font-size: 1rem;
    letter-spacing: 1px;
    margin-top: 12px;
}

@keyframes gradientMove {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

/* =========================
   CARDS
========================= */

.card {
    background: linear-gradient(
        145deg,
        rgba(15, 23, 42, 0.95),
        rgba(10, 18, 38, 0.92)
    );

    border: 1px solid rgba(71, 85, 105, 0.5);

    border-radius: 20px;

    padding: 24px;

    height: 270px;

    display: flex;
    flex-direction: column;
    justify-content: space-between;

    position: relative;
    overflow: hidden;

    transition: all 0.35s ease;

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.25);
}

/* เส้นแสงด้านบน */

.card::before {
    content: "";

    position: absolute;

    top: 0;
    left: 0;

    width: 100%;
    height: 2px;

    background: linear-gradient(
        90deg,
        #22d3ee,
        #3b82f6,
        #8b5cf6
    );

    opacity: 0.8;
}

/* Glow */

.card::after {
    content: "";

    position: absolute;

    width: 150px;
    height: 150px;

    right: -70px;
    bottom: -70px;

    background: rgba(34, 211, 238, 0.08);

    border-radius: 50%;

    filter: blur(30px);
}

.card:hover {
    transform: translateY(-8px);

    border-color: rgba(34, 211, 238, 0.7);

    box-shadow:
        0 15px 40px rgba(0, 0, 0, 0.4),
        0 0 25px rgba(34, 211, 238, 0.12);
}

/* =========================
   CARD CONTENT
========================= */

.card .icon {
    width: 52px;
    height: 52px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 14px;

    background: linear-gradient(
        135deg,
        rgba(34, 211, 238, 0.15),
        rgba(124, 58, 237, 0.15)
    );

    border: 1px solid rgba(34, 211, 238, 0.25);

    font-size: 1.7rem;

    margin-bottom: 15px;
}

.card h3 {
    color: #f1f5f9;

    margin: 5px 0 8px 0;

    font-size: 1.15rem;

    font-weight: 600;
}

.card p {
    color: #94a3b8;

    font-size: 0.88rem;

    line-height: 1.6;

    margin-bottom: 10px;
}

/* =========================
   BUTTON
========================= */

.btn {
    display: block;

    text-align: center;

    text-decoration: none !important;

    padding: 11px 15px;

    border-radius: 12px;

    font-weight: 600;

    color: #ffffff !important;

    background: linear-gradient(
        90deg,
        #0891b2,
        #2563eb,
        #7c3aed
    );

    background-size: 200%;

    transition: all 0.3s ease;

    box-shadow:
        0 5px 15px rgba(37, 99, 235, 0.25);
}

.btn:hover {
    background-position: 100% 50%;

    transform: translateY(-2px);

    box-shadow:
        0 8px 22px rgba(34, 211, 238, 0.25);
}

/* =========================
   SIDEBAR
========================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #070b18,
            #0b1225
        );

    border-right: 1px solid rgba(71, 85, 105, 0.4);
}

[data-testid="stSidebarNav"] {
    padding-top: 8px;
}

/* Sidebar Title */

[data-testid="stSidebarNav"]::before {
    content: "🤖  MACHINE LEARNING HUB";

    display: block;

    margin: 15px 16px 15px 16px;

    padding-bottom: 14px;

    border-bottom: 1px solid rgba(71, 85, 105, 0.4);

    font-family: 'Orbitron', sans-serif;

    font-size: 0.72rem;

    letter-spacing: 1.5px;

    color: #67e8f9;
}

/* Sidebar menu */

[data-testid="stSidebarNav"] a {
    margin: 4px 10px;

    padding: 11px 14px !important;

    border-radius: 11px;

    color: #94a3b8 !important;

    font-family: 'Prompt', sans-serif;

    font-weight: 500;

    transition: all 0.25s ease;
}

[data-testid="stSidebarNav"] a:hover {
    background: rgba(34, 211, 238, 0.08);

    color: #67e8f9 !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background:
        linear-gradient(
            90deg,
            rgba(34, 211, 238, 0.13),
            rgba(124, 58, 237, 0.08)
        );

    color: #67e8f9 !important;

    box-shadow:
        inset 3px 0 0 #22d3ee;
}

/* =========================
   CHANGE MENU NAME
========================= */

[data-testid="stSidebarNav"] li:nth-child(1) a * {
    font-size: 0 !important;
}

[data-testid="stSidebarNav"] li:nth-child(1) a::after {
    content: "หน้าหลัก";
    font-size: 1rem !important;
}

[data-testid="stSidebarNav"] li:nth-child(2) a * {
    font-size: 0 !important;
}

[data-testid="stSidebarNav"] li:nth-child(2) a::after {
    content: "ผู้พัฒนา";
    font-size: 1rem !important;
}

/* =========================
   HIDE DEFAULT UI
========================= */

footer,
#MainMenu {
    visibility: hidden;
}

[data-testid="stSidebarCollapsedControl"] {
    visibility: visible !important;
}

/* =========================
   FOOTER
========================= */

.footer {
    text-align: center;

    color: #64748b;

    font-size: 0.8rem;

    margin-top: 35px;

    padding: 20px;

    border-top: 1px solid rgba(71, 85, 105, 0.25);
}

.footer span {
    color: #22d3ee;
}
</style>

<div class="hero">

    <div class="badge">
        MACHINE LEARNING PROJECTS
    </div>

    <h1>แนะนำสถานที่ท่องเที่ยว</h1>

    <p>
        ศูนย์รวมเว็บแอปพลิเคชันสำหรับการวิเคราะห์
        และแนะนำสถานที่ท่องเที่ยว
    </p>

</div>
""", unsafe_allow_html=True)


# =========================
# APPLICATIONS
# =========================

APPS = [

    (
        "📊",
        "โครงสร้างข้อมูลท่องเที่ยว",
        "นำเสนอและจัดโครงสร้างข้อมูลสถานที่ท่องเที่ยว เพื่อเตรียมข้อมูลสำหรับการวิเคราะห์",
        "https://colab.research.google.com/drive/1ZmBJEQh-4eOANw2rbN9O-rx08Qo6DiSQ?usp=sharing"
    ),

    (
        "🔍",
        "วิเคราะห์ข้อมูลท่องเที่ยว",
        "วิเคราะห์ข้อมูลและศึกษาความสัมพันธ์ของข้อมูลสถานที่ท่องเที่ยว",
        "https://colab.research.google.com/drive/12YK3jnjWNXlemkG97EKQmmonLxFx8Cmi?usp=sharing"
    ),

    (
        "🤖",
        "ระบบแนะนำสถานที่ท่องเที่ยว",
        "ระบบแนะนำสถานที่ท่องเที่ยวจากข้อมูล โดยใช้แนวคิด Machine Learning",
        "https://mzvpqrmpmmrw4htsbjr7tt.streamlit.app/"
    ),

]


# =========================
# CARD DISPLAY
# =========================

cols = st.columns(3)

for i, (icon, title, desc, url) in enumerate(APPS):

    with cols[i % 3]:

        st.markdown(
            f"""
            <div class="card">

                <div>

                    <div class="icon">
                        {icon}
                    </div>

                    <h3>
                        {title}
                    </h3>

                    <p>
                        {desc}
                    </p>

                </div>

                <a
                    class="btn"
                    href="{url}"
                    target="_blank"
                >
                    เปิดแอป →
                </a>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# FOOTER
# =========================

st.markdown(
    """
    <div class="footer">
        <span>●</span>
        Made with Streamlit
        ·
        Machine Learning Projects
        ·
        Tourism Recommendation System
    </div>
    """,
    unsafe_allow_html=True
)