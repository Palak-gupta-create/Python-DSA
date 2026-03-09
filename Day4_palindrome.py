n, m = map(int, input().split())

passed = 0

for i in range(n):
    marks = list(map(int, input().split()))

    avg = sum(marks) / m

    if avg > 50:
        passed += 1

print(passed)