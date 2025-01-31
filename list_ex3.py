# define a function that will take list of words as an argument
# return the list with reverse of every element in that list
# input ['abc','def','ghi']--->['cba','fed','ihg']

words = ['abc','def','ghi']

def reverse_words (a):
    reverse_words = []
    for i in words:
        reverse_words.append(i[::-1])
    return reverse_words

print(reverse_words(words))