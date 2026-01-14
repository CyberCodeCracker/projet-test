"""
Configuration for Golden Fork Restaurant Test Suite
AI-Assisted Development: This configuration file was generated with AI assistance
"""
from datetime import datetime
import os
from pathlib import Path

class Config:
    """Configuration settings for the test suite"""
    
    # Application URLs
    FRONTEND_URL = "http://localhost:5181"
    BACKEND_URL = "http://localhost:5128"
    API_URL = f"{BACKEND_URL}/api"
    
    # Browser Settings
    BROWSER = "chrome"
    HEADLESS = False
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 30
    PAGE_LOAD_TIMEOUT = 60
    
    # Test Users
    TEST_CUSTOMER = {
        "email": "customer@test.com",
        "password": "Password123!"
    }
    
    TEST_ADMIN = {
        "email": "admin@restaurant.com",
        "password": "Admin123!"
    }
    
    TEST_CHEF = {
        "email": "chef@restaurant.com",
        "password": "Chef123!"
    }
    
    # Test Data
    TEST_MENU = {
        "name": "Test Menu " + os.urandom(4).hex(),
        "description": "Test menu description for automated testing"
    }
    
    TEST_CATEGORY = {
        "name": "Test Category " + os.urandom(4).hex(),
        "description": "Test category for automated testing"
    }
    
    TEST_ITEM = {
        "name": "Test Item " + os.urandom(4).hex(),
        "description": "Test item description",
        "price": 19.99,
        "category": "Main Course"
    }
    
    # Paths
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    SCREENSHOT_DIR = PROJECT_ROOT / "documentation" / "reports" / "screenshots"
    LOG_DIR = PROJECT_ROOT / "logs"
    TEST_DATA_DIR = PROJECT_ROOT / "src" / "data"
    
    # Test Execution
    RETRY_COUNT = 2
    TIMEOUT = 30
    SLOW_MO = 0.5  # seconds between actions
    
    @classmethod
    def setup_directories(cls):
        """Create necessary directories for test execution"""
        cls.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
        (cls.SCREENSHOT_DIR / "test_pass").mkdir(exist_ok=True)
        (cls.SCREENSHOT_DIR / "test_fail").mkdir(exist_ok=True)
        (cls.SCREENSHOT_DIR / "evidence").mkdir(exist_ok=True)
        cls.LOG_DIR.mkdir(parents=True, exist_ok=True)
        
    @classmethod
    def get_screenshot_path(cls, test_name, status="fail"):
        """Get path for saving screenshot"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.png"
        return cls.SCREENSHOT_DIR / status / filename