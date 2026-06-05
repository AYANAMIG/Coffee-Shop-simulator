from Order import Order
from Status import OrderStatus
from Coffee import CoffeeMachine

def main():
    order = Order(oid =1, status=OrderStatus.PENDING, quantity = 3)
    coffee = CoffeeMachine()

    print(f"[main] \n order:{order.oid} \n Status: {order.quantity}")
    order.status = OrderStatus.RUNNING
    print(f"[main] \n update:{order.status.name}")
    coffee.make(order.quantity)
    order.status = OrderStatus.COMPLETED
    print(f"[main] \n order: {order.oid} \n update:{order.status.name}")
if __name__ ==  "__main__":
        main()