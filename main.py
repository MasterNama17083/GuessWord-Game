'''
Word Guessing Game by (C) 2025 Master Nama
Version 1.0 (Build Date: 30th May 2025)

Feel free to modify or fork it, Please make sure to give me a credit if you used.
All rights reserved.
'''

Game_Init = { # DO NOT EDIT!!!
    "gameState" : "start",  # <= Game state to start (e.g. win)
    "startGame" : "",       # <= Start at the screen before will answer
    "chance" : 3,           # <= Set to limited attempt while typing if you tried
    "attempt" : 0,          # <= Guess count (current)
}

Game_Config = { # Custom theme:
    "debug" : False,                                                                             # <= Debug Mode (please use for debugging purposes before figure out)
    "mainTitle" : "What are some fruits?",                                                       # <= Custom Main title at the beginning text screen
    "wordFnd" : ["Apple" , "Banana" , "Orange" , "Lemon" , "Cherry" , "Watermelon" , "Grapes"],  # <= Answer Words
    "wonTitle" : "You guessed {resultWord}! You win.",                                           # <= Custom Win text
    "overTitle" : "Sorry, You gave up! didn't guessed yet. Game over!",                          # <= Custom Game Over text
}


if Game_Config["debug"]:
    print("DEBUG MODE - ALL LIST OF ANSWER WORDS:")
    for ans_DbgList in Game_Config["wordFnd"]:
        print("[DEBUG ANSWER]:", ans_DbgList)

def main():
    if Game_Init["gameState"] == "start":
        while Game_Init["startGame"] not in Game_Config["wordFnd"] and Game_Init["gameState"] != "lose":
        # Beginning State:
            if Game_Init["attempt"] < Game_Init["chance"]:
                print("You have chance:" , str(Game_Init["chance"] - Game_Init["attempt"]) + "\n")
                Game_Init["attempt"] += 1
                input_Ans = Game_Init["startGame"] = input(Game_Config["mainTitle"] + "\nEnter the answer: ").lower()
                for answer in Game_Config["wordFnd"]:
                    if input_Ans == answer.lower():
                        Game_Init["startGame"] = answer
                        Game_Init["gameState"] = "won"
                        break
            else:
                Game_Init["gameState"] = "lose"
        # Win State:
            if Game_Init["gameState"] == "won":
                print("\n\n" + Game_Config["wonTitle"].format(resultWord = Game_Init["startGame"]))
        # Lose State:
            elif Game_Init["gameState"] == "lose":
                print("\n\n" + Game_Config["overTitle"])


main()