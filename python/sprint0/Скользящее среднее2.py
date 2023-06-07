n = int(input())
arr = list(map(int, input().split()))
k = int(input())

result = []
window_sum = sum(arr[:k])
result.append(window_sum / k)

for i in range(k, n):
    window_sum += arr[i] - arr[i - k]
    result.append(window_sum / k)

print(*result)