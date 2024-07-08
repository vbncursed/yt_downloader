from pytube import YouTube


def get_available_resolutions(yt: YouTube) -> list[str]:
    """
    Get available resolutions

    @Param:
        - yt: YouTube

    Return:
        - list
    """
    # Remove the file extension filter to get all available streams
    video_streams = yt.streams.filter(type="video")
    resolutions: set[str] = set()

    for stream in video_streams:
        if stream.resolution:
            resolutions.add(stream.resolution)

    return sorted(
        resolutions, key=lambda x: int("".join(filter(str.isdigit, x))), reverse=True
    )  # Sorting by the numerical value of the resolution
