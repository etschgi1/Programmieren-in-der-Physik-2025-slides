def callbyvalue(x):
    x = x + 1

def callbyreference(x):
    x[0] = 42

myvar = 11
myarr = [1, 2, 3]
callbyvalue(myvar)
print("myvar =", myvar)  # 11
callbyreference(myarr)
print("myarr =", myarr)  # [42, 2, 3]
