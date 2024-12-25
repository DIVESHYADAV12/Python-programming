# Default Argument

# def identity(name="Name",cource="BCA",collage="ALLAHABAD UNIVERSITY"):
#     print("Identity is :")
#     print(name,"\n",cource,"\n",collage)

# identity("Divesh yadav","BCA","University of allahabad")    


# Keyword Argument

# def avg(a=20,b=20):# Default argument
#     print("The average is :",(a+b)/2 )
# # Calling the function
# avg(b=13,a=45) # Keyword argument
# avg() 


# # Required argument

# def avg(a,b): # a and b are required argument
#     print((a+b)/2)
# # calling function
# avg(67,87)  


# Variable length argument

def avg(*num):
    sum=0
    for i in num:
        sum=i+sum
    print("Average is: ",sum/len(num) )  
# calling the function
avg(34,45,67,3,78,2,45,2,65)   
