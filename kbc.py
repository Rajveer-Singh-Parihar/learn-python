questions = [
    ["Which Language is used to build facebook ?"
              ,"PYTHON","javascript","java","php",4],
["Which Language is used to build AMAZON ?"
              ,"PYTHON","javascript","java","c",4],
["Which Language is used to build flipkart ?"
              ,"PYTHON","c++","java","php",4],
["Which Language is used to build GOOGLE ?"
              ,"PYTHON","javascript","java","node.js",4],
["Which Language is used to build MEESHO ?"
              ,"PYTHON","javascript","java","c++",4],
["Which Language is used to build MEESHO ?"
              ,"PYTHON","javascript","java","c++",4]
]

levels = [1000,2000,5000,10000,15000,50000,100000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print("QUESTIONS FOR RS .{levels[i]}")
    print(f"a.{question[1]}     b.{question[2]}")
    print(f"c.{question[3]}     d.{question[4]}")
    
    reply = int(input("enter your answer (1-4)"))
    reply = int(input("enter your answer(1-4) or 0 to quit"))
    if(reply==0):
         money = levels[i-1]
         break
    
    if(reply==question[-1]):
        print(f"correct answer , you have won Rs.{levels[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money = 320000
    elif(i==14):
            money = 10000000
    else:
        print("wrong answer !!!")
        break
    print(f"you can take your money is  :{money}")
    
    
    

