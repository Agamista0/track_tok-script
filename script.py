from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 
from  time import sleep 






driver = webdriver.Chrome()
#login
driver.get('https://flat.io/auth/signin')  
driver.find_element(By.XPATH , '//*[@id="emailInput"]').send_keys("gowek66315@gam1fy.com")
driver.find_element(By.XPATH , '//*[@id="app"]/div/div[1]/div/div[3]/div/div[3]/form/div[2]/div/div[1]/input').send_keys("Agamista135")
driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div[3]/div/div[3]/form/button').click()
sleep(3)

driver.get("https://flat.io/community/popular/weekly")
sleep(3)

print("scrolling....")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
prodects = soup.find_all('div' ,attrs={"class" : "info"})
print(len(prodects))




