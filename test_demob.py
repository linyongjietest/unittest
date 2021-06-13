#testcase 的初始化和清除 方法
#unittest.TestCase：TestCase类，所有测试用例类继承的基本类
#setUpClass > setUp > a > tearDown > setUp > b > tearDown > tearDownClass

import unittest

def add(x,y):
    z = x+y
    return z

class TestDemoAdd(unittest.TestCase):          #继承测试类TestCase

#查看setUp()、setUpClass()，tearDown(),tearDownClass（）使用场景
#classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
    @classmethod                              #setUpClass（）&tearDownClass（）前面要加修饰符
    def setUpClass(cls) -> None:
        print("=============执行setUpClass方法==============")

    @classmethod  # setUpClass（）&tearDownClass（）前面要加装饰器
    def tearDownClass(cls) -> None:
         print("=============执行tear DownClass方法==============")

    def setUp(self) -> None:
        print("=============执行setUp方法==============")

    def tearDown(self) -> None:
         print("=============执行tearDown方法==============")

    def test_add01(self):
        print("=============执行test_add01==============")
        self.assertEqual(7, add(3, 4))  # 断言方法：assertEqual

    def test_add02(self):
        print("=============执行test_add02==============")
        self.assertEqual(None, add(3, 4))

    def test_add03(self):
        print("=============执行test_add03==============")
        self.assertEqual(5.7, add(1.2, 4.5))

if __name__ == '__main__':
    unittest.main()

"""
unittest.main():使用她可以方便的将一个单元测试模块变为可直接运行的测试脚本，main()方法使用TestLoader类来搜索所有包含在该模块中
以“test”命名开头的测试方法，并自动执行他们。执行方法的默认顺序是：根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z。
所以以A开头的测试用例方法会优先执行，以a开头会后执行。
"""
