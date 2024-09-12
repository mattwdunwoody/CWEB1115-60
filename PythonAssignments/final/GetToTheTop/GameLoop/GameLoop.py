from Dialogue.Narrator import randomSplash
import model
from view import View

def NextLevel():
    model.GenerateLevel()
    model.InitLevel(model.game.GetLevelMap())
    model.UpdatePlayerMap()

def NewGame():         
    game = model.game
    game.new_save()
            
    model.NewPlayer()
    
    NextLevel()

    NextTurn()
            
def NextTurn():
    View.show_message_fancy_top("")
    View.show_message_scroll_horizontally(model.randomSplash())
    model.handleInput(model.nextTurnDialogue())
    
def CheckAscend():
    View.show_message("You found a staircase leading up to the next level!")
    user_input = View.get_input("Ascend? (Y/N): ").upper()
    match user_input:
        case 'Y':
            return True
        case 'N':
            View.show_message("You decided to stay on the current level for a little while longer.")
            return False
            
def Ascend():
    player_state = model.game.GetPlayerState()
    player_state['floors'] += 1
    model.game.SetPlayerState(player_state)
    current_level = model.game.GetEntireState()['level_data']['current_level']
    world_top = model.game.GetEntireState()['level_data']['top']
    current_level += 1
    if(current_level >= world_top):
        player_state['ascended'] += 1
        model.game.SetPlayerState(player_state)
        
        View.clear_screen()
        View.show_message_game_over(model.ca.win_screen)
        View.show_message("")
        View.show_message_scroll_horizontally("You escaped from the dungeon! Congratulations!")
        View.show_message("")
        View.dramatic_pause()
        View.show_message_scroll_horizontally("Type 'load' at main menu to start a new game using your current character.")
        View.show_message("")
        model.game.GameOver()
    else:
        View.show_message("You go up the stairs and enter another floor of the dungeon...")
        new_state = model.game.GetEntireState()
        new_state['level_data']['current_level'] = current_level
        model.game.SetEntireState(new_state)
        model.game.save_game()
        NextLevel()