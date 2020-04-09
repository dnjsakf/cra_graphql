from api.config.middlewares import PrefixMiddleware
from flask import Flask

def registering(app):
  from api.routes.sample import app as sample
  
  app.register_blueprint(sample, url_prefix="/sample") #sample.name
    
def create_app(env="dev", prefix=None):
  global app
  app = Flask(__name__)
  
  if prefix is not None:
    app.config['APPLICATION_ROOT'] = prefix
    app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix=prefix)
    
  registering(app)
  
  return app