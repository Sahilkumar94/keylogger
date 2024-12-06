KeyLogger
Keyloggers are a particularly insidious type of spyware that can record and steal consecutive keystrokes (and much more) that the user enters on a device.
The term keylogger, or "keystroke logger," is self-explanatory: Software that logs what you type on your keyboard.


Prerequisite
Python package pynput is required.

pip install pynput

Create log.txt file in the same directory of keyLogger.py file.

About the library
pynput- This library allows you to control and monitor input devices.

n this I have used pynput.keyboard subpackage(contains classes for controlling and monitoring the keyboard)

smtplib module
It is the module used to send mails.

Working
Listen the pressed key
Add pressed key to the file
After every 10 keys pressed, send it to the researcher's email.
NOTE
logconfig.py file need to be configured before use.

**Create a seperate email id for this because it can comprise the security of the email id.**
