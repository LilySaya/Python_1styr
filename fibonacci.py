# -*- coding: utf-8 -*-
"""hw1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IKjAV0xPtutZVW9IFTbyivmKMmxDN0xb
"""

def fibo_iter(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    data = {}
    data[0]=0
    data[1]=1
    for i in range (2,n+1):
      data[i]=data[i-1]+data[i-2]
    return data[n]

print(fibo_iter(18))

def fibo_rec(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    res = fibo_rec(n-1)+fibo_rec(n-2)
  return res

print(fibo_rec(18))

