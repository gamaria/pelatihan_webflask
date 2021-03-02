from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app=Flask('__name__', template_folder='ukmummu/templates', static_folder='ukmummu/static')

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///katalogukm.db'
db=SQLAlchemy(app)
bcrypt= Bcrypt(app)

app.config['SECRET_KEY']="pelatihan"


#registasi blueprints

from ukmummu.user.routes import guser
app.register_blueprint(guser)


from ukmummu.admin.routes import gadmin
app.register_blueprint(gadmin)