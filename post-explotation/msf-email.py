#!/usr/bin/python
# Content:	Email notifying by MSF
# Author: 	Florian Hansemann | @HanseSecure | https://hansesecure.de
# Date: 	04/2018
#

import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


def send():
	#	Config here
	yourMail = <yourMail>
	smtpServer = <yourServer>
	smtpPort = <yourServerPort>
	yourPassword = <yourPassword>
	
        msg = MIMEText("Hey User, \nYour session is opened, the backdoor is installed and now it's time for Admin-Hunting!\n\nCheers\nYour C&C-Server")
        msg['From'] = yourMail
        msg['To'] = yourMail
        msg['Subject'] = "Session opened"


        #	Connect to SMTP-Server
        smtpServer = smtplib.SMTP(smtpServer, smtpPort)
        smtpServer.ehlo()
        smtpServer.starttls()
        smtpServer.ehlo()
        smtpServer.login(yourMail, yourPassword)
        smtpServer.sendmail(msg['From'], msg['To'], msg.as_string())
        smtpServer.close()

def main():
    send()


if __name__ == '__main__':
    main()
