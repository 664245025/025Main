import streamlit as st
from textwrap import dedent

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ML Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# CSS
# =========================================================

st.markdown(dedent("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Orbitron:wght@500;700&display=swap');

/* =========================
   MAIN BACKGROUND
========================= */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(0, 229, 255, 0.10),
            transparent 35%
        ),
        radial-gradient(
            circle at 90% 80%,
            rgba(124, 58, 237, 0.13),
            transparent 40%
        ),
        linear-gradient(
            135deg,
            #050816 0%,
            #0a1025 50%,
            #080b18 100%
        );

    min-height: 100vh;
}

html,
body,
[class*="css"] {
    font-family: 'Prompt', sans-serif;
}


/* =========================
   HERO
========================= */

.hero {
    text-align: center;
    padding: 45px 10px 30px 10px;
}

.badge {
    display: inline-block;

    padding: 7px 18px;

    border: 1px solid rgba(34, 211, 238, 0.35);

    border-radius: 50px;

    color: #67e8f9;

    background: rgba(34, 211, 238, 0.06);

    font-size: 0.78rem;

    letter-spacing: 2px;

    margin-bottom: 18px;
}

.hero h1 {
    font-family: 'Orbitron', sans-serif;

    font-size: 3.2rem;

    font-weight: 700;

    letter-spacing: 2px;

    background:
        linear-gradient(
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

    letter-spacing: 0.5px;

    margin-top: 14px;

    line-height: 1.8;
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
    background:
        linear-gradient(
            145deg,
            rgba(15, 23, 42, 0.96),
            rgba(10, 18, 38, 0.95)
        );

    border: 1px solid rgba(71, 85, 105, 0.55);

    border-radius: 20px;

    padding: 25px;

    height: 310px;

    display: flex;

    flex-direction: column;

    justify-content: space-between;

    position: relative;

    overflow: hidden;

    transition: all 0.35s ease;

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.25);
}


/* เส้นด้านบน */

.card::before {
    content: "";

    position: absolute;

    top: 0;
    left: 0;

    width: 100%;
    height: 3px;

    background:
        linear-gradient(
            90deg,
            #22d3ee,
            #3b82f6,
            #8b5cf6
        );
}


/* Glow */

.card::after {
    content: "";

    position: absolute;

    width: 180px;
    height: 180px;

    right: -90px;
    bottom: -90px;

    background: rgba(34, 211, 238, 0.08);

    border-radius: 50%;

    filter: blur(35px);

    pointer-events: none;
}


/* Hover */

.card:hover {

    transform: translateY(-8px);

    border-color: rgba(34, 211, 238, 0.7);

    box-shadow:
        0 18px 45px rgba(0, 0, 0, 0.45),
        0 0 25px rgba(34, 211, 238, 0.12);
}


/* =========================
   CARD ICON
========================= */

.icon {

    width: 58px;
    height: 58px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 16px;

    background:
        linear-gradient(
            135deg,
            rgba(34, 211, 238, 0.15),
            rgba(124, 58, 237, 0.18)
        );

    border: 1px solid rgba(34, 211, 238, 0.25);

    font-size: 1.8rem;

    margin-bottom: 18px;
}


/* =========================
   CARD TITLE
========================= */

.card h3 {

    color: #f1f5f9;

    margin: 0 0 10px 0;

    font-size: 1.18rem;

    font-weight: 600;
}


/* =========================
   CARD DESCRIPTION
========================= */

.card p {

    color: #94a3b8;

    font-size: 0.88rem;

    line-height: 1.7;

    margin: 0;
}


/* =========================
   BUTTON
========================= */

.btn {

    display: block;

    width: 100%;

    text-align: center;

    text-decoration: none !important;

    padding: 12px 15px;

    border-radius: 12px;

    font-weight: 600;

    color: white !important;

    background:
        linear-gradient(
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
        0 8px 22px rgba(34, 211, 238, 0.3);
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


/* Sidebar Header */

[data-testid="stSidebarNav"]::before {

    content: "🤖  MACHINE LEARNING HUB";

    display: block;

    margin: 15px 16px;

    padding-bottom: 14px;

    border-bottom: 1px solid rgba(71, 85, 105, 0.4);

    font-family: 'Orbitron', sans-serif;

    font-size: 0.72rem;

    letter-spacing: 1.5px;

    color: #67e8f9;
}


/* Sidebar Menu */

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


/* เปลี่ยนชื่อเมนู */

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
   HIDE STREAMLIT
========================= */

footer,
#MainMenu {
    visibility: hidden;
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
"""), unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

hero_html = """
<div class="hero">

    <div class="badge">
        MACHINE LEARNING PROJECTS
    </div>

    <h1>
        แนะนำสถานที่ท่องเที่ยว
    </h1>

    <p>
        ศูนย์รวมเว็บแอปพลิเคชันสำหรับการวิเคราะห์
        <br>
        และแนะนำสถานที่ท่องเที่ยว
    </p>

</div>
"""

st.markdown(dedent(hero_html), unsafe_allow_html=True)


# =========================================================
# APP DATA
# =========================================================

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
    )

]


# =========================================================
# CARDS
# =========================================================

cols = st.columns(3)


for i, (icon, title, desc, url) in enumerate(APPS):

    with cols[i]:

        card_html = f"""
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
"""

        st.markdown(
            dedent(card_html),
            unsafe_allow_html=True
        )


# =========================================================
# FOOTER
# =========================================================

footer_html = """
<div class="footer">

    <span>●</span>

    Made with Streamlit
    ·
    Machine Learning Projects
    ·
    Tourism Recommendation System

</div>
"""

st.markdown(
    dedent(footer_html),
    unsafe_allow_html=True
)