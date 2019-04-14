#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:38:50 2019

@author: marco
"""

def is_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def get_primes(N):
    results = list()
    for i in range(2,N+1):
        if is_prime(i):
            results.append(i)
    return results

print(get_primes(20))