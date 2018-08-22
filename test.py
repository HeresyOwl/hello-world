#Headless Chrome=============================================================
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('https://www.baidu.com')
driver.save_screenshot('C:/Users/浚銘/Desktop/test.png')
driver.quit()



#造訪網站並截圖=============================================================
from selenium import webdriver

Browser = webdriver.Chrome()
WebUrl  = ('https://www.ithome.com.tw/')
Browser.get(WebUrl)
Browser.save_screenshot('C:\Users\浚銘\Desktop\test.png')
Browser.quit()


#登入帳密並截圖=============================================================
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Browser = webdriver.Chrome()
LoginUrl= ('https://member.ithome.com.tw/login')
UserName= ('#####')
UserPass= ('#####')

Browser.get(LoginUrl)
Browser.find_element_by_id('account').send_keys(UserName)
Browser.find_element_by_id('password').send_keys(UserPass)
Browser.find_element_by_id('password').send_keys(Keys.ENTER)
Browser.save_screenshot('test.png')
Browser.quit()


#造訪Google並搜尋"天氣"====================================================
from selenium import webdriver

driver = webdriver.Chrome(r"C:\selenium_driver_chrome\chromedriver.exe")
driver.get("https://www.google.com.tw/")

driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys("天氣")
driver.find_element_by_xpath("//input[@jsaction='sf.chk']").submit()


#造訪網頁並更改視窗大小====================================================
from selenium import webdriver
import time

chrome_path = "C:\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)

web.get('http://www.cwb.gov.tw/V7/')
web.set_window_position(0,0) #瀏覽器位置
web.set_window_size(700,700) #瀏覽器大小
time.sleep(5)

web.find_element_by_link_text('天氣預報').click() #點擊頁面上"天氣預報"的連結
time.sleep(5)

web.close()
