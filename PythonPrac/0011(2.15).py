__author__ = 'Esmidth'

input_data = open('filtered_words.txt')

b = input_data.read()

while True:
    c = input("Please input the phrase\n")
    if b.find(c) != -1:
        print("Freedom")
    else:
        print("Human Rights")