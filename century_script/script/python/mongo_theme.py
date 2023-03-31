import sys
sys.path.append("/Users/chenpeng/yX_Proj/spin_client/gen/proto")

import pymongo
import sys
import pprint

from my_mongo import *
import gen.proto as pb
# import gen.proto.slots_util_pb2 as pb_ut

tab_name = "themeStatus"

def main():
    port = sys.argv[1]
    name = sys.argv[2]
    theme_id = sys.argv[3]

    db = get_db(port)
    uid = get_user_id(db, name)
    print("uid", uid)
    print("theme_id", theme_id)

    col = db[tab_name]
    doc = col.find({"uid":uid, "themeId":int(theme_id)})
    for x in doc:
        data = x["data"]
        theme = unmarshal_data(data)
        x["data"] = None
        x["lastSpin"] = None
        print(x)
        print("themeStatus : \n", theme)
        show_extra(theme.Extra)

def show_extra(extra):
    for e in extra:
        print(e.Type, " : ", unmarshal_content(e.Content))


def unmarshal_content(data):
    n = pb.NumberStatus()
    n.ParseFromString(data)
    return n.Num

def unmarshal_data(data):
    theme = pb.ThemeStatus()
    theme.ParseFromString(data)
    return theme

if __name__ == '__main__':
	main()
