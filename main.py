some_words = input('Please enter some comma-separated words: ')


def comma(some_words):
    return some_words.split(",")


def set_sw(some_words):
    return set(some_words)


def lenght(some_words):
    return len(some_words)


def comma2(some_words2):
    return some_words2.split(',')


def set_sw2(some_words2):
    return set(some_words2)


print('In your list {} words'.format(len(comma(some_words))))
some_words2 = input('Please enter {} comma-separated words: '.format(len(comma(some_words))))


d = dict(zip(some_words.split(','), some_words2.split(',')))
print(d)
