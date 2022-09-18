import random

def add(*args):
    answer = 0
    for x in args:
        answer += x

    return answer


print(add(2, 2, 2, 44))
