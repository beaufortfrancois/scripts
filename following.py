#!/usr/bin/python
#
# Copyright 2011 Tony Scelfo. All Rights Reserved.

"""Script to parse reader following json to link to plus profiles.

Script that iterates the following json dump from reader to make links
to G+ profiles so it is easy to make a circle with the people you used
to follow.
"""

__author__ = 'scelfo@gmail.com (Tony Scelfo)'

import json
import sys

def main(argv):
  if len(argv) < 2:
    print 'must specify an input file'
    sys.exit()

  input_file = argv[1]

  print 'Going to read from %s...' % input_file

  f = open(input_file, 'r')
  parsed_json = json.load(f)

  for friend in parsed_json['friends']:
    if 'profileIds' in friend:
      # Friends can have more than one profileId, the first seems to be the
      # one that google+ wants.
      id = friend['profileIds'][0]
      print '%s: https://plus.google.com/%s' % (friend['displayName'], id)

if __name__ == '__main__':
  main(sys.argv)
