#Exercise 4
# Calculating pi 

class Coordinate (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance (self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5


def estimate_pi(precision):
    from random import random

    hit = 0
    miss = 0
    tot = hit + miss

    randx = random()
    randy = random()

    c = Coordinate(randx, randy)
    origin_circle = Coordinate(0.5, 0.5)

    a = c.distance(origin_circle)
    
    while tot <= precision:
        if a < 0.5:
            hit = hit + 1
        elif a > 0.5:
            miss = miss + 1
    
    print(round((4*hit/tot),decimal))


decimal = int(input("estimate pi value up to which decimal places: "))
precision = int(input("how many times you want to pick a dot : "))

print(estimate_pi(precision))






