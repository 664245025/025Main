```python
import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="ML Hub",
    page_icon="🏝️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;500;700&family=Orbitron:wght@700&display=swap');

/* =========================================================
   MAIN APP
   ========================================================= */

.stApp {
    background: #05070f;
    background-image:
        radial-gradient(
            circle at 20% 20%,
            rgba(0,160,255,0.14) 0%,
            transparent 40%
        ),
        radial-gradient(
            circle at 80% 70%,
            rgba(0,90,200,0.18) 0%,
            transparent 40%
        ),
        linear-gradient(
            rgba(0,160,255,0.05) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(0,160,255,0.05) 1px,
            transparent 1px
        );

    background-size:
        auto,
        auto,
        40px 40px,
        40px 40px;

    color: #e6f1ff;
}

/* Streamlit Header */
[data-testid="stHeader"] {
    background: transparent;
}

/* Font */
html,
body,
[class*="css"] {
    font-family: 'Prompt', sans-serif;
}

/* =========================================================
   HERO SECTION
   ========================================================= */

.hero {
    text-align: center;
    padding: 30px 10px 10px 10px;
}

.hero h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 3rem;

    background:
        linear-gradient(
            90deg,
            #00b4ff,
            #38d0ff,
            #7fe3ff
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 0;
}

.hero p {
    color: #8fa8c8;
    letter-spacing: 1px;
    margin-top: 6px;
}

/* =========================================================
   CARDS
   ========================================================= */

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

    box-shadow:
        0 4px 15px rgba(0, 120, 255, 0.10);
}

/* Card Hover */

.card:hover {
    transform: translateY(-6px);

    border-color: #00b4ff;

    box-shadow:
        0 8px 25px rgba(0, 180, 255, 0.30);
}

/* Icon */

.card .icon {
    font-size: 2.2rem;
}

/* Card Title */

.card h3 {
    color: #e6f1ff;

    margin:
        8px
        0
        4px
        0;

    font-size: 1.15rem;

    font-weight: 700;
}

/* Card Description */

.card p {
    color: #8fa8c8;

    font-size: 0.85rem;

    line-height: 1.4;
}

/* =========================================================
   BUTTON
   ========================================================= */

.btn {
    display: block;

    text-align: center;

    text-decoration: none !important;

    padding: 10px;

    border-radius: 10px;

    font-weight: 600;

    color: #ffffff !important;

    background:
        linear-gradient(
            90deg,
            #0066ff,
            #00b4ff
        );

    transition: all .2s;

    box-shadow:
        0 4px 12px rgba(0, 140, 255, 0.35);
}

/* Button Hover */

.btn:hover {
    filter: brightness(1.1);

    box-shadow:
        0 6px 18px rgba(0, 180, 255, 0.5);
}

/* =========================================================
   HIDE DEFAULT ELEMENTS
   ========================================================= */

footer,
#MainMenu {
    visibility: hidden;
}

/* =========================================================
   SIDEBAR
   ========================================================= */

[data-testid="stSidebar"],
[data-testid="stSidebarCollapsedControl"] {
    visibility: visible !important;
}

[data-testid="stSidebar"] {
    background: #070c18;

    border-right:
        1px solid #1b3a63;
}

[data-testid="stSidebarNav"] {
    padding-top: 6px;
}

/* Sidebar Header */

[data-testid="stSidebarNav"]::before {
    content: "MACHINE LEARNING HUB";

    display: block;

    margin:
        14px
        16px
        12px
        16px;

    padding-bottom: 12px;

    border-bottom:
        1px solid #1b3a63;

    font-family: 'Orbitron', sans-serif;

    font-size: 0.78rem;

    letter-spacing: 1.5px;

    background:
        linear-gradient(
            90deg,
            #00b4ff,
            #38d0ff,
            #7fe3ff
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Sidebar Menu */

[data-testid="stSidebarNav"] a {
    margin: 2px 10px;

    padding:
        10px 14px !important;

    border-radius: 10px;

    color: #8fa8c8 !important;

    font-family: 'Prompt', sans-serif;

    font-weight: 500;

    transition: all .2s ease;
}

/* Sidebar Hover */

[data-testid="stSidebarNav"] a:hover {
    background: #0f1d36;

    color: #38d0ff !important;
}

/* Active Page */

[data-testid="stSidebarNav"]
a[aria-current="page"] {

    background:
        linear-gradient(
            90deg,
            #0a1a33,
            #0f2548
        );

    color: #38d0ff !important;

    box-shadow:
        inset 3px 0 0 #00b4ff;
}

/* =========================================================
   CHANGE SIDEBAR MENU TEXT
   ========================================================= */

/* app -> หน้าหลัก */

[data-testid="stSidebarNav"]
li:nth-child(1) a * {
    font-size: 0 !important;
}

[data-testid="stSidebarNav"]
li:nth-child(1) a::after {
    content: "หน้าหลัก";

    font-size: 1rem !important;
}

/* about -> ผู้พัฒนา */

[data-testid="stSidebarNav"]
li:nth-child(2) a * {
    font-size: 0 !important;
}

[data-testid="stSidebarNav"]
li:nth-child(2) a::after {
    content: "ผู้พัฒนา";

    font-size: 1rem !important;
}

/* =========================================================
   RESPONSIVE
   ========================================================= */

/* Tablet */

@media (max-width: 1100px) {

    .hero h1 {
        font-size: 2.5rem;
    }

}

/* Mobile */

@media (max-width: 700px) {

    .hero {
        padding-top: 20px;
    }

    .hero h1 {
        font-size: 2rem;
    }

    .hero p {
        font-size: 0.9rem;
    }

}

</style>

<!-- =====================================================
     HERO
     ===================================================== -->

<div class="hero">

    <h1>
        แนะนำสถานที่ท่องเที่ยว
    </h1>

    <p>
        ศูนย์รวมเว็บแอปพลิเคชัน สถานที่ท่องเที่ยว
    </p>

</div>

""", unsafe_allow_html=True)


# =========================================================
# SPACE
# =========================================================

st.write("")


# =========================================================
# APPLICATION LIST
# =========================================================

APPS = [

    (
        "🏝️",
        "โครงสร้างข้อมูลที่ท่องเที่ยว",
        "นำเสนอข้อมูลและโครงสร้างของสถานที่ท่องเที่ยว",
        "https://colab.research.google.com/drive/1ZmBJEQh-4eOANw2rbN9O-rx08Qo6DiSQ?usp=sharing"
    ),

    (
        "⛰️",
        "วิเคราะห์ข้อมูลท่องเที่ยว",
        "วิเคราะห์ข้อมูลและความสัมพันธ์ของสถานที่ท่องเที่ยว",
        "https://colab.research.google.com/drive/12YK3jnjWNXlemkG97EKQmmonLxFx8Cmi?usp=sharing"
    ),

    (
        "🛕",
        "ระบบแนะนำสถานที่ท่องเที่ยว",
        "แนะนำสถานที่ท่องเที่ยวจากข้อมูล",
        "https://mzvpqrmpmmrw4htsbjr7tt.streamlit.app/"
    ),

    (
        "🎨",
        "Canva นำเสนอโปรเจกต์",
        "นำเสนอรายละเอียดและข้อมูลของโครงงาน",
        "https://canva.link/6sdssxnz2wcjzi4"
    ),

]


# =========================================================
# DISPLAY CARDS
# =========================================================

cols = st.columns(4)

for i, (icon, title, desc, url) in enumerate(APPS):

    with cols[i % 4]:

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


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <p
        style="
            text-align:center;
            color:#8fa8c8;
            margin-top:30px;
            margin-bottom:10px;
        "
    >
        Made with Streamlit · Recommend_Projects
    </p>
    """,
    unsafe_allow_html=True
)
```
