import pymongo
import sys
import pprint

from my_mongo import *

tab_name = "users"

def main():
	port = sys.argv[1]
	name = sys.argv[2]
	_id = sys.argv[3]

	db = get_db(port)
	uid = raise_user_id(db, name, _id)
	print("uid", uid)
	if uid == "":
		print("input not correct~")
 		return

	col = db[tab_name]
	doc = col.find({"_id" : bson.Int64(uid) })
	for x in doc:
		print("find uid:[%s]~" % uid)
		pprint.PrettyPrinter().pprint(x)
		#print(x)
	pass

if __name__ == '__main__':
	main()
