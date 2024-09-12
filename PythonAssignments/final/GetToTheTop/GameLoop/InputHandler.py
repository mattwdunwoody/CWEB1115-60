import model
from view import View

def handleInput(input):
    input = input.upper()
    
    match input:
        case 'M':
            #move
            model.MoveMenu()
        case 'MAP':
            #map
            View.clear_screen()
            model.OpenMapWithKey()
            View.confirm()
            View.show_message("")
            model.NextTurn()
        case 'I':
            #inventory
            model.OpenInventory()
            model.NextTurn()
        case 'H':
            #help
            model.getHelp()
            pass
        case 'Q':
            #quit
            model.game.save_game()
            View.show_message("Saving game...")
            quit()
            pass
        case default:
            View.get_input("Input not recognized, check spelling? (press Enter to continue...)")
            model.NextTurn()
                