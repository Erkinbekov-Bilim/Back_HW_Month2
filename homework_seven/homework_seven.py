# CRUD - Create, Read, Update, Delete

import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER NOT NULL primary key AUTOINCREMENT,
        fio VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

def add_user(fio, age, hobby):
    cursor.execute(
        'INSERT INTO users(fio, age, hobby) VALUES (?,?,?)',
        (fio, age, hobby))
    connect.commit()
    print(f"Пользователь {fio} добавлен")


def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        # print(users)
        print("Список всех пользователей:")
        for user in users:
            print(f"ФИО: {user[1]}, возраст: {user[2]}, хобби: {user[3]}")
    else:
        print("Список пользователей пуст.")

def update_user(fio=None, age=None, hobby=None, rowid=None ):
    if fio:
        cursor.execute(
            'UPDATE users SET fio = ? WHERE rowid = ?',
            (fio, rowid))
        connect.commit()
    if age:
        cursor.execute(
            'UPDATE users SET age = ? WHERE rowid = ?',
            (age, rowid))
        connect.commit()
    if hobby:
        cursor.execute(
            'UPDATE users SET hobby = ? WHERE rowid = ?',
            (hobby, rowid))
        connect.commit()


def get_user_for_id(rowid):
    if rowid:
        cursor.execute('SELECT fio, hobby, age FROM users WHERE rowid = ?', (rowid,))
        print(f"Ползователь под номером {rowid}: {cursor.fetchone()}")



get_all_users()
get_user_for_id(1)

