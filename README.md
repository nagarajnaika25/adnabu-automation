# adnabu-automation
Selenium automation framework using Python and pytest to validate product search and add-to-cart functionality on a Shopify store, with the HTML reporting.

# AdNabu Automation Assignment

##  Objective
Automate product search and add-to-cart functionality on Shopify store.

---

## Tech Stack
- Python
- Selenium  WebDriver
- Pytest
- Pytest-HTML

---

## Project Structure
- test_adnabu.py → Test script
- requirements.txt → Dependencies
- report.html → Test execution report

---

## Setup Instructions

### 1. Clone Repository
git clone https://github.com/your-username/adnabu-automation-assignment.git

### 2. Navigate to Folder
cd adnabu-automation-assignment

### 3. Install Dependencies
pip install -r requirements.txt

---

##  Run Tests

pytest -v --html=report.html

---

## Test Report
After execution, open:
report.html

---

##  Test Scenario Covered
- Open store
- Enter password
- Search product (Snowboard)
- Open product
- Add to cart
- Verify cart update

---

## 📸 Notes
- Explicit waits used for stability
- JavaScript click used for dynamic elements
- Logging added for execution tracking
