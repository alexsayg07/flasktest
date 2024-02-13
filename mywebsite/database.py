import motor.motor_asyncio
from odmantic import AIOEngine
import config
from pymongo import errors

configuration = config.BaseConfig()
database_uri = configuration.database_uri



try: 
    client = motor.motor_asyncio.AsyncIOMotorClient(database_uri)
    print("Successful")
except ConnectionError:
    print("Unable to connect to DB")
except errors.ServerSelectionTimeoutError as err:
    # do whatever you need
    print(err)
engine = AIOEngine(client=client, database=configuration.database_name)

