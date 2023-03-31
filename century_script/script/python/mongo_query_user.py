import pymongo
import sys

from my_mongo import *



def main():
    port = sys.argv[1]
    name = sys.argv[2]
	_id = sys.argv[3]

    db = get_db(port)

    col = db[tab_name]
    uid = get_user_id(db, name)
    print("uid", int(uid))
	if uid == "":
		acc = get_user_acc(db, _id)
		if acc == "":
			print("neither %s nor %s correct~" % (name, _id))
			return _id	
	print("uid", int(_id))

if __name__ == '__main__':
	main()
