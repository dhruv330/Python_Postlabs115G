from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class CounterApp(App):
    def build(self):
        # Set background color to 1970s cream
        Window.clearcolor = (1, 0.953, 0.878, 1)  # #FFF3E0

        self.counter = 0

        layout = BoxLayout(orientation='vertical', padding=50, spacing=30)

        # Label to show counter
        self.label = Label(
            text=str(self.counter),
            font_size=80,
            bold=True,
            color=(0.33, 0.42, 0.18, 1)  # Olive green #556B2F
        )
        layout.add_widget(self.label)

        # Button to increment counter
        btn = Button(
            text="Click Me",
            font_size=30,
            size_hint=(1, 0.3),
            background_normal='',
            background_color=(0.82, 0.41, 0.12, 1),  # Burnt orange #D2691E
            color=(0.31, 0.20, 0.18, 1)  # Dark brown #4E342E
        )
        btn.bind(on_press=self.increment_counter)
        layout.add_widget(btn)

        return layout

    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = str(self.counter)

if __name__ == '__main__':
    CounterApp().run()
