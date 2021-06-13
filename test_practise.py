import unittest

def mul(x,y):    #定义乘法
    z = x*y
    return z

class TestAddDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("=====执行setUpClass方法=====")
    @classmethod
    def tearDownClass(cls) -> None:
        print("=====执行tearDownClass方法=====")
    def setUp(self) -> None:
        print("=====执行setUp方法=====")
    def tearDown(self) -> None:
        print("=====执行tearDown方法=====")
    def test_add01(self):
        self.assertEqual(12,mul(3,4))
        print("=====执行test_add01=====")
    def test_add02(self):
        self.assertEqual(4.7, mul(1.2, 4))
        print("=====执行test_add02=====")
    # def test_add03(self):
    #     self.assertEqual(7, mul(1.2, 5.8))
    #     print("=====执行test_add03=====")

if __name__ == '__main__':
    # unittest.main()              #TestCase ， 执行test开头的命令方法
    suite = unittest.TestSuite()
    suite.addTest(TestAddDemo('test_01'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
