from collections import defaultdict

firstDict =  defaultdict(lambda: 0)

# print(firstDict)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = defaultdict(list)
print(d)
print(type(d))
for k, v in s:
    d[k].append(v)
    # print(k)
    # print(v)
    # print(d[k])
    # print('@'*20)

print(sorted(d.items()))
print(d)
print(type(d))  

new = defaultdict(int)
for i in 'uvbhjdbvjkemjnxmvjcfxmyugwnywkcjckwny7584383852890532057239578njckgfgf':
    new[i] += 1

print(sorted(new.items()))    

from collections import namedtuple

a = namedtuple('myClass', ['x', 'y'])
print(a)
x = a(11,22)
print(x)
print(x[0])

x, y = x
print(x, y)