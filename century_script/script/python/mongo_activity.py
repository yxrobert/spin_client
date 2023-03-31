import pymongo
import sys
import pprint

from my_mongo import *

tab_name = "activity"

def main():
    port = sys.argv[1]
    name = sys.argv[2]
    act_id = sys.argv[3]
	_id = sys.argv[4]

    db = get_db(port)
    uid = raise_user_id(db, name, _id)
    print("uid", uid)
	if uid == "":
		print("error input")
		return 

    col = db[tab_name]
    content = "payload.activity.%s.content" % act_id
    doc = col.find({"owner" : uid }, {content : 1})
    for x in doc:
        # pprint.PrettyPrinter().pprint(x)
        print(x)
    pass

if __name__ == '__main__':
	main()
