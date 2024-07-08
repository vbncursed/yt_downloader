from resolution import get_available_resolutions
from pytube import YouTube
import subprocess
import os


def download_audio_and_video(yt: YouTube) -> None:
    """
    Download audio and video

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

    # Get video and audio stream
    video = yt.streams.filter(res=res).first()
    audio = yt.streams.filter(only_audio=True).first()

    if video and audio:
        try:
            print("Downloading video...")
            # Download video and audio
            video_file: str = video.download(filename="video.mp4")
            audio_file: str = audio.download(filename="audio.mp4")

            # Merge video and audio
            output_file: str = f"{yt.title}.mp4"
            with open(os.devnull, "w") as devnull:
                subprocess.run(
                    [
                        "ffmpeg",
                        "-y",
                        "-i",
                        video_file,
                        "-i",
                        audio_file,
                        "-c",
                        "copy",
                        output_file,
                    ],
                    stdout=devnull,
                    stderr=devnull,
                )
            print(f"Video and audio merged successfully: {output_file}")

            # Delete temp file
            os.remove(video_file)
            os.remove(audio_file)

            print("Video downloaded successfully!")
        except Exception as e:
            print(f"Error merging video and audio: {e}")
    else:
        print("Video stream not available.")
