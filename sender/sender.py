import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Sender:
    def __init__(self):
        self.conn = None
    
    def connect(self, host: str, port: int, username: str, password: str):
        context = ssl.create_default_context()
        self.conn = smtplib.SMTP(host, port)
        self.conn.ehlo()
        self.conn.starttls(context=context)
        self.conn.ehlo()
        self.conn.login(username, password)

    def send(self, fm: str, to: str, subject: str, body: str):
        msg = MIMEMultipart('alternative')
        msg['From'] = fm
        msg['To'] = to
        msg['Subject'] = subject

        # Create a MIMEText object with the body content
        text_part = MIMEText(body, 'html')
        msg.attach(text_part)

        self.conn.sendmail(fm, to, msg.as_string())
