#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

c.execute("DROP TABLE students;")
command = "CREATE TABLE students (name TEXT, age INT, id INT);"
c.execute(command)    # run SQL statement

c.execute("DROP TABLE courses;")
command = "CREATE TABLE courses (code TEXT, mark INT, id INT);"
c.execute(command)

# def csv_to_dict(filename): #make this command with optional args later??
file = open("students.csv", "r")
reader = csv.DictReader(file)
students_dictionary = {}
for row in reader:
    students_dictionary[int(row["id"])] = [row["name"], int(row["age"])]

file = open("courses.csv", "r")
reader = csv.DictReader(file)
course_dictionary = {}
for row in reader:
    course_dictionary[int(row["id"])] = [row["code"], int(row["mark"])]

for key in course_dictionary:
    command = ""
    command += f"INSERT INTO courses VALUES({course_dictionary[key][0]}, {course_dictionary[key][1]}, {key});"
    c.execute(command)
# for key in students_dictionary:
#

#==========================================================

db.commit() #save changes
db.close()  #close database
