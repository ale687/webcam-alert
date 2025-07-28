import smtplib
import imghdr
import os
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
SENDER = os.getenv("SENDER")
RECEIVER = os.getenv("RECEIVER")

def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message['Subject'] = "Alert: Object Detected"
    email_message.set_content("An object has been detected by your webcam. Please check the attached image.")

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))
    
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function finished")
    
if __name__ == "__main__":
    send_email(image_path="images/39.png")  # Example usage