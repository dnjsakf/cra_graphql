import dotenv
from api import create_app
from api.graphql.database import init_db

if __name__ == "__main__":  
  dotenv.load_dotenv(dotenv_path=".env")
  
  init_db()
  
  app = create_app("dev", prefix="/api")
  app.run(host="localhost", port=3000)