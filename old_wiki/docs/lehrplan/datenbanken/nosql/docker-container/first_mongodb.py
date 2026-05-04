from pymongo import MongoClient
import dotenv

ENV = dotenv.dotenv_values()

myclient = MongoClient("mongodb://localhost:27018/")

#mydb = myclient["first_db"]
print(myclient.list_database_names())