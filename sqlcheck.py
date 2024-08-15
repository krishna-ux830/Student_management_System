import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kk@12345/",
        database="ORG"
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        cursor = connection.cursor()

        # query = "insert into t1 values (1, 'John')"
        # cursor.execute(query)

        query = "select * from faculty;"
        cursor.execute(query)
    
        results = cursor.fetchall()
        for row in results:
            print(row)

except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
