import pymysql
conn=pymysql.connect(host="localhost",user="root",passwd="",db="python_db")
myCursor=conn.cursor()


myCursor.execute("SELECT * FROM info")
print(myCursor.fetchall())



conn.commit()
conn.close()