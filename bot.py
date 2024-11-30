import yaml
import requests
import argparse


# Load the YAML file
with open("config.yaml", "r") as file:
    cfg = yaml.safe_load(file)

TOKEN = cfg["telegram"]["bot_token"]
CHAT_ID = cfg["telegram"]["chat_id"]


def send_message(message="hello from your telegram bot"):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url).json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--message",
        nargs='+',
        help="message to be sent",
        required=False,
        default="use -m as an option to addd a message",
    )
    args = parser.parse_args()
    send_message(' '.join(args.message))
