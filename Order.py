from Status import OrderStatus
class Order:
    def __init__(self, oid:int, quantity:int):
        self.oid = oid
        self.quantity = quantity
        self.completed_quantity = 0
        self.status = OrderStatus.PENDING