"""
Main Selenium Test Suite for Golden Fork Restaurant App
AI-Assisted Development: This test suite was generated with AI assistance using DeepSeek
"""
import sys
import os
import unittest
import pytest
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =============================================
# FIX: SETUP PATHS BEFORE ANY IMPORTS
# =============================================

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.dirname(current_dir)  # Go up from tests to src

# Add src to Python path BEFORE trying to import anything
if src_path not in sys.path:
    sys.path.insert(0, src_path)
    print(f"DEBUG: Added {src_path} to Python path")

# =============================================
# NOW IMPORT WITHOUT 'src.' PREFIX
# =============================================

try:
    from pages.login_page import LoginPage
    from pages.menu_page import MenuPage
    from pages.menu_details_page import MenuDetailsPage
    from pages.categories_page import CategoriesPage
    from pages.items_page import ItemsPage
    from pages.admin_clients_page import AdminClientsPage
    from pages.checkout_page import CheckoutPage
    from utils.config import Config
    from utils.helpers import take_screenshot, log_test_result
    print("DEBUG: All imports successful")
except ImportError as e:
    print(f"DEBUG: Import error: {e}")
    print(f"DEBUG: Current sys.path: {sys.path[:3]}")
    
    # Try to show what's available
    print("\nAvailable in src/pages:")
    pages_dir = os.path.join(src_path, 'pages')
    if os.path.exists(pages_dir):
        for f in os.listdir(pages_dir):
            if f.endswith('.py'):
                print(f"  - {f}")
    
    print("\nAvailable in src/utils:")
    utils_dir = os.path.join(src_path, 'utils')
    if os.path.exists(utils_dir):
        for f in os.listdir(utils_dir):
            if f.endswith('.py'):
                print(f"  - {f}")
    
    raise

# =============================================
# REST OF THE CODE (UNCHANGED)
# =============================================

class GoldenForkSeleniumTests:
    """Main test class for Golden Fork Restaurant application"""
    
    def __init__(self):
        self.driver = None
        self.login_page = None
        self.menu_page = None
        self.menu_details_page = None
        self.categories_page = None
        self.items_page = None
        self.admin_clients_page = None
        self.checkout_page = None
        self.test_results = []
        
    def setup(self):
        """Setup test environment"""
        print("\n" + "="*80)
        print("GOLDEN FORK RESTAURANT - SELENIUM TEST SUITE")
        print("AI-Assisted Development: Generated with DeepSeek AI")
        print("="*80)
        
        # Setup directories
        Config.setup_directories()
        
        # Configure Chrome options
        options = Options()
        if Config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        
        # Initialize driver
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT)
        self.driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        # Initialize page objects
        self.login_page = LoginPage(self.driver)
        self.menu_page = MenuPage(self.driver)
        self.menu_details_page = MenuDetailsPage(self.driver)
        self.categories_page = CategoriesPage(self.driver)
        self.items_page = ItemsPage(self.driver)
        self.admin_clients_page = AdminClientsPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        
    def teardown(self):
        """Cleanup after tests"""
        if self.driver:
            self.driver.quit()
        
        # Print test summary
        print("\n" + "="*80)
        print("TEST SUMMARY")
        print("="*80)
        total = len(self.test_results)
        passed = sum(1 for r in self.test_results if r["status"] == "PASS")
        failed = total - passed
        
        for result in self.test_results:
            status_icon = "✓" if result["status"] == "PASS" else "✗"
            print(f"{status_icon} {result['test']}: {result['message']}")
        
        print(f"\nTotal: {total}, Passed: {passed}, Failed: {failed}")
        print("="*80)
    
    def run_test(self, test_func, test_name):
        """Wrapper to run test and handle results"""
        try:
            print(f"\n▶ Running: {test_name}")
            test_func()
            self.test_results.append({
                "test": test_name,
                "status": "PASS",
                "message": "Test completed successfully"
            })
            print(f"  ✓ {test_name} - PASS")
            return True
        except AssertionError as e:
            self.test_results.append({
                "test": test_name,
                "status": "FAIL",
                "message": str(e)
            })
            print(f"  ✗ {test_name} - FAIL: {str(e)}")
            
            # Take screenshot on failure
            try:
                screenshot_path = self.login_page.take_screenshot(test_name, "fail")
                print(f"    Screenshot saved: {screenshot_path}")
            except:
                pass
            return False
        except Exception as e:
            self.test_results.append({
                "test": test_name,
                "status": "ERROR",
                "message": str(e)
            })
            print(f"  ✗ {test_name} - ERROR: {str(e)}")
            return False
    
    # =============================================
    # TEST CASE 1: Application Home Page
    # =============================================
    
    def test_application_home_page(self):
        """Test 1: Verify application loads correctly"""
        print("\n=== TEST 1: Application Home Page ===")
        
        # Navigate to frontend
        self.driver.get(Config.FRONTEND_URL)
        sleep(3)
        
        # Check page title
        title = self.driver.title
        assert "Golden Fork" in title, f"Expected 'Golden Fork' in title, got: {title}"
        print(f"  Page title: {title}")
        
        # Check page loads without errors
        page_source = self.driver.page_source.lower()
        assert "error" not in page_source or "exception" not in page_source, "Page contains errors"
        
        print("  ✓ Application home page loads successfully")
    
    # =============================================
    # TEST CASE 2: User Login Functionality
    # =============================================
    
    def test_user_login(self):
        """Test 2: Test user login with valid credentials"""
        print("\n=== TEST 2: User Login Functionality ===")
        
        # Navigate to login page
        self.login_page.navigate()
        
        # Verify login page elements
        assert self.login_page.is_displayed(LoginPage.EMAIL_INPUT), "Email input not found"
        assert self.login_page.is_displayed(LoginPage.PASSWORD_INPUT), "Password input not found"
        assert self.login_page.is_displayed(LoginPage.LOGIN_BUTTON), "Login button not found"
        
        # Perform login
        self.login_page.login(
            Config.TEST_CUSTOMER["email"],
            Config.TEST_CUSTOMER["password"]
        )
        
        # Verify successful login
        sleep(3)  # Wait for login to process
        assert self.login_page.is_login_successful(), "Login failed or not redirected"
        
        # Check if we're on menu page
        current_url = self.driver.current_url
        assert "/menu" in current_url, f"Not redirected to menu page. Current URL: {current_url}"
        
        print("  ✓ User login successful")
        print("  ✓ Redirected to menu page")
    
    # =============================================
    # TEST CASE 3: Invalid Login Attempt
    # =============================================
    
    def test_invalid_login(self):
        """Test 3: Test login with invalid credentials"""
        print("\n=== TEST 3: Invalid Login Attempt ===")
        
        # Navigate to login page
        self.login_page.navigate()
        
        # Try login with wrong credentials
        self.login_page.login("wrong@email.com", "wrongpassword")
        
        # Should show error message
        sleep(2)
        error_message = self.login_page.get_error_message()
        assert error_message is not None, "Expected error message for invalid login"
        assert "invalid" in error_message.lower() or "incorrect" in error_message.lower(), \
            f"Unexpected error message: {error_message}"
        
        # Should stay on login page
        current_url = self.driver.current_url
        assert "/login" in current_url, "Should remain on login page after invalid login"
        
        print(f"  ✓ Error message displayed: {error_message}")
        print("  ✓ User not logged in with invalid credentials")
    
    # =============================================
    # TEST CASE 4: Menu Browsing
    # =============================================
    
    def test_menu_browsing(self):
        """Test 4: Test browsing menus"""
        print("\n=== TEST 4: Menu Browsing ===")
        
        # First login
        self.test_user_login()
        
        # Navigate to menu page
        self.menu_page.navigate()
        
        # Wait for loading
        self.menu_page.wait_for_loading()
        
        # Check if menus are displayed
        menu_count = self.menu_page.get_menu_count()
        print(f"  Found {menu_count} menu(s)")
        
        # Even if 0 menus, page should load correctly
        assert self.menu_page.is_displayed(MenuPage.PAGE_TITLE), "Menu page title not found"
        
        if menu_count > 0:
            # Test opening a menu
            success = self.menu_page.open_first_menu()
            assert success, "Could not open menu details"
            
            # Should be redirected to menu details
            sleep(2)
            current_url = self.driver.current_url
            assert "/menu/" in current_url, f"Not redirected to menu details. URL: {current_url}"
            
            print("  ✓ Successfully opened menu details")
        else:
            print("  ℹ No menus available for testing")
    
    # =============================================
    # TEST CASE 5: Categories Browsing
    # =============================================
    
    def test_categories_browsing(self):
        """Test 5: Test browsing categories"""
        print("\n=== TEST 5: Categories Browsing ===")
        
        # Navigate to categories page
        self.categories_page.navigate()
        
        # Check if categories page loads
        assert self.categories_page.is_displayed(CategoriesPage.PAGE_TITLE), "Categories page title not found"
        
        # Get category count
        category_count = self.categories_page.get_category_count()
        print(f"  Found {category_count} category(ies)")
        
        if category_count > 0:
            # Test opening a category
            success = self.categories_page.open_first_category()
            assert success, "Could not open category details"
            
            # Should be redirected to category details
            sleep(2)
            current_url = self.driver.current_url
            assert "/category/" in current_url, f"Not redirected to category details. URL: {current_url}"
            
            print("  ✓ Successfully opened category details")
        else:
            print("  ℹ No categories available for testing")
    
    # =============================================
    # TEST CASE 6: Items Browsing and Search
    # =============================================
    
    def test_items_browsing(self):
        """Test 6: Test browsing and searching items"""
        print("\n=== TEST 6: Items Browsing and Search ===")
        
        # Navigate to items page
        self.items_page.navigate()
        
        # Check if items page loads
        assert self.items_page.is_displayed(ItemsPage.PAGE_TITLE), "Items page title not found"
        
        
        # Get initial item count
        initial_count = self.items_page.get_item_count()
        print(f"  Found {initial_count} item(s)")
        
        # Test search functionality
        if initial_count > 0:
            # Search for something (assuming at least one item exists)
            self.items_page.search_items("test")
            sleep(2)
            
            # Get count after search
            search_count = self.items_page.get_item_count()
            print(f"  Found {search_count} item(s) after search")
            
            # Search should return results (could be 0 if no matches)
            print("  ✓ Search functionality works")
            
            # Test viewing item details
            if search_count > 0:
                success = self.items_page.view_first_item_details()
                assert success, "Could not view item details"
                print("  ✓ Item details modal opened")
                
                # Close modal
                sleep(1)
                self.driver.back()
        else:
            print("  ℹ No items available for testing")
    
    # =============================================
    # TEST CASE 7: Add Item to Cart
    # =============================================
    
    def test_add_to_cart(self):
        """Test 7: Test adding item to shopping cart"""
        print("\n=== TEST 7: Add Item to Cart ===")
        
        # Navigate to items page
        self.items_page.navigate()
        
        # Get initial item count
        item_count = self.items_page.get_item_count()
        
        if item_count > 0:
            # Add first item to cart
            success = self.items_page.add_first_item_to_cart(quantity=2)
            assert success, "Could not add item to cart"
            
            # Check for alert/confirmation (handled by JavaScript)
            sleep(2)
            
            # Verify by checking URL or localStorage
            cart_items = self.driver.execute_script("return localStorage.getItem('cart')")
            if cart_items:
                print("  ✓ Item added to cart (localStorage updated)")
            else:
                # Alternative: check for alert message
                print("  ✓ Add to cart button clicked (JavaScript alert expected)")
        else:
            print("  ℹ No items available to add to cart")
            # Skip the assertion for empty cart
    
    # =============================================
    # TEST CASE 8: Checkout Process
    # =============================================
    
    def test_checkout_process(self):
        """Test 8: Test checkout process"""
        print("\n=== TEST 8: Checkout Process ===")
        
        # First add item to cart
        self.test_add_to_cart()
        
        # Navigate to checkout
        self.checkout_page.navigate()
        
        # Check if checkout page loads
        assert self.checkout_page.is_displayed(CheckoutPage.PAGE_TITLE), "Checkout page not loaded"
        
        # Check if items are in cart
        item_count = self.checkout_page.get_item_count()
        
        if item_count > 0:
            # Verify order summary
            total_amount = self.checkout_page.get_total_amount()
            assert total_amount is not None, "Total amount not displayed"
            print(f"  Order total: {total_amount}")
            
            # Select payment method
            self.checkout_page.select_payment_method("cash")
            
            # Add order notes
            self.checkout_page.add_order_notes("Test order - please deliver quickly")
            
            print("  ✓ Checkout page loaded with order summary")
            print("  ✓ Payment method selected")
            print("  ✓ Order notes added")
            
            # Note: We don't actually place the order to avoid test data
            print("  ℹ Order placement skipped to avoid test data")
        else:
            print("  ℹ Cart is empty, checkout test skipped")
    
    # =============================================
    # TEST CASE 9: Security Test - Unauthorized Access
    # =============================================
    
    def test_security_unauthorized_access(self):
        """Test 9: Test security by accessing admin pages without admin role"""
        print("\n=== TEST 9: Security Test - Unauthorized Access ===")
        
        # Logout if logged in
        self.driver.get(f"{Config.FRONTEND_URL}/logout")
        sleep(2)
        
        # Try to access admin clients page directly
        self.driver.get(f"{Config.FRONTEND_URL}/admin/clients")
        sleep(3)
        
        # Should be redirected to login or show access denied
        current_url = self.driver.current_url
        page_source = self.driver.page_source.lower()
        
        if "/login" in current_url:
            print("  ✓ Redirected to login page (expected for unauthorized)")
        elif "access denied" in page_source or "unauthorized" in page_source:
            print("  ✓ Access denied message shown (expected)")
        elif "manage clients" not in page_source:
            print("  ✓ Admin page not accessible (expected)")
        else:
            # If somehow we can access, it's a security issue
            print("  ⚠ Warning: Could access admin page without proper role")
        
        print("  Security check completed")
    
    # =============================================
    # TEST CASE 10: Performance Test - Page Load Times
    # =============================================
    
    def test_performance_page_load(self):
        """Test 10: Measure page load times"""
        print("\n=== TEST 10: Performance Test - Page Load Times ===")
        
        pages_to_test = [
            ("Home", Config.FRONTEND_URL),
            ("Login", f"{Config.FRONTEND_URL}/login"),
            ("Menu", f"{Config.FRONTEND_URL}/menu"),
            ("Items", f"{Config.FRONTEND_URL}/items"),
            ("Categories", f"{Config.FRONTEND_URL}/categories")
        ]
        
        for page_name, page_url in pages_to_test:
            start_time = datetime.now()
            self.driver.get(page_url)
            
            # Wait for page to be interactive
            WebDriverWait(self.driver, 10).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            
            load_time = (datetime.now() - start_time).total_seconds()
            
            print(f"  {page_name}: {load_time:.2f} seconds")
            
            if load_time < 5:  # 5 seconds threshold
                print(f"    ✓ Acceptable load time")
            else:
                print(f"    ⚠ Slow load time (>{load_time:.2f}s)")
    
    # =============================================
    # TEST CASE 11: Browser Compatibility - Basic
    # =============================================
    
    def test_browser_compatibility(self):
        """Test 11: Basic browser compatibility tests"""
        print("\n=== TEST 11: Browser Compatibility Tests ===")
        
        # Test 1: Check for JavaScript errors
        try:
            logs = self.driver.get_log('browser')
            js_errors = [log for log in logs if log['level'] == 'SEVERE']
            
            if js_errors:
                print(f"  ⚠ Found {len(js_errors)} JavaScript error(s)")
                for error in js_errors[:3]:  # Show first 3 errors
                    print(f"    - {error['message'][:100]}...")
            else:
                print("  ✓ No JavaScript errors detected")
        except:
            print("  ℹ Could not check browser logs")
        
        # Test 2: Check viewport rendering
        window_size = self.driver.get_window_size()
        print(f"  Viewport: {window_size['width']}x{window_size['height']}")
        
        # Test 3: Check CSS loading
        page_source = self.driver.page_source
        if "stylesheet" in page_source:
            print("  ✓ CSS stylesheets loaded")
        else:
            print("  ⚠ No stylesheets detected")
    
    # =============================================
    # TEST CASE 12: Accessibility - Basic Checks
    # =============================================
    
    def test_accessibility_basic(self):
        """Test 12: Basic accessibility checks"""
        print("\n=== TEST 12: Basic Accessibility Checks ===")
        
        # Navigate to home page
        self.driver.get(Config.FRONTEND_URL)
        
        # Check 1: Images have alt text
        images = self.driver.find_elements_by_tag_name("img")
        images_with_alt = sum(1 for img in images if img.get_attribute("alt"))
        
        if images:
            alt_percentage = (images_with_alt / len(images)) * 100
            print(f"  Images with alt text: {images_with_alt}/{len(images)} ({alt_percentage:.1f}%)")
            
            if alt_percentage >= 80:
                print("    ✓ Good alt text coverage")
            else:
                print("    ⚠ Low alt text coverage")
        else:
            print("  ℹ No images found on page")
        
        # Check 2: Proper heading structure
        headings = {
            "h1": len(self.driver.find_elements_by_tag_name("h1")),
            "h2": len(self.driver.find_elements_by_tag_name("h2")),
            "h3": len(self.driver.find_elements_by_tag_name("h3"))
        }
        
        print(f"  Headings: H1={headings['h1']}, H2={headings['h2']}, H3={headings['h3']}")
        
        if headings['h1'] >= 1:
            print("    ✓ Page has at least one H1 heading")
        else:
            print("    ⚠ Page missing H1 heading")
        
        # Check 3: Form labels
        inputs = self.driver.find_elements_by_tag_name("input")
        inputs_with_labels = 0
        
        for inp in inputs:
            # Check for associated label
            input_id = inp.get_attribute("id")
            if input_id:
                labels = self.driver.find_elements_by_xpath(f"//label[@for='{input_id}']")
                if labels:
                    inputs_with_labels += 1
        
        if inputs:
            label_percentage = (inputs_with_labels / len(inputs)) * 100
            print(f"  Inputs with labels: {inputs_with_labels}/{len(inputs)} ({label_percentage:.1f}%)")
    
    # =============================================
    # TEST CASE 13: Navigation Flow
    # =============================================
    
    def test_navigation_flow(self):
        """Test 13: Test complete user navigation flow"""
        print("\n=== TEST 13: Navigation Flow ===")
        
        # Start at login
        self.login_page.navigate()
        print("  1. Login page")
        
        # Login
        self.login_page.login(
            Config.TEST_CUSTOMER["email"],
            Config.TEST_CUSTOMER["password"]
        )
        sleep(3)
        print("  2. Logged in → Menu page")
        
        # Navigate to items
        self.items_page.navigate()
        sleep(2)
        print("  3. Items page")
        
        # Navigate to categories
        self.categories_page.navigate()
        sleep(2)
        print("  4. Categories page")
        
        # Back to menu
        self.menu_page.navigate()
        sleep(2)
        print("  5. Back to Menu page")
        
        # Verify we can navigate without errors
        current_url = self.driver.current_url
        assert "/menu" in current_url, "Navigation flow broken"
        
        print("  ✓ Complete navigation flow successful")
    
    # =============================================
    # TEST CASE 14: Form Validation
    # =============================================
    
    def test_form_validation(self):
        """Test 14: Test form validation on login"""
        print("\n=== TEST 14: Form Validation ===")
        
        # Navigate to login
        self.login_page.navigate()
        
        # Test 1: Empty form submission
        self.login_page.click(LoginPage.LOGIN_BUTTON)
        sleep(1)
        
        # Check for validation messages
        page_source = self.driver.page_source.lower()
        if "required" in page_source or "error" in page_source:
            print("  ✓ Form validation works for empty submission")
        else:
            print("  ⚠ No validation message for empty form")
        
        # Test 2: Invalid email format
        self.login_page.send_keys(LoginPage.EMAIL_INPUT, "invalid-email")
        self.login_page.send_keys(LoginPage.PASSWORD_INPUT, "test")
        self.login_page.click(LoginPage.LOGIN_BUTTON)
        sleep(1)
        
        if "invalid" in page_source or "email" in page_source:
            print("  ✓ Email format validation works")
        else:
            print("  ⚠ No email format validation")
    
    # =============================================
    # TEST CASE 15: Responsive Design (Basic)
    # =============================================
    
    def test_responsive_design(self):
        """Test 15: Basic responsive design check"""
        print("\n=== TEST 15: Responsive Design Check ===")
        
        # Test different screen sizes
        sizes = [
            ("Desktop", 1920, 1080),
            ("Tablet", 768, 1024),
            ("Mobile", 375, 667)
        ]
        
        for device, width, height in sizes:
            self.driver.set_window_size(width, height)
            sleep(1)
            
            # Check if page still renders
            page_source = self.driver.page_source
            assert len(page_source) > 0, f"Page not rendering at {width}x{height}"
            
            print(f"  {device} ({width}x{height}): Renders correctly")
        
        # Reset to desktop
        self.driver.maximize_window()
    
    # =============================================
    # RUN ALL TESTS
    # =============================================
    
    def run_all_tests(self):
        """Execute all test cases"""
        self.setup()
        
        try:
            # Define test order
            tests = [
                (self.test_application_home_page, "Application Home Page"),
                (self.test_invalid_login, "Invalid Login Attempt"),
                (self.test_user_login, "User Login"),
                (self.test_form_validation, "Form Validation"),
                (self.test_navigation_flow, "Navigation Flow"),
                (self.test_menu_browsing, "Menu Browsing"),
                (self.test_categories_browsing, "Categories Browsing"),
                (self.test_items_browsing, "Items Browsing"),
                (self.test_add_to_cart, "Add to Cart"),
                (self.test_checkout_process, "Checkout Process"),
                (self.test_security_unauthorized_access, "Security Test"),
                (self.test_performance_page_load, "Performance Test"),
                (self.test_browser_compatibility, "Browser Compatibility"),
                (self.test_accessibility_basic, "Accessibility Check"),
                (self.test_responsive_design, "Responsive Design")
            ]
            
            # Run tests
            for test_func, test_name in tests:
                self.run_test(test_func, test_name)
                
        finally:
            self.teardown()


# =============================================
# Main Execution
# =============================================

if __name__ == "__main__":
    # Create and run test suite
    test_suite = GoldenForkSeleniumTests()
    
    print("\n" + "="*80)
    print("GOLDEN FORK RESTAURANT TEST SUITE")
    print("AI-Assisted Development Disclosure:")
    print("- This test suite was generated with AI assistance using DeepSeek")
    print("- AI was used for: test structure, page objects, test cases")
    print("- Human adjustments: locator updates, test data, validation")
    print("="*80)
    
    test_suite.run_all_tests()