import pymysql
from datetime import datetime  
import time
starttime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

conn=pymysql.connect(host="remotemysql.com",user="LCrnOoIotj",passwd="zbWSCnehu1",db="LCrnOoIotj")
myCursor=conn.cursor()

query = """INSERT INTO bipros (start_time)  VALUES ( %s)"""
data = (starttime)
myCursor.execute(query, data)
print("starttime inserted", starttime)

#last id
myCursor.execute('SELECT last_insert_id()')
result = myCursor.fetchone()
id = result[0]
print("last id : ", id)

conn.commit()

def update_record_processed(record_processed):
    query = "UPDATE bipros SET record_processed = %s WHERE id = %s"
    data = (record_processed,id)
    print("updating", record_processed,id)
    myCursor.execute(query, data)

for i in range(5000):
    time.sleep(0.01)
    if i%500 == 0:
        update_record_processed(i)
        conn.commit()



print("finish")

conn.commit()
cursor.close()
conn.close()
