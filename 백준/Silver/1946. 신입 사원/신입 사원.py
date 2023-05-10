t = int(input())

for _ in range(t):
    n = int(input())

    app = []
    for _ in range(n):
        doc, con = map(int, input().split())
        app.append([doc, con])

    app.sort()

    worker = [app[0]]
    for i in range(1, n):
        if app[i][1] < worker[-1][1]:
            worker.append(app[i])
    print(len(worker))