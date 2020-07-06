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

for i in range(0, len(a)):
    minx = a[i]
    ctx = i
    for j in range(i, len(a)):
        if minx < a[j]:
            minx = a[j]
            ctx = j
    if ctx != i:
        a[ctx] = a[i]
        a[i] = minx

print("select sorting avg time :", time.time() - start) #걸린 시간 출력
ha = len(a)/2 ; ha = int(ha)
tmp = a[0]
for i in range(0, ha):
    a[i] = a[i+1]
a[ha] = tmp

start = time.time()  # 시작 시간 저장

for i in range(0, len(a)):
    minx = a[i]
    ctx = i
    for j in range(i, len(a)):
        if minx < a[j]:
            minx = a[j]
            ctx = j
    if ctx != i:
        a[ctx] = a[i]
        a[i] = minx

print("select sorting worst time :", time.time() - start) #걸린 시간 출력