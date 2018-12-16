#!/usr/bin/env python

# 3 ways to print fibonaccil sequence

""" Interview questions      Fibonaccil Sequence.py, by Abdullahi Yusuf (Lovow)
        6:15 AM       04/12/2017"""
print("\t""This Program is going to add numbers  like 0 1 1 2 3 5 8 13 which means")
print("\t""\t""0 + 1 = 1,   1 + 1 = 2,    1 + 2 = 3,    2 + 3 = 5,    3 + 5 = 8    e.t.c""\n")
print("\t""\t""Let's give it a try...""\n")
print("\t""Way One")

def fibonaccilWayOne(num):
    if num == 1 or num == 2:
        return 1
    return fibonaccilWayOne(num - 1) + fibonaccilWayOne(num - 2)
for i in range (1, 10):
    print (" ",fibonaccilWayOne(i))


print("\t""Way Two")

def fibonaccilWayTwo(num):
    a, b = 1, 1
    for i in range (num - 1):
        a, b = b, a + b
    return a
for i in range (1, 10):
    print (" ",fibonaccilWayTwo(i))


print("\t""Way Three, using generator")

def fibonaccilWayThree():
    a, b = 1, 1
    while True:
        yield a
        a, b = b,  a + b
num = 1
for i in fibonaccilWayThree():
    if num >= 10:
        break;
    print (i)
    num = num + 1
