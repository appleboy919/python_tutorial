import sqlite3


def main():
    print('connect')
    db = sqlite3.connect('Database/db-api.txt')
    # grab a cursor from database handle to keep track while running the database cmds
    cur = db.cursor()
    print('create')
    cur.execute('DROP TABLE IF EXISTS test')
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('four', 4)
        """)

    # commit
    print('commit')
    db.commit()

    # count row number
    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')
    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()


if __name__ == '__main__':
    main()


# Python DB-API is consolidated interface for numbers of databse systems
# though it's not exactly the same for every DB System
# sqlite3 API is suitable for online, mobile database system
