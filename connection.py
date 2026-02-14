import pymysql.cursors

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='hridya2006',
        database='zerowaste_connect',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connection successful!")
    # You can now perform database operations using the connection object
    # For example, to execute a query:
    # with connection.cursor() as cursor:
    #     sql = "SELECT * FROM your_table"
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     print(result)

except pymysql.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Connection closed.")
