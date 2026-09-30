import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. PAGE INITIALIZATION (Must be the very first Streamlit command)
st.set_page_config(
    page_title="Plastic Waste Analyzer", 
    page_icon="♻️", 
    layout="wide"
)

# YOUR API KEY FROM THE SCREENSHOT
GOOGLE_API_KEY = "AQ.Ab8RN6LhPZh4YdoNiefDES_FMVS5oTecVxdTS9S_0HzbDzJPXA"

# Authenticate the Google API
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    st.error("Missing Google API key structure configuration.")

# 2. USER INTERFACE GRAPHICS & HEADERS
st.title("♻️ Plastic Waste Analyzer")
st.markdown("### Multimodal Image Recognition & Chemical Upcycling Report Generator")
st.write("Upload an image of a plastic object or manufacturing scrap piece to identify its polymer code and generate a structural recycling data sheet.")

# 3. SPLIT SCREEN LAYOUT
col1, col2 = st.columns(2)

with col1:
    st.subheader("📷 Image Upload Input")
    uploaded_file = st.file_uploader("Choose a plastic sample photo...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Plastic Sample Matrix", use_container_width=True)
        
        additional_notes = st.text_area("Optional Context: (e.g., 'found in an old electronics bin', 'industrial packaging scrap')")
        generate_button = st.button("🚀 Analyze & Generate Material Report", type="primary")

with col2:
    st.subheader("📊 Generated Industrial Recycling Datasheet")
    
    if uploaded_file is None:
        st.info("Awaiting image upload to trigger the Multimodal Generator engine.")
        
    elif uploaded_file is not None and generate_button:
        with st.spinner("Processing image textures and executing polymer generation rules via Google Gemini..."):
            try:
                # Initialize the model structure
                model = genai.GenerativeModel('gemini-3.5-flash')
                
                # THE SYSTEM PROMPT ENCODE
                system_prompt = (
                    "You are an expert Chemical Engineering and Industrial Plastic Recycling Assistant. "
                    "Your task is to analyze the provided image of plastic waste/scrap and generate a strict, highly detailed, "
                    "professional technical datasheet in Markdown format. You must identify or make a logical assumption "
                    "on the primary plastic material profile.\n\n"
                    "Follow this structure exactly:\n"
                    "### 1. POLYMER IDENTIFICATION\n"
                    "- **Estimated Plastic Type:** (e.g., PETE-1, HDPE-2, PVC-3, LDPE-4, PP-5, PS-6, Other-7)\n"
                    "- **Visual Confidence Level:** (Low/Medium/High based on texture/shape)\n"
                    "- **Key Physical Attributes Identified:** (e.g., flexibility, rigidity, transparency level)\n\n"
                    "### 2. THERMAL & CHEMICAL SPECIFICATIONS\n"
                    "- **Precise Melting Temperature Window:** (Give the specific range in Celsius)\n"
                    "- **Chemical Vulnerabilities:** (List what common liquids or chemicals react dangerously with it)\n"
                    "- **Degradation Lifespan:** (Estimated years required to decompose in natural environments)\n\n"
                    "### 3. INDUSTRIAL SAFETY & DISPOSAL RULES\n"
                    "- **Toxic Off-Gassing Hazard:** (What chemicals are released if burned/heated?)\n"
                    "- **Handling Precautions:** (PPE or structural ventilation required when reprocessing)\n\n"
                    "### 4. AUTOMATED UPCYCLING BLUEPRINT PROJECT\n"
                    "- **Project Name:** (A creative, functional 3D printing or mechanical upcycling idea)\n"
                    "- **Step-by-step Transformation Instructions:** (Provide 3 short, punchy steps explaining how a human worker can manually clean, melt, mold, or downcycle this exact item safely into a new commodity.)"
                )
                
                user_message = f"Analyze this image based on the required engineering guidelines. User notes: {additional_notes if additional_notes else 'None provided.'}"
                
                # Execute the API payload call
                response = model.generate_content([system_prompt, user_message, image])
                
                report_content = response.text
                st.success("Report Generation Successful!")
                st.markdown(report_content)
                
                # Create downloadable data file
                st.download_button(
                    label="📥 Download Technical Markdown Data Sheet",
                    data=report_content,
                    file_name="plastic_recycler_report.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                st.error(f"Engine connection anomaly: {str(e)}")