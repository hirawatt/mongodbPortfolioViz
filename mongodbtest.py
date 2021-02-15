from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://finance:N24PAJ5tmzNa3P4@cluster0.nufgf.mongodb.net/test?authSource=admin&replicaSet=atlas-o53gvq-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
db = client.admin

serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)
