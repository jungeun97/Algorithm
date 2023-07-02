n, m = map(int, input().split())
password = {}
for _ in range(n):
    a, b = input().split()
    password[a] = b
for _ in range(m):
    a = input()
    print(password[a])