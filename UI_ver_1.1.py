from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FamilySavingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        self.amount_input = MDTextField(
            hint_text='Enter deposit amount',
            input_filter='int',
            mode='rectangle'
        )
        self.layout.add_widget(self.amount_input)

        calculate_btn = MDRaisedButton(
            text='Calculate Interest',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5}
        )
        calculate_btn.bind(on_press=self.calculate_interest)
        self.layout.add_widget(calculate_btn)

        self.result_label = MDLabel(
            halign='center',
            theme_text_color='Primary'
        )
        self.layout.add_widget(self.result_label)

        back_btn = MDRaisedButton(
            text='Back to Menu',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5}
        )
        back_btn.bind(on_press=self.go_back)
        self.layout.add_widget(back_btn)

        self.add_widget(self.layout)

    def calculate_interest(self, instance):
        try:
            amount = int(self.amount_input.text)
            result = self.calculate_family_saving_interest(amount)
            self.result_label.text = result
        except ValueError:
            self.result_label.text = "Invalid input. Please enter a valid amount."

    def calculate_family_saving_interest(self, amount):
        # Your interest calculation logic here
        return f"Interest for {amount} is calculated."

    def go_back(self, instance):
        self.manager.current = 'menu'

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        fs_btn = MDRaisedButton(
            text='Family Saving Certificate',
            size_hint=(None, None),
            size=(250, 50),
            pos_hint={'center_x': 0.5}
        )
        fs_btn.bind(on_press=self.go_to_family_saving)
        layout.add_widget(fs_btn)

        self.add_widget(layout)

    def go_to_family_saving(self, instance):
        self.manager.current = 'family_saving'

class SavingsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(FamilySavingScreen(name='family_saving'))
        return sm

if __name__ == '__main__':
    SavingsApp().run()
