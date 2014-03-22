# -*- coding: utf-8 -*-      
#!/usr/bin/python -tt

# Lab 2 SI 601 : Regular expressions
#
# Written by Kevyn Collins-Thompson.
# Some test framework code used courtesy of Dr. Yuhang Wang.
#
# As with Lab 1, you fill in the missing code for the functions below, and
# main() is already set up to check the output of your functions with a few
# different inputs, printing 'OK' when each function is correct.
# Note that the 'return' in each function will need to be replaced to return
# the (correct) value for the specified problem.

import re

# A. leading_and_trailing
# Compile a regular expression to match strings that satisfy ALL of the following conditions
#    - the first character is NOT one of the letters [a,e,i,o,u] (case-insensitive)
#    - all remaining characters are "word characters", (i.e. letters, numbers, regardless of case, or underscore (_)
#    - the word must end in either 'er' or 'est' (case-insensitive)
#
# This function should return True if there was a match, and False otherwise.
#
# For example:
# leading_and_trailing('Awesomer') should return False
# leading_and_trailing('coolest') should return True
# leading_and_trailing('coolest and best') should return False
# leading_and_trailing('zesT') should return True
# leading_and_trailing('@tagger') should return True
# leading_and_trailing('Est') should return False
# leading_and_trailing('#$%est') should return False
def leading_and_trailing(s):
  # Your code here: make sure to modify the return statement to pass back
  # the correct value.
  match = re.search(r'^[^aeiou]\w*e(r|st|R|Ts|tS)$', s, re.IGNORECASE)
  if match:
    return True
  else:
    return False  


# B.  parse_counted_words
# Use regular expressions to find strings of the form:
#  <count> <longword>    e.g. 101 Dalmations
# More specifically, the match much follow these conditions
#   - first word (word1) is a count consisting of a natural number
#     (series of one or more digits, with leading and trailing whitespace)
#   - followed immediately by a second, long word2 having *at least* 7 alphabetic letters
#
#  Your function should return the last (word1, word2) pair found in the string, if they exist
#  or None if no such strings were found
# HINT:  \b matches the beginning or end of a word
# HINT:  you can use findall to get multiple matches in a string
#
# For example:
# parse_counted_words('5 watermelons, 13 pineapples, and 1 papaya.') should return ('13', 'pineapples')
# parse_counted_words('101 dalmations!') should return ('101', 'dalmations')
# parse_counted_words('snow white and the 7 dwarves') should return ('7', 'dwarves')
# parse_counted_words('goldilocks and the 3 little pigs') should return None, because 'little' has less
#    than 7 characters
# parse_counted_words('678 1234567 890')  should return None, because the word following the count does
#    not consist of alphabetic characters
def parse_counted_words(s):
  # Your code here: make sure to modify the return statement to pass back
  # the correct value.
  match = re.findall(r'\s([0-9]+).([a-z]{7,12})', s)
  match2 = re.findall(r'([0-9]+).([a-z]{7,12})', s)
  if match:
      return match[0]
  elif match2:
      return match2[0]


# C. find_tag
# Find the first pair of correctly-matched tags that encloses the given text
# string, and return that tagname.  In case of multiple (nested) tags, return
# the outermost tagname.  For example:
# If the string_to_find is "foo", and the input string is
#  <title>some string using foo as an example</title>
# then your function should return 'title'
# The tags must be correctly matched, i.e. this is not a correct match:
#  <title>some string containing foo </titlexyz>
# If there are nested tags like this:
#  <title>some string using <b>foo</b> as an example</title>
# then return the outermost tag 'title'
#
# HINT:  the \1 metacommand can be used to require a match with the results from
#  the first matching group in the regexp
#
# HINT: non-greedy matching wildcards are useful here.

def find_tag(string_to_find, s):
  # Your code here: make sure to modify the return statement to pass back
  # the correct value.
  match = re.match(r'<(.*?)>(.*?)</\1>', s)
  if match:
    return match.group(1)

# D. mission_report
# Use regular expressions along with findall to extract all pairs of correctly formatted
# Mission number and status pairs.  A mission's status is either 'failed' or the number of targets found.
# Sometimes a mission will be called a 'raid'.
# For example:
# mission_report('Mission 1 accomplished. Target found: 1.') should return [(1,1)]
# mission_report('Note: mission 20 accomplished. Targets found: 500. Raid 21 failed.') should return [(20,500), (21,'failed')]
# mission_report('Yes, mission 3 failed. Raid 48 was accomplished: targets found: 23. mission 96 was accomplished, targets found: 0') should return [(3,'failed'), (48, 23), (96, 0)])
# mission_report("Shopping list: 4 pineapples and 12 eggs.") should return None
#
# HINT:
# Use re.IGNORECASE for case insensitive matching
# http://docs.python.org/2/library/re.html#re.I
# You may use a couple of regular expressions in this function, or you can use only one.
# Remember that each part of a set of alternatives can contain a regular expression.
# You may find non-capturing groups and/or non-greedy wildcards handy.
# You can use the int() function to convert a string to integer
def mission_report(s):
  # Your code here: make sure to modify the return statement to pass back
  # the correct value.
  prior = re.findall(r'raid|mission', s, re.IGNORECASE)
  if prior:
    matchlist = []
    match = re.findall(r'([0-9]+)\s(failed)|([0-9]+)\s.*?\s([0-9]+)', s, flags=re.IGNORECASE)
    if match:
       for i in match:
           yoyo = str(i)
           yoyo = yoyo.strip('(').strip(')').replace("'", " ").replace(",", " ").split()
           if yoyo[0].isdigit():
               yoyo[0] = int(yoyo[0])
           if yoyo[1].isdigit():
               yoyo[1] = int(yoyo[1])


           matchlist.append(tuple(yoyo))
       return matchlist



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
  print '%s got: %s, expected: %s' % (prefix, repr(got), repr(expected))


def main():
  print 'Test results:'

  print 'leading_and_trailing'
  test(leading_and_trailing('Awesomer') , False)
  test(leading_and_trailing('coolest') , True)
  test(leading_and_trailing('coolest and best') , False)
  test(leading_and_trailing('zesT'), True)
  test(leading_and_trailing('@tagger'), True)
  test(leading_and_trailing('Est'), False)
  test(leading_and_trailing('#$%est'), False)

  print 'parse_counted_words'
  test(parse_counted_words('5 watermelons, 13 pineapples, and 1 papaya.') , ('13', 'pineapples'))
  test(parse_counted_words('101 dalmations!') , ('101', 'dalmations'))
  test(parse_counted_words('snow white and the 7 dwarves') , ('7', 'dwarves'))
  test(parse_counted_words('goldilocks and the 3 little pigs') , None)
  test(parse_counted_words('678 1234567 890') , None)
    
  print 'find_tag'
  test(find_tag('foo', '<image>foobar</image>'), 'image')
  test(find_tag('foo', '<h3>foo</h4>'), None)
  test(find_tag('meta', '<html>meta data<body>some text</body></html>'), 'html')
  test(find_tag('introduction', '<title><b>An introduction</b>to using the title tag</title>'), 'title')

  print 'mission_report'
  test(mission_report('Mission 1 accomplished. Target found: 1.'), [(1,1)])
  test(mission_report('Note: mission 20 accomplished. Targets found: 500. Mission 21 failed.'), [(20,500), (21, 'failed')])
  test(mission_report("Yes, mission 3 failed. Mission 48 accomplished. targets found: 23. mission 96 accomplished, targets found: 0"), [(3,'failed'), (48, 23), (96, 0)])
  test(mission_report("Shopping list: 4 pineapples and 12 eggs."), None)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()