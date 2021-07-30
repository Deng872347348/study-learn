from selenium import  webdriver

driver =webdriver.Chrome()

driver.get('https://cs.58.com/chuzu/?PGTID=0d100000-0019-e555-b446-fb717f93be8f&ClickID=4')

el_list = driver.find_elements_by_xpath('/html/body/div[7]/div[2]/ul/li/div[2]/h2/a')

#print(el_list)
# for el in el_list:
#     print(el.text,el.get_attribute('href'))

#driver.quit()