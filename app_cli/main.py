from pytube import YouTube
from menu import menu


def main() -> None:
    while True:
        try:
            url = input("Enter the URL of the YouTube video (or type 'exit' to quit): ")
            if url.lower() == "exit":
                print("Exiting the program.")
                break
            yt: YouTube = YouTube(url)
            menu(yt)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nThank you for using this programm.")
