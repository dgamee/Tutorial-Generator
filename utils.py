import re
from youtube_transcript_api import YouTubeTranscriptApi
from typing import List, Optional
import asyncio
import google.generativeai as genai
import os
from dotenv import load_dotenv
import aiohttp
import streamlit as st
from prompts import build_social_media_prompt, build_tutorial_prompt, build_merged_summary_prompt



# === Environment Variables ===
load_dotenv()

key = os.getenv("GEMINI_API_KEY")
st.session_state.gemini_api_key = key
my_api_key = os.getenv("GEMINI_API_KEY_STR")

TEMPERATURE = 0.7  # Default temperature for Gemini API
VALID_PLATFORMS = ["Twitter", "Facebook", "Instagram", "LinkedIn", "Tutorial Blog"]

def extract_video_id(url):
    """Extract YouTube video ID from full link or short link."""
    regex = r"(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, url)
    return match.group(1) if match else None

# === Fetch YouTube transcript (patched for .to_raw_data()) ===
def get_transcript(video_id: str, languages: List[str] = None) -> str:
    if languages is None:
        languages = ["en"]
    try:
        youtube_api = YouTubeTranscriptApi()
        fetched_transcript = youtube_api.fetch(video_id, languages=languages).to_raw_data()
        transcript_text = " ".join([snippet['text'] for snippet in fetched_transcript])
        return transcript_text
    except Exception as e:
        print(f"[Transcript] Error fetching transcript for {video_id}: {e}")
        return ""

def format_transcript(transcript: str) -> str:
    """Format the transcript text for better readability."""
    # Remove extra spaces and newlines
    formatted = re.sub(r'\s+', ' ', transcript).strip()
    return formatted

def preview_prompt(transcript: str, platform: str, user_query: Optional[str] = None) -> str:
    """Returns the exact prompt that would be sent to Ollama for preview/debug purposes."""
    if platform.lower() == "tutorial blog":
        return build_tutorial_prompt(transcript, platform, user_query)
    return build_social_media_prompt(transcript, platform, user_query)


def get_available_models():
    """Fetch available Gemini models (hardcoded as Gemini doesn't have a dynamic list endpoint like Ollama)."""
    return ["gemini-2.5-flash", "gemini-2.5-flash-lite"]

    

async def gemini_generate(prompt: str, model: str, api_key: str = my_api_key, temperature: float = TEMPERATURE, session: Optional[aiohttp.ClientSession] = None) -> str:
    genai.configure(api_key=api_key)
    gemini_model = genai.GenerativeModel(
        model_name=model,
        generation_config=genai.types.GenerationConfig(
            temperature=temperature,
            # max_output_tokens=MAX_TOKENS,  # Optional, adjust if needed
        )
    )
    full_text = ""
    try:
        response = gemini_model.generate_content(prompt, stream=True)
        for chunk in response:
            if chunk.text:
                full_text += chunk.text
    except Exception as e:
        raise RuntimeError(f"Gemini API error: {str(e)}")

    return full_text.strip()

async def generate_social_media_post(video_transcript: str, model_name: str, social_media_platform: str, api_key: str, user_query: Optional[str] = None) -> str:
    if not video_transcript or not video_transcript.strip():
        raise ValueError("Missing or empty video transcript")
    if social_media_platform.lower() == "tutorial blog":
        prompt = build_tutorial_prompt(video_transcript, social_media_platform, user_query)
    elif social_media_platform.lower() == "summary":
        prompt = build_merged_summary_prompt(video_transcript, social_media_platform, user_query)
    else:
        prompt = build_social_media_prompt(video_transcript, social_media_platform, user_query)

    async with aiohttp.ClientSession() as session:
        result_text = await gemini_generate(prompt=prompt, model=model_name, api_key=api_key, session=session)
    return result_text.strip()

async def generate_posts_for_all_platforms(video_transcript: str, model_name: str, platforms: list[str], api_key: str) -> dict:
    tasks = [
        generate_social_media_post(video_transcript, model_name, platform, api_key)
        for platform in platforms if platform in VALID_PLATFORMS
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    output = {}
    for platform, result in zip(platforms, results):
        if isinstance(result, Exception):
            output[platform] = f"[Error generating content: {result}]"
        else:
            output[platform] = result
    return output