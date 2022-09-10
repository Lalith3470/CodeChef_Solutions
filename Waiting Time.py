testCases = int(input())
for testCase in range(testCases):
    k, x = map(int, input().split())
    print(k*7-x)
