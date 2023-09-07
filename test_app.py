def reverse_words(s):
    string = str(s)
    return ' '.join([word[::-1] for word in string.split(' ')])