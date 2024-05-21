from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mypassword@localhost:3306/EMS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = create_engine('mysql://mysql://root:mypassword@localhost:3306/EMS')
Session = sessionmaker(bind=engine)
migrate = Migrate(app, db)


# import the controllers
from controllers.emp_controller import *

if __name__ == '__main__':
    # SQLAlchemy.create_all()
    app.run(debug=True, port=8080)

