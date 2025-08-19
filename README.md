# 🎥 AI-Powered Tutorial Generator

An intelligent Streamlit application that automatically transforms YouTube videos into high-quality tutorials, summaries, and structured notes using Google's Gemini AI. Perfect for educators, content creators, and learners who want to extract maximum value from video content.

![Tutorial Generator Banner](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge&logo=artificial-intelligence)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google AI](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

## 🌟 Features

### Core Capabilities
- **🎬 YouTube Video Processing**: Extract transcripts from any public YouTube video automatically
- **📝 Tutorial Generation**: Transform video content into comprehensive, step-by-step tutorials with proper Markdown formatting
- **📊 Smart Summarization**: Generate concise summaries with key takeaways for quick understanding
- **📝 Intelligent Note-Taking**: Create structured, organized notes that capture the flow and key insights from videos
- **🤖 AI-Powered**: Leverages Google Gemini 2.5 Flash for intelligent content transformation
- **📱 Modern UI**: Clean, responsive Streamlit interface with custom gradient styling
- **💾 Export Options**: Download generated content as Markdown or text files
- **🔄 Real-time Processing**: Asynchronous content generation with live progress indicators

### Content Types Supported
- **Tutorial Blogs**: Detailed, code-accurate developer tutorials
- **Summaries**: Concise overviews with key takeaways
- **Notes**: Structured, human-like notes with timestamps and insights
- **Social Media Content**: Platform-optimized posts (Twitter, LinkedIn, Facebook, Instagram)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google AI Studio API key (free at [aistudio.google.com](https://aistudio.google.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dgamee/Tutorial-Generator.git
   cd Tutorial-Generator
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   GEMINI_API_KEY_STR=your_gemini_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:8501`

## 🎯 Usage Guide

### Basic Workflow

1. **Input Video Information**
   - Paste a YouTube URL or video ID in the text input
   - Add an optional custom query to guide the AI generation
   - The app supports full URLs, short URLs, and direct video IDs

2. **Select Output Format(s)**
   - ✅ **Generate Tutorial Blog**: Creates detailed, step-by-step tutorials
   - ✅ **Generate Summary**: Produces concise summaries with key takeaways
   - ✅ **Generate Notes**: Creates structured, timestamp-based notes

3. **Generate Content**
   - Click "Generate Content" to start processing
   - Watch real-time progress indicators
   - Content is generated asynchronously for optimal performance

4. **Review and Download**
   - View generated content in expandable sections
   - Download as Markdown files for tutorials/summaries/notes
   - Content is formatted for immediate use in blogs, documentation, or personal notes

### Supported Input Formats

| Format | Example | Description |
|--------|---------|-------------|
| Full YouTube URL | `https://www.youtube.com/watch?v=dQw4w9WgXcQ` | Standard YouTube video URL |
| Short URL | `https://youtu.be/dQw4w9WgXcQ` | YouTube short link format |
| Video ID | `dQw4w9WgXcQ` | Just the 11-character video identifier |

## 🏗️ Project Architecture

```
Tutorial Generator/
├── app.py                # Main Streamlit application
├── utils.py              # Core utility functions
├── prompts.py            # AI prompt engineering templates
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── .gitignore           # Git ignore rules
├── venv/                # Virtual environment (created locally)
└── README.md            # Project documentation
```

### Key Components

#### `app.py` - Main Application
- Streamlit web interface with custom CSS styling
- User input handling and validation
- Asynchronous content generation orchestration
- Content display with expandable sections
- Download functionality for generated content

#### `utils.py` - Core Engine
- **YouTube Integration**: Transcript extraction via `youtube-transcript-api`
- **Gemini AI Integration**: Streaming content generation with error handling
- **Content Processing**: Text formatting and structure optimization
- **Async Operations**: Non-blocking content generation for multiple formats

#### `prompts.py` - AI Prompt Engineering
- **Tutorial Prompts**: Specialized for step-by-step technical content
- **Summary Prompts**: Optimized for concise, high-value summaries
- **Note-Taking Prompts**: Structured for natural, human-like notes
- **Social Media Prompts**: Platform-specific optimization
- **Anti-Hallucination**: Built-in quality assurance and validation

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GEMINI_API_KEY` | Google AI Studio API key | ✅ Yes | None |
| `GEMINI_API_KEY_STR` | Secondary API key (fallback) | ✅ Yes | None |

### Available AI Models

- **`gemini-2.5-flash`** (Default): Fast, efficient processing with high quality
- **`gemini-2.5-flash-lite`**: Lightweight version for basic tasks

### Content Generation Parameters

- **Temperature**: 0.7 (balanced creativity and accuracy)
- **Streaming**: Enabled for real-time response
- **Error Recovery**: Automatic retry with exponential backoff

## 🎨 Advanced Features

### Anti-Hallucination System

The application implements multiple layers of validation:

1. **Step Match Check**: Every tutorial step maps to transcript content
2. **Code Fidelity Check**: All code examples match transcript exactly
3. **No Fabrication Test**: No technical details added beyond transcript
4. **Order Integrity Test**: Sequence matches transcript perfectly
5. **Quality Assurance Loop**: Self-evaluation scoring (1-10) with refinement

### Intelligent Content Processing

- **Transcript Cleaning**: Removes noise, fixes formatting
- **Content Structuring**: Organizes information logically
- **Platform Optimization**: Tailors content for specific use cases
- **Markdown Generation**: Clean, publication-ready formatting

### Real-Time User Experience

- **Progress Indicators**: Live feedback during generation
- **Success Notifications**: Clear status updates
- **Error Handling**: User-friendly error messages
- **Responsive Design**: Works on desktop and mobile

## 🔍 API Reference

### Core Functions

```python
# Extract video ID from various URL formats
extract_video_id(url: str) -> str

# Fetch YouTube transcript
get_transcript(video_id: str, languages: List[str] = None) -> str

# Generate content using Gemini AI
generate_social_media_post(
    video_transcript: str, 
    model_name: str, 
    platform: str, 
    api_key: str, 
    user_query: Optional[str] = None
) -> str

# Core AI generation function
gemini_generate(
    prompt: str, 
    model: str, 
    api_key: str = None, 
    temperature: float = 0.7, 
    session: Optional[aiohttp.ClientSession] = None
) -> str
```

### Supported Platforms

| Platform | Output Type | Characteristics |
|----------|-------------|-----------------|
| Tutorial Blog | Markdown Tutorial | Step-by-step, code-accurate, developer-focused |
| Summary | Structured Summary | Concise overview with key takeaways |
| Note Taking | Organized Notes | Timestamp-based, natural language |
| Twitter/X | Social Post | 280 characters, engaging, with hashtags |
| LinkedIn | Professional Post | Executive tone, no emojis |
| Facebook | Social Content | Conversational, platform-optimized |
| Instagram | Visual Content | Trendy, emoji-enhanced |

## 🚨 Error Handling & Reliability

### Comprehensive Error Management

- **YouTube API Errors**: Graceful handling of unavailable videos or transcripts
- **Gemini API Limits**: Automatic retry with exponential backoff
- **Network Issues**: Connection timeout and retry logic
- **Malformed Content**: Content validation and re-generation
- **User Input Validation**: Real-time input sanitization

### Reliability Features

- **Async Processing**: Non-blocking operations prevent UI freezing
- **Session Management**: Proper cleanup of resources
- **Memory Optimization**: Efficient handling of large transcripts
- **Rate Limiting**: Responsible API usage

## 📊 Performance Metrics

- **Transcript Extraction**: ~2-5 seconds for typical videos
- **Content Generation**: ~10-30 seconds depending on content length
- **Memory Usage**: Optimized for transcripts up to 1M tokens
- **Concurrent Processing**: Supports multiple content types simultaneously

## 🔒 Security & Privacy

### Data Protection
- **API Key Security**: Environment variable storage, never exposed in code
- **Input Sanitization**: All user inputs are validated and cleaned
- **No Data Persistence**: Transcripts and content are not stored permanently
- **Secure Sessions**: Proper session management for API calls

### Privacy Considerations
- Video transcripts are processed temporarily and not stored
- Generated content is only accessible during the session
- No user data is collected or transmitted to third parties

## 🚀 Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Streamlit Cloud Deployment
1. Fork the repository
2. Connect to Streamlit Cloud
3. Add `GEMINI_API_KEY` to Streamlit secrets
4. Deploy automatically

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
   - Follow existing code style
   - Add docstrings for new functions
   - Update tests if applicable

4. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```

5. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**

### Development Guidelines

- **Code Style**: Follow PEP 8 guidelines
- **Documentation**: Add docstrings for all functions
- **Testing**: Test with various YouTube video types
- **Performance**: Ensure async operations remain non-blocking

## 📋 Changelog

### Version 2.0.0 (Current)
- ✨ Added intelligent note-taking functionality
- ✨ Enhanced summary generation with key takeaways
- 🎨 Improved UI with gradient styling and better UX
- 🔧 Enhanced error handling and user feedback
- 📊 Better content parsing and structure
- � Performance improvements for large transcripts

### Version 1.0.0
- 🎉 Initial release
- 📝 Tutorial blog generation
- 🤖 Gemini AI integration
- 🎬 YouTube transcript extraction
- 📱 Streamlit web interface

## 🙏 Acknowledgments

- **Google AI Studio** for providing access to Gemini AI models
- **YouTube Transcript API** for reliable video transcript extraction
- **Streamlit** for the excellent web framework
- **Open Source Community** for inspiration and feedback

## 📞 Support & Contact

- **GitHub Issues**: [Report bugs or request features](https://github.com/dgamee/Tutorial-Generator/issues)
- **Documentation**: This comprehensive README
- **API Documentation**: [Google AI Studio](https://aistudio.google.com)

## � License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**⚙️ 🔧 Built with ❤️ by Aniekan Inyang**

*Transform your video content into structured knowledge with the power of AI!*

> 💡 **Tip**: Star this repository if you find it useful, and don't forget to share it with fellow content creators and educators!
