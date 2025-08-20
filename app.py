import streamlit as st
import os
import re
import asyncio
from dotenv import load_dotenv
from utils import extract_video_id, get_transcript, generate_social_media_post, get_available_models, format_transcript

# Load API Key uncomment to use locally
load_dotenv()
# key = os.getenv("GEMINI_API_KEY")
# st.session_state.gemini_api_key = key
# gemini_api_key = st.session_state.gemini_api_key

#comment this out when using locally
gem_api_key = st.secrets["GEMINI_API_KEY"]
st.session_state.gemini_api_key = gem_api_key
gemini_api_key = st.session_state.gemini_api_key

# Set page config
st.set_page_config(page_title="🎥 Tutorial Generator", page_icon="💡", layout="wide")

# Inject custom CSS
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            background: linear-gradient(90deg, #0072ff, #00c6ff);
            padding: 1.5rem;
            border-radius: 10px;
            color: white;
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 2rem;
        }
        .main-title img {
            height: 50px;
            margin-right: 15px;
        }
        .section-box {
            background-color: #f9f9f9;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            border: 1px solid #ddd;
        }
        .platform-checkbox {
            font-weight: 500;
            font-size: 1.1rem;
        }
        .download-btn button {
            background-color: #0072ff;
            color: white;
            border-radius: 8px;
            padding: 0.4em 1em;
        }
        .copy-btn {
            margin-top: 0.5rem;
            padding: 0.4em 1em;
            border-radius: 6px;
            background-color: #eee;
            border: none;
        }
        .expander-header {
            font-size: 1.2rem;
            font-weight: bold;
        }
             /* Button tweaks */
        .stButton>button {
            background-color: #0072ff !important;  /* your blue */
            color: white !important;
            border: none !important;
            border-radius: 6px !important;
            padding: 0.5em 1em;
        }
        .stButton>button:hover {
            background-color: #005fcc !important; /* darker blue on hover */
            color: white !important;
            border: none !important;
        }
        /* Download button */
        .stDownloadButton>button {
            background-color: #00c6ff !important;
            color: black !important;
            border: none !important;
            border-radius: 8px !important;
            transition: background-color 0.3s ease;
        }

        /* Keep the same color on hover */
        .stDownloadButton>button:hover {
            background-color: #00c6ff !important;
            color: black !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title"><img src="https://img.icons8.com/fluency/96/youtube-play.png" alt="logo"> AI-Powered Tutorial Generator</div>', unsafe_allow_html=True)
st.markdown("Automatically generate blog style tutorials, summaries, or notes from YouTube video with the power of AI ")
# Warning if no API key
if not gemini_api_key:
    st.warning("Please enter a valid Google AI Studio API key to generate content. Get one for free at https://aistudio.google.com.")
    st.stop()

# Model Selection
available_models = get_available_models()
model_name = st.selectbox("Choose a Gemini Model", available_models or ["gemini-2.5-flash"])

# Input Form
st.markdown("### Input Video & Query")
with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        video_id = st.text_input("🎬 YouTube Video ID or URL", placeholder="e.g., OZ5OZZZ2cvk")
        st.caption("Paste the full URL or just the video ID (after `v=` in the link).")
    with col2:
        query = st.text_area("💬 Your Query", placeholder="e.g., Generate a tutorial from this content", height=100)

# Platform Selection
st.markdown("### Output Format")
col1, col2, col3 = st.columns(3)
with col1:
    tutorial_blog = st.checkbox("Generate Tutorial Blog", value=False)
with col2:
    summary_platform = st.checkbox("Generate Summary", value=False)
with col3:
    note_taking = st.checkbox("Generate Notes", value=False)

# Generate Button
generate_clicked = st.button(" Generate Content", type="primary", disabled=not video_id)

# Core function
async def run_agent(video_id, query, platforms, api_key):
    with st.spinner(" Fetching video ..."):
        try:
            transcript = get_transcript(video_id)
            st.success("Video fetched successfully!")
            if not transcript:
                return None, "No video found"
            transcript_text = format_transcript(transcript)
        except Exception as e:
            return None, str(e)

    with st.spinner(f" Generating content using '{model_name}'..."):
        try:
            tasks = [generate_social_media_post(transcript, model_name, platform, api_key, query) for platform in platforms]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            posts = []
            for platform, res in zip(platforms, results):
                if isinstance(res, Exception):
                    content = f"[Error generating for {platform}: {res}]"
                else:
                    content = res
                posts.append({"platform": platform, "content": content})
            return posts, None
        except Exception as e:
            return None, str(e)

# Process on click
if generate_clicked:
    processed_video_id = extract_video_id(video_id) or video_id
    selected_platforms = [] 
    
    if tutorial_blog :
        selected_platforms.append("Tutorial Blog")
    if summary_platform:
        selected_platforms.append("Summary")
    if note_taking:
        selected_platforms.append("Note Taking")

    if not selected_platforms:
        st.error("Please select at least one output format.")
    else:
        result, error = asyncio.run(run_agent(processed_video_id, query, selected_platforms, gemini_api_key))
        if error:
            st.error(f" Error: {error}")
        else:
            for post in result:
                platform = post["platform"]
                content = post["content"]

                final_post = summary = takeaways = blog = notes_content = ""
                try:
                    if platform.lower() == "summary":
                        # summary_match = re.search(r"Summary\s*(.*?)\s*Key Takeaways\s*(.*?)$", content, re.DOTALL)
                        summary_match = re.search(r"Summary\s*:\s*(.*?)\s*Key Takeaways\s*:\s*(.*?)$", content, re.DOTALL | re.IGNORECASE)
                        if summary_match:
                            summary = summary_match.group(1).strip()
                            takeaways = summary_match.group(2).strip()
                        else:
                            summary = content.strip()
                            takeaways = "No key takeaways extracted due to formatting issues."
                    elif platform.lower() == "note taking":
                        # note_match = re.search(r"Notes\s*:\s*(.*)", content, re.DOTALL)
                        notes_match = re.search(r"Summary\s*:?\s*(.*?)\s*Main Notes\s*:?\s*(.*?)$", content, re.DOTALL | re.IGNORECASE)
                        if notes_match:
                            summary = notes_match.group(1).strip().replace("**", "")
                            notes_content = notes_match.group(2).strip().replace("**", "")
                        else:
                            summary = content.strip()
                            notes_content = "No key notes extracted due to formatting issues."
                    else:
                        final_match = re.search(r"Final Post:\s*(.*)", content)
                        summary_match = re.search(r"Summary:\s*(.*)", content)
                        blog_match = re.search(r"Blog:\s*(.*)", content, re.DOTALL)

                        final_post = final_match.group(1).strip() if final_match else ""
                        summary = summary_match.group(1).strip() if summary_match else ""
                        blog = blog_match.group(1).strip() if blog_match else content.strip()
                except:
                    blog = content.strip()
                    summary = blog = ""

                with st.expander(f"📄 {platform} Output", expanded=True):
                    if platform.lower() == "tutorial blog":
                        st.markdown("#### 📝 Blog-style Tutorial")
                        st.markdown(blog, unsafe_allow_html=False)
                        st.download_button("📥 Download Blog Post", data=blog, file_name="tutorial_blog.md", mime="text/markdown", use_container_width=False)
                    elif platform.lower() == "summary":
                        st.markdown("### 📝 Summary")
                        st.markdown(summary, unsafe_allow_html=False)
                        st.markdown("### 🔑 Key Takeaways")
                        st.markdown(takeaways, unsafe_allow_html=False)
                        download_content = f"Summary:\n{summary}\n\nKey Takeaways:\n{takeaways}"
                        st.download_button(label="📥 Download Summary", data=download_content, file_name="content_hub_summary.md", mime="text/markdown")
                    elif platform.lower() == "note taking":
                        st.markdown("### 📝 Notes")
                        st.markdown(summary, unsafe_allow_html=False)
                        st.markdown("###  Main Notes")
                        st.markdown(notes_content, unsafe_allow_html=False)
                        download_content = f"Summary:\n{summary}\n\nMain Notes:\n{notes_content}"
                        st.download_button(label="📥 Download Notes", data=download_content, file_name="notes.md", mime="text/markdown")
                    else:
                        st.text_area("🪧 Final Post", final_post, height=100)
                        if summary:
                            st.markdown("**🧠 Summary**")
                            st.markdown(summary)
                        if blog:
                            st.markdown("**📘 Blog Insight**")
                            st.text_area("Blog", blog, height=200)

                        st.download_button(
                            label=f"📥 Download {platform} Content",
                            data=f"{final_post}\n\n{summary}\n\n{blog}",
                            file_name=f"{platform.lower()}_content.txt",
                            mime="text/plain",
                            use_container_width=True
                        )

# Footer
st.markdown("---")
st.markdown("⚙️ 🔧 Built with ❤️ by **Aniekan Inyang**")