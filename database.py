import sqlite3


def create_tables():
    with sqlite3.connect('db.db') as db:
        c = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS users ( 
                    msg_id INTEGER UNIQUE,
                    name_city TEXT,
                    client_desc TEXT,
                    contact_data TEXT,
                    market_place TEXT);
                    """
        c.execute(sql)
        sql = """DELETE FROM users"""
        c.execute(sql)
        db.commit()


def insert_name_city(msg_id, name_city):
    with sqlite3.connect('db.db') as db:
        c = db.cursor()
        c.execute("""INSERT INTO users (msg_id, name_city) values (""" + str(msg_id) + """, '""" + name_city + """')""")
        db.commit()


def insert_client_desc(msg_id, data):
    with sqlite3.connect('db.db') as db:
        c = db.cursor()
        sql = """Update users set client_desc = '""" + data + """' where msg_id = """ + str(msg_id)
        c.execute(sql)
        db.commit()


def insert_contact_data(msg_id, data):
    with sqlite3.connect('db.db') as db:
        c = db.cursor()
        sql = """Update users set contact_data = '""" + data + """' where msg_id = """ + str(msg_id)
        c.execute(sql)
        db.commit()


def insert_market_place(msg_id, data):
    with sqlite3.connect('db.db') as db:
        c = db.cursor()
        sql = """Update users set market_place = '""" + data + """' where msg_id = """ + str(msg_id)
        c.execute(sql)
        db.commit()


def select_user_data(msg_id):
    with sqlite3.connect('db.db') as db:
        c = db.cursor()
        sql = "select * from users where msg_id = " + str(msg_id)
        c.execute(sql)
        d = c.fetchone()
        delete_user(msg_id)
        return d


def delete_user(msg_id):
    with sqlite3.connect('db.db') as db:
        c = db.cursor()
        sql = """DELETE FROM users where msg_id = """ + str(msg_id)
        c.execute(sql)
        db.commit()