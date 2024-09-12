import model

defaults = {
    "game_state": "start",
    "player_state": {
        "name": "Dumbo",
        "health": 20,
        "buffs": [],
        "debuffs": [],
        "equipped": ['basic sword', 'basic shield', 'basic armor'],
        "inventory": [],
        "kills": 0,
        "deaths": 0,
        "floors": 0,
        "ascended": 0,
        "tiles_traveled": 1,
        "position": {
            "x": 0,
            "y": 0
            }
        },
    "level_data": {
        "current_level": 1,
        "top": 4,
        "level_map": 0,
        "player_map": 0
        },
    "entity_data": {
        "chests": {},
        "enemies": {}
        }    
    }