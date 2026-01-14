"""
Login Page Object Model
AI-Assisted Development: This file was generated with AI assistance
"""
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.utils.config import Config

class LoginPage(BasePage):
    """Login page locators and actions"""
    
    # Locators
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='john@example.com']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @placeholder='••••••••']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login') or contains(text(), 'Logging in')]")
    ERROR_MESSAGE = (By.CLASS_NAME, "alert-error")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
    REGISTER_LINK = (By.LINK_TEXT, "Register here")
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Golden Fork')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Config.FRONTEND_URL}/login"
    
    def navigate(self):
        """Navigate to login page"""
        self.driver.get(self.url)
        self.wait_for_url("/login")
    
    def login(self, email, password):
        """Perform login with given credentials"""
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Get error message if login fails"""
        if self.is_displayed(self.ERROR_MESSAGE, timeout=5):
            return self.get_text(self.ERROR_MESSAGE)
        return None
    
    def get_success_message(self):
        """Get success message if login succeeds"""
        if self.is_displayed(self.SUCCESS_MESSAGE, timeout=5):
            return self.get_text(self.SUCCESS_MESSAGE)
        return None
    
    def is_login_successful(self):
        """Check if login was successful by checking redirect"""
        try:
            self.wait_for_url("/menu", timeout=10)
            return True
        except:
            return False
    
    def click_register_link(self):
        """Click on register link"""
        self.click(self.REGISTER_LINK)