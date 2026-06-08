from enum import Enum
class OrderStatus(Enum):
    PENDING = "PENDING" #等待
    RUNNING = "RUNNING" #运行
    COMPLETED = "COMPLETED" #完成