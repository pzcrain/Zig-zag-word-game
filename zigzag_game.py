def load_words(filename, length):
    filename = open('words.txt','r')
    words = []
    for w in filename:
        w = w.strip('\n')
        if length == len(w):
            words.append(w)
    return words

def prompt_guess(position,length):
    length = int(length)
    
    while True:
        guess = input('Now guess {} letters corresponding to letters {} to {} of the unknown word: '.format(length,position + 1,position + length))
        if length != len(guess):
            print("Invalid guess '{}'. Should be {} characters long.\n".format(guess,length))
        else:
            break
    return guess

def main():
    """
    Handles top-level interaction with user.
    """

    name = input('Welcome to the brain teasing zig-zag word game.\n\nWhat is your name? ')
    x,y,z = name.partition(' ')
    print('\nHi {}! We have selected a 6 letter word for you to guess.\n\nLet the game begin!\n'.format(x))
    wordlist = random.choice(load_words('words.txt', 6))
    total_score = 0
    
if __name__ == "__main__":
    main()
