#运行测试用例的文件
from parameterized import parameterized
import unittest
from test_practise import  TestAddDemo

#生成一个套件对象
'''
#TestLoader:用来加载TestCase到TestSuite中，即加载满足条件的测试用例，并把测试用例封装成测试套件
(start_dir='.', pattern='test*.py'):.代表当前路径（run_case.py)，'test*.py'代表搜索所有test开头的文件
'''
#方法一：TestLoader()
#suite = unittest.TestLoader().discover(start_dir='.', pattern='test*.py')

#方法二：TestSuite()
suite = unittest.TestSuite()                   #用TestSuite调用类TestAddDemo中的测试用例
suite.addTest(TestAddDemo('test_add01'))

runner = unittest.TextTestRunner()            #TextTestRunner:一个基础的测试用例执行器，实现了将结果输出为流的功能。如果stream为None，默认的，sys.stderr会被作为输出流。
runner.run(suite)
