# STRINGS => STRING IS DATA TYPE THAT STORES A SEQUENCE OF CHARACTERS. ANYTHING THAT ENCLOSED WITH DOUBLE QUOTATION OR SINGLE QUOTATION ARE CONSIDER AS STRING.
#CONCATINATION => "HELLO" + "WORLD" -> HELLOWORLD
#LENGTH OF STR => len(str)
var = "rajveer"
len1 = len(var)
print(len1)
#indexing => rajveer-0123456 - helps to access the character
str = "worldisbeautiful"
ch = str[4]
print(ch)
# SLICING =>  ACCESS THE PARTS OF STRING
str = "hamara name baban"
sh =str[1:4]#AMA -1se3 but not4
sh =str[0:4] #HAMA
sh =str[1:] # YAHA SE LAST INDEX TAK
sh =str[:4] # YAHA SE 4 TAK
print(sh) 

#NEGATIVE INDEXING
itr = "apple"
print(itr[-3:-1]) # 1 number ko chod ke - E
print(itr[-5:-1]) # ESCAPE VARIABLE E

# STRING FUNCTIONS
str = " i am a coder"
str.endswith("er") # return true if string ends with substring er
str.capitalize() #capatalize the 1st char
str.replace("a","r") # replace the occurence of old with new(a replace with r)
str.find("a") # return the 1st index of 1st occurence
str.count("am") # counts the occurence of the substring in string.