import random

vacaylist = ['New York City', 'Tokyo', 'Los Angeles', 'Paris', 'San Diego', 'Hawaii', 'Sedona', 'Amsterdam', 'Seoul'  ]




class Vacation:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, pt, age):
        """Built in validation and exception"""

        self._pt = pt
        self._age = 0
        self._display = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.getV()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building book series list, this id called from __init__"""
    def getV(self):
        f = [(random.sample(vacaylist,1))]

        if (self._pt) == "A":
            if (self._age < 30):
                display = (vacaylist[0], vacaylist[2])
            elif (self._age > 30):
                display = (vacaylist[1])
            else:
                display = vacaylist[1]


        elif (self._pt) == "B":
            if (self._age < 30):
                display = (vacaylist[4], vacaylist[5])
            if (self._age > 30):
                display = (vacaylist[3])
            else:
                display = vacaylist[3]

        else:
            if (self._age < 30):
                display = (vacaylist[7], vacaylist[8])
            if (self._age > 30):
                display = (vacaylist[6])
            else:
                display = vacaylist[6]

        self._display = display


    """Method/Function to set data: list, dict, and dictID are instance variables of Class"""



    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._display

    @property
    def number(self):
        return self._display[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]



if __name__ == "__main__":
    '''Value for testing'''

    '''Constructor of Class object'''
    vacay = Vacation("A", 15)
    print(f"Here are some vacay recomendations = {vacay.list}")

    vacay = Vacation ("B", 35)
    print(f"Here are some vacay recomendations = {vacay.list}")