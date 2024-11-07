from DSA.perfectSquare import Solution
from utils import maximum, fibonacci, climbStairs
from utils.excel import process_sheet
from utils.maxSubArray import max_sub_arr
from opp.car import Vivo, Vehicle


class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I'm {self.name}")

class Tan(Person):
    @staticmethod
    def play():
        print("Play game")


tan = Person(name="tan")
# tan.talk()
#
# tan2 = Tan("a")
# tan2.play()
# print(maximum.maximum([1,2,3,5]))
# print(fibonacci.fibonacci(5))
# print(climbStairs.climb_stair([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# print(max_sub_arr([-2,1,-3,4,-1,2,1,-5,4]))

# process_sheet('transition.xlsx')
# car = Car("Vinfast Vf5", 2023)
# Car.wheels = 2
# car.start()
# print(car.wheels)


# car = Vivo("Vivo", 1990, "Tan")
# # methods chaining
# car.start().brake()
# print(car.owner)
# vehicle = Vehicle()

# walrus operator :=
# foods = list()
# while (food := input("what kind of food do u like?: ")) != 'quit':
#     foods.append(food)
#
# print(foods)

solution = Solution()
print(solution.is_perfect_square(17))