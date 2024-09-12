__version__ = "0.0.1a"

# model should basically be ALL data

# game data
from GameData.Game import *
import LevelData.Level
from LevelData.LevelManager import *
import GameData.GameDefaults
from GameLoop.GameLoop import *
from GameLoop.InputHandler import *

# actions
from Actions.Help import *
from Actions.Move import *
from Actions.Inventory import *
from Actions.Map import *
from Actions.Combat import *
from Actions.Looting import *

#dialogue
from Dialogue.Narrator import *
import Dialogue.CustomAscii as ca
import Dialogue.RandomSplash as rs
import Dialogue.HelpText as ht
import Dialogue.UIElements as ui

#entities
from Entities.Player import *
from Entities.Chest import *
from Entities.Enemy import *

#external
import random
import os
import json

game = Game()
item_file = 'Items\Items.json'
enemy_file = 'Entities\EnemyTypes.json'