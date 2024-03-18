# Speech to Text Subtitle Generator

This project is designed to convert speech to text and generate subtitles for videos. It users [whisperX](https://github.com/m-bain/whisperX) to convert speech to text.

The inspiration comes from trying to learn Spanish and wanting to watch Spanish TV shows with Spanish subtitles. Subtitles are often incorrect or missing, so I wanted to create a tool to generate them. Using plex to watch TV shows, I wanted to be able to generate subtitles for all my TV shows and movies.

Running this tool it will recursively search for video files in the current directory and generate subtitles for them. It will generate a `.srt` file for each video file. Plex will automatically pick up the subtitles and display them when you play the video. 

_You may need to refresh the metadata for the video in Plex to get it to pick up the subtitles_
_You may need to change the language of the subtitles in Plex to get them to display_

## Installation

* Install [pytorch](https://github.com/m-bain/whisperX?tab=readme-ov-file#2-install-pytorch-eg-for-linux-and-windows-cuda118)
* Install [whisperX](https://github.com/m-bain/whisperX)
* Install [ffmpeg](https://ffmpeg.org/download.html)

### Install with pip

You can install this project using pip. Run the following command in your terminal:

```bash
pip install git+https://github.com/benjefferies/speech-to-text-subtitle-generator.git
```

## Usage
```bash
speech-to-text-subtitle-generator --language es --threads 10
speech-to-text-subtitle-generator --language es --mac --threads 10  # Mac
```

## Options
* `--language` - Language code
* `--threads` - Number of threads (default: 0)
* `--mac` - Use this flag if you are using a Mac
* `--model` - Whisper model to use (default: large-v2)
* `--ext` - Video file extension to process (default: mkv)
