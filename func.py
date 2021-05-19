import sqlite3


def connect():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS phonebook(id INTEGER PRIMARY KEY, name TEXT,family TEXT, number INTEGER)")
    conn.commit()
    conn.close()


def insert(name, family, number):
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook VALUES(NULL,?,?,?)",
                (name, family, number))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    # کامیت را نمیزاریم چون نمیخوایم تغییر انجام بدیم وقت میخوایم نمایش بدیم
    conn.close()
    return rows


def search(name="", family="", number=""):
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name=? OR family=? OR number=? ",
                (name, family, number))
    rows = cur.fetchall()
    conn.close()
    return rows


def delet(id):
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE id=?", (id,))

    conn.commit()
    conn.close()


def update(id, name, family, number):
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET name=?,family=?,number=? WHERE id=?",
                (name, family, number, id))
    conn.commit()
    conn.close()


connect()

# print(search(author="amir"))
