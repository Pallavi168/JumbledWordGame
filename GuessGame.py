import random

def choose():
    words = ['rainbow', 'computer', 'science', 'programming', 'mathematics', 'player', 'condition', 'water', 'game']
    pick = random.choice(words)
    return pick

def shuffle(word):
    shuffled = ''.join(random.sample(word, len(word)))
    return shuffled

def thank(p1n, p2n, p1, p2):
    print("")
    print(p1n, 'Your score is : ', p1) 
    print(p2n, 'Your score is : ', p2)
    if p1 > p2: 
        print("winner is : ", p1n) 
    elif p2 > p1: 
        print("winner is : ", p2n) 
    else: 
        print("Draw..Well Played")

    print('Thanks for playing...')
    print("")

def play():
    p1name = input("player 1, Please enter your name : ") 
    p2name = input("Player 2 , Please enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = 0

    while(1):
        #Computer's part
        picked_word = choose()
        #create question
        qn = shuffle(picked_word) 
        print("")
        print("Guess the word: ", qn)
        
        #Player 1
        if turn % 2 == 0:
            print(p1name, 'Your Turn.')
            ans = input("Answer: ")

            if ans == picked_word:
                pp1 += 1
                print('Your score is : ', pp1)
            else:
                print("Better luck next time ..")
                
            c = int(input("press 1 to continue and 0 to quit : "))

            if c == 0:
                thank(p1name, p2name, pp1, pp2) 
                break
        #Player 2
        else:
            print(p2name, 'Your Turn.')
            ans = input("Answer: ")

            if ans == picked_word:
                pp2 += 1
                print('Your score is : ', pp2)
            else:
                print("Better luck next time ..")
                
            c = int(input("press 1 to continue and 0 to quit : "))

            if c == 0:
                thank(p1name, p2name, pp1, pp2) 
                break
        turn += 1

play()
