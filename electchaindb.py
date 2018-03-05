import sqlite3

def createdb():
    # conectando...
    conn = sqlite3.connect('electchain.db')
    # definindo um cursor
    cursor = conn.cursor()

    # table blockchain

    cursor.execute("""
    CREATE TABLE blockchain (
            id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            hash varchar(256) NOT NULL,
            proof integer NOT NULL,
            transactions BLOB NOT NULL,
            polls BLOB,
            votes BLOB,
            lasthash varchar(256),
            minedby varchar(256),
            minedat timestamp
    );
    """)

    # table transaction

    cursor.execute("""
    CREATE TABLE transactions (
        hash varchar(256) NOT NULL PRIMARY KEY,
        sender varchar(256) NOT NULL,
        reciever varchar(256) NOT NULL,
        signature varchar(256) NOT NULL,
        ammount real NOT NULL,
        poll varchar(256),
        createdat timestamp,
        fee real NOT NULL,
        block varchar(256)
    );
    """)

    # table poll
    cursor.execute("""
    CREATE TABLE poll (
        hash varchar(256) NOT NULL PRIMARY KEY,
        creator varchar(256) NOT NULL,
        signature varchar(256) NOT NULL,
        createdat timestamp,
        name TEXT NOT NULL,
        description TEXT,
        startat timestamp,
        endat timestamp,
        tip real NOT NULL,
        nominees BLOB NOT NULL,
        block varchar(256)
    );
    """)

    # table vote
    cursor.execute("""
    CREATE TABLE vote (
        hash varchar(256) NOT NULL PRIMARY KEY,
        sender varchar(256) NOT NULL,
        reciever varchar(256) NOT NULL,
        signature varchar(256) NOT NULL,
        poll varchar(256),
        createdat timestamp,
        block varchar(256)
    );
    """)
