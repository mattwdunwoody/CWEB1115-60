from view import View
import model

def TitleScreen():
    View.show_message(model.ca.title_string)
    load = View.get_input("\nType 'load' to load last save or press enter to start a new game...")
    View.show_message("")
    return load

def NewGameDialogue():
    View.show_message_fancy_top("")
    View.show_message_fancy_top_scrollhorizontally("You awake in a dark dungeon...")
    playerName = View.get_input_scroll_horizontally("What is your name, adventurer? ")
    return playerName

def nextTurnDialogue():
    View.show_message_fancy_bottom("What would you like to do?\n1. Move (M)\n2. Check your map (MAP)\n3. Check your inventory (I)\n4. Get help (H)\nor type 'Q' to quit...")
    playerChoice = View.get_input("")
    
    return playerChoice

def randomSplash():
    random_splash = model.rs.splashes[model.random.randint(0, len(model.rs.splashes)-1)]
    return random_splash
    