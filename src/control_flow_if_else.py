#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2014

@author: anroco

In Python, how to use the control structure if-else?

En Python, ¿Cómo usar la estructura de control if-else?
'''

#else statement contains the block of code that executes if the conditional
#expression in the if statement is false.
#if expression:
#    statements
#else:
#    statements

#create a integer
n = 50

#check if the value of n is greater than or equal to 100
if n >= 100:
    print('the value is greater than or equal to 100')
    n = n + 1
else:
    print('the value is less than or equal to 100')
    n = n - 1

#prints the value of n after passing through the if-else statement
print(n)
