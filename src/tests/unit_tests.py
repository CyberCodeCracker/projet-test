"""
Unit Tests for Golden Fork Restaurant API
AI-Assisted Development: This test file was generated with AI assistance
"""
import os, sys

import pytest
import requests
import json
from datetime import datetime
from utils.config import Config

# Add src to Python path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.dirname(current_dir)  # Go up from tests to src
if src_path not in sys.path:
    sys.path.insert(0, src_path)
    print(f"DEBUG: Added {src_path} to Python path in unit_tests.py")

# Now import WITHOUT 'src.' prefix
try:
    from utils.config import Config
    print("DEBUG: Config imported successfully in unit_tests.py")
except ImportError as e:
    print(f"DEBUG: Import error in unit_tests.py: {e}")
    print(f"DEBUG: Current sys.path: {sys.path[:3]}")
    raise

class TestGoldenForkAPI:
    """Unit tests for REST API endpoints"""
    
    # Setup
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup for each test"""
        self.base_url = Config.API_URL
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    # =============================================
    # TEST 1: Menu API Endpoints
    # =============================================
    
    def test_get_menus(self):
        """Test retrieving menus"""
        print("\n=== UNIT TEST 1: Get Menus ===")
        response = requests.get(f"{self.base_url}/menu", headers=self.headers)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        data = response.json()
        assert isinstance(data, dict) or isinstance(data, list), "Response should be JSON object/array"
        
        print(f"  Status: {response.status_code}")
        if isinstance(data, dict) and 'items' in data:
            print(f"  Retrieved {len(data['items'])} menus")
        elif isinstance(data, list):
            print(f"  Retrieved {len(data)} menus")
    
    # =============================================
    # TEST 2: Categories API
    # =============================================
    
    def test_get_categories(self):
        """Test retrieving categories"""
        print("\n=== UNIT TEST 2: Get Categories ===")
        response = requests.get(f"{self.base_url}/category", headers=self.headers)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        data = response.json()
        assert isinstance(data, dict) or isinstance(data, list), "Invalid response format"
        
        print(f"  Status: {response.status_code}")
    
    # =============================================
    # TEST 3: Items API
    # =============================================
    
    def test_get_items(self):
        """Test retrieving items"""
        print("\n=== UNIT TEST 3: Get Items ===")
        response = requests.get(f"{self.base_url}/item", headers=self.headers)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        data = response.json()
        print(f"  Status: {response.status_code}")
    
    # =============================================
    # TEST 4: Error Handling - Invalid Endpoint
    # =============================================
    
    def test_invalid_endpoint(self):
        """Test error handling for invalid endpoint"""
        print("\n=== UNIT TEST 4: Invalid Endpoint ===")
        response = requests.get(f"{self.base_url}/invalid-endpoint", headers=self.headers)
        
        assert response.status_code == 404, f"Expected 404 for invalid endpoint, got {response.status_code}"
        print(f"  Status: {response.status_code} (Correctly returns 404)")
    
    # =============================================
    # TEST 5: API Health Check
    # =============================================
    
    def test_api_health(self):
        """Test API health/status"""
        print("\n=== UNIT TEST 5: API Health Check ===")
        
        # Try to access a simple endpoint
        response = requests.get(f"{self.base_url}/menu", headers=self.headers)
        
        assert response.status_code in [200, 401, 403], \
            f"API not responding properly. Status: {response.status_code}"
        
        print(f"  API Status: {response.status_code}")
        print("  ✓ API is responsive")
    
    # =============================================
    # TEST 6: Response Time Performance
    # =============================================
    
    def test_api_response_time(self):
        """Test API response time"""
        print("\n=== UNIT TEST 6: API Response Time ===")
        
        start_time = datetime.now()
        response = requests.get(f"{self.base_url}/menu", headers=self.headers)
        end_time = datetime.now()
        
        response_time = (end_time - start_time).total_seconds()
        
        print(f"  Response time: {response_time:.3f} seconds")
        
        if response_time < 2.0:
            print("  ✓ Response time acceptable (< 2s)")
        elif response_time < 5.0:
            print("  ⚠ Response time slow (2-5s)")
        else:
            print("  ✗ Response time very slow (> 5s)")
        
        # Still pass the test, just log warning
        assert response_time < 10.0, f"Response time too slow: {response_time:.3f}s"
    
    # =============================================
    # TEST 7: Content Type Validation
    # =============================================
    
    def test_content_type(self):
        """Test API returns correct content type"""
        print("\n=== UNIT TEST 7: Content Type Validation ===")
        
        response = requests.get(f"{self.base_url}/menu", headers=self.headers)
        
        content_type = response.headers.get('Content-Type', '')
        assert 'application/json' in content_type.lower(), \
            f"Expected JSON content type, got: {content_type}"
        
        print(f"  Content-Type: {content_type}")
        print("  ✓ Correct content type returned")
    
    # =============================================
    # RUN ALL UNIT TESTS
    # =============================================
    
    def run_all_tests(self):
        """Run all unit tests"""
        print("\n" + "="*80)
        print("GOLDEN FORK API UNIT TESTS")
        print("="*80)
        
        test_methods = [
            self.test_api_health,
            self.test_get_menus,
            self.test_get_categories,
            self.test_get_items,
            self.test_invalid_endpoint,
            self.test_api_response_time,
            self.test_content_type
        ]
        
        results = []
        for test in test_methods:
            try:
                test()
                results.append((test.__name__, "PASS", ""))
            except AssertionError as e:
                results.append((test.__name__, "FAIL", str(e)))
            except Exception as e:
                results.append((test.__name__, "ERROR", str(e)))
        
        # Print results
        print("\n" + "="*80)
        print("UNIT TEST RESULTS")
        print("="*80)
        
        for name, status, message in results:
            icon = "✓" if status == "PASS" else "✗"
            print(f"{icon} {name}: {status}")
            if message:
                print(f"    {message}")
        
        passed = sum(1 for r in results if r[1] == "PASS")
        total = len(results)
        
        print(f"\nTotal: {total}, Passed: {passed}, Failed: {total - passed}")
        print("="*80)


if __name__ == "__main__":
    # Run unit tests
    api_tests = TestGoldenForkAPI()
    api_tests.run_all_tests()