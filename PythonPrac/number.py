__author__ = 'Esmidth'


class stepper:
    def __getitem__(self, item):
        return self.data[item]

x = stepper()
x.data = 'Spam'

print(x[1])

for item in x:
    print(item)

print('a' in x)