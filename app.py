import streamlit as st
from streamlit_option_menu import option_menu
from Skills import skil
from Intro import intro
from Project import proj
from Certificate import certif
from utils import contact
from Resume import resume
import streamlit.components.v1 as components
from Html_comp import GITHUB_PROFILE,LINKEDIN_PROFILE
from utils import show_image
st.set_page_config(page_title="Sumit Singh",page_icon='👨‍💻',layout='wide')
with st.sidebar:
    show_image()
    components.html(GITHUB_PROFILE)
    components.html(LINKEDIN_PROFILE,height=500,width=900)
st.markdown("""
    <style>
    /* Background for the entire app */
    .css-1v3fvcr {
        background-color: rgba(34, 34, 59, 0.85);  /* Dark purple with slight transparency */
        backdrop-filter: blur(8px);  /* Apply blur effect */
        padding: 10px;
    }
    /* Streamlit sidebar or main panel background */
    .css-16huue1 {
        background-color: rgba(44, 44, 84, 0.9);  /* Slightly darker purple */
        padding: 10px;
        border-radius: 15px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.6);  /* Add shadow effect */
    }
    /* Option menu link styling */
    .nav-pills .nav-link {
        font-size: 18px;
        color: #dcdcdc;  /* Light grey text */
        transition: color 0.3s ease, background-color 0.3s ease;
    }
    .nav-pills .nav-link:hover {
        background-color: #5e60ce;  /* Purple hover */
        color: white;
    }
    .nav-pills .nav-link.active {
        background-color: #7b2cbf;  /* Deeper purple for active */
        color: white;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

app = option_menu(
    None,
    ["Introduction", "Skills", "Projects", "Certificates", "Resume", "Contact us"],
    icons=["person", "laptop", "folder", "award", "file-earmark", "envelope"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding": "0!important", "background-color": "rgba(34, 34, 59, 0.85)"},
        "icon": {"color": "lightblue", "font-size": "24px"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#4a4a4a",
        },
        "nav-link-selected": {"background-color": "#7b2cbf", "color": "white"}, 
    }
)

if app == "Introduction":
    intro()
if app == "Skills":
    skil()
if app == "Projects":
    proj()
if app == "Certificates":
    certif()
if app == "Resume":
    resume()
if app == "Contact us":
    contact()