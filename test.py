import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="Adwai31",
        host="localhost",
        port="5432",
        database="lexus"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
except Exception as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
