import model
from view import View

class Game:
    def __init__(self):
        self.is_over = False
        self.state = ""
        self.outfile = 'game_state.json'

    def save_game(self):
        try: 
            with open(self.outfile, 'w') as file:
                model.json.dump(self.state, file, indent=4)
        except:
            print("error writing to save")

    def load_game(self):
        try:
            with open(self.outfile, 'r') as file:
                self.state = model.json.load(file)
        except FileNotFoundError:
            View.get_input("Error, no save file found. Press enter to start a new game...")
            model.NewGame()
        except model.json.JSONDecodeError as e:
            View.show_message("JSON Decode error: " + str(e))
            View.show_message("Possibly corrupt file?")
            input = View.get_input("Press Enter to start a new game or type Q to quit: ")
            if (input.upper() == 'Q'):
                quit()
            else:
                model.NewGame()
            
    def new_save(self):
        try: 
            with open(self.outfile, 'w') as file:
                #View.debug_msg("tried to write defaults")
                model.json.dump(model.GameData.GameDefaults.defaults, file, indent=4)
        except:
            print("error writing new save file")

    # all of this could get refactored
    def RefreshState(self):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)

    def GetGameState(self):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            game_state = self.state['game_state']
            return game_state

    def SetGameState(self, new_state):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            self.state['game_state'] = new_state
        with open(self.outfile, 'w') as file:
            model.json.dump(self.state, file, indent=4)
            
    def GetPlayerState(self):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            player_state = self.state['player_state']
            return player_state
        
    def SetPlayerState(self, new_state):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            self.state['player_state'] = new_state
        with open(self.outfile, 'w') as file:
            model.json.dump(self.state, file, indent=4)
            
    def GetPlayerMap(self):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            player_map = self.state['level_data']['player_map']
            return player_map
        
    def SetPlayerMap(self, new_map):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            self.state['level_data']['player_map'] = new_map
        with open(self.outfile, 'w') as file:
            model.json.dump(self.state, file, indent=4)
            
    def GetLevelMap(self):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            level_map = self.state['level_data']['level_map']
            return level_map
        
    def SetLevelMap(self, new_map):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            self.state['level_data']['level_map'] = new_map
        with open(self.outfile, 'w') as file:
            model.json.dump(self.state, file, indent=4)
            
    def GetEntireState(self):
        with open(self.outfile, 'r') as file:
            state = model.json.load(file)
            return state
        
    def SetEntireState(self, state):
        self.state = state
        with open(self.outfile, 'w') as file:
            model.json.dump(self.state, file, indent=4)
            
    def SetChestState(self, chest_id, chest_state):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            self.state['entity_data']['chests'][chest_id] = chest_state
            #View.debug_msg("Chest state at " + str(chest_id) + ": " + str(self.state['entity_data']['chests'][chest_id]))
        with open(self.outfile, 'w') as file:
            model.json.dump(self.state, file, indent=4)
            #View.debug_msg("saved new chest state to file.")
            
    def GetChestState(self, chest_id):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            chest_state = self.state['entity_data']['chests'][chest_id]
            return chest_state
        
    def GetChestID(self, x, y):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            chest_data = self.state['entity_data']['chests']
            for chest in chest_data:
                if chest_data[chest]['x'] == x and chest_data[chest]['y'] == y:
                    return chest
            #View.debug_msg("Chest not found!")
            return False
        
    def GetEnemyID(self, x, y):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            enemy_data = self.state['entity_data']['enemies']
            for enemy_id in enemy_data:
                if enemy_data[enemy_id]['x'] == x and enemy_data[enemy_id]['y'] == y:
                    return enemy_id
            #View.debug_msg("Enemy not found!")
            return False
        
    def GetEnemyByID(self, enemy_id):
        with open(self.outfile, 'r') as file:
            self.state = model.json.load(file)
            enemy_state = self.state['entity_data']['enemies'][enemy_id]
            return enemy_state
        
    def SetEnemyState(self, enemy_id, enemy_state):
            with open(self.outfile, 'r') as file:
                self.state = model.json.load(file)
                self.state['entity_data']['enemies'][enemy_id] = enemy_state
                #View.debug_msg("Enemy state at " + str(enemy_id) + ": " + str(self.state['entity_data']['enemies'][enemy_id]))
            with open(self.outfile, 'w') as file:
                model.json.dump(self.state, file, indent=4)
                #View.debug_msg("saved new enemy state to file.")
    
    # this is bad
    def GameOver(self):
        defaults = model.GameData.GameDefaults.defaults
        game_state = self.GetEntireState()
        game_state['level_data'] = defaults['level_data']
        game_state['entity_data'] = defaults['entity_data']
        game_state['player_state']['health'] = defaults['player_state']['health']
        game_state['player_state']['buffs'] = defaults['player_state']['buffs']
        game_state['player_state']['debuffs'] = defaults['player_state']['debuffs']
        game_state['player_state']['equipped'] = defaults['player_state']['equipped']
        game_state['player_state']['inventory'] = defaults['player_state']['inventory']
        game_state['player_state']['position'] = defaults['player_state']['position']
        
        self.SetEntireState(game_state)
        model.NextLevel()
        self.save_game()
        quit()