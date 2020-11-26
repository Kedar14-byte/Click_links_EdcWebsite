from selenium import webdriver
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe", options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://www.tutorialspoint.com/index.htm")
driver.refresh()
links = driver.find_elements_by_tag_name('a')
print(len(links))
driver.find_element_by_link_text("Home").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
time.sleep(2)
driver.find_element_by_link_text("Jobs").click()
time.sleep(2)
driver.find_element_by_link_text("Tools").click()
time.sleep(2)
driver.quit()
