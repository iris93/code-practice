# coding:utf-8

# 我们将首先使用Flask Script扩展。使用它可以创建命令，并在Flask的应用上下文中执行，
# 因为这样才能对Flask对象进行修改。
# Flask Script自带了一些默认的命令，可以运行服务器或者开启带应用上下文的Python命令行。
# 测试：在命令输入：python manage.py server即可启动app服务
# python manage.py shell，使用命令行，可以测试包是否被引入

from flask_script import Manager, Server
from main import app,db,User

manager = Manager(app)

manager.add_command("server", Server())

# make_shell_context函数会创建一个Python命令行，并且在应用上下文中执行。
# 返回的字典告诉Flask Script在打开命令行时进行一些默认
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User)

if __name__ == "__main__":
    manager.run()
