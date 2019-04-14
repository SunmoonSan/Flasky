#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/4/13 19:49
from flask_migrate import Migrate
from flask_script import Manager

from app import create_app, db
from app.models import User

app = create_app("default")
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User)


if __name__ == '__main__':
    manager.run()
