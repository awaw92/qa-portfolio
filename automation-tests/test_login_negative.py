from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("http://127.0.0.1:8000")

    wait = WebDriverWait(driver, 10)

    # czekamy na formularz
    email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password = driver.find_element(By.NAME, "password")

    # 🐢 wolne wpisywanie (jak użytkownik)
    for char in "wrong@test.com":
        email.send_keys(char)
        time.sleep(0.1)

    time.sleep(0.5)

    for char in "wrongpassword":
        password.send_keys(char)
        time.sleep(0.1)

    time.sleep(1)

    password.send_keys(Keys.RETURN)

    # czekamy na reakcję strony
    time.sleep(2)

    # 🔍 szukamy błędu
    errors = driver.find_elements(By.XPATH,
        "//*[contains(@class,'error') or contains(@class,'alert') or contains(text(),'Invalid') or contains(text(),'error')]"
    )

    visible_errors = [e for e in errors if e.is_displayed()]

    print("\n--- TEST DEBUG ---")
    print("All error-like elements:", len(errors))
    print("Visible error elements:", len(visible_errors))

    for e in visible_errors:
        print("TEXT:", e.text)

    if len(visible_errors) > 0:
        print("TEST PASSED - visible error message found")
    else:
        print("TEST FAILED - no visible error message")

    time.sleep(3)  # żebyś widział wynik na ekranie

finally:
    driver.quit()
