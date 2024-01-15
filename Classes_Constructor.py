class Product:
    def __init__(self, name, price, discount_percent = 0):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def getDiscountAmount(self):
        """
        Returns the discount percent
        :return:
        """
        return self.price * (self.discount_percent / 100)

    def getDiscountPrice(self):
        """
        Returns the discount amount
        :return:
        """
        return self.price - self.getDiscountAmount()