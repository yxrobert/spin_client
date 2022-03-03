from distutils.command import config
import re
import ConfigParser
from server_list import server_list

config_file = "config.ini"
def_section = "default"
user_section = "user"
theme_section = "theme"


conf = ConfigParser.ConfigParser()
conf.read(config_file)

def get_user_id():
    return conf.get(user_section, "user_id")

def get_account():
    return conf.get(user_section, "account")

def get_default_bet():
    return conf.get(theme_section, "default_bet")

def get_interval():
    return conf.get(theme_section, "reqest_interval")

def get_svr_url():
    return server_list[get_server()]

def get_server():
    return conf.get(def_section, "server")

def get_token():
    return conf.get(user_section, "token")

def save_user_data(token, user_id):
    conf.set(user_section, "token", str(token))
    conf.set(user_section, "user_id", str(user_id))
    save_all()

def save_all():
    with open(config_file, "w+") as f:
        conf.write(f)
