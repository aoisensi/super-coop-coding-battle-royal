#import numpy as np
import math
import random

def get_euler_number(n: float):
    return _get_euler_number(1.0, n)

def _get_euler_number(a: float, n: float):
    if n == 0:
        return a
    return _get_euler_number(a + 1.0 / math.factorial(n), n - 1)

print(get_euler_number(100.0))

def calc_pi(n: int):
    inside=0
    for i in range(0,n):
        (x, y) = (random.random(), random.random())
        if x*x+y*y <= 1 : inside += 1

    return 4.0*inside/n

print(calc_pi(10))

def motto_sugoi_calc_pi(n: int):
    pi = 0
    for i in range(1, n):
        x = i*2-1
        if i % 2 == 0:
            x *= -1
        pi += 4/x
    return pi

def sugoi(n):
    return 1000000

def totemo(n):
    return 1000000

wakaru = "wakaru"
print(motto_sugoi_calc_pi(sugoi(totemo(sugoi))))

def u_(n):
    n = "u-"+n
    if n == "u-pa-ru-pa-su-pa-ka-pa-ka-":
        return "=(-_ - )="
    return "wrong answer"

def pa_(n):
    return "pa-"+n

def ru_(n):
    return "ru-"+n

def su_(n):
    return "su-"+n

def ka_(n = ""):
    return "ka-"+n

print(u_(pa_(ru_(pa_(su_(pa_(ka_(pa_(ka_())))))))))
