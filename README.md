# QR Code Generator Bot

Telegram бот, который превращает текст и ссылки в QR-коды.

## Что умеет

- Принимает любой текст → создаёт QR-код
- Принимает ссылку → создаёт QR-код (телефон откроет сайт при сканировании)
- Команда `/start` — приветствие и инструкция

## Как запустить

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/nelastik242/todo-cleaner-bot.git
   cd todo-cleaner-bot
2. Создай виртуальное окружение и активируй его:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate.bat  # Windows

3. Установи зависимости:
    ```bash
    pip install -r requirements.txt

4. Создай файл .env и добавь токен бота:
    BOT_TOKEN=твой_токен_от_BotFather

5. Запусти бота:
    ```bash
    python bot.py

Использование

    Найди бота в Telegram: @твой_бот

    Отправь команду /start

    Отправь любой текст или ссылку

    Получи QR-код в ответ

Хочешь доработать?

Вот идеи, что можно добавить:

    Генерация QR из фото (загрузка на файлообменник)

    QR с Wi-Fi паролем

    QR с визиткой (формат vCard)

Форкай репозиторий и делай что хочешь.
Технологии

    Python 3.11+

    python-telegram-bot

    qrcode

    python-dotenv

Лицензия

MIT — делай что угодно, только указывай автора.
Автор

nelastik242