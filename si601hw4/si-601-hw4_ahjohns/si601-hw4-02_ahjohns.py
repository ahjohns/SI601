import sqlite3 as sqlite
import csv

#I used the lab 4 syntax/variables as a point of reference for opening, connecting and executing
#variables from lab 4 were used to be consistent and because the naming conventions made it more human readable
#open database, create table, insert data from profile data, commit
with sqlite.connect(r'si-601-hw4_ahjohns.db') as con:
  cur = con.cursor()

  cur.execute("drop table if exists friend_profile;")

  cur.execute("create table friend_profile(friend_id integer, gender string, birthyear integer, hometown_id integer, hometown_name string, location_id integer, location_name string, checkins integer)")

  reader = csv.reader(open('friend_profile_ahjohns.csv', 'rb'))
  for row in reader:
    cur.execute("insert into friend_profile values (?,?,?,?,?,?,?,?)", row)
    con.commit()

#open database, create table, insert data from education data, commit

with sqlite.connect(r'si-601-hw4_ahjohns.db') as con:
  cur = con.cursor()

  cur.execute("drop table if exists friend_education;")

  cur.execute("create table friend_education(friend_id integer, school_id integer, school_name string, school_type string)")

  reader = csv.reader(open('friend_education_ahjohns.csv', 'rb'))
  for row in reader:
      cur.execute("insert into friend_education values (?,?,?,?)", row)
      con.commit()
