# FUNCTIONS => Block of statements that perform a specific task.
# BUILT IN FUNCTION => print(), len(),type(),range(),dict(),list(),set(),print() etc.
# USER DEFINED FUNCTIONS => when we create function to perform a task as per our need is known as user defined function.

def sum(a,b):  # parameters
    s = a+b
    return s
print(sum(5,4)) # function call or arguments
print(sum(12,18))

def hello():
    print("hello rajveer singh parihar")
    hello()
    hello()

def calculate(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
calculate(2,4,6)

def name(fname , lname):
    print("hello :",fname ,lname)
    name("rajveer","singh")

 # RECURSION => WHEN A FUNCTION CALLS ITSELF REPEATEDLY IS CALLED RECURSION.
    def show(n):
        if(n==0):
            return 
        print(n)
        show(n-1)
        show(5)

        def fact(n):
            if(n ==0 or n==1):
                return 1
            else:
                return n*fact(n-1) # 7 * 6!
            print(fact(7))