# Plastic Waste Analyzer ♻️

An AI-powered web application developed for the **Edunet IBM SkillsBuild Capstone Project**. This system utilizes **Streamlit** and the **Google Gemini Multimodal API** to automatically analyze images of waste items, categorize them into proper material types, and instantly guide users on eco-friendly recycling paths.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPOSITORY_NAME
   ```

2. **Install required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key:**
   * Duplicate the `.env.example` file and rename the new copy to `.env`.
   * Open the `.env` file and replace `your_actual_api_key_here` with your real Google Gemini API Key.

4. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```