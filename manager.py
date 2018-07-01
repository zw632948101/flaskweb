import os
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand, Migrate
from app import create_app, db
from app.models import User, Role

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


@manager.command
def test():
    """执行单元测试命令"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # manager.run()
    app.run()
