from pages.base_page import BasePage
from pages.login_page import LoginPage
class MainPage(BasePage):
    url = "http://xdclass.net/"
    login = {'type':"css",'value': "#__nuxt > div > div:nth-child(1) > div.header-container > div.header > div:nth-child(3) > div > span:nth-child(1)"}
    search = {'type':"css",'value': "#__nuxt > div > div:nth-child(1) > div.header-container > div.header > div.center-tab > div.search > div.ant-select.w-220px\!.rounded-119px.ant-select-show-search.ant-select-auto-complete.ant-select-single.ant-select-show-search"}
    searchb = {'type':"css",'value': "#__nuxt > div > div:nth-child(1) > div.header-container > div.header > div.center-tab > div.search > div:nth-child(1) > img:nth-child(1)"}
    #move_to
    ceshicekai = {'type':'css','value':'#__nuxt > div > div.main-container > div > div > div.main > div.menu > div > ul > li:nth-child(3)'}
    zdhceshi = {'type':'css','value':'#__nuxt > div > div.main-container > div > div > div.main > div.menu > div > ul > div > div > div:nth-child(2) > div > p'}
    #会打开新的窗口
    kechengzhongxin = {'type':'css','value':'#__nuxt > div > div.main-container > div > div > div.main > div.menu > div > ul > div > div > div:nth-child(2) > div > p'}
    tanchuang = {'type':'xpath','value':'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/button[1]/span'}

    def open_url(self):
        self.open(self.url)
    def closetc(self):
        self.click_element(self.tanchuang['type'],self.tanchuang['value'])


    def goto_login(self):
        self.click_element(self.login['type'],self.login['value'])
        return LoginPage()
    def goto_search(self,data = 'JAVA'):
        self.input_data(self.search['type'],self.search['value'],'java')
        self.click_element(self.searchb['type'],self.searchb['value'])
