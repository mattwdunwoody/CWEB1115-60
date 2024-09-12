import model
import controller
from view import View

class Player:
    def __init__(self, name):
        self.default_player_state = model.GameData.GameDefaults.defaults['player_state']
        self.name = name
        self.health = self.default_player_state['health']
        self.buffs = self.default_player_state['buffs']
        self.debuffs = self.default_player_state['debuffs']
        self.equipped = self.default_player_state['equipped']
        self.inventory = self.default_player_state['inventory']
        self.kills = self.default_player_state['kills']
        self.deaths = self.default_player_state['deaths']
        self.floors = self.default_player_state['floors']
        self.ascended = self.default_player_state['ascended']
        self.tiles_traveled = self.default_player_state['tiles_traveled']
        self.position = self.default_player_state['position']
        self.player_state = {
            'name': self.name,
            'health': self.health,
            'buffs': self.buffs,
            'debuffs': self.debuffs,
            'equipped': self.equipped,
            'inventory': self.inventory,
            'kills': self.kills,
            'deaths': self.deaths,
            'floors': self.floors,
            'ascended': self.ascended,
            'tiles_traveled': self.tiles_traveled,
            'position': self.position
        }

def NewPlayer():
    player_name = model.NewGameDialogue()
    if player_name == "":
        player_name = "Paladin         "
    elif len(player_name) > 16:
        player_name = [*player_name]
        while len(player_name) > 16:
            player_name.pop()
        player_name_string = "".join(str(char) for char in player_name)
        player_name = player_name_string
        
    elif len(player_name) < 16:
        player_name = [*player_name]
        while len(player_name) < 16:
            player_name.append(" ")
        player_name_string = "".join(str(char) for char in player_name)
        player_name = player_name_string

    player = Player(player_name)
    model.game.SetPlayerState(player.player_state)