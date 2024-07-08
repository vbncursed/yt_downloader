from pytube import YouTube


def download_audio(url, output_path):
    yt = YouTube(url)

    # Get audio stream
    audio = yt.streams.filter(only_audio=True).first()

    # Download audio
    audio.download(output_path=output_path)

    # Download audio
    try:
        print("Downloading audio...")
        audio.download(output_path=output_path)
        print(f"Audio downloaded successfully: {audio.title}")
    except Exception as e:
        print(f"Error downloading audio: {e}")
