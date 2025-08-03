from drivers.driver_manger import driver
from utils.log_manager import my_log
from utils.sql_manager import sql_manager
class AssertError():
    def equal(self,type='page',value='',target_value='*',table='',column='',limit=''):
        if type == 'page':
            try:
                assert value in driver.page_source
            except Exception as e:
                my_log.logger.error(f'页面上没有发现{value}')
                raise e
        elif type == 'sql':
            my_log.logger.info('开始断言数据库的内容')
            result = sql_manager.get_sql(target_value,table,column,limit)
            try:
                assert value in str(result)
            except Exception as e:
                my_log.logger.error(f'数据库{table}中没有发现:{value}的信息')
                raise e

assert_manager = AssertError()