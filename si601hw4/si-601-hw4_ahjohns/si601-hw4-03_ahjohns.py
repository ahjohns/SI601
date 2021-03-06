import sqlite3 as sqlite
import csv

#I used the lab 4 syntax/variables as a point of reference for opening, connecting and executing
#variables from lab 4 were used to be consistent and because the naming conventions made it more human readable
#open database, do a bunch of stuff to create the analysis

with sqlite.connect(r'si-601-hw4_ahjohns.db') as con:
  cur = con.cursor()
  cur.execute("select friend_profile.friend_id,(2013 - friend_profile.birthyear) as age,0+ifnull(friend_profile.checkins,0) as checkins,max(case when friend_education.school_type='Graduate School' then '3' when friend_education.school_type= 'College' then '2' when friend_education.school_type= 'High School' then '1' when friend_education.school_type= 'NULL' then '0' end) from friend_profile, friend_education where friend_profile.birthyear != 'NULL' and friend_profile.friend_id = friend_education.friend_id group by friend_education.friend_id;")
  rows = cur.fetchall()

  f = open(r'friend_analysis_ahjohns.csv', 'w')
  f.write('friend_id' + ',' + 'age' + ',' + 'checkins' + ',' + 'school_level\n')

  #this code was taken from the lab (which is based off of code from Yuhang Wang, but I am writing
  #them joined by comma separated, rather than tab delimited
  for row in rows:
    f.write(','.join([str(x) for x in row]) + '\n')
  f.close()