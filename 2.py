#!/bin/python3

s = input("Enter a sentence: ").split(' ')
t = list(s)
L = len(t[0])
for i in range(len(t)):
  if len(t[i]) > L:
    L = len(t[i])
    Long = t[i]
print("Longest word: {}".format(Long))
print("Length: {}".format(L))
