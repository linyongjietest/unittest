#跳过测试用例：@unittest.skip('代码未完成')

import unittest
from parameterized import parameterized
version =30
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

    # @parameterized.expand([(8,2,4),(-6,-2,3),(21,3,7)])
    # def test_add(self,c,a,b):
    #     rst = mul(a,b)
    #     self.assertEqual(c,rst)
    @unittest.skip('此用例已经发现bug，暂时跳过')
    def test_add01(self):
        rst1 = mul(3,4)
        self.assertEqual(12,rst1)
        print("=====执行test_add01=====")
    @unittest.skipIf(version!=25,'如果当前版本30为真，跳过当前测试用例，版本不为30才执行')
    def test_add02(self):
        rst2 = mul(1.2, 4)
        self.assertEqual(4.8, rst2)
        print("=====执行test_add02=====")

if __name__ == '__main__':
    unittest.main()              #TestCase ， 执行test开头的命令方法
    # suite = unittest.TestSuite()
    # suite.addTest(TestAddDemo('test_01'))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
