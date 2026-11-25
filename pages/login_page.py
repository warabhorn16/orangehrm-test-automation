from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)


        self.username_input = page.get_by_role(
            'textbox', name='Username'
        )

        self.password_input = page.get_by_role(
            'textbox', name='Password'
        )

        self.login_button = page.get_by_role(
            'button', name='Login'
        )

        self.forgot_password = page.get_by_text(
            'Forgot your password?', exact=True
        )

        self.login_error = page.get_by_role(
            'alert'
        )

        self.username_validation_error = page.locator(
            '.oxd-input-group'
        ).filter(
            has=self.username_input
        ).locator(
            '.oxd-input-field-error-message'
        )

        self.password_validation_error = page.locator(
            '.oxd-input-group'
        ).filter(
            has=self.password_input
        ).locator(
            '.oxd-input-field-error-message'
        )



    def enter_username(self, username):
        self.fill(self.username_input, username)

    def enter_password(self, password):
        self.fill(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def press_enter(self):
        self.password_input.press('Enter')