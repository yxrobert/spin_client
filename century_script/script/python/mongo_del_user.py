import pymongo
import sys

from my_mongo import *

f_backup = "acc.backup"
acc_fmt = '[ port : %s ]\n{ "_id" : "%s", "uid" : NumberLong("%s") }\n'
def backup(port, name, uid):
	with open(f_backup, 'a+') as f:
		s = acc_fmt % (port, name, uid)
		f.write(s)

def main():
    port = sys.argv[1]
    name = sys.argv[2]

    db = get_db(port)
    col = db[tab_name]
    uid = get_user_id(db, name)
    print("check", name)
    print("uid", uid)
    if uid > 0:
        col.delete_one({"_id" : name})
        print("delete", name)
        backup(port, name, uid)
    else:
        print("Delete Failed!")
		

if __name__ == '__main__':
	main()
