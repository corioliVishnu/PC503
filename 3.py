#!/bin/python3

l = []
N = int(input())
for _ in range(N):
  n = int(input())
  for _ in range(n):
    l = list(map(int, input().split(' ')))
    Max = max(l)
    print(Max)
