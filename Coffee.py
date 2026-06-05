import time

class CoffeeMachine:
    def make(self,count):
        print(f"[Coffee] \n Making {count} Coffee]")

        for i in range(1,count + 1):
            print(f"[Coffee] \n Making {i} Coffee]")
            time.sleep(10)
            print(f"[Coffee] \n Making {i} Coffee Finished]")

        print(f"[Coffee] \n All Coffee Finished")