'''
The Great Coder Boys: Jing Feng, Karen Shekyan
SoftDev
K06 -- select a job class from a csv file using weighted randomness.
2022-10-02
Time Spent: 1 hr
'''
'''
DISCO:
 - Files can be read in one line at a time using readline()
 - Values in a dictionary can be accessed either with .get(<KEY>) or [<KEY>]. The latter throws errors if the key isn't present
 - random.uniform(<start>, <end>) returns a float between the start and end values

QCC:
 - How to make sure this script doesn't crash with an empty input??

HOW THIS SCRIPT WORKS:
 - Read in the .csv file
 - Parse the file, creating a dictionary w/ entries of the form {jobclass: percentage}
 - Generate a random number between 0 and the sum of percentages (given in the last line of the file)
 - Loop through keys in the dictionary, subtracting their percentages from the random number
    - Once the random number is <= 0, return the current key
 - FOR TESTING: repeat random selection many times to ensure probability is weighted correctly
'''
import random

file = open("occupations.csv", "r")
dictionary = {}
#the dictionary below is for testing purposes
count = {}
#readline twice to ignore the first line: 'Job Class,Percentage'
line = file.readline()
line = file.readline()
#parse the file to create dictionaries
while line:
    strings = line.split(",")
    job_class = ""
    #job classes with commas in them are put back together
    for i in range(len(strings)-1):
        strings[i] = strings[i].strip('"')
        job_class += strings[i]
    #update dictionary with data
    dictionary[job_class] = float(strings[-1])
    count[job_class] = 0
    line = file.readline()
#remove 'Total' after parsing file, putting its value in a separate variable
total = dictionary['Total']
del dictionary['Total']
del count['Total']


def pickJob(job_percentages):
    #generate random number in range
    random_percent = random.uniform(0, total)
    #get list of keys
    jobs = list(job_percentages.keys())
    #subtract each job class's percentage until random number <= 0, them return
    for job in jobs:
        random_percent -= job_percentages.get(job)
        if (random_percent <= 0):
            return job

#run pickJob() many times to ensure probabilities are weighted correctly
tests = 10000
for i in range(tests):
    count[pickJob(dictionary)] += 1

count_keys = list(count.keys())
#output in a readable form
for job in count_keys:
    print(job + " was selected " + str(count[job] / tests * 100) + " percent of the time (" + str(dictionary[job] / total * 100) + ")\n")
