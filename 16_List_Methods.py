# Methods on list
# To sort any list
l=[1,4,6,8,3,2,4,1,4,73,2,0,]
# Asscending order
l.sort()
print(l)
# Descending Order
l.sort(reverse=True)
print(l)
# reverse the string
l.reverse()
print(l)
# Printing the index of the String
print(l.index(4))
# Count an element in the list
print(l.count(4))
# Copy a list and perform operations on it
m=l.copy()
m[0]=1000
print(m)
print(l)
# Append any number in end of the list
l.append(23323)
print(l)
# Inser any element at the given index
l.insert(3,"fourth")
print(l)
# Concatenate Two list
p=["a","b","c"]
l.extend(p)
print(l)
# Also
print(l+p)