# 导入基础包
import datetime
import time

# 导入第三方包
from tornado.web import RequestHandler, Application
from tornado.options import options, define, parse_command_line
from tornado.ioloop import IOLoop
import tornado.gen

# 默认项目配置启动端口
define('port', default=8000, help='项目默认启动端口')


# 定义基础类
class SleepHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        # time.sleep(5)
        yield tornado.gen.sleep(5)
        self.write(str(datetime.datetime.now()))


# 主程序入口
if __name__ == '__main__':
    # 识别命令行操作
    parse_command_line()
    # 定义app
    app = Application(
        [
            # 定义路由
            (r'/sleep', SleepHandler)
        ],
        # 开启调试
        debug=True,
    )
    # 启动项目监听端口
    app.listen(options.port)
    # 启动轮询事件
    IOLoop.current().start()
