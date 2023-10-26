l = [1, 2, 1, 23, 43, 55, 6, 7, 6]
l.sort()
l.append(9)
l.sort(reverse=True)
ind_l = l.index(43)
print(ind_l)
cont_l = l.count(1)
print(cont_l)

print(l)
m = l
m[0] = 89
print(l)
l.insert(3, 999)
print(l)

x = [122, 322, 343, 4454, 5656]
# x.extend(l)
print(x)
k = x + l
print(k)
