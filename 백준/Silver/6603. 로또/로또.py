from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr.pop(0)
    comb = list(combinations(arr, 6))
    for i in range(len(comb)):
        for j in range(6):
            print(comb[i][j], end=" ")
        print()
    print()