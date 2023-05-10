n = int(input())
# arr = list([0] * 20 for _ in range(20))

lst = []
for _ in range(n):
    l, h = map(int, input().split())
    lst.append([l, h])
#     for i in range(0, h):
#         arr[i][l] = 1

# print(arr)

# 리스트 순서대로 정렬
lst.sort()

# 가장 큰 높이값
maxH = max(lst, key = lambda x:x[1])[1]

# 가장 큰 높이값의 인덱스
maxL = lst.index(max(lst, key = lambda x:x[1]))

# 첫번째 ~ 가장 높은 값 인덱스
nh = lst[0][1]
dap = 0
for i in range(maxL):
    # 다음 인덱스 높이가 현재 높이값보다 높으면
    # 다음 인덱스 전까지의 면적 더하고
    # 현재 높이값 바꿔줌
    if nh < lst[i+1][1]:
        dap += nh * (lst[i+1][0] - lst[i][0])
        nh = lst[i+1][1]
    # 그렇지 않으면 다음 인덱스 전까지의 면적만 더해줌
    else:
        dap += nh * (lst[i+1][0]-lst[i][0])

# 마지막 ~ 가장 높은 값 인덱스
nh = lst[-1][1]
for i in range(n-1, maxL, -1):
    # 전 인덱스 높이가 현재 높이값보다 높으면
    # 전 인덱스까지의 면적 더하고
    # 현재 높이값 바꿔줌
    if nh < lst[i-1][1]:
        dap += nh * (lst[i][0] - lst[i-1][0])
        nh = lst[i-1][1]
    # 그렇지 않으면 전 인덱스까지의 면적만 더해줌
    else:
        dap += nh * (lst[i][0]-lst[i-1][0])
        
# 가장 높은 값 인덱스의 높이 더하기
print(dap+maxH)


