from dataclasses import dataclass

@dataclass
class Product:
    """
    A class representing a
    """
    name:str
    price:float
    discountPercent:int

    def getDiscountAmount(self):
        return self.price * (self.discountPercent / 100)

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
