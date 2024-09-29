import json
import requests
from streamlit_lottie import st_lottie
def load_lottiefile(filepath:str):
    with open (filepath, 'r') as f:
        return json.load(f)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_me = load_lottiefile("https://raw.githubusercontent.com/RAJPUTRoCkStAr/VisionaryStocks/main/lottie/Me.json")
contac = load_lottiefile("https://raw.githubusercontent.com/RAJPUTRoCkStAr/VisionaryStocks/main/lottie/connect.json")
