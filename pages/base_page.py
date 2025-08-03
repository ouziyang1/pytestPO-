from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from drivers.driver_manger import driver

class BasePage():
    #open url
    def open(self,url):
        driver.get(url)

    #定位元素
    def find_element(self,type,value):
        if type=="id":
            el= driver.find_element(By.ID,value)
        elif type=="xpath":
            el= driver.find_element(By.XPATH,value)
        elif type=="name":
            el= driver.find_element(By.NAME,value)
        elif type=="tag":
            el= driver.find_element(By.TAG_NAME,value)
        elif type=="css":
            el= driver.find_element(By.CSS_SELECTOR,value)
        elif type=="link":
            el= driver.find_element(By.LINK_TEXT,value)
        elif type=="plink":
            el= driver.find_element(By.PLINK_TEXT,value)
        elif type=="class":
            el= driver.find_element(By.CLASS_NAME,value)
        else:
            print("输入的定位方式有错误")
        return el

#元素操作
    def click_element(self,type,value):
        self.find_element(type,value).click()

    def input_data(self,type,value,data):
        self.find_element(type,value).send_keys(data)

    def move_to_element(self,type,value):
        ActionChains(driver).move_to_element(self.find_element(type,value)).perform()

    def switch_to_window(self,title):
        handles = driver.window_handles
        for handle in handles:
            if handle.title() == title:
                driver.switch_to.window(handle)

    #删除cookies
    def del_cookies(self):
        driver.delete_all_cookies()



#获取所有文字 数据库执行的数据
#drvier.page_source  cursor.fetchall
#while True 一直循环 可以在条件判断后加break
#异常捕获
#switch_to_window（） handles句柄相关，切换不同网页

#switch_to_frame（） 切换到网页中的网页，嵌套 ##需要一层一层frame定位 find_element
#如果iframe中没有id或name属性，就要将iframe作为元素查找出来，然后再切换
#driver.switch_to_default_content()切换到默认初始页面

#switch_to_alter 切换到警告窗
#无论如何都执行，可以用异常捕获