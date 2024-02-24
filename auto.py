from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("path_to_webpage.html")
    time.sleep(2)

    wait = WebDriverWait(driver, 10)
    name_input = wait.until(EC.visibility_of_element_located((By.ID, "name")))
    address_textarea = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    subscribe_checkbox = wait.until(EC.visibility_of_element_located((By.ID, "subscribe")))
    gender_radio_buttons = wait.until(EC.visibility_of_all_elements_located((By.NAME, "gender")))
    country_dropdown = wait.until(EC.visibility_of_element_located((By.ID, "country")))
    submit_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    time.sleep(2)

    name_input.send_keys("John Doe")
    time.sleep(2)

    address_textarea.send_keys("111 lane 2, New delhi, India")
    time.sleep(2)

    subscribe_checkbox.click()
    time.sleep(2)

    for radio_button in gender_radio_buttons:
        if radio_button.get_attribute("value") == "male":
            radio_button.click()
            break
    time.sleep(2)

    country_dropdown.click()
    time.sleep(1)
    country_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[text()='India']")))
    country_option.click()
    time.sleep(2)


    submit_button.click()
    time.sleep(2)

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
    time.sleep(2)

finally:
    driver.quit()
