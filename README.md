# Video_Summarizer_AI-Project
## AI Video Summarizer Agent

An AI-first Streamlit application that uploads any short video clip, sends it through Google's Gemini multimodal API via a `phidata` agent, and returns structured insights (summary, key events, recommendations). The landing page lives in `index.py`, while the agent workflow and UI controls are in `pages/main.py`.

---

### ✨ Features
- Upload `.mp4`, `.mov`, or `.avi` files and preview them inline.
- Ask natural-language questions about the uploaded video.
- Gemini 2.5 Flash + `phidata` agent orchestrate multimodal reasoning.
- DuckDuckGo search tool available for contextual enrichment when the agent needs supporting facts.
- Glassmorphism + animated dark/light themes for a polished UX.

---

### 🧱 Project Structure
```
.
├── index.py                # Landing page with hero + feature cards
├── pages/
│   └── main.py             # Core agent UI + Gemini inference flow
├── requirements.txt        # Python dependencies
├── README.md               # You are here
└── venv/                   # (Optional) Local virtual environment
```

---

### 🔐 Prerequisites
- Python 3.10+
- Google Cloud project with Generative AI access and a `GOOGLE_API_KEY`
- (Optional) Virtual environment (recommended)

---

### ⚙️ Setup
1. **Clone & enter the project**
   ```bash
   git clone <repo-url>
   cd Video_Summarizer_AI-Project
   ```
2. **Create / activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate            # macOS / Linux
   venv\Scripts\activate               # Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables**
   - Copy `.env.example` ➜ `.env` (or create `.env`)
   - Add your Gemini key:
     ```
     GOOGLE_API_KEY=your-secret-key
     ```

---

### ▶️ Run the App
```bash
streamlit run index.py
```
The landing page (`index.py`) includes a “Get Started” button that routes to `pages/main.py`, so run Streamlit from the repo root to keep relative paths working.

---

### 🧭 Usage Flow
1. Launch the app and click **Get Started**.
2. Upload a video file; wait for the preview to render.
3. Describe what you want to know (e.g., “Summarize the key events and action items”).
4. Press **Analyze Video**; the agent uploads the video to Gemini, waits for processing, then streams back the structured analysis.
5. Download / copy the summary from the results card.

---

### 🧰 Tech Stack
- `streamlit` for the multi-page UI
- `phidata` Agent + `Gemini 2.5 Flash` multimodal model
- `google-generativeai` SDK for file uploads and polling
- `duckduckgo-search` as an external knowledge tool
- `python-dotenv` for secrets management

---

### 🛠️ Troubleshooting
- **`GOOGLE_API_KEY missing`**: ensure `.env` is loaded and Streamlit was started from the project root.
- **Processing stuck on “Uploading & analyzing video”**: Gemini may still be transcoding the file. Longer clips can take up to a couple of minutes.
- **`google.api_core.exceptions.PermissionDenied`**: verify that the API key belongs to a project with Generative AI access enabled.

---

