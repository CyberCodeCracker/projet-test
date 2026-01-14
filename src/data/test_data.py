"""
Test user data for authentication tests
"""

class Users:
    # Valid test users
    VALID_CUSTOMER = {
        "username": "souhailclient",
        "password": "Souhail123",
        "email": "client@gmail.com"
    }
    
    VALID_ADMIN = {
        "username": "souhail",
        "password": "Souhail123",
        "email": "souhail@gmail.com"
    }
    
    # Invalid users for negative testing
    INVALID_USERS = [
        {"username": "wronguser", "password": "password123"},
        {"username": "testuser", "password": "wrongpass"},
        {"username": "", "password": "password123"},
        {"username": "testuser", "password": ""}
    ]
    
    # SQL injection test cases
    SQL_INJECTION_CASES = [
        {"username": "' OR '1'='1", "password": "any"},
        {"username": "admin", "password": "' OR '1'='1"},
        {"username": "\"; DROP TABLE users; --", "password": "any"}
    ]