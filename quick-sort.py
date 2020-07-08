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

def quick_sort(arr):
    def sort(low, high):
        if high > low:
            mid = partition(low, high)
            sort(low, mid - 1)
            sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)
    
quick_sort(a)

print("quick sorting avg time :", time.time() - start) #걸린 시간 출력