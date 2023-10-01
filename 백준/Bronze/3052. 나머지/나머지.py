lst = set()
for _ in range(10):
    a = int(input())
    lst.add(a % 42)
print(len(lst))