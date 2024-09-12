import model
from view import View

def GetPlayerEffectiveness():
    player_state = model.game.GetPlayerState()
    
    total_damage = 0
    total_defense = 0
    total_agility = 0
    
    for item in player_state['equipped']:
        with open(model.item_file) as item_file:
            items_json = model.json.load(item_file)
            item_data = items_json[item]
            
            item_positives = item_data['pos']
            item_negatives = item_data['neg']
                
            for effect in item_positives:
                match effect:
                    case 'damage':
                        total_damage += item_positives['damage']
                    case 'defense':
                        total_defense += item_positives['defense']
                    case 'agility':
                        total_agility += item_positives['agility']
                    case default:
                        View.debug_msg("tried to get a positive effect of an item but no keys were recognized!")
                
            for effect in item_negatives:
                match effect:
                    case 'damage':
                        total_damage += item_negatives['damage']
                    case 'defense':
                        total_defense += item_negatives['defense']
                    case 'agility':
                        total_agility += item_negatives['agility']
                    case default:
                        View.debug_msg("tried to get a negative effect of an item but no keys were recognized!")
                        
    effectiveness = [total_damage, total_defense, total_agility]
    return effectiveness
            
def DisplayPlayer():

    player_state = model.game.GetPlayerState()
    
    View.show_message_scroll("Player name: " + player_state['name'] + " Health: " + str(player_state['health']))
    
    View.show_message_scroll("Stats:")
    View.show_message_scroll("    Enemies felled: " + str(player_state['kills']))
    View.show_message_scroll("    Times slain: " + str(player_state['deaths']))
    View.show_message_scroll("    Tiles treaded: " + str(player_state['tiles_traveled']))
    View.show_message_scroll("    Floors cleared: " + str(player_state['ascended']))
    View.show_message_scroll("    Times ascended: " + str(player_state['ascended']))
    View.show_message_scroll("")
    
    View.show_message_scroll("Combat effectiveness:")
    
    player_total_power = GetPlayerEffectiveness()
    
    player_total_damage = player_total_power[0]
    player_total_defense = player_total_power[1]
    player_total_agility = player_total_power[2]
    
    damage_operator = '+'
    defense_operator = '+'
    agility_operator = '+'
    
    if (player_total_damage < 0):
        damage_operator = ''
        
    if (player_total_defense < 0):
        defense_operator = ''
        
    if (player_total_agility < 0):
        agility_operator = ''
        
    power_string = f"ATK: {damage_operator}{player_total_damage}    DEF: {defense_operator}{player_total_defense}    AGL: {agility_operator}{player_total_agility}"
    View.show_message_scroll(power_string)
    View.show_message_scroll("")
    
    View.show_message_scroll("Current status effects: ")
    View.show_message_scroll("    Buffs:")
    if(len(player_state['buffs']) > 0):
        for effect in player_state['buffs']:
            View.show_message_scroll("    " + effect)
    else:
        View.show_message_scroll("        None!")
    View.show_message_scroll("")
    
    View.show_message_scroll("    De-Buffs:")
    if(len(player_state['debuffs']) > 0):
        for effect in player_state['debuffs']:
            View.show_message_scroll("    " + effect)
    else:
        View.show_message_scroll("        None!")
    View.show_message_scroll("")
    
    View.show_message_scroll("Items currently equipped:")
    blank_lines = (3 - len(player_state['equipped']))
    if(len(player_state['equipped']) > 0):
        for item in player_state['equipped']:
            View.show_message_scroll("    " + item)
    else:
        blank_lines -= 1
        View.show_message_scroll("    None!")
    for x in range(0, blank_lines):
            View.show_message_scroll("")
    #View.debug_msg(str(blank_lines))
    #this just makes it so that if a player doesn't have 3 items equipped it still looks nice

def DisplayInventory():
    
    View.clear_screen()
    
    player_state = model.game.GetPlayerState()
    
    View.show_message("All items currently in inventory (equipped + not equipped):")
    View.show_message("")

    all_player_items = player_state['equipped'] + player_state['inventory']    

    if(len(all_player_items) > 0):
        for item in player_state['equipped']:
            View.show_message(" (equipped) " + item)
        for item in player_state['inventory']:
            View.show_message("            " + item)
    else:
        View.show_message("    None!")
    View.show_message("")

# this is a stupid hack. fix this.
def getItemInfo(user_input):
    View.clear_screen()
    player_state = model.game.GetPlayerState()
    
    all_player_items = player_state['equipped'] + player_state['inventory']
    if(user_input in all_player_items):
        with open(model.item_file) as item_file:
                
            items_json = model.json.load(item_file)
            item_data = items_json[user_input]
            item_info = item_data['info']
            
            View.show_message("Item: " + user_input)
            View.show_message(item_info)
            View.show_message("")
                
            item_positives = item_data['pos']
            item_negatives = item_data['neg']
                
            item_damage = 0
            item_defense = 0
            item_agility = 0
                
            item_damage_operator = '+'
            item_defense_operator = '+'
            item_agility_operator = '+'
                
            for effect in item_positives:
                match effect:
                    case 'damage':
                        item_damage += item_positives['damage']
                    case 'defense':
                        item_defense += item_positives['defense']
                    case 'agility':
                        item_agility += item_positives['agility']
                    case default:
                        View.debug_msg("tried to list a positive effect of an item but no keys were recognized!")
                
            for effect in item_negatives:
                match effect:
                    case 'damage':
                        item_damage += item_negatives['damage']
                    case 'defense':
                        item_defense += item_negatives['defense']
                    case 'agility':
                        item_agility += item_negatives['agility']
                    case default:
                        View.debug_msg("tried to list a positive effect of an item but no keys were recognized!")
                            
            if(item_damage < 0):
                item_damage_operator = ''
                    
            if(item_defense < 0):
                item_defense_operator = ''
                    
            if(item_agility < 0):
                item_agility_operator = ''
                    
            item_stat_string = f"ATK: {item_damage_operator}{item_damage}\nDEF: {item_defense_operator}{item_defense}\nAGL: {item_agility_operator}{item_agility}"
            View.show_message(item_stat_string)
            View.show_message("")
                
    else:
        View.show_message("Item not in inventory!")
        View.show_message("")
                
def canEquip(input_item):
    player_state = model.game.GetPlayerState()
    equipped = player_state['equipped']
    with open(model.item_file) as item_file:              
        items_json = model.json.load(item_file)
    if(input_item in items_json):
        item_type = items_json[input_item]['type']
        match item_type:
            case 'armor':
                armor_equip_flag = False
                for item in equipped:
                    if items_json[item]['type'] == 'armor':
                        armor_equip_flag = False
                        View.show_message("You cannot equip " + input_item + " because you already have a set of armor equipped.")
                        break
                    else:
                        armor_equip_flag = True
                return armor_equip_flag
            case 'weapon':
                input_item_hands = items_json[input_item]['hands']
                player_hands = 0
                for item in equipped:
                    if "hands" in items_json[item]:
                        player_hands += items_json[item]['hands']
                if input_item_hands == 2 and input_item_hands + player_hands > 2:
                    View.show_message("You cannot equip " + input_item + " because it is a two-handed weapon, and your hands are not empty.")
                    return False
                elif input_item_hands + player_hands > 2:
                    View.show_message("You cannot equip " + input_item + " because your hands are currently full.")
                else:
                    return True         
    else:
        View.debug_msg("When checking to see if the player could equip and item it was not in the dictionary.")
        
def playerInventoryFull():
    inventory_limit = 10
    player_state = model.game.GetPlayerState()
    all_player_items = player_state['equipped']+player_state['inventory']
    if len(all_player_items) >= inventory_limit:
        View.show_message("Sorry, you can only carry 10 items at any given time. (equipped + not equipped)")
        View.show_message("")
        return True
    else:
        return False

def equipItem(user_input):
    
    View.clear_screen()

    player_state = model.game.GetPlayerState()
    
    all_player_items = player_state['equipped'] + player_state['inventory']
    
    if(user_input in all_player_items):
        if(canEquip(user_input)):
            player_state['inventory'].remove(user_input)
            player_state['equipped'].append(user_input)
            model.game.SetPlayerState(player_state)
            View.show_message("Successfully equipped: " + user_input + "!")
            View.show_message(" ")
    else:
        View.show_message("Item not in inventory!")
        View.show_message("")
        
def unEquipItem(user_input):
    
    View.clear_screen()

    player_state = model.game.GetPlayerState()
    
    all_player_items = player_state['equipped'] + player_state['inventory']
    
    if(user_input in all_player_items):
        if(user_input in player_state['equipped']):
            player_state['equipped'].remove(user_input)
            player_state['inventory'].append(user_input)
            model.game.SetPlayerState(player_state)
            View.show_message("Successfully unequipped: " + user_input + "!")
            View.show_message("")
        else:
            View.show_message("Item is not equipped!")
            View.show_message("")
    else:
        View.show_message("Item not in inventory!")
        View.show_message("")

def dropItem(user_input):
    
    View.clear_screen()
    
    player_state = model.game.GetPlayerState()
    
    all_player_items = player_state['equipped'] + player_state['inventory']
    
    if(user_input in all_player_items):
        View.show_message("Are you sure you want to drop " + user_input + "? (This will destroy the item and cannot be undone.)\n")
        decision = View.get_input("Type 'YES' in all capital letter to confirm, or anything else to cancel: ")
        View.show_message("")
        if decision == 'YES':
            if(user_input in player_state['equipped']):
                player_state['equipped'].remove(user_input)
            else:
                player_state['inventory'].remove(user_input)
            model.game.SetPlayerState(player_state)
            View.show_message("You dropped your " + user_input + "...")
            View.show_message("")
        else:
            View.show_message("You kept your " + user_input + "...")
            View.show_message("")
    else:
        View.show_message("Item not in inventory!")
        View.show_message("")
     
def handleInventoryInput(user_input):
    list_input = user_input.split()
    operation = list_input[0]
    list_input.remove(operation)
    operation = operation.upper()
    query = ' '.join(list_input)
    #View.debug_msg(str(query))
    
    match operation:
        case 'INFO':
            getItemInfo(query)
        case 'EQUIP':
            equipItem(query)
        case 'UNEQUIP':
            unEquipItem(query)
        case 'DROP':
            dropItem(query)
        case default:
            View.show_message("error! input not recognized, try again?")
    View.confirm()

def OpenInventory():
    
    in_inventory = True
    while(in_inventory):
        View.clear_screen()
        View.show_message(model.ui.inventory_title_text)
        View.show_message("")
        DisplayPlayer()
        user_input = View.get_input("")
        if (user_input == ""):
            View.show_message("input not recognized, try again!")
            View.confirm()
        elif (user_input.upper() == "ALL"):
            DisplayInventory()
            View.confirm()
        elif(user_input.upper() == 'Q'):
            in_inventory = False
            #model.NextTurn()
        else:
            handleInventoryInput(user_input)
       
        
    