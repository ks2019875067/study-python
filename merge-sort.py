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
def sett(a): 
    def div( left, right):
        if right-left > 1:
            mid = (left + right)//2
            div(left, mid)
            div(mid, right)
            merge (left, right)
    def merge(left, right):
        act=[]
        mid = (left + right)//2
        lp = left; rp = mid
        while lp < mid and rp < right:
            if a[lp] < a[rp]:
                act.append(a[lp])
                lp += 1
            else:
                act.append(a[rp])
                rp += 1
        while lp < mid:
            act.append(a[lp])
            lp += 1
        while rp < right:
            act.append(a[rp])
            rp += 1
        for i in range(left, right):
            a[i] = act[i-left]
    div(0, len(a))
    return a

a = sett(a)
print("merge sorting avg time :", time.time() - start) #걸린 시간 출력