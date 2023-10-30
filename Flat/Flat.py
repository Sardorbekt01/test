class Flat:
    def __init__(self, code, dimension):
        self.code = code
        self.dimension = dimension
        self.tariffs = {"low": 0, "medium": 0, "high": 0}

    def getCode(self):
        return self.code

    def getDimension(self):
        return self.dimension

def setTariffs(self, tariffs):
        if len(tariffs) == 3:
            self.tariffs["low"] = tariffs[0]
            self.tariffs["medium"] = tariffs[1]
            self.tariffs["high"] = tariffs[2]
        else:
            print("Tariflar soni noto'g'ri, faqat 3 ta son kiritishingiz lozim.")

def getTariffs(self):
    return self.tariffs

def newFlat(code, dimension):
    flat = Flat(code, dimension)
    return flat
