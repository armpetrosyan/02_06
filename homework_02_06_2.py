arr = []
n = int(input())


for i in range(n):
    col = []
    for j in range(n):
        item = int(input())
        col.append(item)
    col.sort(reverse=True)
    arr.append(col)


a = []

for j in range(0, n):
    a.append(arr[j])

for k in range(0, n):
    arr[n-1-k] = a[k]


print(arr[0])
