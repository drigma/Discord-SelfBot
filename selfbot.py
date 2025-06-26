import requests
import time
import logging

# === Configuration ===
TOKEN = "YOUR_DISCORD_TOKEN"  # ⚠️ Do NOT share your user token
CHANNELS = {
    "CHANNEL_ID": "YOUR_MESSAGE"  # for several lines add two quotation marks between the message
}
SEND_INTERVAL = 1800  # in seconds (1800 = 30 minutes)
# Don't spam or put a short delay because you can find RATE LIMIT
ENABLE_LOGS = True    # Set to False to disable console output

headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json",
}

if ENABLE_LOGS:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
else:
    logging.basicConfig(level=logging.CRITICAL)

def send_to_channel(channel_id, message):
    try:
        response = requests.post(
            f"https://discord.com/api/v9/channels/{channel_id}/messages",
            headers=headers,
            json={"content": message},
            timeout=5
        )
        if response.status_code in (200, 204):
            logging.info(f"Message sent to channel {channel_id}")
        elif response.status_code == 429:
            retry_after = response.json().get("retry_after", 5)
            logging.warning(f"Rate limited. Retrying in {retry_after} seconds...")
            time.sleep(retry_after)
            send_to_channel(channel_id, message)
        else:
            logging.warning(f"HTTP {response.status_code} for channel {channel_id}: {response.text}")

    except requests.exceptions.Timeout:
        logging.error(f"Timeout while sending to channel {channel_id}")
    except requests.exceptions.ConnectionError:
        logging.error(f"Connection error while sending to channel {channel_id}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Unexpected error for channel {channel_id}: {str(e)}")

def main_loop():
    while True:
        for channel_id, message in CHANNELS.items():
            send_to_channel(channel_id, message)
        time.sleep(SEND_INTERVAL)

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        logging.info("Script interrupted by user.")
