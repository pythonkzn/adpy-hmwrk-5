import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


GMAIL_SMTP = 'smtp.gmail.com'
GMAIL_IMAP = 'imap.gmail.com'
LOGIN = 'raravilov@gmail.com'
PASSWORD = 'Ruslan123!'
SUBJECT = 'Subject'
RECIPIENTS = ['raravilov@bars.group', 'raravilov@gmail.com']
MESSAGE = 'Message'
HEADER = None


class MailTool:
    def __init__(self, smtp):
        self.smtp = smtplib.SMTP(smtp, 587)

    def send_email(self):
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo()
        self.smtp.login(LOGIN, PASSWORD)
        self.smtp.send_message(msg)
        self.smtp.quit()

        
msg = MIMEMultipart()
msg['From'] = LOGIN
msg['To'] = ', '.join(RECIPIENTS)
msg['Subject'] = SUBJECT
msg.attach(MIMEText(MESSAGE))
ms = MailTool(GMAIL_SMTP)
ms.send_email()




#recieve
#mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
#mail.login(LOGIN, PASSWORD)
#mail.list()
#mail.select("inbox")
#criterion = '(HEADER Subject "%s")' % HEADER if HEADER else 'ALL'
#result, data = mail.uid('search', None, criterion)
#assert data[0], 'There are no letters with current header'
#latest_email_uid = data[0].split()[-1]
#result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
#raw_email = data[0][1]
#email_message = email.message_from_string(raw_email)
#mail.logout()
#end recieve