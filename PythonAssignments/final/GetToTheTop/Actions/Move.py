import model
from view import View

def look():
    View.show_message("This feature has not been implemented yet.")
    View.show_message("")

def MovePlayerToPos(xWant, yWant):
    
    level_map = model.game.GetLevelMap()
    player_state = model.game.GetPlayerState()
    player_position = player_state['position']

    if level_map[yWant][xWant] != 'H':
        player_position['x'] = xWant
        player_position['y'] = yWant
        
        model.game.SetPlayerState(player_state)

def movePlayer(xWant, yWant):
    
    level = model.game.GetLevelMap()
    player_state = model.game.GetPlayerState()
    xPrevious = player_state['position']['x']
    yPrevious = player_state['position']['y']
    player_state['position']['x'] += xWant
    player_state['position']['y'] += yWant 
    model.game.SetPlayerState(player_state)
    
    if collisionCheck() == True:
        View.show_message("You smack face first into a wall and fall back into your previous tile!")
        player_state['position']['x'] = xPrevious
        player_state['position']['y'] = yPrevious
        model.game.SetPlayerState(player_state)
        return False
    else:
        player_state['tiles_traveled'] += 1
        model.game.SetPlayerState(player_state)
        model.UpdatePlayerMap()
        return True
        
def collisionCheck():
    level = model.game.GetLevelMap()
    player_position = model.game.GetPlayerState()['position']
    if(level[player_position['y']][player_position['x']] == 'H'):
        return True
    else:
        return False

def eventCheck():
    level = model.game.GetLevelMap()
    player_map = model.game.GetPlayerMap()
    player_position = model.game.GetPlayerState()['position']
    tile = level[player_position['y']][player_position['x']]
    ascendCheck = ""
    match tile:
        case " ":
            pass
        case "1":
            tile = "!"
            model.FindEnemy(player_position['x'], player_position['y'])
        case "2":
            if player_map[player_position['y']][player_position['x']] == "$":
                tile = "$"
                View.show_message("You already looted this chest!")
                View.show_message("")
                user_choice = View.get_input("Do you want to open this chest again? (Y/N): ").upper()
                match user_choice:
                    case "Y":
                        #model.ReopenChest(player_position['x'], player_position['y'])
                        model.FindChest(player_position['x'], player_position['y'])
                    case "N":
                        View.show_message("You decide to leave the chest alone...")
                    case _:
                        View.show_message("Input not recognized!")
            else:
                tile = "$"
                model.FindChest(player_position['x'], player_position['y'])
        case "X":
            tile = "E"
            ascendCheck = model.CheckAscend()
    player_map[player_position['y']][player_position['x']] = tile
    model.game.SetPlayerMap(player_map)
    model.UpdatePlayerMap()
    match ascendCheck:
        case "":
            pass
        case True:
            model.Ascend()
        case False:
            pass

# this and all other input could get cleaned up and moved to the input handler file
def handleMoveInput(input):
    match input:
        case 'L' | 'LOOK' | 'E':
            look()
        case 'MAP':
            model.OpenMap()
        case 'I':
            model.OpenInventory()
        case 'W':
            if movePlayer(0, -1):
                moveDialog("North")
            moveCleanup()
        case 'S':
            if movePlayer(0, 1):
                moveDialog("South")
            moveCleanup()
        case 'D':
            if movePlayer(1, 0):
                moveDialog("East")
            moveCleanup()
        case 'A':
            if movePlayer(-1, 0):
                moveDialog("West")
            moveCleanup()
        case default:
            View.show_message("Input not recognized. Check spelling?")
            
def moveDialog(direction):
    View.show_message("You move one tile "+direction+".")

def moveCleanup():
    View.show_message("")
    model.OpenMap()
    eventCheck()

def MoveMenu():
    
    in_move_menu = True
    
    while(in_move_menu):
        View.clear_screen()
        View.show_message(model.ui.map_title_text)
        View.show_message("")
        model.OpenMapWithKey()
        user_input = View.get_input("").upper()
        if(user_input == 'Q'):
            in_move_menu = False
            break
        else:
            View.clear_screen()
            handleMoveInput(user_input)
            View.confirm()
    
    model.NextTurn()