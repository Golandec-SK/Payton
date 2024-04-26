import random
words = ['word1', 'word2', 'hate', 'bronchitis', 'blue']

for i in range(len(words)):
    word = random.choice(words)
    print(word)
    #words.remove(word)

input("\n\nPress enter to exit.")
