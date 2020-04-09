from flask import Flask
from flask_graphql import GraphQLView

from api.graphql.schema import schema
from api.config.middlewares import PrefixMiddleware


def index_page(app):
  from flask import render_template
  @app.route("/")
  def _index():
    return render_template("index.html")

def registering(app):
  from api.routes.sample import app as sample
  
  app.register_blueprint(sample, url_prefix="/sample") #sample.name
    
def create_app(env="dev", prefix=None):
  global app
  
  app = Flask(
    __name__, 
    static_url_path="/api/public",
    static_folder="../client/public",
    template_folder="../client/public",
    instance_path="C:/Users/14D00944/Desktop/python/my_graphql"
  )
  
  app.add_url_rule(
      '/graphql',
      view_func=GraphQLView.as_view(
          'graphql',
          schema=schema,
          graphiql=True # for having the GraphiQL interface
      )
  )
  
  if prefix is not None:
    app.config['APPLICATION_ROOT'] = prefix
    app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix=prefix)
    
  registering(app)
  index_page(app)
  
  return app