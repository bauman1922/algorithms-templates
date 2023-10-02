n = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
target = int(input())
res = []
for x in range(0, len(arr)):
    for y in range(x + 1, len(arr)):
        if arr[x] * arr[y] == target:
            res.append(target)
            break

if res:
    print("ДА")
else:
    print("НЕТ")