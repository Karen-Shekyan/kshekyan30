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

c.execute("DROP TABLE IF EXISTS students;")
command = "CREATE TABLE students (name TEXT, age INT, id INT);"
c.execute(command)    # run SQL statement

c.execute("DROP TABLE IF EXISTS courses;")
command = "CREATE TABLE courses (code TEXT, mark INT, id INT);"
c.execute(command)

# def csv_to_dict(filename): #make this command with optional args later??
file = open("students.csv", "r")
reader = list(csv.reader(file))
for row in reader:
    if (not row == reader[0]):
        command = f"INSERT INTO students VALUES(\"{row[0]}\", {int(row[1])}, {int(row[2])});"
        c.execute(command)

file = open("courses.csv", "r")
reader = list(csv.reader(file))
for row in reader:
    if (not row == reader[0]):
        command = f"INSERT INTO courses VALUES(\"{row[0]}\", {int(row[1])}, {int(row[2])});"
        c.execute(command)

#reorder the tables to make more sense??
# ^does that even matter? ; reorder dictionaries?

# for key in course_dictionary:
#     command = f"INSERT INTO courses VALUES(\"{course_dictionary[key][0]}\", {course_dictionary[key][1]}, {key});"
#     c.execute(command)
#
# for key in students_dictionary:
#     command = f"INSERT INTO students VALUES(\"{students_dictionary[key][0]}\", {students_dictionary[key][1]}, {key});"
#     c.execute(command)


#==========================================================

db.commit() #save changes
db.close()  #close database
