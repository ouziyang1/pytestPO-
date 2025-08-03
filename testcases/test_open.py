import time

import pytest
from pages.main_page import MainPage
from data.data_manager import data_manager
#from pages.login_page import LoginPage
from utils.log_manager import my_log
from utils.assert_manager import assert_manager

@my_log.runtime_logger_class
class TestDemo():

    @pytest.mark.parametrize('name,password,tar_value',data_manager.get_data('test_open','test_login'))
    def test_login(self,name,password,tar_value):
        main_page = MainPage()
        main_page.open_url()
        try:
            main_page.closetc()
        except:
            pass
        login_page = main_page.goto_login()
        #login_page = LoginPage()
        login_page.inputnw(name,password)
        assert_manager.equal(type='page',value=tar_value)
        login_page.del_cookies()




if __name__ == '__main__':
    pytest.main()