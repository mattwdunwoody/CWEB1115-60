import model
from view import View

class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.enemy_id = 0
        self.type = ""
        self.health = 0
        self.stats = {}
        self.abilities = {}
        self.level = 0
        self.initEnemy(self.x, self.y)
        self.enemy_state = {
            "id": self.enemy_id,
            "type": self.type,
            "x": self.x,
            "y": self.y,
            "health": self.health,
            "stats": self.stats,
            "abilities": self.abilities,
            "level": self.level
        }
    
    def initEnemy(self, x, y):
        game_state = model.game.GetEntireState()
        
        enemy_id = model.game.GetEnemyID(x, y)
        
        if(enemy_id == False):
            #View.debug_msg("No enemies found. Creating new enemy at " + str(x) + ", " + str(y) + "...")
            self.createEnemy(game_state, x, y)
        else:
            #View.debug_msg("Enemy already existed at " + str(x) + ", " + str(y))
            enemy_state = model.game.GetEnemyByID(enemy_id)
            self.enemy_id = enemy_id
            self.type = enemy_state['type']
            self.x = enemy_state['x']
            self.y = enemy_state['y']
            self.setStats(self.type)
            
    def createEnemy(self, game_state, x, y):
        self.enemy_id = len(game_state['entity_data']['enemies']) + 1
        
        with open(model.enemy_file, "r") as file:
            enemy_data = model.json.load(file)
            
        possible_enemies = []
        
        for enemy in enemy_data:
            possible_enemies.append(enemy)
            
        enemy_choice = possible_enemies[model.random.randint(0, len(possible_enemies)-1)]
        type_data = enemy_data[enemy_choice]
        
        self.type = enemy_choice
        stats = type_data['stats']
        difficulty = model.game.GetEntireState()['level_data']['current_level'] - 1
        self.health = type_data['health'] + difficulty
        self.stats = {
            "damage":  (stats['damage']  + difficulty),
            "defense": (stats['defense'] + difficulty),
            "agility": (stats['agility'] + difficulty)
        }
        self.abilities = type_data['abilities']
        self.level = difficulty + 1
        self.enemy_state = {
            "type": self.type,
            "x": self.x,
            "y": self.y
        }
           
        model.game.SetEnemyState(self.enemy_id, self.enemy_state)
       
    def setStats(self, enemy_type):
        with open(model.enemy_file, "r") as file:
                enemy_data = model.json.load(file)
            
        type_data = enemy_data[enemy_type]
        stats = type_data['stats']
        abilities = type_data['abilities']
        difficulty = model.game.GetEntireState()['level_data']['current_level'] - 1
        self.health = type_data['health'] + difficulty
        self.stats = {
            "damage":  (stats['damage']  + difficulty),
            "defense": (stats['defense'] + difficulty),
            "agility": (stats['agility'] + difficulty)
        }
        self.abilities = abilities
        self.level = difficulty + 1