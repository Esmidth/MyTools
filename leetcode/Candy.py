__author__ = 'Esmidth'

# @param ratings, a list of integer
# @return an integer

ratings = [1, 3, 5, 4, 5]


def candy(ratings):
    candies = []
    for i in ratings:
        candies.append(1)

    for x in ratings:
        pos = ratings.index(x)
        if x > ratings[pos - 1] and x > ratings[pos + 1]:
            candies[pos] += 1

    print(candies)


candy(ratings)