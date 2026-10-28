from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class BllokuShenimeve(BoxLayout):
    def __init__(self, **kwargs):
        super(BllokuShenimeve, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        # Titulli i aplikacionit
        self.add_widget(Label(
            text='Blloku i Shënimeve',
            font_size=28,
            size_hint_y=None,
            height=50
        ))

        # Kutia ku shkruan shënimin
        self.teksti_input = TextInput(
            hint_text='Shkruaj shënimin tënd këtu...',
            font_size=18,
            multiline=True
        )
        self.add_widget(self.teksti_input)

        # Butoni për të ruajtur/shfaqur
        self.btn_ruaj = Button(
            text='Shfaq Shënimin',
            font_size=18,
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.6, 0.8, 1)
        )
        self.btn_ruaj.bind(on_press=self.shfaq_shenimin)
        self.add_widget(self.btn_ruaj)

        # Etiketa ku shfaqet rezultati
        self.label_rezultati = Label(
            text='',
            font_size=18,
            size_hint_y=None,
            height=80
        )
        self.add_widget(self.label_rezultati)

    def shfaq_shenimin(self, instance):
        teksti = self.teksti_input.text
        if teksti.strip() == "":
            self.label_rezultati.text = "Të lutem shkruaj diçka!"
        else:
            self.label_rezultati.text = f"U ruajt: {teksti}"

class MyApp(App):
    def build(self):
        return BllokuShenimeve()

if __name__ == '__main__':
    MyApp().run()
