import pymysql
# conn=pymysql.connect(host="localhost",user="root",passwd="",db="python_db")
conn=pymysql.connect(host="remotemysql.com",user="LCrnOoIotj",passwd="zbWSCnehu1",db="LCrnOoIotj")
myCursor=conn.cursor()



myCursor.execute("INSERT INTO info(id,name)VALUES(2,'rutu');")
print(">data submitted")

myCursor.execute("SELECT * FROM info")
print(myCursor.fetchall())

#myCursor.execute("DELETE FROM info WHERE id=1;")
#print(">data deleted")

#myCursor.execute("UPDATE info SET name='rutuperna' WHERE id=2;")
#print(">data updated")


conn.commit()
conn.close()