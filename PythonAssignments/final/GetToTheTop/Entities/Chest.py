import model
from view import View

class Chest():
    def __init__(self, x, y):
        self.items = []
        self.x = x
        self.y = y
        self.chest_id = 0
        self.createChest(self.x, self.y)
        self.chest_state = {
            "x": self.x,
            "y": self.y,
            "items": self.items
        }

    @staticmethod
    def fillChest():
        level_data = model.game.GetEntireState()['level_data']
        current_level = level_data['current_level']
        chest_size_limit = model.random.randint(1, 3)
        items_possible = []
        items_in_chest = []
        with open(model.item_file) as item_file:              
            items_json = model.json.load(item_file)
            for item in items_json:
                if items_json[item]['tier'] <= current_level:
                    items_possible.append(item)
                
        while len(items_in_chest) < chest_size_limit:
            random_item_index = model.random.randint(0, len(items_possible)-1)
            if items_possible[random_item_index] not in items_in_chest:
                items_in_chest.append(items_possible[random_item_index])
            
        return items_in_chest

    def createChest(self, x, y):
        game_state = model.game.GetEntireState()
        
        chest_id = model.game.GetChestID(x, y)
        
        if(chest_id == False):
            self.chest_id = len(game_state['entity_data']['chests']) + 1
            self.items = self.fillChest()
            self.chest_state = {
                "x": self.x,
                "y": self.y,
                "items": self.items
                }
            model.game.SetChestState(self.chest_id, self.chest_state)
        else:
            chest_state = model.game.GetChestState(chest_id)
            self.chest_id = chest_id
            self.items = chest_state['items']
            self.x = chest_state['x']
            self.y = chest_state['y']