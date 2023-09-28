def reverse_words(s):
    string = str(s)
    return ' '.join([word[::-1] for word in string.split(' ')])

def test_reverse_words():
    assert reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert reverse_words("God Ding") == "doG gniD"

