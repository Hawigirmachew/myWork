lists=[5,6,1,3,4]

#To find the multiplication of lists
print("The multiplication of items in list")
def mult_items(items):
  mult = 1
  for x in items:
    mult*=x
  return mult

print(mult_items(lists))
print("The largest item  in list")
#TO find the max of lists

lists.sort(reverse=True)
print(lists[0])
#Other way to do it
print("The largest item  in list")
def max_list(items):
  max= items[0]
  for x in items:
    if x > max:
      max = x
  return max
print(max_list(lists))
# To get the smalllest value from the list
print("The smallest item  in list")
lists.sort()
print(lists[0])
#Other way to do it
print("The smallest item  in list")
def min_list(items):
  min= items[0]
  for x in items:
    if x < min:
      min = x
  return min
print(min_list(lists))
#Strings count 
print("Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings")
stringList = ['abc', 'xyz', 'aba', '1221']
def count_strings(lists):
  count = 0
  for x in lists:
    if len(x) > 2 and x[0]==x[-1]:
      
      count+=1
  return count 
print(int(count_strings(stringList)))
#sort tuple inside a list by the last item in each
print("sort tuple inside a list by the last item in each")
tuple_list_sort = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
tuple_list_sort.sort(key = lambda i:i[1])
print(tuple_list_sort)
#To remove duplicate items from list
print("Removes Duplicates")
dupLists=[2,3,4,4,5,6,6]
print(dupLists)

def duplicate_items(dup_lists):
  lists_non_dup = []
  for x in dup_lists:
    if x not in lists_non_dup  :
      lists_non_dup .append(x)
  return lists_non_dup 
print( duplicate_items(dupLists))
#other way to do it
"""listsNonDup = list(dict.fromkeys(dupLists))
print(listsNonDup)"""
#check if list is empty or not
print("Check if list is empty or not")
def check_emptyList(items):
  if len(items) <= 0:
    print("The list is empty")
  else:
    print("The list is not empty")
check_emptyList(lists)
#To copy a list
print("Copy")
#names=["Hawi","Miliki","GGS","Emebet"]
names = lists.copy()
print(names)
# to find the list of words that are longer than n from a given list of words
print("Enter a length of number you want to display:")
n = int(input())

names=["Hawi","Miliki","GGS","Emebet"]
def number_items(strs):
  res=[]
  for x in names:
    if len(x) > n:
      res.append(x)
    
  
  return res
print(number_items(names))
#Python function that takes two lists and returns True if they have at least one common member.
def commonNumber(list1,list2):
  checker = False
  for x in list1:
    for y in list2:
      if x == y:
        checker = True
        break
  return checker
list3 = [7,90]
print(commonNumber(lists,list3)) 
#Python program to print a specified list after removing the 0th, 4th and 5th elements.

names=["Hawi","Miliki","GGS","Emebet","Muna","Mimi"]
names = [x for (i,x) in enumerate(names) if i not in (0,4,5)]
print(names)

  
    































