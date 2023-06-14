import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mycursor.execute("insert into test1.test_table values(3424 , 'sudh' , 234 , 345.56 , 'kumar')")
mydb.commit()
mydb.close()
