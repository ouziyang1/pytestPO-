import pandas

class DataManager():

    def get_data(self,name,sheet_name):
        path = '../data/'+name+'.xls' #设置路径
        df = pandas.read_excel(path,sheet_name=sheet_name)#用pandas读取数据
        data = df.values.tolist()#转换列表
        print(data)
        return data



data_manager = DataManager()

if __name__ == '__main__':
    data = data_manager.get_data('test_open','test_login')
