'''
The Great Coder Boys: Jing Feng, Karen Shekyan
SoftDev
K06 --
2022-10-02
Time Spent:
'''
'''
DISCO:

QCC:

HOW THIS SCRIPT WORKS:

'''
import random

file = open("occupations.csv", "r")
dictionary = {}
count = {}
#readline twice to ignore the first line: 'Job Class,Percentage'
line = file.readline()
line = file.readline()

while line:
    strings = line.split(",")
    job_class = ""
    for i in range(len(strings)-1):
        strings[i] = strings[i].strip('"')
        job_class += strings[i]
    dictionary[job_class] = float(strings[-1])
    count[job_class] = 0
    line = file.readline()

total = dictionary.get('Total')
del dictionary['Total']
del count['Total']


def pickJob(job_percentages):
    random_percent = random.uniform(0, total)
    jobs = list(job_percentages.keys())
    for job in jobs:
        random_percent -= job_percentages.get(job)
        if (random_percent <= 0):
            return job

tests = 10000
for i in range(tests):
    count[pickJob(dictionary)] += 1

count_keys = list(count.keys())
for job in count_keys:
    print(job + " was selected " + str(count[job] / tests * 100) + " percent of the time")
