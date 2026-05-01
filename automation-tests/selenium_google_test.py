from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)

# kliknięcie cookies (jeśli się pojawi)
try:
    accept_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Zaakceptuj')]"))
    )
    accept_btn.click()
except:
    pass  # jeśli nie ma okna, idziemy dalej

# pole wyszukiwania
search_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "q"))
)

search_box.send_keys("QA automation test")
search_box.submit()

driver.quit()
