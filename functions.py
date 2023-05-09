import datetime
import json

database = "database/database.json"

def update_user(user, data):
    with open(database, 'r', encoding='utf-8') as file:
        file_json = json.load(file)
    file_json.get(user).update(data)
    with open(database, 'w', encoding='utf-8') as file_wr:
        json.dump(file_json, file_wr, indent=2)
    return file_json[user]


def get_user(message):
    with open(database, 'r', encoding='utf-8') as file:
        file_json = json.load(file)
    user_info = message.json['from']
    id = str(user_info["id"])
    return file_json[id]


def get_user_from_call(message):
    with open(database, 'r', encoding='utf-8') as file:
        file_json = json.load(file)
    user_info = message.json['chat']
    id = str(user_info["id"])
    return file_json[id]


def get_add_user(message):
    """opens json file and check if user exist if 
        user does not exist add's and returns user info
        if user already exist updates last visited and
        returns user info"""
    user_info = message.json['from']
    id = str(user_info["id"])
    with open(database, 'r', encoding='utf-8') as file:
        file_json = json.load(file)
    if user_info["is_bot"] == False:
        if str(id) not in file_json.keys():
            new_user_object = {
                id: {
                    "user_id": id,
                    "user": user_info["first_name"],
                    "lang": " ",
                    "registered_date": datetime.datetime.now().isoformat(),
                    "is_new_user": True
                }
            }
            file_json.update(new_user_object)
            with open(database, 'w', encoding='utf-8') as file_wr:
                json.dump(file_json, file_wr, indent=2)
            return new_user_object[id]
        else:
            file_json[id]["is_new_user"] = False
            file_json[id]["last_visited"] = datetime.datetime.now().isoformat()
            with open(database, 'w', encoding='utf-8') as file_wr:
                json.dump(file_json, file_wr, indent=2)
            return file_json[id]


def set_lang(user_id, language):
    """sets user_id language and saves to json"""
    with open(database, 'r', encoding='utf-8') as file:
        file_json = json.load(file)
    file_json[user_id]["lang"] = language
    with open(database, 'w', encoding='utf-8') as file_wr:
        json.dump(file_json, file_wr, indent=2)
    return language


def first_name(user_id, name):
    """sets user_id first_name and saves to json"""
    with open(database, 'r', encoding='utf-8') as file:
        file_json = json.load(file)
    file_json[user_id]["first_name"] = name
    with open(database, 'w', encoding='utf-8') as file_wr:
        json.dump(file_json, file_wr, indent=2)
    return name
