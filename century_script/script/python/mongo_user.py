import pymongo
import sys

from my_mongo import *



def main():
    port = sys.argv[1]
    name = sys.argv[2]

    db = get_db(port)

    col = db[tab_name]
    uid = get_user_id(db, name)
    print("uid", int(uid))

if __name__ == '__main__':
	main()
