from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)

# --------------------
# LOGIN
# --------------------
driver.get("http://127.0.0.1:8000/login")

wait.until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys("testuser")
driver.find_element(By.NAME, "password").send_keys("testpass")

login_btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'], button[type='submit']"))
)
login_btn.click()

wait.until(lambda d: "login" not in d.current_url.lower())
print("LOGIN OK")

# --------------------
# CREATE LISTING
# --------------------
driver.get("http://127.0.0.1:8000/create/")

wait.until(EC.presence_of_element_located((By.NAME, "title"))).send_keys("Test Item QA")

driver.find_element(By.NAME, "description").send_keys("Opis testowej aukcji")
driver.find_element(By.NAME, "starting_bid").send_keys("100")
driver.find_element(By.NAME, "image_url").send_keys("https://example.com/image.jpg")

# CATEGORY
category_element = wait.until(
    EC.presence_of_element_located((By.NAME, "category"))
)

select = Select(category_element)

print("AVAILABLE CATEGORIES:")
for option in select.options:
    print("-", option.text)

for option in select.options:
    if option.text.strip().lower() in ["cars", "trucks", "phones"]:
        select.select_by_visible_text(option.text)
        break

# SUBMIT CREATE
create_btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'], button[type='submit']"))
)
create_btn.click()

wait.until(lambda d: "/create" not in d.current_url)
print("LISTING CREATED")

# --------------------
# OPEN LISTING
# --------------------
driver.get("http://127.0.0.1:8000/")

listing = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Test Item QA"))
)
listing.click()

# --------------------
# BID (FIXED)
# --------------------
print("TRYING BID...")

amount_input = wait.until(
    EC.presence_of_element_located((By.NAME, "amount"))
)
amount_input.send_keys("150")

try:
    content_input = driver.find_element(By.NAME, "content")
    content_input.send_keys("Automated Selenium bid")
except:
    pass

bid_btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'], button[type='submit']"))
)
bid_btn.click()

print("BID SUBMITTED")

# --------------------
# ASSERTION
# --------------------
wait.until(lambda d: "highest bid" in d.page_source.lower())

assert "highest bid" in driver.page_source.lower()

print("E2E TEST PASSED - FULL FLOW WORKS")

driver.quit()
