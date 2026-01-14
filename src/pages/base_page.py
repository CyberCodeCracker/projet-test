"""
Base Page Object Model class
AI-Assisted Development: This file was generated with AI assistance
"""
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.utils.config import Config

class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.timeout = Config.TIMEOUT
        
    def find_element(self, locator, timeout=None):
        """Find single element with wait"""
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator, timeout=None):
        """Find multiple elements with wait"""
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator, timeout=None):
        """Click on element with wait"""
        element = self.find_element(locator, timeout)
        element.click()
        sleep(Config.SLOW_MO)
    
    def send_keys(self, locator, text, timeout=None):
        """Send keys to element with wait"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        sleep(Config.SLOW_MO)
    
    def get_text(self, locator, timeout=None):
        """Get text from element"""
        element = self.find_element(locator, timeout)
        return element.text
    
    def is_displayed(self, locator, timeout=None):
        """Check if element is displayed"""
        try:
            element = self.find_element(locator, timeout)
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False
    
    def wait_for_url(self, url_part, timeout=None):
        """Wait for URL to contain specific part"""
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.url_contains(url_part))
    
    def take_screenshot(self, test_name, status="fail"):
        """Take screenshot of current page"""
        path = Config.get_screenshot_path(test_name, status)
        self.driver.save_screenshot(str(path))
        return path
    
    def execute_script(self, script, *args):
        """Execute JavaScript"""
        return self.driver.execute_script(script, *args)