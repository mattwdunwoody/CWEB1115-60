from model import *
from view import View

def main():
    
    title_input = TitleScreen()

    if(title_input == 'load'):
        model.game.load_game()
        NextTurn()
    elif(title_input == ''):
        NewGame()
    else:
        input = View.get_input("Did you mean to spell 'load'? (Y/N): ")
        input = input.upper()
        if(input == 'Y'):
            model.game.load_game()
            NextTurn()
        elif(input == 'N'):
            NewGame()
        else:
            View.show_message("You misspelled some easy stuff twice. Your punishment(?) is to start a new game anyway, even if didn't want to.")
            View.confirm()
            NewGame()
        

if __name__ == "__main__":
    main()