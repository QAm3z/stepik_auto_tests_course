from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
driver.find_element(By.ID, "book").click()

num = int(driver.find_element(By.ID, "input_value").text)

def result(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver.find_element(By.ID, "answer").send_keys(result(num))
driver.find_element(By.ID, "solve").click()

alert = driver.switch_to.alert
alert_text = alert.text

print(alert_text)





