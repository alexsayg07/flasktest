import os
from pydantic_settings import BaseSettings 
from dotenv.main import load_dotenv


class BaseConfig(BaseSettings):
    load_dotenv()
    dev_secret_access_key: str = os.getenv("DEV_SECRET_ACCESS_KEY")
    mongo_database_name: str = 'girlstocks'
    mongo_database_uri: str = os.getenv("DATABASE_URI")
   


    # Authentication Headers if needed
