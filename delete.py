import pymysql
conn=pymysql.connect(host="localhost",user="root",passwd="",db="python_db")
myCursor=conn.cursor()


myCursor.execute("DELETE FROM info WHERE id=1;")
print(">data deleted")


conn.commit()
conn.close()