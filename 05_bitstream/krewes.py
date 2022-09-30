'''
Jing Feng, Karen Shekyan
SoftDev
K05 --
2022-09-28
Time Spent:
'''
'''
DISCO:
 - Tuples! They're used to initialize many variables at once:
    - (x,y,z) = (1,2,3) initializes x to 1, etc
 - Tuples can be printed:
    - print(x,y,z) prints "x y z"
 - .strip() removes whitespace from the start and end of a string
    - a character can be specified to remove instead
 - Local/global variables don't work the way they do in Java

QCC:
'''

import random

file = open("krewes.txt", "r")
string = file.read()
data = string.split("@@@")
for i in range(len(data)):
    data[i] = data[i].split("$$$")

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = data[i][j].strip()

periods = []
info = []
for i in range(len(data)):
    period = data[i][0]
    periods.append(period)

    dev_info = []
    for j in range(len(data)):
        if (data[j][0] == period):
            dev_info.append(data[j][1:])
    info.append(dev_info)

dictionary = dict(zip(periods, info))


def getRandKrew(krewes):
    #get key list
    keys = list(krewes.keys())
    #get random key
    key_index = random.randint(0, len(keys)-1)
    period = keys[key_index]
    #get the value (list) at the random key
    key_info = krewes.get(period)
    #get a random index for the list
    info_index = random.randint(0, len(key_info)-1)
    #check for empty input
    if (len(key_info[info_index]) == 0):
        return "Input file is empty"
    #get the random item in the list
    (devo, ducky) = (key_info[info_index][0], key_info[info_index][1])
    return "Devo " + str(devo) + " from period " + str(period) + " with ducky named " + str(ducky)


for i in range(20):
    print(getRandKrew(dictionary))
