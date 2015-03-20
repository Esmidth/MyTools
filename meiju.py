__author__ = 'Esmidth'

a = ""
i = 0
while i < 100:
    a += str(i + 1)
    i += 1

temp = raw_input("Input the number\n")
temp_pos = a.find(temp)
print(temp_pos + 1)
