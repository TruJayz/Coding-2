import _sqlite3.connect()



# 2. The connect method creats/starts or database 
connect = _sqlite3.connect()

# 3. The connect variable creates a new object that lets us send objects to our database
cursor = connect.curor()


# 4. we need to create a schem for our data
cursor.execute('''
create table computers
(id integer primary key, model text)''')

