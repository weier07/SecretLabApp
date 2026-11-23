import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(Screen):
    def login_user(self):
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE login = ? AND password = ?',(login,password))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.manager.current = 'menu'
        else:
            self.ids.message.text ='Неверный логин или пароль'

        App.get_running_app().current_user = login
        self.manager.current = 'menu'

class RegisterScreen(Screen):
    def register_user(self):
        login = self.ids.reg_login.text
        password = self.ids.reg_password.text
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (login,password) VALUES(?,?)', (login, password))
            conn.commit()
            self.ids.reg_message.text = 'Регистрация успешна'

        except sqlite3.IntegrityError:
            self.ids.reg_message.text = 'Такой логин уже существует'
            conn.close()

class MainMenuScreen(Screen):
    def greet_agent(self):
        user = App.get_running_app().current_user
        self.ids.info_label.text = f'Добро пожаловать в систему, агент {user}!'

    def show_agent_info(self):
        user = App.get_running_app().current_user
        self.ids.info_label.text = f'Информация: Агент {user} | Статус: Активен | Отдел: Кибербезопасность'

    def show_secret_mission(self):
        self.ids.info_label.text = 'Секретная миссия: Расшифровать архив лаборатории до 00:00.'

    def check_access(self):
        self.ids.info_label.text = 'Проверка пройдена: Уровень допуска — СЕКРЕТНО (Уровень 4).'

class SecretLabApp(App):
    def build(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT UNIQUE, password TEXT)')
        conn.commit()
        conn.close()
        return Builder.load_file('kivy.kv')

SecretLabApp().run()
