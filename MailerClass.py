import os
import smtplib
from dotenv import load_dotenv
load_dotenv()

class MailerClass(): 
  def __init__(self) -> None:
    self.sender_email = os.environ.get('DEFAULT_MAIL_SENDER')
    self.receiver_email = os.environ.get('DEFAULT_MAIL_RECEIVER')
    self.sender = "Server Alerts <{}>".format(self.sender_email)
    self.receiver = "Client <{}>".format(self.receiver_email)
    
  def sendAlert(self, subject: str, message: str):
    self.subject = "[Alert Message] An error has occurred on the server" if subject == "" else subject
    self.message =  f"""\
Subject: {subject}
To: {self.receiver}
From: {self.sender}

{"Something happened on the server. Please check the logs for more details!" if message == "" else message}."""
  
    self._sendMail()

  def _sendMail(self): 
    with smtplib.SMTP(os.environ.get('MAIL_SERVER'), os.environ.get('MAIL_PORT')) as server:
      server.login(os.environ.get('MAIL_USER'), os.environ.get('MAIL_PASSWORD'))
      server.sendmail(self.sender_email, self.receiver_email, self.message)
