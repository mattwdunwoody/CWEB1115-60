import model
from view import View

def takeItems(user_input, chest):
    items = chest.items
    #user_input = user_input.lower()
    player_state = model.game.GetPlayerState()
    if not model.playerInventoryFull():
        if user_input == 'all':
            temp_list = []
            for item in items:
                temp_list.append(item)
                if not model.playerInventoryFull():
                    player_state['inventory'].append(item)
                    model.game.SetPlayerState(player_state)
                    temp_list.remove(item)
            items.clear()
            for item in temp_list:
                items.append(item)
            if len(items) == 0:
                View.show_message("You took all the items in the chest...")
            else:
                for item in items:
                    View.show_message("You left the " + item + " in the chest...")
            View.show_message("")
        elif user_input in items:
            items.remove(user_input)
            player_state['inventory'].append(user_input)
            model.game.SetPlayerState(player_state)
            View.show_message("You took the " + user_input + "...")
            View.show_message("")
        else:
            View.show_message("Error! Item is not in chest.")
            View.show_message("")

def swapItems(user_input, chest):
    items = chest.items
    #user_input = user_input.lower()
    player_state = model.game.GetPlayerState()
    all_player_items = player_state['inventory'] + player_state['equipped']
    if len(all_player_items) <= 0:
        View.show_message("You don't currently have anything to swap with!")
    elif user_input == 'all':
        View.show_message("Error! Can only swap one item at a time!")
    elif user_input in items:
        View.show_message("Select an item to swap " + user_input + " with:")
        View.show_message("")
        for item in all_player_items:
            View.show_message_scroll(item)
        View.show_message("")
        item_swap_input = View.get_input("")
        if(item_swap_input in player_state['inventory']):
            player_state['inventory'].append(user_input)
            chest.items.remove(user_input)
            player_state['inventory'].remove(item_swap_input)
            chest.items.append(item_swap_input)
            View.show_message("Successfully swapped " + item_swap_input + " for " + user_input)
            View.show_message("")
        elif(item_swap_input in player_state['equipped']):
            equip_input = View.get_input(item_swap_input + " is currently equipped. Do you still want to swap it out? This will attempt to equip the new item. (Y/N): ").upper()
            match equip_input:
                case "Y":
                    player_state['equipped'].remove(item_swap_input)
                    model.game.SetPlayerState(player_state)
                    if(model.canEquip(user_input)):
                        player_state['equipped'].append(user_input)
                        chest.items.remove(user_input)
                        chest.items.append(item_swap_input)
                        model.game.SetPlayerState(player_state)
                        View.show_message("Successfully swapped " + item_swap_input + " for " + user_input + "!")
                        View.show_message("")
                    else:
                        player_state['equipped'].append(item_swap_input)
                        #View.show_message(str(player_state['equipped']))
                        model.game.SetPlayerState(player_state)
                case "N":
                    View.show_message("You kept your " + item_swap_input + "...")
                case default:
                    View.show_message("Error! Input not recognized. Cancelling swap...")
                    View.show_message("")
    else:
        View.show_message("Error! Item not in chest!")
        
               
def handleLootInput(user_input, chest):
    user_input_split = user_input.split()
    operation = user_input_split[0]
    user_input_split.remove(operation)
    operation = operation.upper()
    item_choice = ' '.join(user_input_split)
    #View.debug_msg(item_choice)
    
    match operation:
        case 'TAKE':
            takeItems(item_choice, chest)
        case 'SWAP':
            swapItems(item_choice, chest)
        case default:
            View.show_message("error! input not recognized, try again?")
            View.show_message("")
            View.confirm()

def lootChest(chest):
    View.show_message("Welcome to the loot menu. Type the name of an item to transfer to your inventory,\nType 'all' to transfer all items,\nOr type 'Q' to stop looting.")
    
    items = chest.items
    
    in_loot_menu = True
    
    while(in_loot_menu):
        View.clear_screen()
        View.show_message(model.ui.looting_text)
        View.show_message("")
        View.show_message("Items in chest:")
        View.show_message("")
        
        for item in items:
            View.show_message_scroll(item)
            
        View.show_message("")
        
        user_input = View.get_input("")
        if user_input == "":
            View.show_message("Error! Input not recognized, try again!")
            View.confirm()
        elif(user_input.upper() == 'Q'):
            in_loot_menu = False
            model.game.SetChestState(chest.chest_id, chest.chest_state)
            View.clear_screen()
            View.show_message("You finish looting and close the heavy lid to the chest.")
            View.show_message("")
            break
        else:
            View.clear_screen()
            handleLootInput(user_input, chest)
            View.confirm()
            

def FindChest(x, y):
    #View.debug_msg("You find some loot.")
    chest = model.Chest(x, y)
    lootChest(chest)