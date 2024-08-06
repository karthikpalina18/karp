from flask import Flask
import mysql.connector 
app=Flask(__name__)
con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)
mycursor=con.cursor()
a="insert into karthi values(%d,%s,%d,%d)"
val=(5,'cn',37,3456)
mycursor.execute(a,val)
print(mycursor)
datalist=mycursor.fetchall()
print(datalist)
mycursor.close()
con.close()


if __name__=='__main__':
    app.run(debug=True)