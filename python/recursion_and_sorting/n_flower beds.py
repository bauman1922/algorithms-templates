def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


n = int(input())
intervals = []
for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

merged_intervals = merge_intervals(intervals)
for interval in merged_intervals:
    print(interval[0], interval[1])