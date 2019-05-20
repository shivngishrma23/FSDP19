####web scrapping using selenium
from selenium import webdriver
driver = webdriver.Chrome("C:/Users/Shivangi Sharma/Desktop/ML-SUMMERtraining/chromedriver.exe")
driver.get("https://bidplus.gem.gov.in/bidlists")


driver.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[1]/p[1]').click()
