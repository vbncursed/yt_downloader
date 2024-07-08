import os
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

from download_audio import download_audio
from download_video_without_audio import download_video_without_audio
from download import download

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Привет! Я ваш бот для скачивания видео и аудио.")


@app.on_message(filters.command("download_audio"))
def handle_download_audio(client, message: Message):
    url = message.text.split(" ", 1)[1]
    output_path = "audio.mp3"
    download_audio(url, output_path)
    message.reply_document(output_path)
    os.remove(output_path)


@app.on_message(filters.command("download_video"))
def handle_download_video(client, message: Message):
    url = message.text.split(" ", 1)[1]
    output_path = "video.mp4"
    download_video_without_audio(url, output_path)
    message.reply_document(output_path)
    os.remove(output_path)


@app.on_message(filters.command("download"))
def handle_download(client, message: Message):
    url = message.text.split(" ", 1)[1]
    output_path = "downloaded_file.mp4"
    download(url, output_path)
    message.reply_document(output_path)
    os.remove(output_path)


if __name__ == "__main__":
    app.run()
