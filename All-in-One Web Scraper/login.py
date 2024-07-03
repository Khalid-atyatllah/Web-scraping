from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(self):
    self.driver.get(self.login_url)
    wait = WebDriverWait(self.driver, 10)

    # Assuming login form has fields with IDs 'username' and 'password'
    wait.until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(self.username)
    wait.until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(self.password)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()

    time.sleep(5)  # Wait for login to complete
