import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3

# Create a connecting to the user.db database
with sqlite3.connect("users.db") as db:
    cursor = db.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
userID INTEGER PRIMARY KEY,
email VARCHAR(40) NOT NULL,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
surname VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')

email = "josh_blackmore@hotmail.co.uk"
username = "Kcorb"
firstname = "Joshua"
surname = "Blackmore"
password = "Kcrubber22"

insert_data = '''
INSERT INTO users(email, username, firstname, surname, password) 
VALUES("{}", "{}", "{}", "{}", "{}")
'''.format(email, username, firstname, surname, password)

cursor.execute(insert_data)

db.commit()

class LoginWindow(Screen):
    pass

class CreateAccount(Screen):
    pass

class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

class MyApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
