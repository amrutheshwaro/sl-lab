import sys
import os
from collections import Counter
from functools import reduce
from prettytable import PrettyTable

word_dict = {}
word_len = []

if(len(sys.argv) != 2):
    print("Invalid arguments.")
    sys.exit()

if(not(os.path.exists(sys.argv[0]))):
    print("Invalid file path.")
    sys.exit()

if(sys.argv[1].strip().split('.')[-1] != 'txt'):
    print("Invalid file type. Only 'txt' files allowed")
    sys.exit()

with open(sys.argv[1]) as file:
    word_dict = Counter(file.read().strip().split())

sorted_dict = sorted(word_dict.items(), key=lambda dict_item: dict_item[1], reverse=True)
print("The occurances of various words is")
print(sorted_dict)

t = PrettyTable(['Word', 'Frequency', 'Length'])
flag = 0

for i in range(10):
    try:
        word_tuple = sorted_dict[i]
        word_len.append(len(word_tuple[0]))
        t.add_row([word_tuple[0], word_tuple[1], word_len[i]])
    except IndexError:
        flag = 1
        print("File has less than 10 words")
        break

if (flag != 1):
    print("\nThe top 10 most used words are")
    print(t)

sum = reduce(lambda x, y: x + y, word_len)
print("The average lengths of 10 most used words are", sum/len(word_len))

odd_squares = [x*x for x in word_len if x % 2 == 1]
print("The squares of odd lengths in the list are", odd_squares)