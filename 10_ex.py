# %% 1. 答えの単語をリストからランダムに選ぶようにする
import random

ans = ["owl", "potter", "iphone", "program"]


def hangman(word):
    wrong = 0   # 回答者が間違えた回数をカウントする
    stages = ["",   # 文字列を１行に１つずつ出力して、吊られた男の状況を示す
              "________      ", 
              "|      |      ", 
              "|      0      ", 
              "|     /|\     ", 
              "|     / \     ", 
              "|             "
              ]
    rletters = list(word)   # 答えなければいけない残りの文字を格納
    board = ["_"] * len(word)   # _でヒントを示す文字列のリスト e.g.['_', '_', '_']
    win = False     # 勝敗の状態を記録
    print("Welcome to Hangman!!")
    
    while wrong < len(stages)-1:    # ループの試行回数制限は、間違えた回数がハングマン出力が終わる６回までである
        print("\n") # 空行
        char = input("Type an alphabet : ")
        if char in rletters:
            cidx = rletters.index(char) # 先頭インデックス値は0の、インデックス値を返す
            board[cidx] = char      # 正解時には、インデックス値にある'_'をcharに置き換える
            rletters[cidx] = '$'    # 正解の単語に同じ文字が複数あるときに、
                                    # rlettersの正解した文字を$マークに置き換える
                                    # 次ループでは、indexメソッドがもう１つの文字のインデックス値を返すようになる？
        else:
            wrong += 1
        print("hint: " + " ".join(board))      # スコアボードを出力
        e = wrong + 1
        print("\n".join(stages[0:e]))   # stagesリストから失敗した回数分(初期は絞首棒と縄で+2分表示されている)ハングマンが描かれる
        # 勝利判定
        if "_" not in board:
            print("You Win!!")
            print("answer: " + " ".join(board))  #答えの表示
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose! The answer is {}.".format(word))


hangman(random.choice(ans))








