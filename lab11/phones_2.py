import psycopg2 as pgsql

connection = pgsql.connect(
    host = 'localhost',
    dbname = 'postgres',
    user = 'postgres',
    password = 'hhhohoh'
)

cur = connection.cursor()

def insert(name, surname, phone_number):
    cur.execute(
        "SELECT count(*) FROM phone_book WHERE name='{}' AND surname='{}'".format(name, surname))
    if cur.fetchone()[0] == 0:
        cur.execute("""INSERT INTO phone_book VALUES ('{}','{}', {})""".format(
            name, surname, phone_number))
    else:
        cur.execute("""UPDATE phone_book
         SET phone_number={}
         WHERE name='{}' AND surname='{}'
         """.format(phone_number, surname, name))

name = str(input("name: "))
surname = str(input("surname: "))
phone_number = str(input("phone: "))
insert(name, surname, phone_number)
connection.commit()