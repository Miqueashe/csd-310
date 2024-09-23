import mysql.connector

# Connect to MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='PC-7C61205958',      # Replace with your MySQL host
            user='Miqueas',           # Replace with your MySQL username
            password='Coolcat11!', # Replace with your MySQL password
            database='movies'   # Replace with your database name
        )
        if connection.is_connected():
            print("Successfully connected to the database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to execute queries and fetch results
def execute_query(query, description):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        print(f"\n-- {description} --")
        for row in results:
            print(row)

        cursor.close()
        connection.close()

# Query 1: Select all fields from the Studio table
query1 = "SELECT * FROM Studio;"
description1 = "DISPLAYING Studio RECORDS"

# Query 2: Select all fields from the Genre table
query2 = "SELECT * FROM Genre;"
description2 = "DISPLAYING Genre RECORDS"

# Query 3: Select movie names with runtime less than 2 hours (less than 120 minutes)
query3 = """
    SELECT film_name, film_runtime 
    FROM Film 
    WHERE film_runtime < 120;
"""
description3 = "DISPLAYING Short Film RECORDS"

# Query 4: Select film names and directors, grouped by director
query4 = """
    SELECT film_name, film_director 
    FROM Film 
    ORDER BY film_director;
"""
description4 = "DISPLAYING Director RECORDS in Order"

# Execute each query
execute_query(query1, description1)
execute_query(query2, description2)
execute_query(query3, description3)
execute_query(query4, description4)
