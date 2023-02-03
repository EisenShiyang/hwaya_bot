import pymongo
from Helper.DateHelper import *
import Utils.DBConstant
client = pymongo.MongoClient(Utils.DBConstant.DB_CONN)

def Register(id, name):
    print("START REGISTER")
    
    if CheckRegistered(id):
        return None
    
    col = setUserDB()
    user_dict = { "id":id, "name":name }
    return col.insert_one(user_dict)

def CheckRegistered(id):
    col = setUserDB()
    query = { "id" : id }
    return col.count_documents(query) > 0

def LoadUser():
    col = setUserDB()
    print("The number of users is: " + str(col.count_documents({})))

def AddFood(command):
    col = setFoodDB()
    food_dict = {
        "id": command.GetId(),
        "item": command.GetItem(),
        "date": CheckYear(command.GetDate()),
        "Location": command.GetLocation(),
        "insert_date": GetCurrentTime()
    }
    return col.insert_one(food_dict)

def LoadFood():
    col = setFoodDB()
    print("The number of food is: " + str(col.count_documents({})))

def setUserDB():
    db = client[Utils.DBConstant.USER_DBNAME]
    col = db[Utils.DBConstant.USER_COLLECTION]
    return col

def setFoodDB():
    db = client[Utils.DBConstant.FOOD_DBNAME]
    col = db[Utils.DBConstant.FOOD_COLLECTION]
    return col