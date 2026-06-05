from Status import OrderStatus

class Order:
    def __init__(self, oid:int, quantity:int, status):
        self.oid = oid
        self.quantity = quantity
        self.status = OrderStatus.PENDING