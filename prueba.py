import psycopg2

conn = None
cursor = None

try:
    conn = psycopg2.connect(host="192.168.122.98", dbname="maravilla", user="admin", password="admin")
    cursor = conn.cursor()
    sql_query = "select * from pelicula;"
    cursor.execute(sql_query)
    result = cursor.fetchall()  # fetchone()
    print (result)
except Exception as e:
    print("No puedo conectar a la base de datos:",e)
