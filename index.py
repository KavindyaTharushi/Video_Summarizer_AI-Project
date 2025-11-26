import streamlit as st

st.set_page_config(
    page_title="AI Video Summarizer",
    page_icon="🎬",
    layout="wide"
)

# -------------------------------- DARK MODE CSS --------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

/* DARK BACKGROUND ANIMATED */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0d0d0d, #1a1a1a, #0f0f33);
    background-size: 300% 300%;
    animation: gradientShift 12s ease infinite;
}

@keyframes gradientShift {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* HERO CARD */
.hero {
    margin-top: 120px;
    text-align: center;
    padding: 60px;
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(14px);
    border-radius: 25px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.55);
    animation: float 4s ease-in-out infinite;
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-14px);}
    100% {transform: translateY(0px);}
}

.hero h1 {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 12px;
    background: linear-gradient(135deg, #8a2be2, #ff00ff, #00eaff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 1.2rem;
    color: #e0e0e0;
}

/* GLOW BUTTON */
.start-btn {
    display: inline-block;
    margin-top: 30px;
    padding: 16px 40px;
    border-radius: 50px;
    font-size: 1.25rem;
    font-weight: 600;
    color: white !important;
    background: linear-gradient(135deg, #8a2be2, #ff00ff);
    box-shadow: 0 0 18px #8a2be2, 0 0 28px #ff00ff;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: none;
}

.start-btn:hover {
    transform: scale(1.08);
    box-shadow: 0 0 25px #ff00ff, 0 0 35px #8a2be2;
}

/* FEATURES */
.feature-card {
    background: rgba(255,255,255,0.06);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 0 25px rgba(255,255,255,0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    text-align: center;
}

.feature-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 0 35px rgba(255,255,255,0.12);
}

.feature-card h4 {
    color: white;
}

.feature-card p {
    color: #cfcfcf;
}

.feature-icon {
    font-size: 50px;
    color: #a64aff;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------- HERO SECTION -----------------------------
st.markdown("""
<div class="hero">
    <h1>🎬 AI Video Summarizer</h1>
    <p>Turn long videos into smart summaries, insights, and highlights using advanced Agentic AI.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------- BUTTON -----------------------------
center = st.columns([1,1,1])
with center[1]:
    start = st.button("🚀 Get Started", key="start-btn")

if start:
    st.switch_page("pages/main.py")

# ----------------------------- FEATURES SECTION -----------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("✨ Features", divider="rainbow")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📤</div>
        <h4>Upload Any Video</h4>
        <p>MP4, AVI, MOV — process any format instantly.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <h4>Intelligent Summaries</h4>
        <p>Get structured summaries, highlights, events & insights.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <h4>Powered by AI</h4>
        <p>Runs on Google's Gemini + agentic reasoning.</p>
    </div>
    """, unsafe_allow_html=True)
