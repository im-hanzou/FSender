from template import Template
from sender import Sender
from configparser import ConfigParser
import os
import time

class Main:
    def __init__(self):
        self.emails = []
        self.template = Template()
        self.sender = Sender()
        self.config = None

    def banner(self):
        banner = f'''
\x1b[1;31m _____ _____           _         
|   __|   __|___ ___ _| |___ ___ 
|   __|__   | -_|   | . | -_|  _|
|__|  |_____|___|_|_|___|___|_|  

\x1b[1;37mPython Emails Sender By @faizdotid\x1b[0m\n'''
        print(banner)

    def load_configuration(self):
        if not os.path.isfile('config.ini'):
            exit('\x1b[1;31m[!] \x1b[0;37mConfiguration file not found!\x1b[0m')
        config = ConfigParser()
        config.read('config copy.ini')
        self.config = config
        print('\x1b[1;32m[+] \x1b[0;37mConfiguration loaded!\x1b[0m')

    def configure_smtp(self):
        try:
            print('\x1b[1;33m[*] \x1b[0;37mConnecting to SMTP server...\x1b[0m')
            self.sender.connect(
                self.config['smtp'].get('host'),
                self.config['smtp'].getint('port'),
                self.config['smtp'].get('username'),
                self.config['smtp'].get('password')
            )
            print('\x1b[1;32m[+] \x1b[0;37mConnected to SMTP server!\x1b[0m')
        except Exception as e:
            exit(f'\x1b[1;31m[!] \x1b[0;37m{e}\x1b[0m')

    def load_letter(self):
        letter = input('\x1b[1;34m[?] \x1b[0;37mLetter: \x1b[0m')
        if not os.path.isfile(letter):
            exit(f'\x1b[1;31m[!] \x1b[0;37m{letter} file not found!\x1b[0m')
        with open(letter, 'r') as f:
            self.letter = f.read()
    
    def load_emails(self):
        emails = input('\x1b[1;34m[?] \x1b[0;37mEmails: \x1b[0m')
        if not os.path.isfile(emails):
            exit(f'\x1b[1;31m[!] \x1b[0;37m{emails} file not found!\x1b[0m')
        with open(emails, 'r') as f:
            self.emails = f.read().splitlines()

    def start_sending(self):
        count = 0
        print(f'\x1b[1;34m[?] \x1b[0;37mTotal emails: \x1b[0;34m{len(self.emails)}\x1b[0m')
        print('\x1b[1;32m[+] \x1b[0;37mSending emails...\x1b[0m')
        for email in self.emails:
            count += 1
            try:
                self.sender.send(
                    self.config.get('smtp', 'from'),
                    email,
                    self.template.build(self.config.get('template', 'subject'), email),
                    self.template.build(self.letter, email)
                )
                print(f'\x1b[1;34m[ \x1b[0;37m{count} \x1b[1;36m/ \x1b[0;37m{len(self.emails)} \x1b[1;34m] \x1b[0;37m{email} \x1b[1;32mSent!\x1b[0m')
            except Exception as e:
                print(f'\x1b[1;34m[ \x1b[0;37m{count} \x1b[1;36m/ \x1b[0;37m{len(self.emails)} \x1b[1;34m] \x1b[0;37m{email} \x1b[1;31m{e}\x1b[0m')
            time.sleep(self.config.getint('settings', 'delay'))
        self.sender.conn.quit()
        print('\x1b[1;32m[+] \x1b[0;37mDone!\x1b[0m')

    def main(self):
        self.banner()
        self.load_configuration()
        self.configure_smtp()
        self.load_letter()
        self.load_emails()
        self.start_sending()


if __name__ == '__main__':
    Main().main()


# $random_string(10) -> dsjdsnjsdnj
# $random_number(10) -> 1234567890
# $time(day) -> Monday
# $time(date) -> 01
# $time(month) -> 01
# $time(year) -> 2021
# $time(hour) -> 01
# $time(minute) -> 01
# $time(second) -> 01