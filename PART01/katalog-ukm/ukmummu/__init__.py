from flask import Flask
app=Flask('__name__', template_folder='ukmummu/templates', static_folder='ukmummu/static')


#registasi blueprints

from ukmummu.user.routes import guser
app.register_blueprint(guser)


from ukmummu.admin.routes import gadmin
app.register_blueprint(gadmin)