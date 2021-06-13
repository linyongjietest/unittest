#数据参数化，一个函数代替多个函数

import unittest
from parameterized import parameterized

def mul(x,y):    #定义乘法
    z = x*y
    return z

class TestAddDemo(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("=====执行setUpClass方法=====")
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("=====执行tearDownClass方法=====")
    # def setUp(self) -> None:
    #     print("=====执行setUp方法=====")
    # def tearDown(self) -> None:
    #     print("=====执行tearDown方法=====")

    #使用方式1：
    # @parameterized.expand([(8,2,4),(-6,-2,3),(21,3,7)])
    # 使用方式2：
    # data1 =[(8,2,4),(-6,-2,3),(21,3,7)]
    # @parameterized.expand(data1)          #装饰器@parameterized：实现参数化
    # 使用方式3：
    def built_data():
        return ([(8,2,4),(-6,-2,3),(21,3,7)])
    @parameterized.expand(built_data)

    def test_add(self,c,a,b):
        rst = mul(a,b)
        self.assertEqual(c,rst)
    '''
    def test_add01(self):
        rst1 = mul(3,4)
        self.assertEqual(12,rst1)
        print("=====执行test_add01=====")
    def test_add02(self):
        rst2 = mul(1.2, 4)
        self.assertEqual(4.8, rst2)
        print("=====执行test_add02=====")
    def test_add03(self):
        rst3 = mul(3,9)
        self.assertEqual(27, rst3)
        print("=====执行test_add03=====")

    '''

if __name__ == '__main__':
    unittest.main()              #TestCase ， 执行test开头的命令方法
    # suite = unittest.TestSuite()
    # suite.addTest(TestAddDemo('test_01'))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
