print ("Which vacation spot is right for you?")

pt = input("Enter your Personality Type!!: ")
age = int(input ("Enter your age!: "))

vacaylist = ['New York City', 'Tokyo', 'Los Angeles', 'Paris', 'San Diego', 'Hawaii', 'Sedona', 'Amsterdam', 'Seoul'  ]

# here we're defining the procedure, and the algorithm


# here, we're calling the method. now here, it actually displays with this line of code



class Vacation:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, pt, age):
        """Built in validation and exception"""
        self._pt = pt
        self._age = age
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.sortV()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building book series list, this id called from __init__"""
    def sortV(self):
        if (pt) == 'A':
            if (age < 30):
                print (vacaylist[0], vacaylist[2])
            else:
                print(vacaylist[1])

        elif (pt) == 'B':
            if (age < 30):
                print(vacaylist[4], vacaylist[5])
            else:
                print(vacaylist[3])

        else:
            if (age < 30):
                print (vacaylist[7], vacaylist[8])
            else:
                print(vacaylist[6])
        #self.set_data(f[0])


    """Method/Function to set data: list, dict, and dictID are instance variables of Class"""
    # def set_data(self, num):
    #self._list.append(num)
    # self._dict[self._dictID] = self._list.copy()
    # self._dictID += 1


    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]



if __name__ == "__main__":
    '''Value for testing'''

    '''Constructor of Class object'''
    vlist = Vacation(1, 15)
    print(vlist)

