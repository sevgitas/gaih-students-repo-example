# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:32:32 2021

@author: sevgi.tas
"""


# sayi1=int(input("Sayı giriniz:"))
def prime_first():
    for i in range(0,500):
        if i > 1 :
        
            asal=False
    
            for j in range(2,i):
                if i % j == 0:
                    asal=True
            
            if asal==False:
                print(i)

prime_first()


def prime_second():
    for i in range(500,1001):
        if i > 1:
            asal=False
            for j in range(2,i):
                if i % j ==0:
                    asal=True
            if asal==False:
                print(i)
                
                
prime_second()
