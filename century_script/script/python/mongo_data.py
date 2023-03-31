import pymongo
import sys
import pprint

from my_mongo import *

def main():
    port = sys.argv[1]
    name = sys.argv[2]
    tab_name = sys.argv[3]

    db = get_db(port)
    uid = get_user_id(db, name)
    print("uid", uid)

    col = db[tab_name]
    doc = col.find({"_id" : { "uid" : uid, "key" : 0 }})
    for x in doc:
        print(x)
    pass

if __name__ == '__main__':
	main()
