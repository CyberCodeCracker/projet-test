# Golden Fork Restaurant - Test Cases

## AI Assistance Disclosure
This test documentation was generated with AI assistance using DeepSeek. AI was used for:
- Test case generation
- Documentation structure
- Test data creation

## Test Case Template

| Field | Description |
|-------|-------------|
| ID | TC001, TC002, etc. |
| Title | Brief test description |
| Type | Functional/Non-functional |
| Level | Unit/Integration/System |
| Priority | High/Medium/Low |
| Preconditions | Setup requirements |
| Test Steps | Step-by-step instructions |
| Expected Result | Expected outcome |
| Status | Pass/Fail/Not Executed |

## Test Cases List

### TC001: Application Home Page Load
- **Type**: Functional
- **Level**: System
- **Priority**: High
- **Preconditions**: Application running on http://localhost:5181
- **Test Steps**: 
  1. Navigate to home page
  2. Wait for page load
  3. Check page title
  4. Verify no errors on page
- **Expected**: Page loads with "Golden Fork" in title, no errors

### TC002: User Login with Valid Credentials
- **Type**: Functional
- **Level**: System
- **Priority**: High
- **Preconditions**: Valid user account exists
- **Test Steps**:
  1. Navigate to /login
  2. Enter valid email
  3. Enter valid password
  4. Click Login button
- **Expected**: User logged in, redirected to /menu

### TC003: Invalid Login Attempt
- **Type**: Security
- **Level**: System
- **Priority**: High
- **Preconditions**: Login page accessible
- **Test Steps**:
  1. Navigate to /login
  2. Enter invalid credentials
  3. Click Login button
- **Expected**: Error message shown, remains on login page

### TC004: Menu Browsing
- **Type**: Functional
- **Level**: Integration
- **Priority**: Medium
- **Preconditions**: User logged in, menus exist
- **Test Steps**:
  1. Navigate to /menu
  2. Verify menus displayed
  3. Click on a menu
  4. Verify menu details page
- **Expected**: Menus displayed, details page loads correctly

### TC005: Add Item to Cart
- **Type**: Functional
- **Level**: Integration
- **Priority**: High
- **Preconditions**: User logged in, items available
- **Test Steps**:
  1. Navigate to /items
  2. Find an item
  3. Set quantity
  4. Click Add to Cart
- **Expected**: Item added to cart, confirmation shown

### TC006: Checkout Process
- **Type**: Functional
- **Level**: System
- **Priority**: High
- **Preconditions**: Items in cart
- **Test Steps**:
  1. Navigate to /orders/checkout
  2. Verify order summary
  3. Select payment method
  4. Add order notes
- **Expected**: Checkout page loads, order summary correct

### TC007: Security - Unauthorized Admin Access
- **Type**: Security
- **Level**: System
- **Priority**: High
- **Preconditions**: Non-admin user logged in
- **Test Steps**:
  1. Try to access /admin/clients
  2. Check response
- **Expected**: Redirect to login or access denied

### TC008: Performance - Page Load Times
- **Type**: Non-functional (Performance)
- **Level**: System
- **Priority**: Medium
- **Preconditions**: Application running
- **Test Steps**:
  1. Measure load time for each major page
  2. Record times
- **Expected**: All pages load within 5 seconds

### TC009: Browser Compatibility
- **Type**: Non-functional (Compatibility)
- **Level**: System
- **Priority**: Medium
- **Test Steps**:
  1. Check for JavaScript errors
  2. Verify CSS loads
  3. Check viewport rendering
- **Expected**: No JS errors, proper rendering

### TC010: Accessibility - Basic Checks
- **Type**: Non-functional (Accessibility)
- **Level**: System
- **Priority**: Low
- **Test Steps**:
  1. Check image alt text
  2. Verify heading structure
  3. Check form labels
- **Expected**: Good accessibility practices followed