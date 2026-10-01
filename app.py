import streamlit as st

st.set_page_config(
    page_title="Travel Graph Hub",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Orbitron:wght@600;700&display=swap');

/* =========================
   GLOBAL
========================= */

.stApp {
    background:
        radial-gradient(
            circle at 15% 15%,
            rgba(0, 174, 255, 0.12) 0%,
            transparent 35%
        ),
        radial-gradient(
            circle at 85% 75%,
            rgba(0, 102, 255, 0.10) 0%,
            transparent 35%
        ),
        linear-gradient(
            rgba(0, 174, 255, 0.035) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(0, 174, 255, 0.035) 1px,
            transparent 1px
        ),
        #05080d;

    background-size:
        auto,
        auto,
        42px 42px,
        42px 42px;
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
    padding: 42px 10px 25px 10px;
}

.hero h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 3rem;
    letter-spacing: 1px;

    background: linear-gradient(
        90deg,
        #00b7ff,
        #00e5ff,
        #4da6ff
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 0;

    text-shadow:
        0 0 30px rgba(0, 183, 255, 0.20);
}

.hero p {
    color: #8ca3b8;
    letter-spacing: 1px;
    margin-top: 8px;
    font-size: 0.95rem;
}

/* =========================
   CARDS
========================= */

.card {
    background:
        linear-gradient(
            145deg,
            rgba(14, 22, 32, 0.98),
            rgba(7, 12, 18, 0.98)
        );

    border: 1px solid #183449;
    border-radius: 18px;

    padding: 24px;

    height: 250px;

    display: flex;
    flex-direction: column;
    justify-content: space-between;

    transition:
        transform .25s ease,
        border-color .25s ease,
        box-shadow .25s ease;

    margin-bottom: 18px;

    box-shadow:
        0 8px 30px rgba(0, 0, 0, 0.35);
}

.card:hover {
    transform: translateY(-6px);

    border-color: #00b7ff;

    box-shadow:
        0 12px 35px rgba(0, 183, 255, 0.16),
        0 0 25px rgba(0, 183, 255, 0.06);
}

.card .icon {
    font-size: 2.3rem;

    filter:
        drop-shadow(
            0 0 10px rgba(0, 183, 255, 0.35)
        );
}

.card h3 {
    color: #eaf7ff;

    margin:
        10px 0 6px 0;

    font-size: 1.15rem;

    font-weight: 700;
}

.card p {
    color: #8da4b8;

    font-size: 0.86rem;

    line-height: 1.55;

    margin: 0;
}

/* =========================
   BUTTON
========================= */

.btn {
    display: block;

    text-align: center;

    text-decoration: none !important;

    padding: 11px;

    border-radius: 10px;

    font-weight: 600;

    color: #ffffff !important;

    background:
        linear-gradient(
            90deg,
            #0077ff,
            #00b7ff
        );

    transition:
        all .2s ease;

    box-shadow:
        0 5px 18px rgba(0, 140, 255, 0.25);
}

.btn:hover {
    transform: translateY(-1px);

    background:
        linear-gradient(
            90deg,
            #0095ff,
            #00d5ff
        );

    box-shadow:
        0 7px 24px rgba(0, 183, 255, 0.38);
}

/* =========================
   SIDEBAR
========================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #070b11,
            #05080d
        );

    border-right: 1px solid #183449;
}

[data-testid="stSidebarNav"] {
    padding-top: 6px;
}

[data-testid="stSidebarNav"]::before {
    content: "TRAVEL GRAPH HUB";

    display: block;

    margin:
        14px 16px 12px 16px;

    padding-bottom: 12px;

    border-bottom:
        1px solid #183449;

    font-family: 'Orbitron', sans-serif;

    font-size: 0.78rem;

    letter-spacing: 1.5px;

    background:
        linear-gradient(
            90deg,
            #00aaff,
            #00e5ff
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

[data-testid="stSidebarNav"] a {
    margin: 2px 10px;

    padding:
        10px 14px !important;

    border-radius: 10px;

    color: #8499aa !important;

    font-family: 'Prompt', sans-serif;

    font-weight: 500;

    transition:
        all .2s ease;
}

[data-testid="stSidebarNav"] a:hover {
    background:
        rgba(0, 174, 255, 0.08);

    color: #00c8ff !important;
}

[data-testid="stSidebarNav"]
a[aria-current="page"] {
    background:
        linear-gradient(
            90deg,
            rgba(0, 140, 255, 0.14),
            rgba(0, 200, 255, 0.05)
        );

    color: #00c8ff !important;

    box-shadow:
        inset 3px 0 0 #00b7ff;
}

/* =========================
   STREAMLIT UI
========================= */

div[data-testid="stVerticalBlock"] {
    gap: 0.5rem;
}

.stButton > button {
    border: 1px solid #16435c;

    background: #0b1118;

    color: #b9d8e8;

    border-radius: 10px;
}

.stButton > button:hover {
    border-color: #00b7ff;

    color: #00c8ff;

    background: #0d1720;
}

/* =========================
   FOOTER / MENU
========================= */

footer,
#MainMenu {
    visibility: hidden;
}

[data-testid="stSidebarCollapsedControl"] {
    visibility: visible !important;
}

/* =========================
   RESPONSIVE
========================= */

@media (max-width: 768px) {

    .hero {
        padding-top: 25px;
    }

    .hero h1 {
        font-size: 2rem;
    }

    .card {
        height: auto;
        min-height: 220px;
    }
}
</style>

<div class="hero">
    <h1>แนะนำสถานที่ท่องเที่ยว</h1>
    <p>
        ศูนย์รวมเว็บแอปพลิเคชันสำหรับข้อมูล
        วิเคราะห์ และแนะนำสถานที่ท่องเที่ยว
    </p>
</div>
""", unsafe_allow_html=True)


st.write("")


# =========================
# APPLICATIONS
# =========================

APPS = [
    (
        "🌐",
        "โครงสร้างข้อมูลท่องเที่ยว",
        "นำเสนอข้อมูลและโครงสร้างความสัมพันธ์ของผู้ใช้ เพื่อน และสถานที่ท่องเที่ยว",
        "https://colab.research.google.com/drive/1ZmBJEQh-4eOANw2rbN9O-rx08Qo6DiSQ?usp=sharing",
    ),

    (
        "📊",
        "วิเคราะห์ข้อมูลท่องเที่ยว",
        "วิเคราะห์ข้อมูลและความสัมพันธ์ของสถานที่ท่องเที่ยวผ่านข้อมูลที่จัดเก็บไว้",
        "https://colab.research.google.com/drive/12YK3jnjWNXlemkG97EKQmmonLxFx8Cmi?usp=sharing",
    ),

    (
        "✦",
        "ระบบแนะนำสถานที่ท่องเที่ยว",
        "แนะนำสถานที่ท่องเที่ยวจากข้อมูลและความสัมพันธ์ของผู้ใช้งาน",
        "https://mzvpqrmpmmrw4htsbjr7tt.streamlit.app/",
    ),
]


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
            unsafe_allow_html=True,
        )


# =========================
# FOOTER
# =========================

st.markdown(
    """
    <p style="
        text-align:center;
        color:#52697a;
        margin-top:30px;
        font-size:0.8rem;
        letter-spacing:0.5px;
    ">
        Made with Streamlit · Travel Graph Projects
    </p>
    """,
    unsafe_allow_html=True,
)