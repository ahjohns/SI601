#!/usr/bin/python -tt

# Lab 1 SI 601 Fall 2013 class
#
# Based on code by Yuhang Wang and from Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# For each task below, fill in the code for the functions below.
# main() will call the functions with a few different inputs, check
# the results, and print 'OK' when each function's output is correct.
#
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. You need to fill in code
# for the function that returns the correct result as specified.

# Task A. String manipulation (function 'middle_part')
#
# Given a string s:
#     - First remove leading and trailing whitespace (i.e. at beginning or end)
#     - If the string length of s is less than or equal to 6 after
#       removing leading and trailing white space, return the empty string.
#     - Else return a string consisting of the middle part of the string,
#       excluding the first 3 and the last 3 chars of the remaining string.
#     Example: ' Friedrichshafen   ' yields 'edrichsha'.
#
# HINT - Look up these Python functions:
#     str.strip()
#     len()

def middle_part(s):
  # +++your code here+++
  s1 = str.strip(s)
  if len(s1) >= 6:
    return s1[3:-3]
  else:
    return ""

# Task B. Loops (function 'donuts')
#
# Given an integer count, return a string
# of the form 'donut 1, donut 2, ..., donut <count>', where <count> is the number
# passed in. However, if the count is 5 or more, then use the string
# 'and <num> more donuts' as the last item instead of the actual list of donuts,
# where <num> is the number of remaining donuts.
# Examples:
#     donuts(3)  returns 'donut 1, donut 2, donut 3'
#     donuts(4)  returns 'donut 1, donut 2, donut 3, donut 4'
#     donuts(10) returns 'donut 1, donut 2, donut 3, donut 4, and 6 more donuts'
#     donuts(20) returns 'donut 1, donut 2, donut 3, donut 4, and 16 more donuts'
#
# HINT - Look up these Python functions:
#   range()
#   str()

def donuts(count):
  # +++your code here+++
  c = str(count)
  num = count - 4
  if count == 1:
    return "donut 1"
  elif count == 2:
    return "donut 1, donut 2"
  elif count == 3:
    return "donut 1, donut 2, donut 3"
  elif count == 4:
    return "donut 1, donut 2, donut 3, donut 4" 
  else:
    return "donut 1, donut 2, donut 3, donut 4, and %s more donuts" %(num) 
 


# Task C. Sets and string operations (function 'match_ends')
#
# Given a list of strings, return the count of UNIQUE strings
# in the list that
#      - have string length is 9 or more AND
#      - the string starts with 'a' AND
#      - ends with 'ology'
#
# Example:
#   match_ends(['aerobiology', 'neurology', 'aerology', 'anthropology', 'aerobiology', 'neurology', 'aerology', 'anthropology'])
# should return 2
#
# HINT - Look up these Python functions:
#   set()
#   set.add()
#   str.startswith()
#   str.endswith()

def match_ends(words):
  # +++your code here+++
  s = set()
  for i in words:
    if i.endswith('ology') and i.startswith('a') and len(i) >= 9:
        s.add(i)
  return len(s)
        


# Task D. Dictionaries and sorting (function 'unique_counts')
#
# Given a list of strings, return a list of tuples containing the counts of each of the
# UNIQUE strings. The returned results should be ordered by the counts
# in decreasing order. In case of ties of counts, break the tie by string value in increasing order.
#
# Examples:
#   unique_counts(['Aurora', 'Jasmine', 'Jasmine', 'Jasmine', 'Belle', 'Belle'])
# should return [('Jasmine', 3), ('Belle', 2), ('Aurora', 1)]
#
#   unique_counts(['Belle', 'Adella', 'Aurora', 'Belle', 'Irene', 'Jasmine', 'Belle', 'Aurora'])
# should return [('Belle', 3), ('Aurora', 2), ('Adella', 1), ('Irene', 1), ('Jasmine', 1)])
#
# HINT - Look up these Python functions:
#   dict.items()
#   sorted()
#   You will need to write a helper (key) function to use with sorted()
#   You can either write a named function or an anonymous lambda function

def unique_counts(words):
  # +++your code here+++
  d = {}
  for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
  return sorted(d.items(), key=lambda(k,v): (-v,k))




#######################################################################
# DO NOT MODIFY ANY CODE BELOW
#######################################################################

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print
  print 'Task A:  middle_part'
  """ If this is what you get, you are good. Each OK is worth one point.
  OK  got: 'edrichsha' expected: 'edrichsha'
  OK  got: 'ce' expected: 'ce'
  OK  got: '' expected: ''
  OK  got: '' expected: ''
  OK  got: '' expected: ''
  """
  test(middle_part(' Friedrichshafen   '), 'edrichsha')
  test(middle_part('Mercedes'), 'ce')
  test(middle_part('python'), '')
  test(middle_part('abc'), '')
  test(middle_part(''), '')


  print 'Task B: donuts'
  # Each line calls donuts, compares its result to the expected for that call.
  """ If this is what you get, you are good. Each OK is worth one point.
   OK  got: 'donut 1' expected: 'donut 1'
   OK  got: 'donut 1, donut 2, donut 3' expected: 'donut 1, donut 2, donut 3'
   OK  got: 'donut 1, donut 2, donut 3, donut 4' expected: 'donut 1, donut 2, donut 3, donut 4'
   OK  got: 'donut 1, donut 2, donut 3, donut 4, and 6 more donuts' expected:  'donut 1, donut 2, donut 3, donut 4, and 6 more donuts'
   OK  got: 'donut 1, donut 2, donut 3, donut 4, and 95 more donuts' expected: 'donut 1, donut 2, donut 3, donut 4, and 95 more donuts'
  """
  test(donuts(1), 'donut 1')
  test(donuts(3), 'donut 1, donut 2, donut 3')
  test(donuts(4), 'donut 1, donut 2, donut 3, donut 4')
  test(donuts(10), 'donut 1, donut 2, donut 3, donut 4, and 6 more donuts')
  test(donuts(99), 'donut 1, donut 2, donut 3, donut 4, and 95 more donuts')


  print 'Task C: match_ends'
  """ If this is what you get, you are good. Each OK is worth one point.
  OK  got: 2 expected: 2
  OK  got: 2 expected: 2
  OK  got: 2 expected: 2
  OK  got: 3 expected: 3
  OK  got: 0 expected: 0
  """
  test(match_ends(['aerobiology', 'neurology', 'aerology', 'anthropology']), 2)
  test(match_ends(['aerobiology', 'neurology', 'Battlestar Galactica', 'aerology', 'anthropology']), 2)
  test(match_ends(['aerobiology', 'neurology', 'aerology', 'anthropology', 'aerobiology', 'neurology', 'aerology', 'anthropology']), 2)
  test(match_ends(['anthropology', 'anthropology', 'aerobiology', 'neurology', 'Battlestar', 'Galactica', 'aerology', 'anthropology', 'antitechnology']), 3)
  test(match_ends([]), 0)

  print 'Task D: unique_counts'
  """ If this is what you get, you are good. Each OK is worth one point.
  OK  got: [] expected: []
  OK  got: [('Jasmine', 1)] expected: [('Jasmine', 1)]
  OK  got: [('Jasmine', 2)] expected: [('Jasmine', 2)]
  OK  got: [('Jasmine', 3), ('Belle', 2), ('Aurora', 1)] expected: [('Jasmine', 3), ('Belle', 2), ('Aurora', 1)]
  OK  got: [('Belle', 3), ('Aurora', 2), ('Adella', 1), ('Irene', 1), ('Jasmine', 1)] expected: [('Belle', 3), ('Aurora', 2), ('Adella', 1), ('Irene', 1), ('Jasmine', 1)]
  """
  test(unique_counts([]), [])
  test(unique_counts(['Jasmine']), [('Jasmine', 1)])
  test(unique_counts(['Jasmine', 'Jasmine']), [('Jasmine', 2)])
  test(unique_counts(['Aurora', 'Jasmine', 'Jasmine', 'Jasmine', 'Belle', 'Belle']), [('Jasmine', 3), ('Belle', 2), ('Aurora', 1)])
  test(unique_counts(['Belle', 'Adella', 'Aurora', 'Belle', 'Irene', 'Jasmine', 'Belle', 'Aurora']), [('Belle', 3), ('Aurora', 2), ('Adella', 1), ('Irene', 1), ('Jasmine', 1)])
  
  
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()

