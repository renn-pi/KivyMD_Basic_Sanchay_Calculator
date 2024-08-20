from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDToolbar

KV = '''
<FamilySavingScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Family Saving Certificate"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(50)
            spacing: dp(10)
            MDTextField:
                id: amount_input
                hint_text: 'Enter deposit amount'
                input_filter: 'int'
                mode: "rectangle"
            MDRaisedButton:
                text: "Calculate Interest"
                size_hint_y: None
                height: dp(50)
                on_release: root.calculate_interest()
            MDLabel:
                id: result_label
                size_hint_y: None
                height: dp(200)
                halign: 'center'
                
<InterestCalculatorMenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Interest Calculator"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(40)
            spacing: dp(20)
            MDRaisedButton:
                text: "Family Saving Certificate"
                size_hint_y: None
                height: dp(50)
                on_release: root.go_to_family_saving()
            MDRaisedButton:
                text: "Five-Year BD Saving Certificate"
                size_hint_y: None
                height: dp(50)
                on_release: root.go_to_five_year_saving()
            MDRaisedButton:
                text: "Three-Month Profit-Bearing Certificate"
                size_hint_y: None
                height: dp(50)
                on_release: root.go_to_profit_bearing()
            MDRaisedButton:
                text: "Pensioner Saving Certificate"
                size_hint_y: None
                height: dp(50)
                on_release: root.go_to_pensioner_saving()

<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Sanchay App"
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(50)
            spacing: dp(10)
            MDLabel:
                text: "Welcome to Sanchay App!"
                halign: 'center'
                font_style: 'H5'
            MDRaisedButton:
                text: "Interest Calculator"
                size_hint_y: None
                height: dp(50)
                on_release: root.go_to_interest_calculator()
            MDRaisedButton:
                text: "Saving Schemes"
                size_hint_y: None
                height: dp(50)
            MDRaisedButton:
                text: "Locations"
                size_hint_y: None
                height: dp(50)
'''

class FamilySavingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_interest(self):
        amount_input = self.ids.amount_input
        result_label = self.ids.result_label
        try:
            amount = int(amount_input.text)
            result = self.calculate_family_saving_interest(amount)
            result_label.text = result
        except ValueError:
            result_label.text = "Invalid input. Please enter a valid amount."

    def calculate_family_saving_interest(self, amount):
        def calculate_interest_family(amount, rate):
            yearly = amount * rate
            monthly = yearly / 12
            rate_src = .05 if amount <= 500000 else .10
            tax = monthly * rate_src
            interest = monthly - tax
            return interest

        first_half_interest = calculate_interest_family(1500000, .1152)
        second_half_interest = calculate_interest_family(1500000, .1050)

        if amount <= 500000:
            rate = .1152
            return f"Receive interest per month: {calculate_interest_family(amount, rate)}"
        elif amount <= 1500000:
            rate = .1152
            return f"Receive interest per month: {calculate_interest_family(amount, rate)}"
        elif amount <= 3000000:
            rate = .1050
            rest = amount - 1500000
            second_interest = calculate_interest_family(rest, rate)
            total_interest = first_half_interest + second_interest
            return (f"Receive interest on the first 1,500,000 taka: {first_half_interest}\n"
                    f"Receive interest on the rest {rest} taka: {second_interest}\n"
                    f"Total interest per month: {total_interest}")
        elif amount <= 4500000:
            rate = .0950
            rest_over = amount - 3000000
            third_interest = calculate_interest_family(rest_over, rate)
            total_interest = first_half_interest + second_half_interest + third_interest
            return (f"Receive interest on the first 1,500,000 taka: {first_half_interest}\n"
                    f"Receive interest on the second 1,500,000 taka: {second_half_interest}\n"
                    f"Receive interest on the rest {rest_over} taka: {third_interest}\n"
                    f"Total interest per month: {total_interest}")
        else:
            return ("Individual deposit amount exceeded for this scheme (family saving certificate).\n"
                    "Please input any amount up to 4,500,000 taka for Family Savings Certificate and try again.")

    def go_back(self):
        self.manager.current = 'interest_calculator_menu'

class InterestCalculatorMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def go_to_family_saving(self):
        self.manager.current = 'family_saving'

    def go_to_five_year_saving(self):
        self.manager.current = 'five_year_saving'

    def go_to_profit_bearing(self):
        self.manager.current = 'profit_bearing'

    def go_to_pensioner_saving(self):
        self.manager.current = 'pensioner_saving'

    def go_back(self):
        self.manager.current = 'main'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def go_to_interest_calculator(self):
        self.manager.current = 'interest_calculator_menu'

class SavingsApp(MDApp):
    def build(self):
        Builder.load_string(KV)
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(InterestCalculatorMenuScreen(name='interest_calculator_menu'))
        sm.add_widget(FamilySavingScreen(name='family_saving'))
        sm.add_widget(Screen(name='five_year_saving'))
        sm.add_widget(Screen(name='profit_bearing'))
        sm.add_widget(Screen(name='pensioner_saving'))
        return sm

if __name__ == '__main__':
    SavingsApp().run()
