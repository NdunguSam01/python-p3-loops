#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i >= 0:
        print(i)
        i = i- 1
    else:
        print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    # code goes here!
    # return int_list
    return [num ** 2 for num in int_list]

print(square_integers([1, 2, 3, 4, 5]))

def fizzbuzz():
    # code goes here!
    for x in range(1, 101):
        if x % 3 ==0 and x % 5 ==0:
            print("FizzBuzz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 3 == 0:
            print("Fizz")
        else:
            print(x)

fizzbuzz()