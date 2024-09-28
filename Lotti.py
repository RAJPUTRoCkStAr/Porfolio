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
lottie_me = load_lottiefile("lottie/Me.json")
project = load_lottiefile("lottie/project.json")
pyhon = load_lottiefile("lottie/pyhon.json")
skills = load_lottiefile("lottie/skills.json")
contac = load_lottiefile("lottie/connect.json")
github = load_lottiefile("lottie/github.json")
company = load_lottiefile("lottie/company.json")
Certificate = load_lottiefile("lottie/Certificate.json")