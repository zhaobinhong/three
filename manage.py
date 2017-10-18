# -*- coding:utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from server import *
from three import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', app.run())
manager.add_command('runserver --debug', rundebug)
manager.add_command('rundev', dev)

# 数据库操作
# python three.py db migrate
# python three.py db upgrade

if __name__ == '__main__':
    manager.run()
