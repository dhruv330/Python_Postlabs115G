from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class RoboticsTextInputApp(App):
    def build(self):
        # Set window background to dark steel
        Window.clearcolor = (0.07, 0.07, 0.07, 1)  # #121212

        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # Input field with bright futuristic look
        self.input_text = TextInput(
            hint_text="Type your command...",
            multiline=False,
            font_size=22,
            foreground_color=(0, 1, 1, 1),  # Cyan text
            background_color=(0.15, 0.15, 0.15, 1),  # Dark input field
            cursor_color=(0, 1, 1, 1),
            halign='center',
        )
        self.layout.add_widget(self.input_text)

        # Display label
        self.display_label = Label(
            text="",
            font_size=28,
            color=(1, 1, 1, 1),  # White
            bold=True
        )
        self.layout.add_widget(self.display_label)

        # Button with electric blue futuristic color
        self.button = Button(
            text="Execute",
            font_size=24,
            background_normal='',
            background_color=(0, 1, 1, 1),  # Electric Blue #00FFFF
            color=(0, 0, 0, 1),  # Black text
            size_hint=(1, 0.3)
        )
        self.button.bind(on_press=self.display_input)
        self.layout.add_widget(self.button)

        return self.layout

    def display_input(self, instance):
        self.display_label.text = f"Command Received: {self.input_text.text}"

if __name__ == '__main__':
    RoboticsTextInputApp().run()
