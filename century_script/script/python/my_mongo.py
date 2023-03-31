import pymongo
import pprint
import bson

user = "root"
password = "passwd"
db_name = "plutus"

tab_name = "names"
tab_act = "activity"

def get_act_tab(db):
	return db[tab_act]

def get_db_tab(db):
	return db[tab_act]

def get_db(port):
	url = "mongodb://%s:%s@10.0.84.16:" + str(port) + "/"
	cli = pymongo.MongoClient(url % (user, password))
	return cli[db_name]

def get_user_id(db, name):
	col = db[tab_name]
	doc = col.find({"_id" : name})
	for x in doc:
		return x["uid"]
	return -1

def get_user_acc(db, _id):
	col = db[tab_name]
	doc = col.find({"uid" : bson.Int64(_id)})
	for x in doc:
		return x["_id"]
	return ""

def raise_user_id(db, name, _id):
	acc = get_user_acc(db, _id)
	if acc != "":
		return _id
	uid = get_user_id(db, name)
	return uid
		
