## Requirement ffmpeg
To install in powershell - `winget install ffmpeg`

## Setup as Virtual Environment
- Create venv: `python -m venv venv`
- Activate: `. venv/Scripts/activate`
- Install Module: `pip install -r requirements.txt`
- Run python script to download mp3 from youtube: `python mp3-downloader.py <youtube-playlist> --output-dir=<dir-name>`
- Deactivate: `deactivate`
