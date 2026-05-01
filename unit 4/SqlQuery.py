import _sqlite3

def getData():
    connect = _sqlite3.connect("testDb1.sql")


    cursor = connect.cursor()

    query1= f"SELECT price FORM cumputers WHERE id ={computerSearch}"

    query= "SELECT model FROM computers"

    cursor.execute(query1)

    results = cursor.fetchall()

    print(results)


getData()