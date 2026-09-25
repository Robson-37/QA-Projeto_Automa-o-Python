import pytest
import allure
from selenium import webdriver

from pages.login_page import LoginPage


@allure.epic("Automação de Interface (GUI)")
@allure.feature("Módulo de Autenticação")
class TestLogin:
    """Suíte de testes para uma página fictícia de login."""

    @pytest.fixture(autouse=True)
    def setup_page(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1366,768")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=options)
        self.login_page = LoginPage(self.driver).open()
        yield
        self.driver.quit()

    @allure.story("Login com Sucesso")
    @allure.title("CT01 - Validar login com credenciais válidas")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_sucesso(self):
        with allure.step("1. Preencher credenciais válidas e efetuar login"):
            status_login = self.login_page.login(username="usuario_valido", password="SenhaSegura123")
            assert status_login, "Falha ao interagir com os campos da tela de login."

        with allure.step("2. Validar que o login foi realizado com sucesso"):
            assert self.login_page.is_login_successful(), "Elemento de confirmação de login com sucesso não foi localizado na tela."

    @allure.story("Login com Erro")
    @allure.title("CT02 - Validar login com senha incorreta")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_senha_invalida(self):
        with allure.step("1. Preencher credenciais com senha incorreta"):
            status_login = self.login_page.login(username="usuario_valido", password="SenhaErrada")
            assert status_login, "Falha ao interagir com os campos da tela de login."

        with allure.step("2. Validar se a mensagem de erro de autenticação é exibida"):
            assert self.login_page.is_error_message_displayed(), "Mensagem de erro de login não foi exibida para credenciais inválidas."

    @allure.story("Login com Erro")
    @allure.title("CT03 - Validar tentativa de login com usuário inexistente")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_usuario_inexistente(self):
        with allure.step("1. Informar usuário inexistente e tentar autenticar"):
            status_login = self.login_page.login(username="usuario_inexistente", password="Senha123")
            assert status_login, "Falha ao interagir com os campos da tela de login."

        with allure.step("2. Validar exibição do aviso de erro"):
            assert self.login_page.is_error_message_displayed(), "Aviso de erro não foi localizado na tela."

    @allure.story("Validação de Campos")
    @allure.title("CT04 - Validar submissão sem preencher senha")
    @allure.severity(allure.severity_level.MINOR)
    def test_login_apenas_usuario(self):
        with allure.step("1. Preencher apenas o campo de usuário"):
            assert self.login_page.enter_username("usuario_valido"), "Não foi possível interagir com o campo de usuário."

        with allure.step("2. Clicar diretamente no botão de login"):
            assert self.login_page.click_login_button(), "Não foi possível clicar no botão de login."

        with allure.step("3. Verificar se a validação/mensagem de erro é apresentada"):
            assert self.login_page.is_error_message_displayed(), "Erro esperado ao omitir a senha não foi exibido."
