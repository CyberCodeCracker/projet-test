"""
Helper functions for test suite
AI-Assisted Development: This file was generated with AI assistance
"""
import time
from datetime import datetime
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def take_screenshot(driver, test_name, status="fail"):
    """Take screenshot and save with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    return filename

def log_test_result(test_name, status, message=""):
    """Log test result to file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | {test_name} | {status} | {message}\n"
    
    with open("test_results.log", "a") as f:
        f.write(log_entry)

def wait_for_element(driver, locator, timeout=30):
    """Wait for element to be present and visible"""
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element
    except TimeoutException:
        return None

def is_element_present(driver, locator, timeout=5):
    """Check if element is present within timeout"""
    try:
        wait_for_element(driver, locator, timeout)
        return True
    except:
        return False

def scroll_to_element(driver, element):
    """Scroll to element using JavaScript"""
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.5)

def get_element_text(driver, locator, default=""):
    """Get text from element with default if not found"""
    try:
        element = driver.find_element(*locator)
        return element.text
    except NoSuchElementException:
        return default

def execute_ajax_wait(driver, timeout=10):
    """Wait for AJAX calls to complete"""
    time.sleep(2)  # Initial wait
    try:
        driver.execute_script("return jQuery.active == 0")
    except:
        pass