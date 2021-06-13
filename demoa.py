import unittest                                 #导入unittest框架

#加法操作
def add(x,y):
    z = x+y
    return z
#最原始的测试操作
# print(add(3,4) == 7)
# print(add(3,4) == None)
# print(add(1.2,4.5) ==5.7)
"""
断言：两个值进行比较
测试断言：预期结果与实际结果进行相比
"""
class TestDemoAdd(unittest.TestCase):          #继承测试类TestCase
    def test_add01(self):
        self.assertEqual(7,add(3,4))           #断言方法：assertEqual，验证arg1=arg2，不等则fail
    def test_add02(self):
        self.assertEqual(None,add(3,4))
    def test_add03(self):
        self.assertEqual(5.7, add(1.2,4.5))

if __name__ == '__main__':
    unittest.main()                            #执行main函数

#运行结果：.代表成功，F代表失败