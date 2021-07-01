Anya, Borya = map(int, input().split())
n = set()
m = set()
for i in range(Anya):
    n.add(int(input()))
for i in range(Borya):
    m.add(int(input()))

print(len(n.intersection(m)))
print(*sorted(n.intersection(m)))
print(len(n.difference(m)))
print(*sorted(n.difference(m)))
print(len(m.difference(n)))
print(*sorted(m.difference(n)))