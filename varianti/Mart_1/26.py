def pd(arr):
    ans = 1
    p = 0
    while p < len(arr):
        i = 1
        while p + i < len(arr) and arr[p + i] == arr[p] + i:
            i += 1
        ans = max(ans, i)
        p += i
    return ans


base = ''
fd = open(base + '26.txt')
N = int(fd.readline())
tasks = {}
for line in fd:
    i, n = map(int, line.split())
    if tasks.get(i):
        tasks[i].append(n)
    else:
        tasks[i] = [n]
arr = [(pd(sorted(v)), -k) for k, v in tasks.items()]
arr.sort(reverse=True)
print(-arr[0][1], arr[0][0])