# Code Review Checklist

## General Code Quality
- [ ] Code follows PEP 8 style guide
- [ ] Functions and methods are properly documented
- [ ] No dead code or unused imports
- [ ] Meaningful variable and function names

## Test Code Specific
- [ ] Tests are independent and isolated
- [ ] Proper use of setup and teardown
- [ ] Assertions are clear and meaningful
- [ ] Error handling is appropriate
- [ ] Test data is properly managed

## Security
- [ ] No hardcoded sensitive information
- [ ] Input validation in tests
- [ ] Secure handling of credentials

## Performance
- [ ] Tests run in reasonable time
- [ ] Proper use of waits (not sleep when possible)
- [ ] Efficient locator strategies