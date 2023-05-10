s, c = map(int, input().split())
pa = []
for _ in range(s):
    pa.append(int(input()))

start = 1
# 최대한 많은 양의 파를 넣고 싶으므로 가장 긴 파
end = max(pa)
# 하나의 파닭에 들어가는 파의 길이
l = 0

# 이분 탐색
while start <= end:
    mid = (start + end) // 2
    
    # mid 길이일 때 나올 수 있는 파의 개수
    cnt = 0
    for i in pa:
        cnt += i//mid
    
    # 더 많은 양을 넣기 위해 mid길이 ++
    if cnt >= c:
        l = mid
        start = mid + 1
        
    # 치킨에 넣을 파 개수가 모자라므로 mid 길이 --
    else:
        end = mid - 1

# 전체 파 길이 - 치킨에 넣을 파
dap = sum(pa) - c*l
print(dap)