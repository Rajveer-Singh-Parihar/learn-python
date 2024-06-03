#DICTIONARY => Dictionary are used to store data values in key :value pairs. they are unordered , mutable (changebale) & dont allow duplicate keys.
# they store multiple items in a single variable and enclosed with curly braces {}.
info ={
    "name" : "rajveer",
    "age": 21,
    "subject": ["python" ,"c" ,"c++","Java"]
}
info["name"] = "rajveersinghparihar"
print(info)

#NESTED DICTIONARY
student = {
    "name": "rudra",
    "score":{
        "chem" : 88,
        "physics" : 89,
        "maths": 95
    }
}
print(student)

#DICTIONARY METHODS
student.keys() #returns all keys
student.values() #returns all values
student.items() #returns all (key,val) pairs as tuples
student.get("name") #returns the key according to value
student.update({"city" : "delhi"})#inserts the specified items  to the dictionary
print(student)