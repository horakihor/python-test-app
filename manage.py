import os
import unittest
from flask_script import Manager
from web.main import create_app
from web.main.config import Config

app = create_app(os.getenv('ENVIRONMENT') or 'dev')

app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    app.run(host=Config.HOST,port=Config.PORT)

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('web/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
