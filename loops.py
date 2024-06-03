# LOOPS => Loops are used to repeat instruction.

# WHILE LOOP => While loop we can execute a set of statement as long as a condition is true.
count = 1
while(count<=5):
    print("hello")
    count += 1 #count = count+1

#BREAK => Used to terminate the loop when encountered.
    i =0
    while(i<=5):
        if(i==4):
            break
        print(i)
        i += 1

#CONTINUE => terminate execution in the current iteration & continue execution of the loop with the next iteration.
        i =0
    while(i<=5):
        if(i==4):
            continue
        print(i)
        i += 1

# FOR LOOPS => Are used for sequential traversal . for traversing list ,string,tuples etc.
nums = [1,2,3,4,5]
for val in nums :
    print(val)

friends = ("vijendra" ,"mohinder","pradeep ji","chauhan saab")
for rajveer in friends :
    print(rajveer)
     
# RANGE() => range function returns a sequence of numbers , starting from 0 by default and increments bt 1 (by deafault) ans stops before a specified number.
for el in range(5):
    print(el) # 0,1,2,3,4

for ell in range(1,5):
     print(ell)

for raj in range(1,5,2): #start , stop , step -1,3
    print(raj)

for ell in range(1,22,3): # output - 1,4,7,10,13,16,19 - not 22
     print(ell)

# PASS STATEMENT => Pass is a null statement that does nothing . it is used a placeholder for future code
     for el in range(10):
         pass     #used to skip the code where we can put some code in the future
     print("useful work")