#Each step of the game
STEPS = (
    #position, length
    (0, 2),
    (0, 3),
    (1, 3),
    (2, 3),
    (3, 3),
    (2, 4),
    (1, 4),
    (0, 4),
    (0, 5),
    (1, 5),
    (0, 6),
)

#Score values for correctly guessing a letter
RIGHT_POSITION_VALUE = 100
WRONG_POSITION_VALUE = 20


def load_words(filename,length):
    filename = open('words.txt','r')
    a = []
    for w in filename:
        w = w.strip('\n')
        if length == len(w):
            a.append(w)
    return a


def prompt_guess(position,length):
    length = int(length)
    
    while True:
        guess = input('Now guess {} letters corresponding to letters {} to {} of the unknown word: '.format(length,position + 1,position + length))
        if length != len(guess):
            print("Invalid guess '{}'. Should be {} characters long.\n".format(guess,length))
        else:
            break
    return guess


def compute_score(guess,position,word):
    score = 0
    #pos = STEPS[position][0]
    for i, item in enumerate(guess):
        if item in word:
            score += 20
        if guess[i] == word[i + position]:
            score += 80
    return score


def main():
    name = input('Welcome to the brain teasing zig-zag word game.\n\nWhat is your name? ')
    x,y,z = name.partition(' ')
    print('\nHi {}! We have selected a 6 letter word for you to guess.\n\nLet the game begin!\n'.format(x))
    wordlist = random.choice(load_words('words.txt', 6))
    total_score = 0
    for step in STEPS:
        guess = prompt_guess(step[0], step[1])
        position = step[0]
        length = step[1]
        score = compute_score(guess,step[0],wordlist)
        total_score += score
        #print(guess)        
        print("Your guess and score were: {} : {}\n".format('_'*position + guess + '_'*(6 - length - position),score))
    if guess == wordlist:
        print("Congratulations! You correctly guessed the word '{}'.\nYour total score was {}.".format(wordlist,total_score))
    else:
        print("You did not manage to guess the correct word. It was '{}'. Better luck next time.\nYour total score was {}.".format(wordlist,total_score))

if __name__ == "__main__":
    main()
