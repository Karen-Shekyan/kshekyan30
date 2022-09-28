'''
Karen Shekyan
SoftDev
K04 -- function that takes in dictionary and returns a random value from the dictionary
2022-09-22
Time Spent: 0.5 hours
'''
'''
DISCO:
 - Python has a .keys() function to get a list of keys from a dictionary
 - random.randint is inclusive on BOTH endpoints
 - .keys() returns a dict_keys object, which is not subscriptable (can't get element by index)
    - dict_keys can be type-cast into a list with "list(dict_keys)"
 - Try-catch statements in python! They function similar to java, and the syntax is


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

def getRandKrew(krewes):
    keys = list(krewes.keys())
    keyIndex = random.randint(0, len(keys)-1)
    devos = krewes.get(keys[keyIndex])
    devosIndex = random.randint(0, len(devos)-1)
    return (devos[devosIndex], keys[keyIndex])

#########################################################
######################### TESTS #########################
#########################################################

krewes1 = {2:["A", "B", "C"], 3:["D", "E", "F"]}
krewes2 = {
    2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"],
    7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
    8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
}
krewes3 = {}
krewes4 = {4:[], 5:[], 6:[]}

for i in range(20):
    try:
        (devo,period) = getRandKrew(krewes1)
        print(str(devo) + " from period " + str(period))
    except ValueError:
        print("ERROR: Dictionary has length 0")
print("\n")

for i in range(20):
    try:
        (devo,period) = getRandKrew(krewes2)
        print(str(devo) + " from period " + str(period))
    except ValueError:
        print("ERROR: Dictionary has length 0")
print("\n")

for i in range(1):
    try:
        (devo,period) = getRandKrew(krewes3)
        print(str(devo) + " from period " + str(period))
    except ValueError:
        print("ERROR: Dictionary has length 0")
print("\n")

for i in range(20):
    try:
        (devo,period) = getRandKrew(krewes4)
        print(str(devo) + " from period " + str(period))
