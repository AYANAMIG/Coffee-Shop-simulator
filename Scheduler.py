from Order import OrderStatus
class Scheduler:
    def __init__(self,orders,coffee):
        self.orders = orders
        self.coffee = coffee

    def has_unfinished_orders(self):
        for order in self.orders:
            if order.completed_quantity < order.quantity:
                return True
        return False
    def run(self):
        while self.has_unfinished_orders():
            for order in self.orders:
                if order.completed_quantity == order.quantity:
                    continue
                if order.status == OrderStatus.PENDING:
                    order.status = OrderStatus.RUNNING
                    print(
                        f"Order {order.oid} Status -> {order.status.name}"
                    )

                self.coffee.make_one()

                order.completed_quantity += 1
                print(
                    f"Order {order.oid}: "
                    f"{order.completed_quantity}/"
                    f"{order.quantity}"
                )

                if order.completed_quantity == order.quantity:
                    order.status = OrderStatus.COMPLETED

                    print(
                        f"Order {order.oid} Status -> {order.status.name}"
                    )
                print("-----------------------")