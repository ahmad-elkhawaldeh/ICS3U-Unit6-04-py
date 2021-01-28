#!/usr/bin/env python3

# Created by: Ahmad
# Created on: Jan 2021
# This program uses an array


import random


def getAvg(array):
    length=0
    total=0
    for subList in array:
        for loop in subList:
            length+=1
            total += loop
    return total/length

def main():
    array=[]
    rows = int(input("How many row would you like: "))
    cols = int(input("How many columns would you like: "))
    for loop in range(rows):
        list=[]
        for y in range(cols):
            list.append(random.randint(1,50))
        array.append(list)
    for subList in array:
        for loop in subList:
            print(loop,end=" ")
        print()
    print("Average of al the numbers is:",getAvg(array))

if __name__ == "__main__":
    main()