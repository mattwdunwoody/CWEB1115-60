import model
from view import View

def OpenMap():
    
    player_map = model.game.GetPlayerMap()
    player_position = model.game.GetPlayerState()['position']
    
    # print("Your position: ", player_position)
    
    player_map[player_position['y']][player_position['x']] = '@'
    
    for row in player_map:
        display_row = []
        for item in row:
            if item == '_' or item == '~':
                item = ' '
            elif item == "1" or item == "2" or item == 'X':
                item = "?"
            display_row.append(item)
            display_row.append(" ")
            #print(item, end="")
            #print(" ", end="")
        if not all(x == display_row[0] for x in display_row):
            for item in display_row:
                print(item, end="")
            print("")
        else:
            pass
    View.show_message("")

# these two functions should be consolidated with a decorator    
def OpenMapWithKey():
    View.show_message(model.ui.map_key)
    View.show_message("Up = North")
    
    player_map = model.game.GetPlayerMap()
    player_position = model.game.GetPlayerState()['position']
    
    # print("Your position: ", player_position)
    
    player_map[player_position['y']][player_position['x']] = '@'
    
    for row in player_map:
        display_row = []
        for item in row:
            if item == '_' or item == '~':
                item = ' '
            elif item == "1" or item == "2" or item == 'X':
                item = "?"
            display_row.append(item)
            display_row.append(" ")
            #print(item, end="")
            #print(" ", end="")
        if not all(x == display_row[0] for x in display_row):
            for item in display_row:
                print(item, end="")
            print("")
        else:
            pass
    View.show_message("")
    
def UpdatePlayerMap():
    view_distance = 1
    player_position = model.game.GetPlayerState()['position']
    playerMap = model.game.GetPlayerMap()
    level_map = model.game.GetLevelMap()
    
    #this needs to get refactored
    row_index = 0
    for row in playerMap:
        if abs(row_index - player_position['y']) <= view_distance+1:
            if abs(row_index - player_position['y']) <= view_distance:
                i = 0
                while i < len(row):
                    if abs(i - player_position['x']) <= view_distance:
                        if row[i] == '.' or row[i] == '_':
                            temp_index_y = row_index
                            temp_index_x = i
                            playerMap[temp_index_y][temp_index_x] = level_map[temp_index_y][temp_index_x]
                    elif abs(i - player_position['x']) <= (view_distance + 1):
                        if row[i] == '_':
                            playerMap[row_index][i] = '.'
                    i += 1
            else:
                i = 0
                while i < len(row):
                    if abs(i - player_position['x']) <= (view_distance + 1):
                        if row[i] == '_':
                            playerMap[row_index][i] = '.'

                    i += 1
        row_index += 1
                        
    model.game.SetPlayerMap(playerMap)
            
def EnemyKilledOnMap():
    player_state = model.game.GetPlayerState()
    level_map = model.game.GetLevelMap()
    level_map[player_state['position']['y']][player_state['position']['x']] = '#'
    model.game.SetLevelMap(level_map)
    player_map = model.game.GetPlayerMap()
    player_map[player_state['position']['y']][player_state['position']['x']] = '#'
    model.game.SetPlayerMap(player_map)
    #model.UpdatePlayerMap()