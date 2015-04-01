__author__ = 'Esmidth'


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


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




clean_james = [sanitize(each_t) for each_t in james]
clean_julie = [sanitize(each_t) for each_t in julie]
clean_sarah = [sanitize(each_t) for each_t in sarah]

print(sorted(clean_james))
