#!/bin/python3

l = list(map(int, input("Enter numbers (space-seperated): ").split(' ')))
total = sum(l)
avg = total/len(l)
Max = max(l)
Min = min(l)
print("Sum: {}".format(total))
print("Average: {}".format(avg))
print("Max: {}".format(Max))
print("Min: {}".format(Min))

