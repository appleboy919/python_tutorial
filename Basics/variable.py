# ERROR
#print("this is an error" +123)


#Global vs local 
f = 1234
def someFunction():
    f="def"
    print(f)

someFunction()
print(f)

# del f
# print(f)