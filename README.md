
# 🤖 Discord-SelfBot

A simple Python script that sends scheduled messages to one or more Discord channels using a **user token**.

> ⚠️ **Disclaimer**: This script uses a **Discord user token**, which goes against Discord's Terms of Service. Using it may result in your account being **rate-limited or banned**. This project is for **educational purposes only**.

---

## 📦 Features

- Send custom messages to any channel via the Discord API
- Automatic retries on rate-limiting (`HTTP 429`)
- Optional console logging
- Easily customizable delay between sends

---

## 🖥️ Requirements

- Python 3.6 or higher
- [`requests`](https://pypi.org/project/requests/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) *(optional, for token management)*

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/discord-selfbot.git
cd discord-selfbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install requests python-dotenv
```

---

## ⚙️ Configuration

Open the Python script (e.g. `main.py`) and edit the configuration section:

```python
TOKEN = "YOUR_DISCORD_TOKEN"
CHANNELS = {
    "CHANNEL_ID_1": "Your message here",
    "CHANNEL_ID_2": "Another message"
}
SEND_INTERVAL = 1800  # Delay between loops (in seconds)
```

> 🧠 Replace `YOUR_DISCORD_TOKEN` with your **user token**, and each `CHANNEL_ID` with the **Discord channel ID** you want to send messages to.

---

## 🚀 Usage

Simply run:

```bash
python3 main.py
```

The script will send the configured messages to each channel in a loop, with a delay of `SEND_INTERVAL` seconds between each full cycle.

---

## 🛑 Stopping the Script

To stop the script safely, press:

```bash
CTRL + C
```

---

## 🔐 Token Security (Recommended)

To avoid exposing your token:
1. Install `python-dotenv`
2. Create a `.env` file in the project folder:
    ```
    DISCORD_TOKEN=your_token_here
    ```
3. In your script, replace:
    ```python
    from dotenv import load_dotenv
    import os

    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    ```
4. Add `.env` to your `.gitignore`

---

## 📄 License

This project is released under the [MIT License](LICENSE).
