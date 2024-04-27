import psycopg2

conn = psycopg2.connect(
	host = 'localhost',
    dbname = 'postgres',
    user = 'postgres',
    password = 'hhhohoh'
)

cursor = conn.cursor()
conn.commit()

name = str(input("name: "))
cursor.callproc('get_records', [name])
result = cursor.fetchall()
print(result)