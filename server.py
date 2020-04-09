import dotenv
from api import create_app

if __name__ == "__main__":  
  dotenv.load_dotenv(dotenv_path=".env")
  
  app = create_app("dev", prefix="/api")
  app.run(host="localhost", port=3001)