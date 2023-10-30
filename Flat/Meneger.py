from Flat import flat
class menejer:
    def __init__(self) -> None:
        self._flat_list:list[flat] = []

    def getCode(self,code:flat):
        return code

    def getDimension(self,dimetion:flat):
        return dimetion

    def newflat(self,flat:flat):
        self._flat_list.append(flat)
        return
    
    
        