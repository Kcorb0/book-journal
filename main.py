import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3

# Create a connection to the user.db database
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


def create_account(email, u_name, f_name, s_name, pwd):
    """Create new user account, add to the users database"""

    insert_data = '''
    INSERT INTO users(email, username, firstname, surname, password) 
    VALUES("{}", "{}", "{}", "{}", "{}")
    '''.format(email, u_name, f_name, s_name, pwd)

    cursor.execute(insert_data)
    db.commit()
    print("user created")

def test(name):
    print(name)

class LoginWindow(Screen):
    pass

class CreateAccount(Screen):


    def create_account(self, email, u_name, f_name, s_name, pwd):
        """Create new user account, add to the users database"""

        insert_data = '''
        INSERT INTO users(email, username, firstname, surname, password) 
        VALUES("{}", "{}", "{}", "{}", "{}")
        '''.format(email, u_name, f_name, s_name, pwd)

        cursor.execute(insert_data)
        db.commit()
        print("user created")

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
