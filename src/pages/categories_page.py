"""
Categories Page Object Model
AI-Assisted Development: This file was generated with AI assistance
"""
from .base_page import BasePage
from selenium.webdriver.common.by import By
from utils.config import Config

class CategoriesPage(BasePage):
    """Categories page locators and actions"""
    
    # Locators
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Categories')]")
    ADD_CATEGORY_BUTTON = (By.XPATH, "//button[contains(text(), 'Add New Category')]")
    CATEGORY_CARDS = (By.CLASS_NAME, "card")
    CATEGORY_NAMES = (By.CLASS_NAME, "card-title")
    VIEW_DETAILS_BUTTONS = (By.XPATH, "//button[contains(text(), 'View Details')]")
    DELETE_CATEGORY_BUTTONS = (By.XPATH, "//button[contains(@class, 'text-red-600')]")
    MODAL_TITLE = (By.XPATH, "//h3[contains(text(), 'Add New Category')]")
    MODAL_NAME_INPUT = (By.XPATH, "//input[@placeholder='Name']")
    MODAL_DESCRIPTION_INPUT = (By.XPATH, "//textarea[@placeholder='Description']")
    MODAL_SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Add Category')]")
    PAGINATION_NEXT = (By.XPATH, "//button[contains(text(), 'Next')]")
    PAGINATION_PREV = (By.XPATH, "//button[contains(text(), 'Previous')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Config.FRONTEND_URL}/categories"
    
    def navigate(self):
        """Navigate to categories page"""
        self.driver.get(self.url)
        self.wait_for_url("/categories")
    
    def get_category_count(self):
        """Get number of category cards"""
        try:
            cards = self.find_elements(self.CATEGORY_CARDS, timeout=5)
            return len(cards)
        except:
            return 0
    
    def click_add_category(self):
        """Click Add New Category button"""
        self.click(self.ADD_CATEGORY_BUTTON)
    
    def fill_category_form(self, name, description=""):
        """Fill category form in modal"""
        self.send_keys(self.MODAL_NAME_INPUT, name)
        if description:
            self.send_keys(self.MODAL_DESCRIPTION_INPUT, description)
    
    def save_category(self):
        """Click save button in modal"""
        self.click(self.MODAL_SAVE_BUTTON)
    
    def open_first_category(self):
        """Open first category details"""
        buttons = self.find_elements(self.VIEW_DETAILS_BUTTONS)
        if buttons:
            buttons[0].click()
            return True
        return False
    
    def is_modal_visible(self):
        """Check if modal is visible"""
        return self.is_displayed(self.MODAL_TITLE)