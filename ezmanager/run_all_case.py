import unittest
from common import HTMLTestRunner

casePath = 'D:\\pycharm\\ezLink\\case'

discover = unittest.defaultTestLoader.discover(casePath, "test*.py")
print(discover)

reportPath = 'D:\\pycharm\\ezLink\\report\\result.html'

# 把报告写入该路径下
fp = open(reportPath, "wb")
runner = HTMLTestRunner.HTMLTestRunner(fp, verbosity=2,
                                       title='接口自动化测试报告',
                                       description='ezLink预约系统')
runner.run(discover)
fp.close()