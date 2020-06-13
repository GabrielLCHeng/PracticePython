# this one uses a for loop
def deldupe_v1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

#this one uses sets
def deldupe_v2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print(a)
print(deldupe_v1(a))
print(deldupe_v2(a))