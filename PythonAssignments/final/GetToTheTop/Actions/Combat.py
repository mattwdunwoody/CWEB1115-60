import model
from view import View

class Battle():
    def __init__(self, player_state, enemy_state):
        self.player_turn = False
        self.npc_turn = False
        self.in_combat = False
        self.player_state = player_state
        self.enemy_state = enemy_state
        self.player_stumble = False
        self.enemy_stumble = False
        self.initial_turn = True

def StartCombat(enemy):
    #View.debug_msg("Starting combat!")
    #View.debug_msg("Enemy type: " + str(enemy.type))
    #View.debug_msg("Enemy stats: " + str(enemy.stats))
    
    player_state = model.game.GetPlayerState()
    enemy_state = enemy.enemy_state
    
    battle = Battle(player_state, enemy_state)
    
    View.clear_screen()
    model.OpenMap()
    DisplayCombatInfo(battle)
    View.show_message("")
    
    player_stats = model.GetPlayerEffectiveness()

    player_agility = player_stats[2]
    enemy_agility = enemy.stats['agility']
    
    while(player_agility < 1):
        enemy_agility += 1
        player_agility += 1
        
    while(enemy_agility < 1):
        player_agility += 1
        enemy_agility += 1
    
    # picks who goes first weighted towards the agilty stat for both the player and the enemy
    first_turn = model.random.choices(population=[0, 1], weights=[player_agility, enemy_agility], k=1)
    #View.debug_msg("first_turn: " + str(first_turn))
    
    match first_turn[0]:
        case 0:
            View.show_message_scroll_horizontally_fast("You catch an enemy by surprise!")
            View.show_message_scroll_horizontally_fast("")
            View.confirm()
            playerTurn(battle)
        case 1:
            View.show_message("You are ambushed by an enemy!")
            View.show_message("")
            View.confirm()
            enemyTurn(battle)

def DisplayCombatInfo(battle):
    player_name = model.game.GetPlayerState()['name']
    player_stats = model.GetPlayerEffectiveness()
    enemy_stats = battle.enemy_state['stats']
    
    player_health = battle.player_state['health']
    if len(str(player_health)) < 2:
        player_health = " " + str(player_health)
        
    enemy_health = battle.enemy_state['health']
    if len(str(enemy_health)) < 2:
        enemy_health = " " + str(enemy_health)
    
    player_damage_operator = '+'
    player_defense_operator = '+'
    player_agility_operator = '+'
    enemy_damage_operator = '+'
    enemy_defense_operator = '+'
    enemy_agility_operator = '+'
    
    if (player_stats[0] < 0):
        player_damage_operator = ''
        
    if (player_stats[1] < 0):
        player_defense_operator = ''
        
    if (player_stats[2] < 0):
        player_agility_operator = ''
        
    if (enemy_stats['damage'] < 0):
        enemy_damage_operator = ''
        
    if (enemy_stats['defense'] < 0):
        enemy_defense_operator = ''
        
    if (enemy_stats['agility'] < 0):
        enemy_agility_operator = ''

    View.show_message(player_name + " VS. Lvl. " + str(battle.enemy_state['level']) + " " + battle.enemy_state['type'].upper())
    View.show_message("===========================================")
    View.show_message("Health: " + str(player_health) + "       ||  Health: " + str(enemy_health))
    View.show_message("ATK:    " + str(player_damage_operator) + str(player_stats[0]) + "       ||  ATK:    " + str(enemy_damage_operator) + str(enemy_stats['damage']))
    View.show_message("DEF:    " + str(player_defense_operator) + str(player_stats[1]) + "       ||  DEF:    " + str(enemy_defense_operator) + str(enemy_stats['defense']))
    View.show_message("AGL:    " + str(player_agility_operator) + str(player_stats[2]) + "       ||  AGL:    " + str(enemy_agility_operator) + str(enemy_stats['agility']))


def FindEnemy(x, y):
    #View.show_message("You find an enemy!")
    enemy = model.Enemy(x, y)
    #View.show_message(str(enemy.stats))
    StartCombat(enemy)
    
def playerTurn(battle):
    
    if battle.player_stumble == True:
        battle.player_stumble = False
    
    View.clear_screen()
    model.OpenMap()
    
    battle.player_turn = True
    while battle.player_turn:
        DisplayCombatInfo(battle)
        View.show_message("")
        
        player_input = View.get_input("What do you want to do?\n\nAttack (A), use an Item (I), or Flee (F): ").upper()
        match player_input:
            case 'A':
                playerAttack(battle)
            case 'I':
                playerItem(battle)
            case 'F':
                playerFlee(battle)
            case _:
                View.show_message("")
                View.show_message("Input not recognized, check spelling?")
                View.show_message("")
                View.confirm()
                View.clear_screen()

def enemyTurn(battle):
        
    View.clear_screen()
    model.OpenMap()

    enemy_health = battle.enemy_state['health']
    
    if(enemy_health <= 0):
        combatReport(battle)
    
    battle.enemy_stumble == False
        
    enemy_agility = battle.enemy_state['stats']['agility'] + 10
    player_agility = model.GetPlayerEffectiveness()[2]
    if battle.player_stumble == True:
        player_agility -= 5
    
    while(player_agility < 1):
        enemy_agility += 1
        player_agility += 1

    while(enemy_agility < 1):
        player_agility += 1
        enemy_agility += 1
    
    hit = model.random.choices(population=[0, 1], weights=[enemy_agility, player_agility], k=1)
    damage = 0
    
    match hit[0]:
        case 0:
            damage = _hitPlayer(battle)
            battle.player_state['health'] -= damage
            DisplayCombatInfo(battle)
            View.show_message("")
            if damage == 0:
                View.show_message_scroll_horizontally_fast("The " + str(battle.enemy_state['type']).upper() + " tries to hit you but it is ineffective against your armor!")
                battle.enemy_stumble = True
            else:
                View.show_message_scroll_horizontally_fast(str(battle.enemy_state['type']).upper() + " strikes you and and deals " + str(damage) + " damage!")
        case 1:
            DisplayCombatInfo(battle)
            View.show_message("")
            _missPlayer(battle)
            battle.enemy_stumble = True
    
    View.show_message("")
    View.confirm()
    View.clear_screen()
    
    if battle.player_state['health'] <= 0:
        combatReport(battle)
    else:
        playerTurn(battle)
        
def _hitPlayer(battle):

    enemy_attack = battle.enemy_state['stats']['damage']
    player_defense = model.GetPlayerEffectiveness()[1]

    if enemy_attack > player_defense:
        damage = model.random.randint(1, enemy_attack)           
    elif enemy_attack <= player_defense:
        damage = model.random.randint(0, enemy_attack)
            
    return damage
    
def _missPlayer(battle):
    View.show_message_scroll_horizontally_fast("The " + str(battle.enemy_state['type']).upper() + " tries to hit you but you dodge it! You see an opening to attack!")

def playerAttack(battle):
    
    View.clear_screen()
    model.OpenMap()

    # in the future, have the character be able to pick an equipped item or to use an ability/magic etc
    # buffs/debuffs also need to be put in
    
    player_agility = model.GetPlayerEffectiveness()[2] + 10
    enemy_agility = battle.enemy_state['stats']['agility']
    if battle.enemy_stumble == True:
        enemy_agility -= 5
    
    while(player_agility < 1):
        enemy_agility += 1
        player_agility += 1
        
    while(enemy_agility < 1):
        player_agility += 1
        enemy_agility += 1
    
    hit = model.random.choices(population=[0, 1], weights=[player_agility, enemy_agility], k=1)
    damage = 0
    
    match hit[0]:
        case 0:
            damage = _hitEnemy(battle)
            critical_hit = model.random.randint(0, 5)
            if critical_hit == 0 and damage != 0:
                damage *= 3
            battle.enemy_state['health'] -= damage
            DisplayCombatInfo(battle)
            View.show_message("")
            if damage == 0:
                View.show_message_scroll_horizontally_fast("Your weapon glances off of " + str(battle.enemy_state['type']).upper() + "'s armor!")
            else:
                if critical_hit == 0:
                    View.show_message("Critical hit! 3X damage!")
                View.show_message_scroll_horizontally_fast("You strike " + str(battle.enemy_state['type']).upper() + " and deal " + str(damage) + " damage!")
        case 1:
            DisplayCombatInfo(battle)
            View.show_message("")
            _missEnemy(battle)
            battle.player_stumble = True
            
    battle.player_turn = False
    
    View.show_message("")
    View.confirm()
    
    if battle.enemy_state['health'] <= 0:
        combatReport(battle)
    else:  
        enemyTurn(battle)
         
def _hitEnemy(battle):

    player_attack = model.GetPlayerEffectiveness()[0]
    enemy_defense = battle.enemy_state['stats']['defense']
    
    if battle.enemy_stumble == True:
        damage = player_attack       
    elif enemy_defense == 0:
        damage = player_attack
    elif player_attack > enemy_defense:
        damage = model.random.randint(player_attack-enemy_defense, player_attack)           
    elif player_attack <= enemy_defense:
        damage = model.random.randint(0, player_attack)          
            
    return damage
    
def _missEnemy(battle):
    View.show_message_scroll_horizontally_fast("You swing and " + str(battle.enemy_state['type']).upper() + " dodges! You stumble a bit, and the " + str(battle.enemy_state['type']).upper() + " attacks your opening!")
    
def playerFlee(battle):
    View.clear_screen()
    model.OpenMap()
    
    player_agility = model.GetPlayerEffectiveness()[2]
    enemy_agility = battle.enemy_state['stats']['agility']
    if battle.enemy_stumble == True:
        enemy_agility -= 5
    
    while(player_agility < 1):
        enemy_agility += 1
        player_agility += 1
        
    while(enemy_agility < 1):
        player_agility += 1
        enemy_agility += 1
        
    flee = model.random.choices(population=[0, 1], weights=[enemy_agility, player_agility], k=1)
    
    DisplayCombatInfo(battle)
    View.show_message("")

    match flee[0]:
        case 0:
            View.show_message("You attempt to run away from the " + str(battle.enemy_state['type']).upper() + " but they attack you while your back is turned!")
            battle.player_stumble = True
        case 1:
            View.show_message("You were able to escape from the " + str(battle.enemy_state['type']).upper() + "!")
        
    battle.player_turn = False
    
    View.show_message("")
    View.confirm()
    
    if battle.player_stumble == True:
        enemyTurn(battle)
    else:  
        combatReport(battle)
        
def playerItem(battle):
    View.clear_screen()
    model.OpenMap()
    DisplayCombatInfo(battle)
    View.show_message("")
    View.show_message("Sorry, this feature has not been implemented yet.")
    View.show_message("")
    View.confirm()
    
    playerTurn(battle)
      
def combatReport(battle):
    #View.debug_msg("someone died")
    if battle.player_state['health'] <= 0:
        View.show_message_game_over(model.ca.game_over)
        View.show_message("")
        View.show_message_scroll_horizontally("You were slain by " + str(battle.enemy_state['type']).upper() + "...")
        View.show_message("")
        View.dramatic_pause()
        View.show_message_scroll_horizontally("Type 'load' at main menu to start a new game using your current character.")
        View.show_message("")
        battle.player_state['deaths'] += 1
        model.game.SetPlayerState(battle.player_state)
        model.game.GameOver()
    elif battle.enemy_state['health'] <= 0:
        View.clear_screen()
        model.OpenMap()
        DisplayCombatInfo(battle)
        View.show_message("")
        View.show_message_scroll_horizontally_fast("You defeated the " + str(battle.enemy_state['type']).upper() + "!")
        View.show_message("")
        
        model.EnemyKilledOnMap()
        
        battle.player_state['kills'] += 1
        model.game.SetPlayerState(battle.player_state)
        
    else:
        View.clear_screen()
        model.OpenMap()
        View.show_message("")
        View.show_message("You ran away!")
        View.show_message("")
        
        model.game.SetPlayerState(battle.player_state)