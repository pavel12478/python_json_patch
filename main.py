import json
import jsonpatch
import os
from mysql.connector import Error
from connect import connection


def first_status(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        row_headers = [x[0] for x in cursor.description]
        result = cursor.fetchall()
        json_data = []
        for rv in result:
            json_data.append(dict(zip(row_headers, rv)))
        return json.dumps(json_data, indent=4)
    except Error as er:
        print(f"The error '{er}' occurred")


def write_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        bool_json = os.stat('data.json').st_size == 0
        if bool_json == True:
            file.write(data)


def json_patch_write(query, connection):
    cursor = connection.cursor()
    try:

        cursor.execute(query)
    except Error as er:
        print(f"The error '{er}' occurred")


def json_read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


# def list_to_json():
#     alist = json_read('data.json')
#     jsonStr = json.dumps(alist, indent=4)
#     return jsonStr


def write_json_patch(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        jsonpatch.JsonPatch.to_string(data)
        file.write(str(data))


def json_patch():
    scr = json_read('data.json')
    dst = json.loads(first_status(connection, select_users))
    # dst = json.loads(users)
    patch = jsonpatch.make_patch(scr, dst)
    # print("scr", type(scr))
    # print("dst", type(dst))
    return patch


if __name__ == '__main__':
    select_users = "SELECT * FROM users"
    users = first_status(connection, select_users)
    # print(json_patch())
    write_json_patch('json_patch.json', json_patch())
    write_to_json('data.json', users)
