import subprocess
import requests
import time
import logging
from datetime import datetime
import pytz

# Configuration
domain = "www.example.com"  # Replace with your target domain
port = 51820  # Replace with your target port
discord_webhook_url = "https://discordapp.com/api/webhooks/yourwebhookurl" # Replace with your discord webhook url
period = 300 # Checks every 5 minutes
down_flag = 0 # used to send notification once service becomes availble again
service = "Wireguard"
log_file="/home/user/wg-uptime.log"

# Function to send a message to the Discord webhook
def send_discord_notification(message):
    data = {
        "content": message
    }
    response = requests.post(discord_webhook_url, json=data)
    if response.status_code != 204:
        logging.error(f"Failed to send notification. Status code: {response.status_code}")

# Function to run nping and check for failures
def check_service():
    try:
        global down_flag
        # Run nping command
        result = subprocess.run(["nping", "--udp", "-p", str(port), domain], capture_output=True, text=True)
        
        # Check if the nping command failed
        if "Nping done" not in result.stdout and down_flag == 0:
            send_discord_notification(f"**{service} Monitor**\n"
                f"**Status:** :x: **DOWN**\n"
                f"**Domain:** `{domain}`\n"
                f"**Port:** `{port}`\n"
                f"**Time:** {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S %Z')}\n"
                f"Please check the service as soon as possible.")
            down_flag = 1
            logging.error(f"{service} service is down. Please check the service as soon as possible")
        if "Nping done" in result.stdout and down_flag == 1:
            send_discord_notification(f"**Wireguard Monitor**\n"
                f"**Status:** :white_check_mark: **UP**\n"
                f"**Domain:** `{domain}`\n"
                f"**Port:** `{port}`\n"
                f"**Time:** {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S %Z')}\n")
            down_flag = 0    
            logging.info(f"{service} service successfully pinged after previously being down")
        logging.info(f"{service} service successfully pinged and wasn't down prior to ping, no notification sent...")
    except Exception as e:
        logging.error(f"An unexpected error occurred while running nping {e}")
        send_discord_notification(f"An unexpected error occurred while running nping: {e}")

def setup_logging():
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filemode='a')  # 'a' for append mode

# Setup logging
setup_logging()

# Run the check
while True:
    check_service()
# Checks domain every 5 minutes
    time.sleep(period)
