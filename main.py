from Order import Order
from Status import OrderStatus
from Coffee import CoffeeMachine
from Scheduler import Scheduler

def main():
    orders = [
        Order(1,3),
        Order(2,2),
        Order(3,3)
    ]

    coffee = CoffeeMachine()

    scheduler = Scheduler(orders,coffee)
    scheduler.run()
    
if __name__ ==  "__main__":
        main()