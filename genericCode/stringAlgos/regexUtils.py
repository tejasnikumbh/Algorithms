# Utilities for regex

import re

'''
  Method: findallNonOverlapping(pattern, searchString)
  Explanation: Finds indices of all occurences of a pattern p inside a string. The pattern is passed as 
  a string and not as a compiled regex. 
  Returns: The list of starting indices of all occurences of pattern, non Overlapping
'''
def findallNonOverlapping(pattern, searchString):
  pattern = re.compile(pattern)
  return [x.start() for x in pattern.findall(searchString)]
  
'''
  Method: findallOverlapping(pattern, searchString)
  Explanation: Finds indices of all occurences of a pattern p inside a string. The pattern is passed as 
  a string and not as a compiled regex. 
  Returns: The list of starting indices of all occurences of pattern, Overlapping
'''
def findallOverlapping(pattern, searchString):
  pattern = "(?=" + pattern + ")"
  pattern = re.compile(pattern)
  return [x.start() for x in pattern.finditer(searchString)]


