__author__ = 'Esmidth'

with open("james.txt") as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open("julie.txt") as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open("sarah.txt") as sar:
    data = sar.readline()
sarah = data.strip().split(',')

print("%s\n%s\n%s\n" % (sorted(james), julie, sarah))
# print(james)


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


clean_james = []
clean_julie = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))
print('\t', sorted(clean_james), '\n\t', sorted(clean_julie), '\n\t', sorted(clean_sarah))