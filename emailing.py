import smtplib
import imghdr
import os
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

PASSWOR = os.getenv("PASSWOR")
SENDER = os.getenv("SENDER")
RECEIVER = os.getenv("RECEIVER")

def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = "Alert: Object Detected"
    email_message.set_content("An object has been detected by your webcam. Please check the attached image.")

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))
    
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWOR)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    
if __name__ == "__main__":
    send_email(image_path="images/39.png")  # Example usage