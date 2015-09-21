number = [1,2,3,5]
number2 = []
#number2 = number
i = 0
while i < len(number):
    number2.append(number[i])
    number2.append(number[i]*2)
    i+=1
number2.sort()
print(number2)
#for x in number:


#def nthUglyNumber(n):
#    number = [1,2,3,5]
