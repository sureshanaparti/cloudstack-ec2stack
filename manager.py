#!/usr/bin/env python
# encoding: utf-8

from ec2stack import create_app
from ec2stack.core import DB
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

APP = create_app()

MIGRATE = Migrate(APP, DB)
MANAGER = Manager(APP)
MANAGER.add_command('db', MigrateCommand)

if __name__ == "__main__":
    MANAGER.run()
