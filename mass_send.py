import smtplib
import os
import sys
import config

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

class MassMail(object):

    def __init__(self, user, pwd, server, auth, port=None):
        self.send_from = user
        self.init_mailserver(user, pwd, server, port, auth)

    
    def init_mailserver(self, user, pwd, server, port, auth):
        """
        Set up the smtp mailserver
        """
        if port:
            self.smtp = smtplib.SMTP(server, port)
        else:
            self.smtp = smtplib.SMTP(server)

        # TLS handshake
        if auth == "tls":
            self.smtp.ehlo()
            self.smtp.starttls()
            self.smtp.ehlo()
            self.smtp.login(user, pwd)

        # TODO: ssl authentication
        if auth == "ssl":
            pass

    def mass_send(self, send_list, path, subject, text):
        """
        Mass sends emails in send_list
        """
        for s in send_list:
            uni = s.split('@')[0]
            f = os.path.join(path, uni + ".txt")
            self.send([s], subject, text, files=[f])

    def send(self, send_to, subject, text, files=[]):
        """
        Sends one email
        """
        assert type(send_to) == list
        assert type(files) == list

        # Setting up email msg protocol
        msg = MIMEMultipart()
        msg['From'] = self.send_from
        msg['To'] = COMMASPACE.join(send_to)
        msg['Cc'] = self.send_from
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach(MIMEText(text))

        # Message does not send if expected file is not found
        try:
            for f in files:
                part = MIMEBase('application', "octet-stream")
                part.set_payload(open(f,"rb").read())
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 
                        'attachment; filename="%s"' % os.path.basename(f))
                msg.attach(part)

            self.smtp.sendmail(self.send_from, send_to, msg.as_string())    
            print "Message sent to: " + str(send_to)
        except IOError:
            print "Message not sent to %s. %s doesn't exist" % (str(send_to), 
                    str(files))
    
    def close(self):
        self.smtp.quit()

def help():
    print"""
        python mass_send.py <your_email> <uni_list> <grade_report_directory>
    """

if __name__ == "__main__":
    if len(sys.argv) != 4:
        help()
        exit(1)

    email_file_path = sys.argv[1]
    students_file_path = sys.argv[2]
    reports_path = sys.argv[3]

    email_file = open(email_file_path, 'r')
    subject = email_file.readline()
    text = email_file.read()
    email_file.close()
    
    students_file = open(students_file_path, 'r')
    students = students_file.read().strip().split('\n')
    students_file.close()

    # smtp config
    USER = config.USERNAME
    PWD = config.PWD 
    SERVER = config.SERVER
    PORT = config.PORT
    AUTH = config.AUTHENTICATION
    
    sender = MassMail(USER, PWD, SERVER, AUTH, PORT)
    sender.mass_send(students, reports_path, subject, text)
    sender.close()

