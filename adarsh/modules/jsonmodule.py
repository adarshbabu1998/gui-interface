import json


x = '[1,2,3]'
print(type(x))
y = json.loads(x)

print(type(y))

m = (1,2,3)
print(type(m))

n = json.dumps(m)
print(type(n))