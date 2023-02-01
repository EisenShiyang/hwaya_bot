import pymongo
import Utils.DBConstant
client = pymongo.MongoClient(Utils.DBConstant.DB_CONN)

def LoadUser():
    db = client[Utils.DBConstant.USER_DBNAME]
    col = db[Utils.DBConstant.USER_COLLECTION]
    print("The number of users is: " + str(col.count_documents({})))

def LoadFood():
    db = client[Utils.DBConstant.FOOD_DBNAME]
    col = db[Utils.DBConstant.FOOD_COLLECTION]
    print("The number of food is: " + str(col.count_documents({})))