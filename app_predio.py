from flask import Flask
from utils.db import db
from services.predio import predios
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

app_predio=Flask(__name__)
app_predio.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

#SQLAlchemy(app)

db.init_app(app_predio) 
app_predio.register_blueprint(predios)

with app_predio.app_context():
    db.create_all

if __name__=='__main__':
    app_predio.run(host='0.0.0.0',debug=True,port=5000)