n = int(input('Enter the end of the range: '))
a = []
b = 0
for i in range(1,1000000000000000000):
    b = (24*i+1)**0.5
    if b%1 == 0 and int(b) < n:
        a.append(int(b))
    elif int(b) > n:
        break
for i in range(2,10):
    for z in a:
            if z%i  == 0:
                a.remove(z)
z = [y**2 for y in a]
for i in z:
    for hh in a:
        if hh == i:
            a.remove(hh)
aaa = [2,3,5,7]
a = a + aaa
print(sorted(a))
