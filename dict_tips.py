# tips 01

d = {'apple':3, 'orange':2}

# the another way

d = dict(aplle=3, orange=2)

# tips 02 > combine the dicts

a = {1:1, 2:2}
b = {3:3, 4:4}

x = {**a, **b, 5:5}
print(x)

# tips 03 

def test(a, b, c):
  print(a, b, c)

mydict = dict(a=1, b=2, c=3)
test(**mydict)

# tips 04

d = {i:i**2 for i in range(1,5)}
print(d)

# OR

d = {(i,j):0 for i in range(2) for j in range(2,4)}
print(d)

# tips 05

d = {1:1, 2:2, 3:3}
print(d.get(1, 100)) # 1
print(d.get(4)) # None
print(d.get(9, 100)) # 100

# tips 06 > tuplas for dict

ls = [('apple', 4), ('orange', 5)]
d = dict(ls)
print(d)

# tips 07

d = dict(apple=4, orange=5)
print(d)

# for generate only values
for i in d.values():
  print (i)

#OR

for k,v in d.items():
  print(k,v)



