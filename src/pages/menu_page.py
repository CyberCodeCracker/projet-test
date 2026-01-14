"""
Menu Page Object Model
AI-Assisted Development: This file was generated with AI assistance
"""
from .base_page import BasePage
from selenium.webdriver.common.by import By
from utils.config import Config

class MenuPage(BasePage):
    """Menu page locators and actions"""
    
    # Locators
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Our Menus')]")
    ADD_MENU_BUTTON = (By.XPATH, "//button[contains(text(), 'Add New Menu')]")
    MENU_CARDS = (By.CLASS_NAME, "card")
    MENU_NAMES = (By.CLASS_NAME, "card-title")
    VIEW_MENU_BUTTONS = (By.XPATH, "//a[contains(text(), 'View Menu')]")
    EDIT_MENU_BUTTONS = (By.XPATH, "//a[contains(text(), 'Edit')]")
    DELETE_MENU_BUTTONS = (By.XPATH, "//a[contains(@class, 'text-red-600')]")
    MODAL_TITLE = (By.XPATH, "//h3[contains(text(), 'Add New Menu') or contains(text(), 'Edit Menu')]")
    MODAL_NAME_INPUT = (By.XPATH, "//input[@placeholder='Name']")
    MODAL_DESCRIPTION_INPUT = (By.XPATH, "//textarea[@placeholder='Description']")
    MODAL_SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Save')]")
    MODAL_CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Cancel')]")
    LOADING_SPINNER = (By.CLASS_NAME, "loading-spinner")
    NO_MENUS_MESSAGE = (By.XPATH, "//p[contains(text(), 'No menus available yet')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Config.FRONTEND_URL}/menu"
    
    def navigate(self):
        """Navigate to menu page"""
        self.driver.get(self.url)
        self.wait_for_url("/menu")
    
    def get_menu_count(self):
        """Get number of menu cards displayed"""
        try:
            cards = self.find_elements(self.MENU_CARDS, timeout=5)
            return len(cards)
        except:
            return 0
    
    def click_add_menu(self):
        """Click Add New Menu button"""
        self.click(self.ADD_MENU_BUTTON)
    
    def fill_menu_form(self, name, description):
        """Fill menu form in modal"""
        self.send_keys(self.MODAL_NAME_INPUT, name)
        self.send_keys(self.MODAL_DESCRIPTION_INPUT, description)
    
    def save_menu(self):
        """Click save button in modal"""
        self.click(self.MODAL_SAVE_BUTTON)
    
    def cancel_menu(self):
        """Click cancel button in modal"""
        self.click(self.MODAL_CANCEL_BUTTON)
    
    def open_first_menu(self):
        """Click on first View Menu button"""
        buttons = self.find_elements(self.VIEW_MENU_BUTTONS)
        if buttons:
            buttons[0].click()
            return True
        return False
    
    def is_modal_visible(self):
        """Check if modal is visible"""
        return self.is_displayed(self.MODAL_TITLE)
    
    def wait_for_loading(self):
        """Wait for loading spinner to disappear"""
        try:
            self.wait.until(EC.invisibility_of_element_located(self.LOADING_SPINNER))
        except:
            pass