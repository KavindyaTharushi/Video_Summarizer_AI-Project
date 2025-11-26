import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai
import time
import os
from pathlib import Path
import tempfile
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure API Key
if API_KEY:
    os.environ["GOOGLE_API_KEY"] = API_KEY
    genai.configure(api_key=API_KEY)
else:
    st.error("⚠️ GOOGLE_API_KEY missing in .env")

# -------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Video Summarizer Agent",
    layout="wide",
    page_icon="🎬"
)

# -------------- CUSTOM CSS ----------------
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #fffaf0, #e0f7fa, #ffffff);
}

h1, h2, h3, label {
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    padding-top: 2rem;
}

.glass-card {
    background: rgba(255,255,255,0.15);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.3);
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
}

.stTextArea textarea {
    height: 130px !important;
    background: rgba(255,255,255,0.08);
    color: black !important;
}

.stFileUploader label {
    color: #e5e5e5 !important;
}

button[kind="primary"] {
    background: linear-gradient(135deg, #7f00ff, #e100ff);
    color: white;
    padding: 0.8rem 1rem;
    border-radius: 12px;
}

.success-box {
    background: rgba(255,255,255,0.12);
    padding: 20px;
    border-radius: 15px;
}

.video-container video {
    border-radius: 18px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
}

</style>
""", unsafe_allow_html=True)


# -------------- HEADER ----------------
st.markdown("""
<h1 style='text-align:center; color:black;'>
🎬 Video Summarizer Agent
</h1>
<p style='text-align:center; color:#dcdcdc; font-size:18px;'>
Powered by Google's Gemini + Agentic Intelligence
</p>
""", unsafe_allow_html=True)

# -------------- AGENT INITIALIZATION ----------------
def init_agent():
    return Agent(
        name="Video Summarizer Agent",
        model=Gemini(id="gemini-2.5-flash"),
        tools=[DuckDuckGo()],
        markdown=True
    )

agent = init_agent()

# -------------- UI LAYOUT ----------------
left, right = st.columns([1,1])

with left:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    st.subheader("📤 Upload Video")

    video_file = st.file_uploader(
        "Choose a video file",
        type=['mp4', 'mov', 'avi']
    )

    if video_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
            tmp.write(video_file.read())
            video_path = tmp.name

        st.video(video_path)

    st.markdown("</div>", unsafe_allow_html=True)


with right:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    st.subheader("💬 Ask Your Question")

    query = st.text_area(
        "Describe what insights you want",
        placeholder="Example: Provide a detailed summary of the events in the video..."
    )

    analyze_btn = st.button("✨ Analyze Video", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------- ANALYSIS ----------------
if analyze_btn:
    if not video_file:
        st.warning("⚠️ Please upload a video first.")
    elif not query.strip():
        st.warning("⚠️ Please enter a question or query for the analysis.")
    else:
        try:
            with st.spinner("⏳ Uploading & analyzing video… Please wait..."):

                processed = upload_file(video_path)
                while processed.state.name == "PROCESSING":
                    time.sleep(1)
                    processed = get_file(processed.name)

                prompt = f"""
                Analyze the uploaded video using multimodal reasoning.
                Then answer the following user query:

                {query}

                Provide:  
                ✓ Summary  
                ✓ Key events  
                ✓ Important insights  
                ✓ Any recommendations if applicable  
                """

                response = agent.run(prompt, videos=[processed])

            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.subheader("📊 Analysis Result")
            st.markdown(response.content)
            st.markdown("</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error: {e}")

        finally:
            Path(video_path).unlink(missing_ok=True)

else:
    st.info("👆 Upload a video and enter a question to begin.")
