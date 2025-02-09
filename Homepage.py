"""
HomePage.py

Program : File containing the Locators for OrangeHRM
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
   def __init__(self, driver):
      self.driver = driver
      self.username_field = (By.NAME, 'username')
      self.password_field = (By.NAME, 'password')
      self.login_button = (By.XPATH, '//button[@type="submit"]')
      self.error_message = (By.XPATH, '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')

   def login(self, username, password):
      WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
      WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)
      WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

   def is_login_successful(self):
      try:
         WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.error_message))
         return False
      except:
         return True
