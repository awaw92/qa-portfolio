from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# uruchom przeglądarkę
driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/register")

time.sleep(3)

print("Start testu...")

# znajdź pola
username = driver.find_element(By.NAME, "username")
email = driver.find_element(By.NAME, "email")
password1 = driver.find_element(By.NAME, "password1")
password2 = driver.find_element(By.NAME, "password2")

# generuj unikalnego usera (żeby nie było błędu "user exists")
unique_user = "user" + str(int(time.time()))

# wpisz dane
username.send_keys(unique_user)
print("OK - username")

email.send_keys(unique_user + "@test.pl")
print("OK - email")

# mocne hasło (niepodobne do username)
password1.send_keys("K9!zPq7#Lm2")
print("OK - password1")

password2.send_keys("K9!zPq7#Lm2")
print("OK - password2")

time.sleep(2)

# wyślij formularz
driver.find_element(By.TAG_NAME, "form").submit()
print("Formularz wysłany")

time.sleep(5)

input("ENTER żeby zamknąć...")
driver.quit()
