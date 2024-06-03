#LISTS => A LIST IS DATATYPE THAT STORES SET OF VALUE . LIST IS ORDERED COLLECTION OF DATA ITEMS. STORE MULTIPLE ITEMS IN SINGLE VARIABLE.

# we can store elements of different types (integer , float , string etc)

# marks =  [ 88, "karan", 18 , "delhi"] - store differnt items.

marks = [87,56,55,44,77] 
print(marks)
print(marks[0])
print(marks[1])
print(marks[1:4]) # not 4 but 1-3
print(marks[-3:-1]) # -1 nahi reverse order me negative indexing hoti hai 77 = -1

# LIST METHODS
list = [2,1,3]
list.append(4) # add one element at the end [2,1,3,4]
list.sort() # sorts in ascending order[1,2,3]
list.sort(reverse=True) # sorts in decending order [3,2,1]
list.reverse() # reverse list [3,1,2]
list.insert(1,5) #insert element at index [2,5,1,3]
list.remove(1) # remoes the first occurence of the string [2,3]
list.pop(2) # removes the 2nd index element [2,1]
print(list)