from pytube import YouTube
import customtkinter
from PIL import Image
import requests
from io import BytesIO
from resolution import get_available_resolutions


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("650x400")  # Увеличим высоту окна
        self.title("Youtube Downloader")

        # Create a transparent frame
        self.frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame.pack(padx=20, pady=20)

        # Add label, entry, button to the frame
        self.label = customtkinter.CTkLabel(self.frame, text="Link on video:")
        self.label.pack(side="left", padx=5)

        self.entry = customtkinter.CTkEntry(self.frame, placeholder_text="URL")
        self.entry.pack(side="left", padx=5)

        self.button = customtkinter.CTkButton(
            self.frame, text="Search", command=self.search_video
        )
        self.button.pack(side="left", padx=5)

        # Add a frame for displaying video information
        self.info_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.info_frame.pack(padx=20, pady=10, fill="both", expand=False)

        self.thumbnail_label = customtkinter.CTkLabel(self.info_frame, text="")
        self.thumbnail_label.pack(side="left", padx=5)

        self.video_info_label = customtkinter.CTkLabel(self.info_frame, text="")
        self.video_info_label.pack(side="left", padx=5)

        # Add a frame for radio buttons and download button
        self.radio_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.radio_frame.pack(padx=20, pady=10, fill="both", expand=False)

        # Add radio buttons for download options
        self.download_option = customtkinter.StringVar(value="Video")
        self.radio_video = customtkinter.CTkRadioButton(
            self.radio_frame,
            text="Video",
            variable=self.download_option,
            value="Video",
            command=self.update_resolution_options,
        )
        self.radio_audio = customtkinter.CTkRadioButton(
            self.radio_frame,
            text="Audio",
            variable=self.download_option,
            value="Audio",
            command=self.update_resolution_options,
        )
        self.radio_video_no_audio = customtkinter.CTkRadioButton(
            self.radio_frame,
            text="Video without audio",
            variable=self.download_option,
            value="Video without audio",
            command=self.update_resolution_options,
        )

        # Add a dropdown for resolution options
        self.resolution_var = customtkinter.StringVar(value="Select resolution")
        self.resolution_dropdown = customtkinter.CTkOptionMenu(
            self.radio_frame, variable=self.resolution_var, values=[]
        )

        # Add download button
        self.download_button = customtkinter.CTkButton(
            self.radio_frame, text="Download", command=self.download_video
        )

    def search_video(self):
        url = self.entry.get()
        try:
            yt = YouTube(url)
            video_info = f"{yt.title}"
            thumbnail_url = yt.thumbnail_url

            response = requests.get(thumbnail_url)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((160, 90), Image.LANCZOS)  # Прямоугольный размер
            photo = customtkinter.CTkImage(
                light_image=img, dark_image=img, size=(160, 90)
            )

            self.thumbnail_label.configure(image=photo)
            self.thumbnail_label.image = (
                photo  # Keep a reference to avoid garbage collection
            )

            self.video_info_label.configure(text=video_info)

            # Display radio buttons and download button after video is found
            self.radio_video.pack(side="top", padx=5, pady=5)
            self.radio_audio.pack(side="top", padx=5, pady=5)
            self.radio_video_no_audio.pack(side="top", padx=5, pady=5)

            # Get available resolutions
            self.available_resolutions = get_available_resolutions(yt)
            self.resolution_dropdown.configure(values=self.available_resolutions)
            self.resolution_dropdown.pack(side="top", padx=5, pady=5)

            self.download_button.pack(side="top", padx=5, pady=5)

        except Exception as e:
            self.video_info_label.configure(text=f"Ошибка: {str(e)}")
        finally:
            self.update_idletasks()  # Обновляем интерфейс

    def update_resolution_options(self):
        if self.download_option.get() in ["Video", "Video without audio"]:
            self.resolution_dropdown.pack(side="top", padx=5, pady=5)
        else:
            self.resolution_dropdown.pack_forget()

    def download_video(self):
        # Implement download functionality here
        pass


if __name__ == "__main__":
    customtkinter.set_default_color_theme("dark-blue")
    app = App()
    app.mainloop()
