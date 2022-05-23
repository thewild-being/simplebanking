import sqlite3

# _____________________________SQLITE actions per muoversi nel DB
CREATE_CARDS_TABLE = """CREATE TABLE IF NOT EXISTS cards (id INTEGER PRIMARY KEY, number TEXT, pin TEXT,
                     balance INTEGER DEFAULT 0); """
INSERT_CARDS = "INSERT INTO cards (number, pin) VALUES (?, ?); "

UPDATE_BALANCE = """UPDATE cards SET balance = (?) WHERE id = (SELECT MAX(id) FROM cards);"""

SEE_DB = "SELECT * FROM cards;"

CHECK_CARD = "SELECT * FROM cards WHERE number = (?);"

DROP_ACCOUNT = "DELETE FROM cards WHERE id = (SELECT MAX(id) FROM cards);"

COMMIT = "COMMIT;"


# _____________________________FX per chiamare azioni SQLITE
# _____________________________per connettere e creare un file in cui store the data
def commit(connection):
    with connection:
        return COMMIT


def connect():
    return sqlite3.connect('card.s3db')


def create_table(connection):
    with connection:
        connection.execute(CREATE_CARDS_TABLE)


# _____________________________per aggiungere rows nel db
def add_cards(connection, number, pin):
    with connection:
        connection.execute(INSERT_CARDS, (number, pin))
        # return connection.execute(INSERT_CARDS, (number, pin, balance)).fetchall()


def add_balance(connection, balance):
    with connection:
        connection.execute(UPDATE_BALANCE, (balance,))


# _____________________________per vedere nel db
def see_db(connection):
    with connection:
        return connection.execute(SEE_DB).fetchall()


def check_cards(connection, number):
    with connection:
        return connection.execute(CHECK_CARD, (number,))


def delete_card(connection):
    with connection:
        return connection.execute(DROP_ACCOUNT)


def save(connection):
    with connection:
        return COMMIT

"""
EMPTY = "DELETE * FROM cards;"


def empty_cards(connection):
    with connection:
        return EMPTY
"""
