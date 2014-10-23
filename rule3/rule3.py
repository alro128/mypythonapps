#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import string

#s = sys.argv
#s[0] = '0'

s = []
s = {1, 2, 3}

while (len(s) == 3):
 s = raw_input("Valores: ").split()
 try:
  d = list(map(float, s))
  res = (d[1]*d[2])/d[0]

  adj = 10
  if len(s[1]) > len(str(res)):
      adj = len(s[1])
  else:
      adj = len(str(res))
  if len(s) > 2:
   print(string.rjust(s[0], 10) + " --> " + string.rjust(s[1], adj))
   print(string.rjust(s[2], 10) + " --> " + string.rjust(str(round(res,2)), adj))
 except ValueError:
     print("ValueError")
 except IndexError:
     break
