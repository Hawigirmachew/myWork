#Python program to convert a tuple to a dictionary
tup1=(("m",1),("h",2))
dict1 = dict(tup1)
print(dict1)
#Python program to unzip a list of tuples into individual lists. 
list1 = [(1,2,3),(4,5,4,6)]
print(list(zip(*list1)))
#Python program to reverse a tuple
tup2 =(1,2,3)
tup3=tuple()
for x in reversed(tup2):
  tup3 +=(x,)
print(tup3)
#print(tup2[::-1])
