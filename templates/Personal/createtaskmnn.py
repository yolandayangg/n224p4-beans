
print ("Which vacation spot is right for you?")

pt = input("Enter your Personality Type!!: ")
age = int(input ("Enter your age!: "))

vacaylist = ['New York City', 'Tokyo', 'Los Angeles', 'Paris', 'San Diego', 'Hawaii', 'Sedona', 'Amsterdam', 'Seoul'  ]

if (pt) == "A":
    if (age < 30):
     print (vacaylist[0], vacaylist[2])
    else:
     print(vacaylist[1])

if (pt) == "B":
    if (age < 30):
        print(vacaylist[4], vacaylist[5])
    else:
        print(vacaylist[3])

elif (pt) == "C":
    if (age < 30):
        print (vacaylist[7], vacaylist[8])
    else:
        print(vacaylist[6])





