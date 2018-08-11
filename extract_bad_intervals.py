#!/usr/bin/python

from argparse import ArgumentParser
import re

def reverse_enum(L):
   for index in reversed(range(len(L))):
      yield index, L[index]


# parse arguments
parser = ArgumentParser()
parser.add_argument("-i", "--input", dest="input", help="The INPUT file path", metavar="INPUT", required=True)
parser.add_argument("-o", "--output", dest="output", help="The OUTPUT file name", metavar="OUTPUT", required=True)

args = parser.parse_args()

input_file_name = args.input
output_file_name = args.output

# read whole file
with open(input_file_name) as f:
    lines = f.readlines()
# remove whitespace characters like `\n` at the end of each line
lines = [x.strip() for x in lines]


# find first Stimulus occurence
first_line_index = 0
for num, line in enumerate(lines):
    if "Stimulus" not in line:
        continue
    first_line_index = num
    break

# find last Stimulus occurence
last_line_index = 0
for num, line in reverse_enum(lines):
    if "Stimulus" not in line:
        continue
    last_line_index = num
    break

# remove all lines until first ocurrence
lines = lines[first_line_index:last_line_index]

# take only the lines wth "Bad Interval" in them
lines = [k for k in lines if "Bad Interval" in k]

for num, line in enumerate(lines):
    line = re.sub('[,]', '', line)
    line = re.sub('[^\s0-9]', '', line).strip()
    words = line.split(' ')
    lines[num] = '{}, {}'.format(words[0], words[1])

#output to file
output_file = open(output_file_name, 'w')
for num, line in enumerate(lines):
    output_file.write('{}\n'.format(line))
