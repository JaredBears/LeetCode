# Runtime: 265 ms, faster than 65.83% of Python3 online submissions for Design
# Parking System.
# Memory Usage: 14.5 MB, less than 63.79% of Python3 online submissions for
# Design Parking System.
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big:
            self.big -= 1
            return True
        if carType == 2 and self.medium:
            self.medium -= 1
            return True
        if carType == 3 and self.small:
            self.small -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
