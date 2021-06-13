#日志
"""
logging库提供了多个组件：Logger、Handler、Filter、Formatter。
Logger对象提供应用程序可直接使用的接口
Handler发送日志到适当的目的地
Filter提供了过滤日志信息的方法
Formatter指定日志显示格式
"""

from loguru import logger
import  logging

# #日志格式化
logger.info("这是一条日志信息")
#
#输出不同级别的日志
'''
debug : 调试日志
info ：普通日志
warning ：警告日志
success ：成功日志
error ：错误日志
critical :严重错误日志
越往下级别越高
'''
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")
logger.critical("这是一条critical日志")

#输出日志到文件
#语法：add(sys.stderr,format,level)           add(输出文件，设置格式化，设置级别)
logger.add("file.log", format="{time} {level} {message}", level="DEBUG")     #级别要大写，否则报错，高级别不能输出低级别的日志，所以level填最低的debug
#时间格式化
#logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} {level} {message}", level="INFO")
logger.debug('这是一条debug日志')
logger.info("这是一条info日志")

#字符串格式化
logger.info("hello,{} ,hello,{th}".format("python",th="java"))

#日志保存
logger.add("file_1.log", rotation="500 MB")          # 文件过大就会重新生成一个文件,rotation:循环
logger.add("file_2.log", rotation="12:00")           # 每天12点创建新文件
logger.add("file_3.log", rotation="1 week")          # 文件时间过长就会创建新文件
logger.add("file_X.log", retention="10 days")        # 一段时间后会清空,retention=10 days：保留时间为10天
logger.add("file_Y.log", compression="zip")          # 保存zip格式,compression:压缩
logger.add("file_4.log", retention="1 minute")

