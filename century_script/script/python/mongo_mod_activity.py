import pymongo
import sys
import pprint

from my_mongo import *

tab_name = "activity"

def mod_act_data(db, _id, condition, content, vals):
    col = get_act_tab(db)
    doc = col.find(condition, {content : 1})
    hit = False
    for x in doc:
        # print(x)
        pl = x["payload"]["activity"][_id]["content"]
        for m in pl:
            fs = pl[m]
            for k in fs:
                if k in vals:
                    print("mod", k, fs[k])
                    fs[k] = vals[k]
                    hit = True
            # print(fs)
            if hit:
                key = "payload.activity.%s.content.%s" % (_id, m)
                cmd = {"$set" : {key : fs}}
                col.update_one(condition, cmd)

def parse_val(s):
    l = s.split(",")
    m = {}
    for i in range(0, len(l), 2):
        m[l[i]] = l[i+1]
    return m

def main():
	port = sys.argv[1]
	name = sys.argv[2]
	act_id = sys.argv[3]
	_id = sys.argv[4]
	vals = parse_val(sys.argv[5])
	print(vals)

	db = get_db(port)
	uid = raise_user_id(db, name, _id)
	print("uid", uid)
	if uid == "":
		print("input not correct~")
		return
	
	col = db["activity"]
	content = "payload.activity.%s.content" % act_id
	condition = {"owner" : bson.Int64(uid)}
	if len(vals) > 0:
		mod_act_data(db, act_id, condition, content, vals)

	rd = col.find(condition, {content:1})
	for x in rd:
		pprint.PrettyPrinter().pprint(x)

if __name__ == '__main__':
	main()
