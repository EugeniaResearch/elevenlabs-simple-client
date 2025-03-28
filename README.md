
```markdown
# ElevenLabs Simple Client

![Python 3.12.2](https://img.shields.io/badge/python-3.12.2-blue) 
![FFmpeg Required](https://img.shields.io/badge/FFmpeg-required-orange) 
![MIT License](https://img.shields.io/badge/license-MIT-green)

A lightweight Python interface for ElevenLabs Text-to-Speech API.

## Quick Start

```bash
# Clone and setup
git clone https://github.com/your-username/elevenlabs-simple-client.git
cd elevenlabs-simple-client

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Add API key
echo "ELEVENLABS_API_KEY=your_api_key_here" > .env

# Run client
python apitest.py
```

## Requirements
- [Python 3.12.2](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html) (add to system PATH)
- ElevenLabs API key (get one at [elevenlabs.io](https://elevenlabs.io))

## Configuration
Edit the `.env` file:

```ini
# Required
ELEVENLABS_API_KEY=your_api_key_here

# Optional parameters
# VOICE_ID=21m00Tcm4TlvDq8ikWAM
# MODEL_ID=eleven_monolingual_v1
# OUTPUT_FORMAT=mp3_44100_128
```

## Features
- Convert text to natural sounding speech
- Support for multiple voices and languages
- Audio output processing via FFmpeg
- Simple Python interface (<100 LOC)

## Troubleshooting

| Error | Solution |
|-------|----------|
| `FFmpeg not found` | Install FFmpeg and add to PATH |
| `403 Forbidden` | Check your API key in `.env` |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |

## License
MIT License - See [LICENSE](LICENSE) for details.
```

This version includes:
1. Clear visual badges
2. Copy-paste friendly code blocks
3. Minimal dependencies list
4. Straightforward configuration
5. Essential troubleshooting table

Just replace:
- `your-username` with your GitHub username
- `your_api_key_here` with a default key if desired

The formatting will render perfectly on GitHub. Let me know if you'd like to add any additional sections!