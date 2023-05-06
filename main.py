from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd
import time

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--user-agent=' + user_agent)

driver = webdriver.Chrome(chrome_options=options, executable_path="chromedriver")

target_url = 'https://portal.titech.ac.jp/'
driver.get(target_url)
time.sleep(3)

search_box = driver.find_element(by=By.XPATH, value='//*[@id="portal-form"]/form[2]/input')
search_box.click()
time.sleep(3)


#first rayer
df_id = pd.read_csv('student_info/student_id.csv')
account_number = df_id['info'][0]
account_password = df_id['info'][1]

account_box = driver.find_element(by=By.NAME, value="usr_name")
account_box.send_keys(account_number)

password_box = driver.find_element(by=By.NAME, value="usr_password")
password_box.send_keys(account_password)

submit_box_r1 = driver.find_element(by=By.NAME, value="OK")
time.sleep(3)
submit_box_r1.click()


#second rayer
df_matrix = pd.read_csv('student_info/student_matrix.csv')

m_1 = (driver.find_element(by=By.XPATH, value= '//*[@id="authentication"]/tbody/tr[4]/th[1]')).text
m_2 =(driver.find_element(by=By.XPATH, value= '//*[@id="authentication"]/tbody/tr[5]/th[1]')).text
m_3 =(driver.find_element(by=By.XPATH, value= '//*[@id="authentication"]/tbody/tr[6]/th[1]')).text

m_1_code = df_matrix[m_1[1]][int(m_1[3])-1]
m_2_code = df_matrix[m_2[1]][int(m_2[3])-1]
m_3_code = df_matrix[m_3[1]][int(m_3[3])-1]

matrix_element_1 = driver.find_element(by=By.NAME, value="message3")
matrix_element_1.send_keys(m_1_code)

matrix_element_2 = driver.find_element(by=By.NAME, value="message4")
matrix_element_2.send_keys(m_2_code)

matrix_element_3 = driver.find_element(by=By.NAME, value="message5")
matrix_element_3.send_keys(m_3_code)
time.sleep(3)

submit_box_r2 = driver.find_element(by=By.NAME, value="OK")
submit_box_r2.click()

time.sleep(3)