#!/usr/bin/env python
import os
from app import create_app, mongo
from app.models import Customer
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from werkzeug.security import generate_password_hash

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
# migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=mongo.db, Customer=Customer)

@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def initdb():
    """Init the database"""
    mongo.db.drop_collection('customers')
    mongo.db.drop_collection('admins')
    mongo.db.drop_collection('results')
    mongo.db.drop_collection('result_ids')
    password = generate_password_hash('testpass')
    customer = {
            'name': 'Foo',
            'lastname': 'Jiang',
            'email': 'foo@example.com',
            'password': password,
            'org': None,
            'new_org': None,
            }
    password = generate_password_hash('testpass')
    admin = {
            'email': 'admin@example.com',
            'password': password,
            }

    mongo.db.admins.insert(admin, safe=True)
    mongo.db.customers.insert(customer, safe=True)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
