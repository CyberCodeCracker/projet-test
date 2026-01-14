import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.utils.config import Config

@pytest.fixture(scope="session")
def setup():
    """Setup test environment"""
    Config.setup_directories()
    print("Test environment setup complete")

@pytest.fixture(scope="function")
def driver():
    """Create WebDriver instance"""
    options = Options()
    if Config.HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.maximize_window()
    
    yield driver
    
    # Teardown
    driver.quit()

@pytest.fixture
def api_client():
    """Create API test client"""
    import requests
    session = requests.Session()
    session.headers.update({'Content-Type': 'application/json'})
    return session