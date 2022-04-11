from selenium import webdriver
driver_path = "C:/Users/dylan/Desktop/My_Python/WebDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")
print(driver.page_source)