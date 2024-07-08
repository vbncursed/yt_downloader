from pytube import YouTube


def download_audio(yt: YouTube) -> None:
    """
    Download audio

    @Param:
        - yt: YouTube

    Return:
        -
    """
    # Get audio stream
    audio = yt.streams.filter(only_audio=True).first()

    # Download audio
    try:
        print("Downloading audio...")
        audio.download(filename=f"{yt.title}.mp3")
        print(f"Audio downloaded successfully: {audio.title}")
    except Exception as e:
        print(f"Error downloading audio: {e}")
