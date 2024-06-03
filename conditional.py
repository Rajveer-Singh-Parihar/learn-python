#CONDITIONAL STATEMENT => ALLOWS YOU TO MAKE DECISION BASED ON THE VALUES OF VARIABLES.
#TRAFFIC LIGHT CODE

light = input("light Color:")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("you can go")
else:
    print("Light is Broken")

#GRADE OF THE STUDENT
    marks = int(input("marks of student:"))
    if(marks>=90):
        print("A++")
    elif(marks>=80 and marks<90):
        print("A")
    elif(marks>=60 and marks<80):
        print("B")
    elif(marks>=33 and marks<60):
        print("C")
    else:
        print("Sorry you are fail")

#SINGLE LINE CONDITIONAL STATEMENT
food = input("food is:")
eat = "yes" if food == "cake" else "no"
print(eat)

#ANATHER EXAMPLE OF CONDTIONAL STAMENT
food = input("food :")
print("sweet") if food == "cake" or food == "pastry" else print("SPICY")

#NESTED LOOPS
age =34
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")