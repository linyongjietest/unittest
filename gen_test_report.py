#1.把HTMLTestRunner拖入目录中
#2.导入HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner
import  unittest

#3.定义一个测试报告文件
report_file = "test_report.html"

#4.创建套件
suite = unittest.TestLoader().discover(start_dir='.', pattern='test*.py')

#5.生成一个runner运行器
'''
    runner = HTMLTestRunner(stream=f,[title],[description]) 
    参数说明：
     stream：文件流，打开写入报告的名称及写入编码格式) 
     title：[可选参数]，为报告标题，如XXX自动化测试报告 
     description：[可选参数]，为报告描述信息；比如操作系统、浏览器等版本
'''
with open(report_file,"wb") as f:               #open语法： open(name[, mode[, buffering]]) ，mode中w代表写入，b代表二进制
    runner =HTMLTestRunner(f,title="测试报告",description="v1.2版本的测试报告")
    runner.run(suite)