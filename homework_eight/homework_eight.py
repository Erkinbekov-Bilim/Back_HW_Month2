import sqlite3


def connect_or_create_db():
    return sqlite3.connect('user_with_grades.db')


def create_table():
    connect_or_create_db()
    connect = connect_or_create_db()
    cursor = connect.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER,
            subject VARCHAR(100) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (userid) REFERENCES users(id)
        )
    ''')

    connect.commit()
    connect.close()


def add_user(fio, age):
    connect = connect_or_create_db()
    cursor = connect.cursor()
    cursor.execute(
        'INSERT INTO users (fio, age) VALUES (?, ?)',
        (fio, age)
    )
    connect.commit()
    connect.close()

def add_grade(userid, subject, grade):
    connect = connect_or_create_db()
    cursor = connect.cursor()
    cursor.execute(
        'INSERT INTO grades (userid, subject, grade) VALUES (?, ?, ?)',
        (userid, subject, grade)
    )
    connect.commit()
    connect.close()

def get_user_with_grades():
    connect = connect_or_create_db()
    cursor = connect.cursor()

    cursor.execute('''
        SELECT users.id , users.fio, grades.subject, grades.grade
        FROM users
        LEFT JOIN grades ON users.id = grades.userid
        
    ''')

    rows = cursor.fetchall()
    print(rows)

    for row in rows:
        print(row)

    connect.close()

create_table()

# add_user('Ardager', 25)
# add_user('Maxim', 25)
#
# add_grade(1, "Algebra", 3)
# add_grade(1, "Rus-Lang", 2)
# add_grade(2, "Algebra", 5)
add_user("Max", 45)
get_user_with_grades()