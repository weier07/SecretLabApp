from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("kivy.kv")

class MainScreen(Screen):
    def test_button(self):
        self.ids.status.text = "Кнопка работает!"

class MyApp(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(MainScreen(name = "main"))
        return sm

if __name__ == '__main__':
    MyApp().run()
