import time
import sqlite3
a = []
con = sqlite3.connect("testDB.db")
cur = con.cursor()
cur.execute("select x from randX")
start = time.time()
rows= cur.fetchall()
for i in rows:
    a.append(i[0])
print("input time :", time.time() - start) #걸린 시간 출력
start = time.time()  # 시작 시간 저장

for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else: break

print("insert sorting avg time :", time.time() - start) #걸린 시간 출력

start = time.time()  # 시작 시간 저장

for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j] > a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else: break

print("insert sorting worst time :", time.time() - start) #걸린 시간 출력