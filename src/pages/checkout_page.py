"""
Checkout Page Object Model
AI-Assisted Development: This file was generated with AI assistance
"""
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.utils.config import Config

class CheckoutPage(BasePage):
    """Checkout page locators and actions"""
    
    # Locators
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Checkout')]")
    ORDER_ITEMS_TABLE = (By.TAG_NAME, "table")
    ORDER_ITEMS_ROWS = (By.XPATH, "//tbody/tr")
    SUBTOTAL = (By.XPATH, "//div[contains(text(), 'Subtotal')]/following-sibling::span")
    TOTAL = (By.XPATH, "//div[contains(text(), 'Total')]/following-sibling::span")
    CASH_RADIO = (By.XPATH, "//input[@value='cash']")
    CARD_RADIO = (By.XPATH, "//input[@value='card']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Place Order')]")
    CANCEL_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Cancel Order')]")
    ORDER_NOTES = (By.TAG_NAME, "textarea")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
    ERROR_MESSAGE = (By.CLASS_NAME, "alert-error")
    EMPTY_CART_MESSAGE = (By.XPATH, "//span[contains(text(), 'Your cart is empty')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Config.FRONTEND_URL}/orders/checkout"
    
    def navigate(self):
        """Navigate to checkout page"""
        self.driver.get(self.url)
        self.wait_for_url("/orders/checkout")
    
    def get_item_count(self):
        """Get number of items in order"""
        try:
            rows = self.find_elements(self.ORDER_ITEMS_ROWS, timeout=5)
            return len(rows)
        except:
            return 0
    
    def select_payment_method(self, method="cash"):
        """Select payment method"""
        if method.lower() == "cash":
            self.click(self.CASH_RADIO)
        else:
            self.click(self.CARD_RADIO)
    
    def add_order_notes(self, notes):
        """Add order notes"""
        self.send_keys(self.ORDER_NOTES, notes)
    
    def place_order(self):
        """Click Place Order button"""
        self.click(self.PLACE_ORDER_BUTTON)
    
    def cancel_order(self):
        """Click Cancel Order button"""
        self.click(self.CANCEL_ORDER_BUTTON)
    
    def get_total_amount(self):
        """Get total amount from page"""
        try:
            return self.get_text(self.TOTAL)
        except:
            return None
    
    def is_success_message_displayed(self):
        """Check if success message is displayed"""
        return self.is_displayed(self.SUCCESS_MESSAGE, timeout=10)