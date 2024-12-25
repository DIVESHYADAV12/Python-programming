str1="DiVEsh"
# to print all letters of a string in uppercase
print(str1.upper())
# to print all letters of a string in lowercase
print(str1.lower())
# to remove any white spaces before and after the string
a = "  hello world "
print(a.strip())
# to remove any trailing characters after a string
b = "heloo world !!!!!"
print(b.rstrip("!"))
# to replace all occurence of the string with another string
print(b.replace("heloo","hello"))
# print list splitted using specified instances of a string
print(a.split(" "))
# convert the first letter of the string into uppercase and rest in lowercase
print(b.capitalize(),str1.capitalize())
# align String to center as per the parameter
print(b.center(50))
# to count the no of times given value occer in the string
print(b.count('o'))
# checks if the string starts with the given vale or ends with given value respectively
print(a.startswith(' '))
print(b.endswith("!"))
# return the index of the given value in the string
print(str1.find("VEs"))
# return index of value if not present throws error
print(str1.index("h"))
# checks if the string is only cosist of 'a-z',A-Z','0-9'
print(str1.isalnum())
# checks if the string is only cosist of 'a-z',A-Z'
print(a.isalpha())
# checks wheather the string is lowecase or not
print(str1.islower())