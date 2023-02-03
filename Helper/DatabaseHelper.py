import pymongo
from Helper.DateHelper import *
import Utils.DBConstant
client = pymongo.MongoClient(Utils.DBConstant.DB_CONN)

def Register(id, name): 
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

def AddFood(command):
    col = setFoodDB()
    food_dict = {
        "id": command.GetId(),
        "item": command.GetItem(),
        "date": CheckYear(command.GetDate()),
        "Location": command.GetLocation(),
        "insert_date": GetCurrentTime()
    }
    col.insert_one(food_dict)

def DeleteFood(command):
    col = setFoodDB()
    check_duplicated_name_dict = {
        "id": command.GetId(),
        "name": command.GetItem(),
        "date": CheckYear(command.GetDate())
    }
    
    if col.count_documents(check_duplicated_name_dict) > 1:
        # Multiple items with the same name and expiration date
        # Will delete the one with the earliest insert date
        col.delete_one({"insert_date": col.find_one(check_duplicated_name_dict).sort({"insert_date", 1})["insert_date"]})
    else:
        col.delete_one(check_duplicated_name_dict)

def LoadFood():
    col = setFoodDB()

def setUserDB():
    db = client[Utils.DBConstant.USER_DBNAME]
    col = db[Utils.DBConstant.USER_COLLECTION]
    return col

def setFoodDB():
    db = client[Utils.DBConstant.FOOD_DBNAME]
    col = db[Utils.DBConstant.FOOD_COLLECTION]
    return col