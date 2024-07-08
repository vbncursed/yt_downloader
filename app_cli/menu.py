from download_video_without_audio import download_video_without_audio
from download import download_audio_and_video
from download_audio import download_audio
from pytube import YouTube


def menu(yt: YouTube) -> None:
    print(
        "\n1. Download video\n"
        "2. Download audio\n"
        "3. Download video without audio\n"
    )

    choice: str = input("Enter your choice: ")
    match choice:
        case "1":
            download_audio_and_video(yt)
        case "2":
            download_audio(yt)
        case "3":
            download_video_without_audio(yt)
        case _:
            print("Invalid choice")
