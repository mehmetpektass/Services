# 🎤 Audio Transcription & Segmentation Pipeline

## Description
A professional Python pipeline for transcribing audio files using OpenAI's Whisper API and segmenting them into smaller chunks with precise timestamps. Then creating datasets for speech processing and machine learning applications.

<br>

## Features

### 1. AI Development News Analyzer 📰🔍
* **🎯 Accurate Transcription:** Utilizes OpenAI's Whisper API for high-quality speech-to-text conversion
* **⏱️ Timestamp Preservation:** Maintains precise timing information for each audio segment
* **🔪 Smart Segmentation:** Splits large audio files into manageable chunks with configurable duration
* **📊 Dataset Export:** Generates organized CSV datasets with metadata and file paths
* **⚡ Large File Support:** Automatically handles files exceeding 25MB using chunked processing
* **🔈Audio Optimization:** Converts audio to optimal format for processing (16kHz, mono, 64kbps)

<br>

## Core Technologies
### Frameworks & Libraries
* **Python 3.8+:** Main programming language - rich ecosystem, easy integration, and excellent data processing support.
* **OpenAI Whisper API:** Industry-leading speech recognition accuracy with automatic timestamping and multilingual support.
* **FFmpeg (via Pydub):** Audio processing and format conversion with precise timing control.
* **Pandas:** Dataset management and CSV export for structured metadata organization.
* **Pydub:** Simple audio manipulation API with millisecond precision cutting.
* **Python-dotenv:** Secure API key management and environment separation.
* **Pathlib:** Cross-platform path handling and automatic directory creation.
* **Requests:** Reliable HTTP communication with OpenAI API.
<br>

## Installation & Setup

**Prerequisites**:
- Python 3.8+

- OpenAI API key

- FFmpeg (for audio processing)

```
git clone https://github.com/mehmetpektass/Services.git
cd Creating_Dataset_With_Whisper
```
```
pip install -r requirements.txt
```
<br>

## 🔧 Additional System Requirements:
#### FFmpeg (must be installed separately):

- Windows: Download from https://ffmpeg.org/
- macOS: ``` brew install ffmpeg ```
- Linux: ``` sudo apt-get install ffmpeg ```

<br>

# 📊 Output

## 🎵 Audio Segments
- Individual WAV files for each transcribed segment
- Precisely trimmed based on Whisper timestamps
- Optimized for speech processing (16kHz, mono)

## 📋 Dataset CSV
Comprehensive metadata including:

| Column | Description | Format |
|--------|-------------|---------|
| `id` | Segment identifier | Integer |
| `filename` | Audio file name | String |
| `start` | Start timestamp (seconds) | Float |
| `end` | End timestamp (seconds) | Float |
| `duration` | Segment duration (seconds) | Float |
| `text` | Transcribed content | String |
| `file_path` | Relative path to audio file | String |

## 📄 Sample CSV Data:
| id | filename | start | end | duration | text | file_path |
|----|----------|-------|-----|----------|------|-----------|
| 1 | segment_001.wav | 0.0 | 4.5 | 4.5 | Hello world | ./segment_001.wav |
| 2 | segment_002.wav | 4.5 | 8.2 | 3.7 | How are you? | ./segment_002.wav |
| 3 | segment_003.wav | 8.2 | 12.1 | 3.9 | I'm fine thanks | ./segment_003.wav |

<br>
<br>

## Contribution Guidelines  🚀
 Pull requests are welcome. If you'd like to contribute, please:

* Fork the repository.
* Create a feature branch.
* Submit a pull request with a clear description of changes.

