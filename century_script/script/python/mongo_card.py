import pymongo
import sys
import pprint

from my_mongo import *

tab_name = "gathering"

def main():
    port = sys.argv[1]
    name = sys.argv[2]

    db = get_db(port)
    uid = get_user_id(db, name)
    print("uid", uid)

    col = db[tab_name]
    doc = col.find({"_id.uid" : uid }, {"pl.gathering.cards" : 1})
    for x in doc:
        # pprint.PrettyPrinter().pprint(x)
        
        cards = sorted(x["pl"]["gathering"]["cards"].items())
        for k in cards:
            print(k)
            # print("[id:%s num:%s]" % (k[1]["entry"], k[1]["num"]))
            # print("[id:%s num:%s]" % (cards[k]["entry"], cards[k]["num"]))
        pass
    pass

if __name__ == '__main__':
	main()
