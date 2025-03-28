from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("LOGIN_USERNAME")
password = os.getenv("LOGIN_PASSWORD")