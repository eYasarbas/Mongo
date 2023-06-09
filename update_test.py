import pymongo

myclients = pymongo.MongoClient("mongodb://localhost:27017/")
"""mydb = myclients["deneme"]
mycollection = mydb["test"]

mycollection.update_many(  # update_one tekli günceller.
    {"ad": "ali"},
    {"$set": {
        "ad": "mehmet",
        "yaş": 10
    }}
)"""
mydb = myclients["user"]
mycollection = mydb["info"]
result = mycollection.find({
    "name": {
        "$in": ["Samsung S6"]  # içinde sanmsung s6 ve s7 bulunduran verileri seçer
    }
})

mycollection.find({
    "price": {
        "$gt": 3000  # fiyatı 3000 den fazla olanları secer
    }
})
mycollection.find({
    "price": {
        "$lt": 3000  # fiyatı 3000 den az olanları secer
    }
})
"""for i in mycollection.find():
    print(i)"""
