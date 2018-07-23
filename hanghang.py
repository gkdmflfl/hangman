def hangman(word):
    wrong = 0
    stages = ["",                       #0
              "--------         ",      #1
              "|        |       ",      #2
              "|        |       ",      #3
              "|        0       ",      #4
              "|       /|]      ",      #5
              "|        |       ",      #6
              "|       / ]      ",      #7
              "|                "       #8
              ]

    rletters = list(word)                       #rletter = ["c", "a", "t"]
    board = ["__"] * len(word)                  #len('cat') = 3, board = "__"*3
    win = False
    print("Welcome to hangman")
    
    while wrong < len(stages) - 1:              #len(stages)-1 = 8
        print("\n")
        msg = "Guess a letter : "
        char = input(msg)
        
        if char in rletters:
            cind = rletters.index(char)         #cind에 맞춘 자리를 저장
            board[cind] = char                  
            rletters[cind] = '$'                #rletters의 바뀐 부분은 $로 바
        else:
            wrong += 1
        print((" ".join(board)))                #board를 "__"사이에 ' '를 넣어 출
        print("\n".join(stages[0: wrong + 1]))  #stages(행맨)를 0~wrong+1까지 개행을 넣어 출력

        if "__" not in board:                   
            print("You win! It was : ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

hangman("letter")

              
