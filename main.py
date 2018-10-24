#!/usr/bin/env python

with open('01-exam.txt') as myfile:
    exam_lines= myfile.readlines()

# 1. print lines in a list
print(exam_lines)

# 2. print number of lines
print('Number of Lines: ' + str(len(exam_lines)))

# 3. print the fifth line
print(exam_lines[4])

# 4. save last line to last_line and print
last_line = exam_lines[-1]
print('last_line: ' + last_line)

# use indexing to print 'o' from last line
print(last_line[last_line.find('o')])

# print number of words in last_line
word_count = len(last_line.split(' '))
print('word_count: ' + str(word_count))

# type from expression
print(type(2/3) , type(2 + 2.0), type(1+1) , type('2' + '2') , type(1 > 2))

# dig into dict to print string
d = {"levelone":[1,2,{'leveltwo':[5,6,[1,['get me please']]]}]}
print(d['levelone'][2]['leveltwo'][2][1][0])

# find number of unique integers in list
mylist = [1,2,3,4,5,6,4,3,2,1,2,3,4,5,6,6,7,8,5,6,7,8,9,8,9,8,9,7,10,123,1,2,2,3,1,3,2,4,1,4,4,1,2,2,22,3,4,1,4,1]
print(len(set(mylist)))