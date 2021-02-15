from pymongo import MongoClient
from pprint import pprint
from random import randint
import pandas as pd
import json
import requests

path = "https://www1.nseindia.com/content/indices/top10nifty50_120221.csv"
top_50_hol = requests.get(path)

top_50_hol = top_50_hol.content.json()

client = MongoClient("mongodb+srv://finance:N24PAJ5tmzNa3P4@cluster0.nufgf.mongodb.net/test?authSource=admin&replicaSet=atlas-o53gvq-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
db = client['stock_sectors_india']

collection_name = 'nse'
db_cm = db[collection_name]

db_cm.insert_many(top_50_hol)
