import model
from view import View

in_help_menu = False

def getHelp():
    View.clear_screen()
    View.show_message("Welcome to the help menu. Enter the name of what you want help with to get started or type 'Q' to exit back to game.")
    View.show_message("")
    
    in_help_menu = True

    while(in_help_menu):
        help_choice = View.get_input("")
        if(help_choice == 'Q'):
            in_help_menu = False
            break
        else:
            View.show_message("")
            View.show_message_scroll_lines(getHelpText(help_choice))
            View.show_message("")
            View.confirm()
            View.clear_screen()
            View.show_message("Enter the name of another term to get help or type 'Q' to exit back to the game.")
            View.show_message("")
            
    model.NextTurn()
                
def getHelpText(input):
    input = input.upper()
    for help_text, searches in model.ht.help_text_dict.items():
        if input in searches:
            return help_text
    help_text = 'No help was found for entered term. Check spelling?'
    return help_text
        

            
        
            
    