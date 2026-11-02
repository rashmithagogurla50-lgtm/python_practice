import random
def guessing_game(max_trials=6):
    secreat=random.randint(1,100)
    print(f"\n guessnumber(1,100).you have{max_trials}trails")
    for attempts in range(1,max_trials+1):
        guess=int(input(f"try{attempts}"))
        if guess==secreat:
            print(f"correct"in {attempts})
            break
        print("too low"if guess<secreat else"too high")
    else:
        print(f"out of trails.it was{secreat}")
guessing_game()