from pytube import YouTube


def download_video_without_audio(url, output_path):
    yt = YouTube(url)
    video_stream = yt.streams.filter(
        adaptive=True, file_extension="mp4", only_video=True
    ).first()
    video_stream.download(output_path=output_path)
