import pymongo
import numpy as np
import json
import pandas as pd

from numyencoder import NumpyEncoder

myclients = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclients["test"]
mycol = mydb["customers"]
mycol2 = mydb["Magnetism"]
mycol3 = mydb["Sound"]
"""
mycollection.insert_one({"ad": "ali", "yaş": 20})

for i in mycollection.find():
    print(i)

mydb = myclients["user"]
mycollection = mydb["info"]
produceList = [
    {"name": "Samsung S6", "price": 9500},
    {"name": "Samsung S7", "price": 9700},
    {"name": "Samsung S8", "price": 9900},
    {"name": "Samsung S9", "price": 10000, "tanım": "mükemmel"},
    {"name": "Samsung S10", "price": 11100}

]
result = mycollection.insert_many(produceList)
for i in mycollection.find():
    print(i)

mycollection.delete_one({"ad": "mehmet"})
for i in mycollection.find():
    print(i)

mydict = {"name": "John", "address": "Highway 37"}
mylist = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]
mylist2 = [
    {"_id": 1, "name": "John", "address": "Highway 37"},
    {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    {"_id": 3, "name": "Amy", "address": "Apple st 652"},
    {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
    {"_id": 5, "name": "Michael", "address": "Valley 345"},
    {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
    {"_id": 8, "name": "Richard", "address": "Sky st 331"},
    {"_id": 9, "name": "Susan", "address": "One way 98"},
    {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
    {"_id": 12, "name": "William", "address": "Central st 954"},
    {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
    {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
y = mycol.insert_many(mylist2)
x = mycol.insert_one(mydict)
print(myclients.list_database_names())
print(mydb2.list_collection_names())
collist = mydb2.list_collection_names()
if "customers" in collist:
    print("The collection exists.")
print(x.inserted_id)
print(y.inserted_ids)
y = mycol.find_one()


myquery = {"address": "Park Lane 38"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
myquery = {"address": "Park Lane 38"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
mydoc = mycol.find().sort("name")
print("sadfdsfdsagadgdf")
for x in mydoc:
    print(x)
"""


def same_sensor_data():
    _message = dict()
    _message["sa"] = 16
    _message["se"] = "A1"
    _message["si"] = 250
    _message["st"] = 16
    _message["te"] = "E"
    _message["fs"] = 4000
    _message["me"] = "OMAXGVSM1234"
    return _message


def create_mock_vibration_data():
    _message = same_sensor_data()
    _message["x"] = np.random.uniform(low=-1.5, high=1.5, size=(40,))
    _message["y"] = np.random.uniform(low=-1.5, high=1.5, size=(40,))
    _message["z"] = np.random.uniform(low=-1.5, high=1.5, size=(40,))
    return _message


def create_mock_ultrasound_data():
    _message = same_sensor_data()
    _message["s"] = np.random.randint(low=-20, high=-1, size=(10,))
    return _message


vib = create_mock_vibration_data()
sound = create_mock_ultrasound_data()
print("Vibration\n", vib)
print("\nSound\n", sound)
js_vib = json.dumps(vib, cls=NumpyEncoder)
js_sound = json.dumps(sound, cls=NumpyEncoder)
"""js_vib = pd.Series(vib).to_json(orient='values')
js_vib2 = json.loads(js_vib)
js_sound = pd.Series(sound).to_json(orient='values')
js_sound2 = json.loads(js_sound)
print("\njson vib\n", js_vib)
print("\njson sound\n", js_sound)"""
# magnetisim_data=create_mock_vibration_data()
# sound_data=create_mock_ultrasound_data()
print("Vibration\n")

for i in js_vib:
    print(i)
print("\nSound\n")
for i in js_sound:
    print(i)
mycol3.insert_many([{'data': doc} for doc in js_sound])
mycol2.insert_many([{'data': doc} for doc in js_vib])
print("\n vibration data\n ")


"""
myclients.drop_database("mydatabase")
myclients.drop_database("deneme")
"""
print("\n vibration  data\n ")

for i in mycol2.find():
    print(i)
print("\n sound  data\n ")

for i in mycol3.find():
    print(i)
vib_json = json.loads(mycol2)
sound_json = json.loads(mycol3)


print("\n vibration  data\n ")

for i in vib_json:
    print(i)
print("\n sound  data\n ")

for i in sound_json:
    print(i)
