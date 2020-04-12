import pymysql
from datetime import datetime  
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

conn=pymysql.connect(host="remotemysql.com",user="LCrnOoIotj",passwd="zbWSCnehu1",db="LCrnOoIotj")
myCursor=conn.cursor()

query = """INSERT INTO starttime (start_time)  VALUES ( %s)"""
data = (now)
myCursor.execute(query, data)

#last id
myCursor.execute('SELECT last_insert_id()')
print(myCursor.fetchone())

# myCursor.execute(f"INSERT INTO starttime_str(id,start_time)VALUES(2,{now});")
# print(">data submitted")

# myCursor.execute("SELECT * FROM starttime")
# print(myCursor.fetchall())

#myCursor.execute("DELETE FROM info WHERE id=1;")
#print(">data deleted")

#myCursor.execute("UPDATE info SET name='rutuperna' WHERE id=2;")
#print(">data updated")


conn.commit()
conn.close()