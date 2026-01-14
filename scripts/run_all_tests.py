#!/usr/bin/env python3
"""
Main test runner for Golden Fork Restaurant Tests
AI-Assisted Development: This script was generated with AI assistance
"""
import sys
import os
import subprocess

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

def run_selenium_tests():
    """Run Selenium tests"""
    print("\n" + "="*80)
    print("RUNNING SELENIUM TESTS")
    print("="*80)
    
    from src.tests.selenium_tests import GoldenForkSeleniumTests
    test_suite = GoldenForkSeleniumTests()
    test_suite.run_all_tests()

def run_unit_tests():
    """Run API unit tests"""
    print("\n" + "="*80)
    print("RUNNING API UNIT TESTS")
    print("="*80)
    
    from src.tests.unit_tests import TestGoldenForkAPI
    api_tests = TestGoldenForkAPI()
    api_tests.run_all_tests()

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

TEST COVERAGE:
- Functional Tests: 10 test cases
- Security Tests: 2 test cases
- Performance Tests: 2 test cases
- Accessibility Tests: 1 test case
- Total: 15 test cases

REQUIREMENTS COVERED:
- User authentication
- Menu/Item browsing
- Shopping cart
- Checkout process
- Security controls
- Performance requirements
- Accessibility standards

NEXT STEPS:
1. Update locators based on actual HTML
2. Add test data for your environment
3. Configure test users
4. Run tests and adjust as needed
"""
    
    with open("test_report.md", "w") as f:
        f.write(report)
    
    print("Report generated: test_report.md")

def main():
    """Main function"""
    print("\n" + "="*80)
    print("GOLDEN FORK RESTAURANT TEST SUITE")
    print("="*80)
    
    # Create necessary directories
    os.makedirs("documentation/reports/screenshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    try:
        # Run tests
        run_unit_tests()
        run_selenium_tests()
        
        # Generate report
        generate_report()
        
        print("\n" + "="*80)
        print("ALL TESTS COMPLETED")
        print("="*80)
        
    except Exception as e:
        print(f"\nError running tests: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()