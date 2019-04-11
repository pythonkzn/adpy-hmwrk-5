import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


GMAIL_SMTP = 'smtp.gmail.com'
GMAIL_IMAP = 'imap.gmail.com'
LOGIN = '...'
PASSWORD = '...!'
SUBJECT = 'Subject'
RECIPIENTS = ['...', '...']
MESSAGE = 'Message'
HEADER = None


class MailTool:
    def __init__(self, smtp_in, imap_in):
        self.smtp = smtplib.SMTP(smtp_in, 587)
        self.imap = imaplib.IMAP4_SSL(imap_in)

    def send_email(self, msg_in):
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo()
        self.smtp.login(LOGIN, PASSWORD)
        self.smtp.send_message(msg_in)
        self.smtp.quit()

    def receive_email(self, criterion_in):
        self.imap.login(LOGIN, PASSWORD)
        self.imap.list()
        self.imap.select('inbox')
        result_out, data_out = self.imap.uid('search', None, criterion_in)
        assert data_out[0], 'There are no letters with current header'
        latest_email_uid = data_out[0].split()[-1]
        result_out, data_out = self.imap.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email_out = data_out[0][1]
        email_message_out = email.message_from_string(str(raw_email_out))
        self.imap.logout()
        return email_message_out


def main():
    # send
    msg = MIMEMultipart()
    msg['From'] = LOGIN
    msg['To'] = ', '.join(RECIPIENTS)
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(MESSAGE))
    ms = MailTool(GMAIL_SMTP, GMAIL_IMAP)
    ms.send_email(msg)

    # receive
    criterion = '(HEADER Subject {})'.format(HEADER) if HEADER else 'ALL'
    email_message = ms.receive_email(criterion)


if __name__ == '__main__':
    main()
