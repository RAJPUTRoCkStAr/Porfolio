import json
import requests
from streamlit_lottie import st_lottie
import requests

def load_lottiefile(filepath: str):
    if filepath.startswith("http"):
        # Fetching the JSON file from a URL
        response = requests.get(filepath)
        if response.status_code == 200:
            return response.json()  # Parse the JSON if the request was successful
        else:
            raise FileNotFoundError(f"Could not retrieve file from URL: {filepath}")
    else:
        # Local file handling
        with open(filepath, 'r') as f:
            return json.load(f)

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_me = load_lottiefile("lottie/Me.json")
contac = load_lottiefile("lottie/Connect.json")
