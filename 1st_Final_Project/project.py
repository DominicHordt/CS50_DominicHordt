import re
import random
import string
import sqlite3
import secrets
import urllib.parse
from cryptography.fernet import Fernet

'''
The DataStruct class operates with SQLite database where the passwords are stored
'''
class DataStruct:
    # This constant store a path to file with an encryption key
    KEY_FILE = 'spanish_inquisition.file'

    '''
    The pass_encryption method creates an encrypt key if there are none and fetches it
    '''
    @staticmethod
    def pass_encryption():
        try:
            with open(DataStruct.KEY_FILE, 'rb') as file:
                return file.read().strip()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open(DataStruct.KEY_FILE, 'wb') as file:
                file.write(key)
            return key
    '''
    The connect_to_db function connects to the database and creates a cursor
    '''
    @staticmethod
    def connect_to_db():
        try:
            conn = sqlite3.connect("PassMng.db")
            cursor = conn.cursor()
            return conn, cursor
        except sqlite3.OperationalError as e:
            print("Failed to open database:", e)
            return None, None
    '''
    The add_account method creates a new db table if there are none and puts a new entry in the existing database.
    The method requires a url, email, and password, which will be encrypted
    '''
    @classmethod
    def add_account(cls, domain, email, password):
        conn, cursor = cls.connect_to_db()
        if not conn:
            return

        key = cls.pass_encryption()
        cryptor = Fernet(key)

        cursor.execute("""CREATE TABLE IF NOT EXISTS ACCOUNTS(ID INTEGER PRIMARY KEY AUTOINCREMENT,
         DOMAIN VARCHAR(255), EMAIL VARCHAR(255), PASS BLOB);""")
        cursor.execute("SELECT * FROM ACCOUNTS WHERE DOMAIN = ? AND EMAIL = ?", (domain, email))
        acc_exist = cursor.fetchone()

        if acc_exist:
            print(f"An account for {email} already exists on {domain}.")
            return None
        else:
            cursor.execute('INSERT INTO ACCOUNTS (DOMAIN, EMAIL, PASS) VALUES (?, ?, ?)',
                           (domain, email, cryptor.encrypt(password.encode())))

        conn.commit()
        print(f"Account for {email} on {domain} added successfully.")
        conn.close()

    '''
    The update_password method lets a user update the password of an existing account
    '''
    @classmethod
    def update_password(cls, domain, email, password):
        conn, cursor = cls.connect_to_db()
        if not conn:
            return

        key = cls.pass_encryption()
        cryptor = Fernet(key)
        password = cryptor.encrypt(password.encode())

        try:
            cursor.execute('UPDATE ACCOUNTS SET PASS = ? WHERE DOMAIN = ? AND EMAIL = ?',
                           (password, domain, email))
            conn.commit()
            print(f"Password updated for {email}.")
        except sqlite3.Error as e:
            print("An error occurred:", e)
        finally:
            conn.close()

    '''
    The delete_account method lets the user to delete an entry from the database
    '''
    @classmethod
    def delete_account(cls, domain, email):
        conn, cursor = cls.connect_to_db()
        if not conn:
            return

        try:
            cursor.execute('DELETE FROM ACCOUNTS WHERE DOMAIN = ? AND EMAIL = ?', (domain, email))
            print(f"The record for {email} has been deleted successfully.")
            conn.commit()

        except sqlite3.Error as e:
            print("An error occurred:", e)
        finally:
            conn.close()

    '''
    The fetch_data lets the user get the entry with decrypted passworddecode
    '''
    @classmethod
    def fetch_data(cls, domain):
        conn, cursor = cls.connect_to_db()
        if not conn:
            return

        key = cls.pass_encryption()
        cryptor = Fernet(key)

        try:
            cursor.execute("SELECT * FROM ACCOUNTS WHERE DOMAIN = ?", (domain,))
            output = cursor.fetchall()
            if output:
                for _, domain, email, cr_password in output:
                    try:
                        password = cryptor.decrypt(cr_password).decode()
                        print(f"Website: {domain}, email: {email}, password: {password}")
                    except Exception as e:
                        print(f"Error decrypting password for {email}: {e}")
            else:
                print("No accounts found for this website.")

        except sqlite3.Error as e:
            print("An error occurred:", e)
        finally:
            conn.close()

    '''
    The drop_table method is never used, but it erases the whole table, which is useful for debug purpose :)
    '''
    @classmethod
    def drop_table(cls):
        conn, cursor = cls.connect_to_db()
        if not conn:
            return
        try:
            cursor.execute("DROP TABLE ACCOUNTS")
            print(f"The table cleared successfully.")

        except sqlite3.Error as e:
            print("An error occurred:", e)
        finally:
            conn.close()

    '''
    The print_db method prints everything that is stored in a database, with passwords being encrypted
    '''
    @classmethod
    def print_db(cls):
        conn, cursor = cls.connect_to_db()
        if not conn:
            return

        try:
            data = cursor.execute('SELECT * FROM ACCOUNTS')
            for row in data:
                print(row)
        except sqlite3.Error as e:
            print("An error occurred:", e)
        finally:
            conn.close()

'''
The URLParser class parses the URL given by user and fetches the website location (e.g.: "example.org")
'''
class URLParser:
    def __init__(self, domain):
        self.domain = domain

    @classmethod
    def parse_url(cls, domain):
        if not domain:
            raise ValueError("Invalid URL")
        return urllib.parse.urlparse(cls.validate_string(domain)).netloc

    @staticmethod
    def validate_string(domain):
        scheme = re.search(r"^http(|s)://", domain)
        chk_dmn = re.search(r".\..", domain)
        if not scheme:
            if not chk_dmn:
                raise ValueError("Invalid URL")
            else:
                # urlparse doesn't recognise URLs if written without protocol
                return f"https://{domain}"
        return domain

'''
The Email class parses and validates the user input
'''
class Email:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not email:
            raise ValueError("Invalid email")
        self._email = email

    def email_validator(self):
        if re.search(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
                     r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", self.email):
            return self.email
        else:
            raise ValueError("Email is invalid!")

    def __str__(self):
        return self.email

'''
The Password class validates the user input and generates password
'''
class Password:
    def __init__(self, password=''):
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    '''
    The pass_method function lets the user choose whether they want to generate password or enter their own
    '''
    def pass_method(self):
        option = input("Select an option: 1. Generate password. 2. Enter your own password. ")
        while True:
            if option == '1':
                return self.generate_pass()
            elif option == '2':
                password = input("Enter your password: ")
                self.password = password
                try:
                    self.validate_pass()
                    print("Password is valid!")
                    return self.password
                except ValueError as e:
                    print(e)
                    continue
            else:
                print('Please choose correct option.')
                option = input("Select an option: 1. Generate password. 2. Enter your own password. ")

    '''
    The validate_pass method validates if the user's password is strong, and if not, asks them to create another one
    '''
    def validate_pass(self):
        if len(self.password) < 8:
            raise ValueError("Password is too short! Create another one.")
        if (re.search(r"[a-z]", self.password) and re.search(r"[A-Z]", self.password) and
                re.search(r"[!@#$%^&*()-_+=]", self.password)):
            return "Password is strong!"
        else:
            raise ValueError("Try thinking of a stronger password")

    def __str__(self):
        return self.password

    '''
    The generate_pass method creates a password. It uses string library to create pools of uppercase letters, lowercase
    letters and digits, and secrets library to randomly pick characters. Python documentation says that secrets is more
    preferable than random, so I picked this one
    '''
    @staticmethod
    def generate_pass(length=16):
        if length < 8:
            raise ValueError("Password length should be at least 8 characters.")

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special = "!@#$%^&*()-_+="
        all_chars = lower + upper + digits + special

        password = [
            secrets.choice(lower),
            secrets.choice(upper),
            secrets.choice(digits),
            secrets.choice(special)
        ]

        password += [secrets.choice(all_chars) for _ in range(length)]

        secrets.SystemRandom().shuffle(password)
        return ''.join(password)

'''
This is an Easter egg :)
'''
class BullsAndCows:
    @classmethod
    def is_unique_chars(cls, n):
        for i in n:
            if n.count(i) > 1:
                return False
        return True

    @classmethod
    def generate_number(cls):
        n = ''.join(map(str, random.sample(range(10), 4)))
        if cls.is_unique_chars(n):
            return n

    @classmethod
    def enter_num(cls):
        while True:
            n = input("Enter your number: ")
            if not n.isdigit():
                print("It's not a number!")
                continue
            else:
                if not cls.is_unique_chars(n):
                    print("Your number has duplicate digits! Try again.")
                    continue
                elif len(n) > 4 or len(n) < 4:
                    print("The number must consist of exactly 4 digits! Try again.")
                    continue
                else:
                    return n

    @classmethod
    def check_num(cls, guess, real):
        bulls = 0
        cows = 0
        for _ in range(len(guess)):
            if guess[_] == real[_]:
                bulls += 1
            elif guess[_] in real:
                cows += 1
        return bulls, cows

    @staticmethod
    def ask_to_play():
        while True:
            new_game = input("Would you like to play again? y/n ")
            if new_game.lower() == "y":
                return True
            elif new_game.lower() == "n":
                return False
            else:
                print("I don't understand. Try again!")
                continue

def add_account():
    print("Creating account:")
    while True:
        try:
            domain = URLParser.parse_url(input("Enter website for account: "))
        except ValueError as e:
            print(e)
            continue
        else:
            while True:
                try:
                    mail = Email(input("Enter email: ")).email_validator()
                    password = Password()
                    return DataStruct.add_account(domain, mail, password.pass_method())
                except ValueError as er:
                    print(er)
                    continue

def change_password():
    print("Changing password for the following account:")
    while True:
        try:
            domain = URLParser.parse_url(input("Enter account website: "))
        except ValueError as e:
            print(e)
            continue
        else:
            while True:
                try:
                    mail = Email(input("Enter email: ")).email_validator()
                    password = Password()
                    return DataStruct.update_password(domain, mail, password.pass_method())
                except ValueError as er:
                    print(er)
                    continue

def fetch_data():
    print("Retrieving data by URL:")
    while True:
        try:
            domain = URLParser.parse_url(input("Enter account website: "))
            return DataStruct.fetch_data(domain)
        except ValueError as e:
            print(e)
            continue

def print_all():
    print("Table contents:")
    return DataStruct.print_db()

def delete_account():
    print("Deleting an existing account:")
    while True:
        try:
            domain = URLParser.parse_url(input("Enter account website: "))
        except ValueError as e:
            print(e)
            continue
        else:
            while True:
                try:
                    mail = input("What email do you want to erase? ")
                    return DataStruct.delete_account(domain, mail)
                except ValueError as er:
                    print(er)
                    continue

def the_game():
    play = True
    while True:
        print("Aha! You found it! Welcome to Bulls and Cows!")
        print("In this game computer sets the number, and your goal is to guess it.\n"
              "Bulls are the matching digits in their right positions, and cows are "
              "the matching digits in the number in different positions.\nGood luck!")

        num = BullsAndCows.generate_number()

        while play:
            guess = BullsAndCows.enter_num()
            bulls, cows = BullsAndCows.check_num(guess, num)
            if bulls == 4:
                print("Congratulations! You won!")
                break
            else:
                print(f"Bulls: {bulls}, cows: {cows}")

        play_again = BullsAndCows.ask_to_play()

        if play_again:
            play = True
            continue
        else:
            print("Thanks for playing!")
            break

def main():
    print("Welcome to Password Manager!")
    print("I can:\n1. Add a new account,\n2. Update existing account with a new password,\n3. Fetch a password\n"
          "4. Delete an existing account,\n5. Show whole database.")
    option = input("What do you want me to do? Enter a number of an option without a dot. ")
    while True:
        if option == '1':
            return add_account()
        elif option == '2':
            return change_password()
        elif option == '3':
            return fetch_data()
        elif option == '4':
            return delete_account()
        elif option == '5':
            return print_all()
        elif option == 'bull':
            return the_game()
        else:
            print('Please choose correct option.')
            option = input("What do you want me to do? Enter a number of an option without a dot. ")

if __name__ == "__main__":
    main()
