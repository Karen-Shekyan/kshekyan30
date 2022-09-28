'''
Jing Feng, Karen Shekyan
SoftDev
K05 --
2022-09-28
Time Spent:
'''
'''
DISCO:


QCC:
'''

import random

file = open("krewes.txt", "r")
str = file.read()
str = 

def getRandKrew(krewes):
    keys = list(krewes.keys())
    keyIndex = random.randint(0, len(keys)-1)
    devos = krewes.get(keys[keyIndex])
    devosIndex = random.randint(0, len(devos)-1)
    return (devos[devosIndex], keys[keyIndex])
