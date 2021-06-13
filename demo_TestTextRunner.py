import unittest

def add(x,y):    #定义加法
    z = x+y
    return z

class TestAddDemo(unittest.TestCase):
    """
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
    """
    def test_add01(self):
        self.assertEqual(7,add(3,4))
        print("=====执行test_add01=====")
    def test_add02(self):
        self.assertEqual(None, add(3, 4))
        print("=====执行test_add02=====")
    def test_add03(self):
        self.assertEqual(7, add(1.2, 5.8))
        print("=====执行test_add03=====")

if __name__ == '__main__':
    # unittest.main()              #TestCase ， 执行test开头的命令方法
    suite = unittest.TestSuite()
    suite.addTest(TestAddDemo(test_01))            #类当中的方法： 类（方法）

    runner = unittest.TextTestRunner()
    runner.run(suite)             #运行测试套件，并收集结果信息传递给测试报告对象。
#思路：通过生成的对象runner调用里边run方法去运行suite套件

#运行返回结果应该为一个