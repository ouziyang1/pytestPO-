from pages.base_page import BasePage



class LoginPage(BasePage):
    url = "http://xdclass.net/"
    username = {'type': 'css', 'value': '#form_item_account'}
    password = {'type': 'css', 'value': '#form_item_password'}
    button = {'type': 'css',
              'value': '#__nuxt > div > div:nth-child(1) > div.header-container > div.reg-modal > div > div > div:nth-child(2) > form > div:nth-child(4) > div > div > div > button'}


    user = {
        'username': '13798042717',
        'password': 'a2267282995', }

    def inputnw(self,name,password):
        self.input_data(self.username['type'],self.username['value'],name)
        self.input_data(self.password['type'],self.password['value'],password)
        self.click_element(self.button['type'],self.button['value'])
