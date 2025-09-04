import random
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class CaraCoroaApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Clique no botão para jogar!", font_size=24)
        self.layout.add_widget(self.label)

        self.image = Image(source="")
        self.layout.add_widget(self.image)

        self.button = Button(text="Jogar", font_size=24, size_hint=(1, 0.3))
        self.button.bind(on_press=self.jogar)
        self.layout.add_widget(self.button)

        return self.layout

    def jogar(self, instance):
        resultado = random.choice(["cara", "coroa"])
        self.label.text = f"Deu {resultado.upper()}!"
        self.image.source = f"{resultado}.png"

if __name__ == '__main__':
    CaraCoroaApp().run()
