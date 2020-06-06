from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import app
from exts import db
from model import User,Question,Answer


#使用migrate绑定app和db
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command("db",MigrateCommand)

if __name__ == "__main__":
    manager.run()
