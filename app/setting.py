from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv


from kucoin.client import Client


env_file = Path(find_dotenv(usecwd=True))
load_dotenv(verbose=True, dotenv_path=env_file)

api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
api_passphrase = os.environ.get("API_PASSPHRASE")
message_passpharase = os.environ.get("WEBHOOK_PASSPHRASE")

client = Client(api_key, api_secret, api_passphrase)
