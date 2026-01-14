"""
Menu Details Page Object Model
AI-Assisted Development: This file was generated with AI assistance
"""
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.utils.config import Config

class MenuDetailsPage(BasePage):
    """Menu details page locators and actions"""
    
    # Locators
    MENU_TITLE = (By.XPATH, "//h1[contains(@class, 'text-orange-600')]")
    MENU_DESCRIPTION = (By.XPATH, "//p[contains(@class, 'text-gray-700')]")
    ADD_ITEMS_BUTTON = (By.XPATH, "//button[contains(text(), 'Add Items to Menu')]")
    ITEM_CARDS = (By.CLASS_NAME, "card")
    ITEM_NAMES = (By.CLASS_NAME, "card-title")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    VIEW_DETAILS_BUTTONS = (By.XPATH, "//button[contains(text(), 'Details')]")
    QUANTITY_INPUTS = (By.XPATH, "//input[@type='number']")
    BACK_TO_MENUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Back to Menus')]")
    ITEM_DETAILS_MODAL = (By.XPATH, "//h3[contains(@class, 'font-bold')]")
    ITEM_PRICE = (By.XPATH, "//strong[contains(text(), 'Price:')]/following-sibling::span")
    ITEM_CATEGORY = (By.XPATH, "//strong[contains(text(), 'Category:')]/following-sibling::span")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate(self, menu_id):
        """Navigate to specific menu details page"""
        url = f"{Config.FRONTEND_URL}/menu/{menu_id}"
        self.driver.get(url)
        self.wait_for_url(f"/menu/{menu_id}")
    
    def get_menu_title(self):
        """Get menu title"""
        return self.get_text(self.MENU_TITLE)
    
    def get_item_count(self):
        """Get number of items in menu"""
        try:
            cards = self.find_elements(self.ITEM_CARDS, timeout=5)
            return len(cards)
        except:
            return 0
    
    def click_add_items(self):
        """Click Add Items to Menu button"""
        self.click(self.ADD_ITEMS_BUTTON)
    
    def add_first_item_to_cart(self, quantity=1):
        """Add first item to cart with specified quantity"""
        try:
            # Set quantity if input exists
            inputs = self.find_elements(self.QUANTITY_INPUTS)
            if inputs:
                inputs[0].clear()
                inputs[0].send_keys(str(quantity))
            
            # Click Add to Cart button
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
                return self.is_displayed(self.ITEM_DETAILS_MODAL)
        except:
            pass
        return False
    
    def close_item_details(self):
        """Close item details modal"""
        # Click outside or close button
        self.execute_script("document.querySelector('.modal').style.display = 'none'")