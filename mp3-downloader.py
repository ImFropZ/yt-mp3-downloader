import argparse
import yt_dlp
import os

def download_youtube_playlist(playlist_url, output_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def main():
    parser = argparse.ArgumentParser(description='Download a YouTube playlist as MP3 files.')
    parser.add_argument('playlist_url', help='URL of the YouTube playlist')
    parser.add_argument('--output-dir', '-o', default='.', help='Output directory for downloaded files')
    args = parser.parse_args()

    download_youtube_playlist(args.playlist_url, args.output_dir)

if __name__ == "__main__":
    main()
