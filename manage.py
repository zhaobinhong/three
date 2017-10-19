# -*- coding:utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from three import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# 数据库操作
# python three.py db migrate
# python three.py db upgrade

if __name__ == '__main__':
    manager.run()
