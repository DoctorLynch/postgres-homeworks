"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

# employees
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='02011999')
cur = conn.cursor()
with open('/Users/Катюша/postgres-homeworks/homework-1/north_data/employees_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропустит первую строчку
    for row in reader:
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
conn.commit()

# customers
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='02011999')
cur = conn.cursor()
with open('/Users/Катюша/postgres-homeworks/homework-1/north_data/customers_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропустит первую строчку
    for row in reader:
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
conn.commit()

# orders
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='02011999')
cur = conn.cursor()
with open('/Users/Катюша/postgres-homeworks/homework-1/north_data/orders_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропустит первую строчку
    for row in reader:
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)
conn.commit()