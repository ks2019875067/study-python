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

b = [None, ]
for i in a:
    b.append(i)
    ct = len(b)-1
    while ct > 1:
        ht = int(ct/2)
        if b[ct] < b[ht]:
            tmp = b[ct]
            b[ct] = b[ht]
            b[ht] = tmp
        ct = ht
for i in range(len(a)):
    a[i] = b[1]
    ct = 1
    b[1] = b[len(b)-1]
    b.pop(len(b)-1)
    while ct*2+1 <= len(b):
        if ct*2+1 == len(b):
            if b[ct*2] < b[ct]:
                tmp = b[ct*2]
                b[ct*2] = b[ct]
                b[ct] = tmp
                ct *= 2
            else:
                break
        elif b[ct*2]<b[ct*2+1]:
            if b[ct] > b[ct*2]:
                tmp = b[ct*2]
                b[ct*2] = b[ct]
                b[ct] = tmp
                ct *= 2
            else:
                break
        else:
            if b[ct] > b[ct*2+1]:
                tmp = b[ct*2+1]
                b[ct*2+1] = b[ct]
                b[ct] = tmp
                ct *= 2; ct+=1
            else:
                break
            
print("heap sorting avg time :", time.time() - start) #걸린 시간 출력