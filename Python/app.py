#Imports
from flask import Flask  
from flask_sqlalchemy import SQLAlchemy   
from flask_migrate import Migrate
from routes import register_routes  

#creating database object 
db = SQLAlchemy() 

#My app
def create_app():
    app = Flask(__name__)   #creating flask instance
    app.secret_key = "Deepak@Hemant"   #Flask's Built-in Security

    #Configure SQL Alchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"  #configur of database location 
    app.config["SQLALCHEMY_TRACK_MODIFICATONS"] = False  
    
    db.init_app(app)    #databse intialisation to link app
  
    register_routes(app)  #get and post on the routes
    migrate = Migrate(app,db)  #migration of database

    return app
   
