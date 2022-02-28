
x = 21
y = 16
print (x,y)
def swap (x,y):
    q = x
# we set one of our variables to a temporary variable
    x = y
#swap the original two variables
    y = q
#set y equal to the temp

    return x,y

a,b= swap(21,16)
print(a, b)