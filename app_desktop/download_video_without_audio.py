from resolution import get_available_resolutions
from pytube import YouTube


def download_video_without_audio(yt: YouTube) -> None:
    """
    Download video without audio

    @Param:
        - yt: YouTube

    Get:
        - resolution

    Return:
        -
    """

    # Get available resolutions
    available_resolutions: list[str] = get_available_resolutions(yt)

    if not available_resolutions:
        print("No video streams available.")
        return

    # Display available resolutions
    print("Choose the resolution of the video you want to download:")
    for idx, res in enumerate(available_resolutions, start=1):
        print(f"{idx}. {res}")

    choice: str = input("Enter your choice: ")

    try:
        res: str = available_resolutions[int(choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice")
        return

    # Get video stream
    video = yt.streams.filter(res=res).first()

    # Download video
    try:
        print("Downloading video without audio...")
        video.download(filename=f"{yt.title}.mp4")
        print(f"Video downloaded successfully: {video.title}")
    except Exception as e:
        print(f"Error downloading video: {e}")
