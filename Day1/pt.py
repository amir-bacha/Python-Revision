# String
# String is data type that store  sequence of character e.g name="amir bacha"
#  if a string have five character then five size memory is allocated in memory
#   Note: spaces are  also counted
# string have indexes like array and starts from 0 
# string are immutable 
name ="Amir bacha"
print(type(name)),  # string 
print(len(name)) # 10 bc space is also counted
print (name[0])
# name[2]="k" this is not allowed bc string are not mutable

# Basic operation  on string 

string = "Hello" + "world"   # concatenation 
print(string) # Hello world

