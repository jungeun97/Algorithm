x, y, w, h = map(int, input().split())
dap = min(abs(y - 0), abs(y - h), abs(x - 0), abs(x - w))
print(dap)