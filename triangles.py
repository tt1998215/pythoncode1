def triangles():
    N=[1]
    while True:
        yield N
        N.append(0)
        N = [N[i - 1] + N[i] for i in range(len(N))]


results = []
n=0
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break