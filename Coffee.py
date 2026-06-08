import time

class CoffeeMachine:
    def make_one(self):
        print("[Coffee] Making 1 coffee")
        time.sleep(1)
        print("[Coffee] Making Finished")
    # def make_ONE(self,count):
    #     print(f"[Coffee] \n Making {count} Coffee]")
    #
    #     for i in range(1,count + 1):
    #         print(f"[Coffee] \n Making {i} Coffee]")
    #         time.sleep(1)
    #         print(f"[Coffee] \n Making {i} Coffee Finished]")
    #
    #     print(f"[Coffee] \n All Coffee Finished")