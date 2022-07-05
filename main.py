import json
import jsonpatch
import pymysql
import mysql.connector
from mysql.connector import Error
from connect import connection

'''n_data = {
    "users": [{
        "id": users[0][0],
        "name": users[0][1],
        "age": users[0][2]
    },
        {
            "id": users[1][0],
            "name": users[1][1],
            "age": users[1][2]
        }
    ]
}'''


"""def write(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        tests = json.load(file, indent=4)
        for test in tests:
            try:
                if 'expected' is not test:
                    continue
            except Exception:
                if test.get('error'):
                    continue
                else:
                    raise
"""


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
    # data = json.dumps(data)
    # data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)



# for user in users:
#    print(users)


# print(len(users))

# print(users)


def json_patch_write(query, connection):
    cursor = connection.cursor()
    try:

        cursor.execute(query)
    except Error as er:
        print(f"The error '{er}' occurred")


def json_patch_read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


'''def json_patch():
    second_data = json_patch_read('data.json')
    first_data = first_status(connection, select_users)'''


# n_data = read_json("data.json")

select_users = "SELECT * FROM users"
users = first_status(connection, select_users)
write_to_json('data.json', users)
