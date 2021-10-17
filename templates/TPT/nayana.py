###Challenge 1

var1 = 3
var2 = "Mr. Mortensen"
var3 = 'f'
var4 = 0.4

print(var1,var2)


###Challenge 2

list1 = [5, 3, 4, 1, 2]
list2 = list1[3], list1[4], list1[1], list1[2], list1[0]
print(list2)


###Challenge 3
averageList = [23, 41, 90, 55, 71, 83]
new_averageList=[x+3 for x in averageList]
print(new_averageList)
avg=sum(new_averageList)/len(new_averageList)
print("The average is", round(avg,2))