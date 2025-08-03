from selenium import webdriver
from selenium.webdriver.edge.options import Options


class WebdriverManger:
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_experimental_option("detach", True )
        self.d = webdriver.Edge(options=self.options)

driver = WebdriverManger()
driver = driver.d
driver.implicitly_wait(10)


