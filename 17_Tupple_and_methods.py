# To create a tuple
tup=("hii",1,3,4,5)
# print(tup)
# print(tup[1:4])
# print(tup[1:])
# print(tup[:4])
# if 'hii' in tup:
#     print("yes present")
# else:
#     print("no")

# To manipulate a tuple
# temp=list(tup)
# temp.append("yooohoohoho")
# temp.insert(3,"dehehe")
# tup=tuple(temp)
# print(tup)

# To concatenate tuple
tup2=(2,4,5,3,21,45)
tupf=tup+tup2
print(tupf)
print(tupf.count(4))
print(tupf.index(21))
print(len(tupf))