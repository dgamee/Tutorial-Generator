# 🎥 AI-Powered Tutorial Generator

An intelligent Streamlit application that automatically converts YouTube videos into high-quality, blog-style tutorials and social media content using Google's Gemini AI.

![Tutorial Generator Banner](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge&logo=artificial-intelligence)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google AI](https://img.shields.io/badge/Google_AI-4285F4?style=for-the-badge&logo=google&logoColor=white)

## 🌟 Features

- **🎬 YouTube Video Processing**: Extract transcripts from any public YouTube video
- **📝 Tutorial Generation**: Convert video content into structured, step-by-step tutorials
- **🎯 Multi-Platform Content**: Generate content optimized for different social media platforms
- **🤖 AI-Powered**: Leverages Google Gemini AI for intelligent content transformation
- **📱 Modern UI**: Clean, responsive Streamlit interface with custom styling
- **💾 Export Options**: Download generated content as Markdown or text files
- **🔄 Real-time Processing**: Asynchronous content generation for improved performance

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google AI Studio API key (free at [aistudio.google.com](https://aistudio.google.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Tutorial Generator"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   GEMINI_API_KEY_STR=your_gemini_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run new_streamlit.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 🎯 Usage

### Basic Tutorial Generation

1. **Enter Video Information**
   - Paste a YouTube URL or video ID
   - Add an optional query to customize the output

2. **Select Output Format**
   - Check "Generate Blog-style Tutorial" for detailed tutorials
   - Choose additional platforms for social media content

3. **Generate Content**
   - Click "Generate Content" to start processing
   - Wait for AI to analyze the video and create content

4. **Download Results**
   - View generated content in expandable sections
   - Download as Markdown (tutorials) or text files

### Supported Input Formats

- **Full YouTube URLs**: `https://www.youtube.com/watch?v=VIDEO_ID`
- **Short URLs**: `https://youtu.be/VIDEO_ID`
- **Video IDs**: Just the 11-character video identifier

## 🛠️ Project Structure

```
Tutorial Generator/
├── new_streamlit.py      # Main Streamlit application
├── utils.py              # Core utility functions
├── prompts.py            # AI prompt templates
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
└── README.md            # Project documentation
```

### Key Components

#### `new_streamlit.py`
- Main application interface
- User input handling
- Content display and download
- Custom CSS styling

#### `utils.py`
- YouTube transcript extraction
- Google Gemini AI integration
- Content generation functions
- Async processing utilities

#### `prompts.py`
- Specialized prompts for different content types
- Social media optimization templates
- Tutorial formatting instructions
- Anti-hallucination guardrails

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google AI Studio API key | Yes |
| `GEMINI_API_KEY_STR` | Secondary API key (fallback) | Yes |

### Available Models

- `gemini-2.5-flash` (Default) - Fast, efficient processing
- `gemini-2.5-flash-lite` - Lightweight version

### Supported Platforms

- **Tutorial Blog** - Detailed, step-by-step tutorials
- **Twitter/X** - Short, engaging posts (280 characters)
- **LinkedIn** - Professional content
- **Facebook** - Social media posts
- **Instagram** - Visual platform content

## 🎨 Features Deep Dive

### AI-Powered Content Generation

The application uses advanced prompt engineering to ensure:
- **Accuracy**: Content stays true to the original video
- **Quality**: Professional, engaging writing style
- **Structure**: Well-organized, easy-to-follow format
- **Platform Optimization**: Content tailored for each platform

### Tutorial Generation Process

1. **Transcript Extraction**: Get accurate video transcripts
2. **Content Analysis**: AI analyzes and structures information
3. **Format Optimization**: Convert to tutorial format
4. **Quality Assurance**: Built-in validation and error checking
5. **Output Generation**: Create downloadable content

### Anti-Hallucination System

- Step-by-step validation
- Code fidelity checks
- Mapping table fallbacks
- Quality assurance loops

## 🔍 API Reference

### Key Functions

#### `extract_video_id(url)`
Extracts YouTube video ID from various URL formats.

#### `get_transcript(video_id, languages)`
Fetches video transcript using YouTube Transcript API.

#### `generate_social_media_post(transcript, model, platform, api_key, query)`
Generates platform-specific content using Gemini AI.

#### `gemini_generate(prompt, model, api_key, temperature, session)`
Core function for AI content generation.

## 🚨 Error Handling

The application includes comprehensive error handling for:
- Invalid YouTube URLs
- Missing transcripts
- API rate limits
- Network connectivity issues
- Malformed content responses

## 📊 Performance

- **Async Processing**: Non-blocking content generation
- **Streaming Responses**: Real-time AI output
- **Efficient Caching**: Minimize redundant API calls
- **Resource Management**: Proper session handling

## 🔒 Security

- **API Key Protection**: Environment variable storage
- **Input Validation**: Sanitized user inputs
- **Error Masking**: Secure error messages
- **Rate Limiting**: Responsible API usage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Run with debug mode
streamlit run new_streamlit.py --server.runOnSave true
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google AI Studio** for Gemini AI access
- **YouTube Transcript API** for video transcript extraction
- **Streamlit** for the amazing web framework
- **Community** for feedback and contributions

## 📞 Support

- **Issues**: [GitHub Issues](../../issues)
- **Documentation**: This README
- **API Documentation**: [Google AI Studio](https://aistudio.google.com)

## 🔄 Changelog

### v1.0.0
- Initial release
- YouTube transcript extraction
- Gemini AI integration
- Tutorial generation
- Multi-platform content creation
- Streamlit web interface

---

**Built with ❤️ by Aniekan Inyang**

*Transform your video content into engaging tutorials with the power of AI!*
