n = str(input())
a=0
b=1

for i in range(0,len(n)):
    a=a+int(n[i])
    b=b*int(n[i])

total=b-a
print(total)