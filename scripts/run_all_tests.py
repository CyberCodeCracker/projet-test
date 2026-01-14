#!/usr/bin/env python3
"""
Main test runner for Golden Fork Restaurant Tests
AI-Assisted Development: This script was generated with AI assistance
"""
import sys
import os
import traceback

print("="*80)
print("GOLDEN FORK RESTAURANT TEST RUNNER")
print("="*80)

# Get absolute paths
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)  # projet-test folder
src_path = os.path.join(project_root, 'src')

print(f"Script location: {current_dir}")
print(f"Project root: {project_root}")
print(f"Src path: {src_path}")

# Verify src exists
if not os.path.exists(src_path):
    print(f"❌ ERROR: src folder not found at {src_path}")
    sys.exit(1)

print(f"✅ Src folder found")

# Add src to Python path - THIS IS CRITICAL
sys.path.insert(0, src_path)
print(f"✅ Added to Python path: {src_path}")

print(f"\nPython will search for modules in these locations:")
for i, path in enumerate(sys.path[:3], 1):
    print(f"  {i}. {path}")

print("\n" + "="*80)
print("ATTEMPTING IMPORTS")
print("="*80)

# IMPORTANT: Now we can import WITHOUT 'src.' prefix
# Because src folder is in the path, Python will find tests module inside it

try:
    # Test 1: Try importing config first
    print("1. Testing import of utils.config...")
    from utils.config import Config
    print("   ✅ utils.config imported successfully")
    
    # Test 2: Try importing selenium tests
    print("\n2. Testing import of tests.selenium_tests...")
    from tests.selenium_tests import GoldenForkSeleniumTests
    print("   ✅ tests.selenium_tests imported successfully")
    
    # Test 3: Try importing unit tests
    print("\n3. Testing import of tests.unit_tests...")
    from tests.unit_tests import TestGoldenForkAPI
    print("   ✅ tests.unit_tests imported successfully")
    
except ImportError as e:
    print(f"\n❌ IMPORT ERROR: {e}")
    print("\nTroubleshooting info:")
    print(f"Current sys.path: {sys.path[:3]}")
    print(f"Files in src folder: {os.listdir(src_path)}")
    
    if 'tests' in os.listdir(src_path):
        print(f"\nContents of src/tests:")
        for item in os.listdir(os.path.join(src_path, 'tests')):
            print(f"  - {item}")
    
    print("\nAvailable modules in src/tests:")
    tests_dir = os.path.join(src_path, 'tests')
    for file in os.listdir(tests_dir):
        if file.endswith('.py') and file != '__init__.py':
            module_name = file[:-3]  # Remove .py
            print(f"  - {module_name}")
    
    sys.exit(1)

print("\n" + "="*80)
print("IMPORTS SUCCESSFUL - STARTING TESTS")
print("="*80)

def run_unit_tests():
    """Run API unit tests"""
    print("\n" + "="*80)
    print("RUNNING API UNIT TESTS")
    print("="*80)
    
    try:
        api_tests = TestGoldenForkAPI()
        api_tests.run_all_tests()
    except Exception as e:
        print(f"❌ Error in unit tests: {e}")
        traceback.print_exc()

def run_selenium_tests():
    """Run Selenium tests"""
    print("\n" + "="*80)
    print("RUNNING SELENIUM TESTS")
    print("="*80)
    
    try:
        # Create screenshots directory
        os.makedirs("screenshots/pass", exist_ok=True)
        os.makedirs("screenshots/fail", exist_ok=True)
        os.makedirs("logs", exist_ok=True)
        
        test_suite = GoldenForkSeleniumTests()
        test_suite.run_all_tests()
    except Exception as e:
        print(f"❌ Error in Selenium tests: {e}")
        traceback.print_exc()

def generate_report():
    """Generate test report"""
    print("\n" + "="*80)
    print("GENERATING TEST REPORT")
    print("="*80)
    
    import datetime
    report = f"""
Golden Fork Restaurant - Test Report
Generated: {datetime.datetime.now()}

AI ASSISTANCE DISCLOSURE:
- This test suite was developed with AI assistance using DeepSeek
- AI was used for: test structure, page objects, test cases
- Human contributions: business logic, validation, adjustments

TEST EXECUTION SUMMARY:
- API Tests: Executed
- Selenium Tests: Executed
- Test artifacts saved in screenshots/ and logs/ folders

NEXT STEPS:
1. Review test results in console output
2. Check screenshots for failed tests
3. Update test data for your production environment
"""
    
    os.makedirs("documentation/reports", exist_ok=True)
    report_path = "documentation/reports/test_report.md"
    with open(report_path, "w") as f:
        f.write(report)
    
    print(f"Report generated: {report_path}")

def main():
    """Main function"""
    try:
        # Create necessary directories
        os.makedirs("documentation/reports/screenshots", exist_ok=True)
        os.makedirs("logs", exist_ok=True)
        
        # Run tests
        run_unit_tests()
        run_selenium_tests()
        
        # Generate report
        generate_report()
        
        print("\n" + "="*80)
        print("ALL TESTS COMPLETED")
        print("="*80)
        
    except Exception as e:
        print(f"\n❌ Error running tests: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()