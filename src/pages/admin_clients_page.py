"""
Admin Clients Page Object Model
AI-Assisted Development: This file was generated with AI assistance
"""
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.config import Config

class AdminClientsPage(BasePage):
    """Admin Clients Management page locators"""
    
    # Locators
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Manage Clients')]")
    CLIENTS_TABLE = (By.TAG_NAME, "table")
    CLIENT_ROWS = (By.XPATH, "//tbody/tr")
    ROLE_SELECTS = (By.XPATH, "//select[@class='select select-bordered']")
    UPDATE_ROLE_BUTTONS = (By.XPATH, "//button[contains(text(), 'Update Role')]")
    DELETE_USER_BUTTONS = (By.XPATH, "//button[contains(text(), 'Delete')]")
    CLIENT_NAMES = (By.XPATH, "//td[1]//div[contains(@class, 'font-bold')]")
    CLIENT_EMAILS = (By.XPATH, "//td[2]")
    ROLE_BADGES = (By.CLASS_NAME, "badge")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Config.FRONTEND_URL}/admin/clients"
    
    def navigate(self):
        """Navigate to admin clients page"""
        self.driver.get(self.url)
        self.wait_for_url("/admin/clients")
    
    def get_client_count(self):
        """Get number of clients in table"""
        try:
            rows = self.find_elements(self.CLIENT_ROWS, timeout=5)
            return len(rows)
        except:
            return 0
    
    def update_client_role(self, row_index, new_role):
        """Update role for client at specific row"""
        try:
            selects = self.find_elements(self.ROLE_SELECTS)
            if row_index < len(selects):
                select = Select(selects[row_index])
                select.select_by_visible_text(new_role)
                
                # Click update button
                buttons = self.find_elements(self.UPDATE_ROLE_BUTTONS)
                if row_index < len(buttons):
                    buttons[row_index].click()
                    return True
        except:
            pass
        return False
    
    def get_client_role(self, row_index):
        """Get current role of client"""
        try:
            badges = self.find_elements(self.ROLE_BADGES)
            if row_index < len(badges):
                return badges[row_index].text
        except:
            pass
        return None