from pathlib import Path

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = f"file://{Path(__file__).resolve().parents[1] / 'login.html'}"

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def open(self):
        return super().open(self.URL)

    def enter_username(self, username):
        return self.fill(By.ID, "username", username)

    def enter_password(self, password):
        return self.fill(By.ID, "password", password)

    def click_login_button(self):
        return self.click(By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return True

    def is_login_successful(self):
        message = self.wait.until(lambda d: d.find_element(By.ID, "message"))
        return "Login realizado com sucesso" in message.text

    def is_error_message_displayed(self):
        message = self.wait.until(lambda d: d.find_element(By.ID, "message"))
        return "Credenciais inválidas" in message.text or "Preencha usuário e senha" in message.text
