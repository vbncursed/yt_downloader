# YouTube Downloader

Этот проект представляет собой приложение для загрузки видео и аудио с YouTube. Он состоит из двух частей: командной строки (`app_cli`) и графического интерфейса (`app_desktop`).

## Установка

1. Клонируйте репозиторий:
```sh
git clone https://github.com/vbncursed/yt_downloader.git
cd yt_downloader
```

2. Установите необходимые зависимости:
```sh
pip install -r requirements.txt
```

## Использование

### Командная строка (CLI)

1. Перейдите в директорию `app_cli`:
```sh
cd app_cli
```

2. Запустите скрипт `main.py`:
```sh
python main.py
```

3. Следуйте инструкциям на экране для загрузки видео или аудио.

### Графический интерфейс (Desktop)

1. Перейдите в директорию `app_desktop`:
```sh
cd app_desktop
```

2. Запустите скрипт `main.py`:
```sh
python main.py
```

3. Введите URL видео и выберите опции для загрузки.

## Функции

### Командная строка (CLI)

- Загрузка видео с аудио
- Загрузка только аудио
- Загрузка видео без аудио

### Графический интерфейс (Desktop)

- Ввод URL видео
- Отображение информации о видео
- Выбор разрешения для загрузки
- Загрузка видео или аудио

## Зависимости

- [pytube](https://pytube.io/)
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Pillow](https://python-pillow.org/)
- [requests](https://docs.python-requests.org/en/latest/)

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности см. в файле `LICENSE`.

## Авторы

- Edaurd - [Ваш GitHub профиль](https://github.com/vbncursed)
