"""
Items Page Object Model
AI-Assisted Development: This file was generated with AI assistance
"""
from .base_page import BasePage
from selenium.webdriver.common.by import By
from utils.config import Config

class ItemsPage(BasePage):
    """Items page locators and actions"""
    
    # Locators
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'All Items')]")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search by name or description...']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(), 'Search')]")
    ADD_ITEM_BUTTON = (By.XPATH, "//button[contains(text(), 'Add New Item')]")
    ITEM_CARDS = (By.CLASS_NAME, "card")
    ITEM_NAMES = (By.CLASS_NAME, "card-title")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(), 'Add')]")
    VIEW_DETAILS_BUTTONS = (By.XPATH, "//button[contains(text(), 'Details')]")
    EDIT_ITEM_BUTTONS = (By.XPATH, "//button[contains(text(), 'Edit')]")
    DELETE_ITEM_BUTTONS = (By.XPATH, "//button[contains(text(), 'Delete')]")
    QUANTITY_INPUTS = (By.XPATH, "//input[@type='number']")
    CATEGORY_BADGES = (By.CLASS_NAME, "badge-secondary")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Config.FRONTEND_URL}/items"
    
    def navigate(self):
        """Navigate to items page"""
        self.driver.get(self.url)
        self.wait_for_url("/items")
    
    def search_items(self, search_term):
        """Search for items"""
        self.send_keys(self.SEARCH_INPUT, search_term)
        self.click(self.SEARCH_BUTTON)
    
    def get_item_count(self):
        """Get number of item cards"""
        try:
            cards = self.find_elements(self.ITEM_CARDS, timeout=5)
            return len(cards)
        except:
            return 0
    
    def add_first_item_to_cart(self, quantity=1):
        """Add first item to cart"""
        try:
            # Set quantity
            inputs = self.find_elements(self.QUANTITY_INPUTS)
            if inputs:
                inputs[0].clear()
                inputs[0].send_keys(str(quantity))
            
            # Click Add button
            buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
            if buttons:
                buttons[0].click()
                return True
        except:
            pass
        return False
    
    def view_first_item_details(self):
        """View details of first item"""
        try:
            buttons = self.find_elements(self.VIEW_DETAILS_BUTTONS)
            if buttons:
                buttons[0].click()
                return True
        except:
            pass
        return False