import datetime
import time

from tornado.web import RequestHandler, Application
from tornado.options import options, define, parse_command_line
from tornado.ioloop import IOLoop
import tornado.gen

define('port', default=8000, help='项目默认启动端口')


class SleepHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        # time.sleep(5)
        yield tornado.gen.sleep(5)
        self.write(str(datetime.datetime.now()))


if __name__ == '__main__':
    parse_command_line()
    app = Application(
        [
            (r'/sleep', SleepHandler)
        ],
        debug=True,
    )
    app.listen(options.port)
    IOLoop.current().start()
