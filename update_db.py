import pymysql
conn=pymysql.connect(host="localhost",user="root",passwd="",db="python_db")
myCursor=conn.cursor()


myCursor.execute("UPDATE info SET name='rutuperna' WHERE id=2;")
print(">data updated")


conn.commit()
conn.close()