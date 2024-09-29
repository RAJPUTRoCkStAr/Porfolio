from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageOps, ImageDraw
from streamlit_lottie import st_lottie
from email.mime.text import MIMEText
from dotenv import load_dotenv
from Lotti import contac
import streamlit as st
import smtplib
import re
import os
load_dotenv()
#############################################################################
def make_image_round(image):
    width, height = image.size
    min_size = min(width, height)
    image = image.resize((min_size, min_size))
    mask = Image.new('L', (min_size, min_size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, min_size, min_size), fill=255)
    result = ImageOps.fit(image, (min_size, min_size), centering=(0.5, 0.5))
    result.putalpha(mask)
    return result
def show_image():
    image_path = "https://raw.githubusercontent.com/RAJPUTRoCkStAr/VisionaryStocks/main/lottie/passportsize_profile.jpeg"  
    image = Image.open(image_path)
    rounded_image = make_image_round(image)
    st.image(rounded_image, caption="Sumit Kumar Singh", use_column_width=True)
###########################################################################
    st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
############################################################################
def send_contact_email(name, email, subject, message):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = os.getenv('SMTP_USERNAME')
        smtp_password = os.getenv('SMTP_PASSWORD')
        recipient_email = "luciferdevil565656@gmail.com" 
        mail_content = f"""
        <html>
        <body>
            <div style="font-family: Arial, sans-serif; color: #333;">
                <h1 style="color: #1a73e8;">Contact Us Message</h1>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Subject:</strong> {subject}</p>
                <p><strong>Message:</strong></p>
                <p>{message}</p>
                <p>Best regards,<br>{name}</p>
            </div>
        </body>
        </html>
        """
        message_obj = MIMEMultipart()
        message_obj['From'] = smtp_username
        message_obj['To'] = recipient_email
        message_obj['Subject'] = subject
        message_obj.attach(MIMEText(mail_content, 'html'))
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(message_obj)
        st.success("Thank you for contacting us! Your message has been sent successfully.")
    except Exception as e:
        st.error(f"Failed to send email: {e}")
#############################################################################
def contact():
    st.subheader("📧 Feel free to reach out!",divider="rainbow")
    col1,col2 = st.columns([3,1])
    with col1:
        with st.form(key="contact_form", clear_on_submit=True):
            name = st.text_input("Enter your name")
            email = st.text_input("Enter your email address")
            subject = st.text_input("Subject")
            message = st.text_area("Your message")
            submit_button = st.form_submit_button("Send Message")

            if submit_button:
                if not name or not email or not subject or not message:
                    st.error("Please fill in all required fields.")

                elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    st.error("Please enter a valid email address.")

                else:
                    send_contact_email(name, email, subject, message)
    with col2:
         st_lottie(contac, speed=1, reverse=False, loop=True, quality='high', height=400, width=260)