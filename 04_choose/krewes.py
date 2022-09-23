'''
DISCO:
 - Python has a .keys() function to get a list of keys from a dictionary
 - random.randint is inclusive on BOTH endpoints
 - .keys() returns a dict_keys object, which is not subscriptable (can't get element by index)
    - dict_keys can be type-cast into a list with "list(dict_keys)"

QCC:
 - Usually ranges are exclusive at the end, why is randint inclusive?

OPS SUMMARY:
 - Input: krewes = {dict(int : list)}
 - Operation:
    1) Get list of keys in krewes
    2) Generate a random index from 0 to len(keys)
    3) Get the value (list of devos) associated with the key at the random index
    4) Generate another random index, this time from 0 to len(value)
    5) Return the devo at the random index
'''

import random

krewes = {2:["A", "B", "C"], 3:["D", "E", "F"]}

def getRandKrew():
    keys = list(krewes.keys())
    keyIndex = random.randint(0, len(keys)-1)
    devos = krewes.get(keys[keyIndex])
    devosIndex = random.randint(0, len(devos)-1)
    return devos[devosIndex]

for i in range(20):
    print(getRandKrew())
