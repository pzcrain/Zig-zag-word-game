def load_words(filename, length):
    filename = open('words.txt','r')
    words = []
    for w in filename:
        w = w.strip('\n')
        if length == len(w):
            words.append(w)
    return words
