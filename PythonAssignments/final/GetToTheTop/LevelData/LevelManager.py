import model
from view import View

#this will break when levels are randomly generated
def GetItemPosition(user_input):
    for i, row in enumerate(model.LevelData.Level.level):
        if user_input in row:
            item_position = [row.index(user_input), i]
            return item_position

def GenerateLevel():
    #placeholder for generating a level (just uses default one for now)
    game_state = model.game.GetEntireState()
    game_state['level_data'] = model.GameData.GameDefaults.defaults['level_data']
    game_state['entity_data'] = model.GameData.GameDefaults.defaults['entity_data']
    level = model.LevelData.Level.level
    model.game.SetLevelMap(level)
    
def initPlayerMap():
    level_map = model.game.GetLevelMap()
    level_height = len(level_map)
    level_width = len(level_map[0])
    
    player_map = []
    for x in range(0, level_height):
        temp_row = []
        for y in range(0, level_width):
            temp_row.append("_")
        player_map.append(temp_row)
        
    model.game.SetPlayerMap(player_map)

def InitLevel(level):
    player_map = initPlayerMap()
    start_position = GetItemPosition('S')
    model.MovePlayerToPos(start_position[0], start_position[1])
    level = populateLevel()
    model.game.SetLevelMap(level)
    
def populateLevel():
    unallowed_tiles = ["H", "S", "X", "1", "2"]
    level = model.game.GetLevelMap()
    for row in level:
        temp_row_index = level.index(row)
        temp_tile_index = 0
        for tile in row:
            if tile not in unallowed_tiles:
                random_val = model.random.random()
                if(random_val < 0.25):
                    if level[temp_row_index][temp_tile_index] == "~":
                        _random_event_2 = model.random.randint(0,3)
                        match _random_event_2:
                            case 0:         
                                random_event = " "
                            case 1:
                                random_event = "1"
                            case 2:
                                random_event = "2"
                            case 3:
                                random_event = " "
                    else:
                        random_event = "H"
                elif(random_val < 0.75):
                    random_event = " "
                elif(random_val < 0.89):
                    random_event = "1"
                elif(random_val < 0.995):
                    random_event = "2"
                elif(random_val >= 0.995):
                    random_event = "X"
                level[temp_row_index][temp_tile_index] = random_event
            temp_tile_index += 1
                
    return level