"""
Centralized locators for the application
"""

class LoginLocators:
    USERNAME_INPUT = ("id", "username")
    PASSWORD_INPUT = ("id", "password")
    LOGIN_BUTTON = ("id", "login-button")
    REGISTER_LINK = ("link text", "Register")
    ERROR_MESSAGE = ("class name", "error-message")

class MenuLocators:
    MENU_ITEMS = ("class name", "menu-item")
    ADD_TO_CART_BUTTONS = ("class name", "add-to-cart")
    ITEM_PRICES = ("class name", "item-price")
    CATEGORY_FILTER = ("id", "category-filter")
    SEARCH_INPUT = ("id", "menu-search")

class CartLocators:
    CART_ITEMS = ("class name", "cart-item")
    REMOVE_BUTTONS = ("class name", "remove-item")
    QUANTITY_INPUTS = ("class name", "quantity-input")
    TOTAL_PRICE = ("id", "total-price")
    CHECKOUT_BUTTON = ("id", "checkout-button")
    EMPTY_CART_MESSAGE = ("id", "empty-cart-message")

class CheckoutLocators:
    NAME_INPUT = ("id", "name")
    ADDRESS_INPUT = ("id", "address")
    PHONE_INPUT = ("id", "phone")
    PAYMENT_METHOD = ("id", "payment-method")
    PLACE_ORDER_BUTTON = ("id", "place-order")
    ORDER_CONFIRMATION = ("id", "order-confirmation")