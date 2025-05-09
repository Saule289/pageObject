import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Получение параметра языка из командной строки
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language")

# Фикстура для получения выбранного языка
@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("language")

# Фикстура для запуска браузера с нужным языком
@pytest.fixture(scope="function")
def browser(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    service = Service(ChromeDriverManager().install())
    print(f"\n[START] Launching Chrome with language: {language}")
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    print("\n[END] Quit browser")
    browser.quit()

# Фикстура для формирования URL с языком
@pytest.fixture(scope="function")
def product_url(language):
    return f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"