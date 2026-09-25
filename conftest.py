import os
import datetime
import pytest

try:
    import pyautogui
except ImportError:
    pyautogui = None

try:
    import allure
except ImportError:
    allure = None


@pytest.fixture(scope="session", autouse=True)
def ensure_logs_dir():
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    return logs_dir


def capture_test_evidence(item, report):
    """Salva uma evidência final do monitor do PC em logs/ e anexa ao Allure."""
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    if report.passed:
        status = "PASS"
    elif report.failed:
        status = "FAIL"
    else:
        status = "SKIP"

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_name = item.name
    screenshot_filename = f"{status}_{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(logs_dir, screenshot_filename)

    if pyautogui is not None:
        try:
            pyautogui.screenshot(screenshot_path)
        except Exception as e:
            print(f"\n[ERRO PyAutoGUI] Não foi possível capturar o monitor: {e}")

            driver = getattr(item.instance, "driver", None) if hasattr(item, "instance") else None
            if driver is not None:
                try:
                    driver.save_screenshot(screenshot_path)
                except Exception as driver_error:
                    print(f"\n[ERRO Selenium] Não foi possível capturar o navegador: {driver_error}")
    else:
        driver = getattr(item.instance, "driver", None) if hasattr(item, "instance") else None
        if driver is not None:
            try:
                driver.save_screenshot(screenshot_path)
            except Exception as e:
                print(f"\n[ERRO Selenium] Não foi possível capturar a tela do navegador: {e}")

    if allure is not None and os.path.exists(screenshot_path):
        try:
            allure.attach.file(
                screenshot_path,
                name=f"Evidência - {status} - {test_name}",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print(f"\n[ERRO Allure] Não foi possível anexar o screenshot ao Allure: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura a tela ao final de cada execução de teste e grava a evidência em logs/."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        capture_test_evidence(item, report)
