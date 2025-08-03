import os
#对文件交互用os
#获取可以用for循环
from multiprocessing import Pool

class RunManager:

    def __init__(self):
        folder_path = '../report/result'
        if len(os.listdir(folder_path)) >0:
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)


    def run_pytest(self, file):
        cmd = f"pytest {os.path.abspath(file)} --alluredir ../report/result"
        os.system(cmd)

    def run_and_create_report(self):
        files = ['../testcases/test_open.py','../testcases/test_logger.py']
        with Pool(2) as pool:
            pool.map(self.run_pytest, files)
        os.path.abspath(__file__)
        os.system("allure generate --clean ../report/result -o ../report/html")


if __name__ == '__main__':
    manager = RunManager()
    manager.run_and_create_report()