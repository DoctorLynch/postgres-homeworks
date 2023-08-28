"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

#  connect to database
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='02011999')
try:
    with conn:
        with conn.cursor() as cur:
            # execute query
            cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', (1, 'Nancy', 'Davolio' ,'Sales Representative', '1948-12-08', 'Education includes a BA in psychology from Colorado State University in 1970.  She also completed The Art of the Cold Call.  Nancy is a member of Toastmasters International.'
))
            cur.execute('SELECT * FROM employees')
            rows = cur.fetchall()
            for row in rows:
                print(row)
finally:
    conn.close()