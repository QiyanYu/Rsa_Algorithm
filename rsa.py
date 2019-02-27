import random


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def is_prime(num){
    if num > 1:
        for i in range(2, num):
            if(num%i) == 0:}
