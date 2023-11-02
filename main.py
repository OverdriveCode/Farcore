import os
import pickle
from json import loads
from items import items_all, weapons_all, shield_all, staffs_all, enemies_all

with open("secrets.pickle", 'rb') as file:
    skey = pickle.load(file)


def encode_string(string, key):
    encoded = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                encoded += chr((ord(char) - 97 + key) % 26 + 97)
            else:
                encoded += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            encoded += char
    return encoded
    
def decode_string(string, key):
    decoded = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                decoded += chr((ord(char) - 97 - key) % 26 + 97)
            else:
                decoded += chr((ord(char) - 65 - key) % 26 + 65)
        else:
            decoded += char
    return decoded


if True:
    from os import system, name
    import random
    import time
    import calendar
    from time import sleep
    import pickle
    import sys
    import math

    pycharm = False

    try:
        from replit import db
    except:
        pycharm = True

    bold = '\x1b[1m'
    normal = '\x1b[0m' + '\x1b[38;2;255;255;255m'
    italic = '\x1B[3m'

    gold = '\x1b[38;2;230;190;0m\x1b[1m'
    silver = '\x1b[38;2;221;221;221m\x1b[1m'
    copper = '\x1b[38;2;170;44;0m\x1b[1m'

    paleyellow = '\x1b[38;2;255;255;215m\x1b[1m'
    lime = '\x1b[38;2;00;255;00m\x1b[1m'
    turquoise = '\x1b[38;2;0;255;255m\x1b[1m'
    teal = '\x1b[38;2;0;170;170m\x1b[1m'

    yellow = '\x1b[38;2;255;255;0m\x1b[1m'
    green = '\x1b[38;2;00;160;00m\x1b[1m'
    blue = '\x1b[38;2;0;40;255m\x1b[1m'
    purple = '\x1b[38;2;130;0;250m\x1b[1m'
    brown = '\x1b[38;2;135;62;35m\x1b[1m'
    red = '\x1b[0;31m\x1b[1m'
    orange = '\x1b[38;2;255;90;0m\x1b[1m'

    darkgrey = '\x1b[38;2;100;100;100m\x1b[1m'
    grey = '\x1b[38;2;130;130;130m\x1b[1m'

    white = '\x1b[38;2;255;255;255m\x1b[1m'
    platinum = '\x1b[38;2;205;192;255m\x1b[1m'
    ironc = '\x1b[38;2;255;205;192m\x1b[1m'


    clrs_list = ['\x1b[38;2;230;190;0m\x1b[1m', '\x1b[38;2;221;221;221m\x1b[1m', '\x1b[38;2;170;44;0m\x1b[1m', '\x1b[38;2;255;255;215m\x1b[1m', '\x1b[38;2;00;255;00m\x1b[1m', '\x1b[38;2;0;255;255m\x1b[1m', '\x1b[38;2;0;170;170m\x1b[1m', '\x1b[38;2;255;255;0m\x1b[1m', '\x1b[38;2;00;160;00m\x1b[1m', '\x1b[38;2;0;40;255m\x1b[1m', '\x1b[38;2;130;0;250m\x1b[1m', '\x1b[38;2;135;62;35m\x1b[1m', '\x1b[0;31m\x1b[1m', '\x1b[38;2;255;90;0m\x1b[1m', '\x1b[38;2;100;100;100m\x1b[1m', '\x1b[38;2;130;130;130m\x1b[1m', '\x1b[38;2;205;192;255m\x1b[1m', '\x1b[38;2;255;205;192m\x1b[1m']

    location = 'village'

    items_all_copy = items_all.copy()

    weapons_all_copy = weapons_all.copy()

    shield_all_copy = shield_all.copy()

    spells_all = {
        "blurr mind": f"You shoot a {grey}dark cloud{white} at your {red}target's{white} head. This causes it to move {purple}sluggishly{white}.",
        "magic missile": f"You fire 3 {green}green missiles{white} at your {red}targets{white}. It makes a {yellow}sizzling{white} sound.",
        "shield of the magi": f"You wave your {teal}staff{white} in the {silver}air{white}. A {green}greenish{white} bubble surrounds you.",
        "firebolt": f"You hurl a giant {orange}fireball{white} at your {red}target{white}. Your {red}targe{white} lit on {red}fire{white}",
        "aura of weakening": f"You mutter an {purple}encantation{white} and a {darkgrey}dark cloud{white} surounds all the {red}enemies{white}.",
        "dagger swarm": f"A swarm of {darkgrey}daggers{white} {yellow}buzz{white} around your {red}target{white} slashing relenlessly",
        "poison nova": f"{green}Toxic{white} {copper}dust{white} burst out filling the {darkgrey}area{white}. Your {red}targets{white} turn a {lime}pale-green{white} and cry out.",
        "hyper heal": f"You {paleyellow}wave{white} your hand over all your {red}wounds{white} and they {blue}mend{white}.",
        "ice shards": f'You send {gold}thousands{white} of {turquoise}ice shards{white} flying at your {red}opponents{white}.',
        "shadow spear": f"You send a {darkgrey}shadowy spear{white} hurling at your {red}target{white}. It slams into your {orange}opponent{white} dealing {red}massive damage{white}",
        "dark chromatic orb": f"You shoot a {darkgrey}dark orb{white} at your {red}target{white}. You can feel your {red}targets{white} {blue}life force{white} being drained into yours..",
        "dark arrows": f"You fire a volley of {darkgrey}dark arrows{white} at your {red}targets{white}. The {purple}crackeling{white} of {red}dark energy{white} fills the air.",
        "tornado burst": f"You hurl a {darkgrey}wirling tornado{white} full of deadly {red}projecticles{white} at you {orange}target{white}. Sending your {orange}target{white} into a frenzy",
    }

    chatGPT = {
        "wooden sword": "The Wooden Sword, a humble weapon forged from sturdy timber, may lack the elegance of steel but compensates with its unwavering reliability in the hands of a nimble warrior, delivering swift and precise strikes with surprising power.",
        "bronze sword": "The Bronze Sword, a modest yet dependable weapon cast from durable alloy, possesses a rustic charm that belies its effectiveness in close combat. Though lacking the luster of higher-tiered blades, it compensates with its reliability and affordability, making it an ideal choice for novice warriors or those seeking a practical weapon on a limited budget.",
        "iron sword": "The Iron Sword, a classic and reliable weapon forged from sturdy iron, showcases a perfect balance of strength and versatility. Its razor-sharp edge cleaves through enemies with ease, while its durability ensures it remains a steadfast companion throughout countless battles, making it a staple choice for warriors seeking a reliable blade to wield.",
        "steel sword": "The Steel Sword, a formidable weapon crafted by skilled blacksmiths, gleams with a deadly edge that effortlessly cleaves through armor and adversaries alike, instilling fear in the hearts of those who dare to face its wielder. Its balanced weight and exceptional durability make it the trusted choice of warriors seeking both elegance and efficiency on the battlefield.",
        "health potion": "The Health Potion, a shimmering vial brimming with revitalizing energy, instantly restores the vitality of the imbiber, mending wounds and rejuvenating the weary. A true lifeline in dire situations, it grants adventurers a moment of respite, allowing them to face their trials with renewed vigor and resilience.",
        "ember potion": "The Ember Potion, a flickering concoction infused with the essence of fire, bestows upon the drinker an inner flame that ignites their abilities, enhancing their offensive prowess and engulfing their strikes with scorching power. Imbued with the elemental forces of heat and fury, it grants adventurers the means to leave a trail of smoldering destruction in their wake.",
        "magi potion": "The Magi Potion, a shimmering elixir swirling with arcane energies, empowers the imbiber with heightened magical aptitude, unleashing a surge of mystic potential and amplifying their spellcasting abilities. Sought after by spellcasters and enchanters, it grants a temporary but formidable boost to their magical prowess, allowing them to weave intricate spells and bend reality to their will.",
        "potion of knowledge": "The Potion of Knowledge, a swirling elixir infused with ancient wisdom, bestows upon the drinker profound insights and heightened intellect, unlocking hidden knowledge and granting a temporary boost to their mental faculties. A coveted elixir among scholars and sages, it opens the doors of understanding and grants adventurers access to arcane secrets that lie beyond the realm of ordinary comprehension.",
        "citrine staff": "The Citrine Staff, a mesmerizing arcane artifact adorned with a captivating citrine gem, crackles with electrifying power, harnessing the raw energy of lightning to devastating effect. With each spellcast, it unleashes bolts of thunderous electricity, arcing through the air and electrifying enemies, leaving a trail of electrified chaos in its wake.",
        "ruby staff": "The Ruby Staff, an enchanting staff adorned with a brilliant crimson ruby at its apex, pulsates with intense elemental fire energy, capable of unleashing devastating pyromantic spells that scorch foes and leave trails of molten destruction in its wake. A symbol of raw power and ferocity, it grants its wielder mastery over flames, making them a force to be reckoned with on the battlefield.",
        "sapphire staff": "The Sapphire Staff, a graceful staff adorned with a mesmerizing sapphire gem, harnesses the untamed power of water, empowering its wielder to command surges, torrents, and healing mists. With a mere wave, it unleashes the fluid forces of the elemental realm, drenching enemies, soothing wounds, and flowing through the battlefield with an unwavering strength and fluidity.",
        "quartz staff": "The Quartz Staff, an ethereal arcane instrument adorned with a mesmerizing quartz crystal, harnesses the boundless power of wind, imbuing its wielder with mastery over gusts, gales, and the ethereal currents of air. With each invocation, it conjures swirling vortexes, unleashing tempests and cutting winds that can topple adversaries and manipulate the very fabric of the atmosphere, making it an essential tool for those who seek control over the unseen forces of the sky.",
        "troll heart": "The Troll Heart, a pulsating organ harvested from a slain troll, radiates an eerie aura of primal power, offering the bearer enhanced regeneration and resilience, while also serving as a macabre trophy that strikes fear into the hearts of enemies who witness its gruesome presence. Caution is advised, as its possession may draw the attention of other dark creatures, lured by the dark energies contained within.",
        "crossbow": "The Crossbow, a formidable ranged weapon crafted with precision, offers deadly accuracy and piercing power from a safe distance. Its sturdy frame and intricate mechanisms allow for quick reloads, enabling skilled marksmen to strike down foes swiftly and efficiently.",
        "gold trophy": "The Gold Trophy, an exquisite symbol of victory, shimmers with a radiant glow, signifying triumph over formidable challenges and relentless perseverance. Displayed proudly, it not only showcases the prowess of its owner but also grants them a boost in reputation and admiration from fellow adventurers."
    }
    

    inv = []

    health = 15
    max_health = 15

    crystals = 0

    weapon = 'none'
    offhand = 'none'

    dexterity = 3
    strength = 3

    gp = 0

    special_moves = ["dodge", 'heal wounds']
    shield_moves = ["shield bash", 'block']
    offhand_moves = ["attack", "fast attack"]
    effects = {}

    title = True

    known_spells = ["firebolt", "magic missile", "shield of the magi"]
    current_spells = known_spells.copy()

    triggers = []
    quests = {}
    time_triggers = {}

    enemies_killed = {}

    effects_length = {
        "poison": 4,
        "burn": 1,
        "dragon burn": 2,
        "bleed": 2,
        "hyper bleed": 5,
        "drain": 2,
        "freeze": 2,
        "hyper freeze": 3,
        "shock": 4,
        "life steal": 3,
        "force drain": 2,
        "rust": 5,
        "crunch": 1,
        "confusion": 2,
        "lightning": 2,
        "echo blast": 2,
        "silence waves": 3,
        'dirtify': 2,
        "acid": 3,
    }

    effects_stack = {
        "poison": 3,
        "burn": 2,
        "dragon burn": 1,
        "bleed": 3,
        "hyper bleed": 10,
        "drain": 2,
        "freeze": 2,
        "shock": 1,
        "life steal": 5,
        "force drain": 3,
        "rust": 1,
        "crunch": 2,
        "confusion": 2,
        "hyper freeze": 1,
        "lightning": 1,
        "echo blast": 5,
        "silence waves": 3,
        "dirtify": 3,
        "acid": 2
    }

    areas_to_names = {
        "lockwood": "lockwood",
        "lost plains": "orc layer",
        "scarred plains": "troll & goblin encamp",
        "the forge": "the forge",
        "low grass": "merchant",
        "snowy mountain": "snowy mountain",
        "blessed lake": "shrine",
        "cursed shores": "bandit hideout",
        "jade forest": "magic forest",
        "blue shores": "merchant 2",
        "darkwood": "dragon worshipers",
        "dragon cave": "dragon cave",
    }
    areas_to_fr = {
        "white bridge": "white bridge",
        "sunken graveyard": "sunken graveyard",
        "frosted cave": "frosted cave",
        "goliaths burrow": "goliaths burrow",
        "core-sail arena": "core-sail arena",
        "dead lake": "dead lake",
        "monk cliffs": "monk cliffs"
    }

    lvl = 1
    exp = 0
    exp_max = 100
    fighter_class = ""

    location = "lockwood"

    settings = {
        "print out des": True,
        "surroundings": True,
        "minimap": True,
        "auto saving": True,
        "color": "normal"
    }

    durability_weapon = {

    }

    testing = False

    multimove = ["the stranger", "orc warlord", "bandit", "yeti", "bandit lord", "jade guardian", "jade knight", "drowned monstrosity", "the dreadwood", "forest horror", "lich", "gelatinous cube", "the dark dragon", "death knight", "necromancer", "guardian of the jungle", "spike gang leader", "frost giant", 'assasin', "merrow", "monk lvl [1]", "monk lvl [2]", "monk lvl [3]", "monk lvl [4]", "muck the mutant", "zanders the pirate", "the rock giant", "blade of the north", "other worlder"]
    bosses = ["the stranger", "orc warlord", "yeti", "bandit lord", "jade guardian", "the dreadwood", "the dark dragon", "necromancer", "guardian of the jungle"]
    enemies_weapon_weakness = {
        "fungi monster": ["rusty sword", 10],
        "rust monster": ["wooden sword", 5]
    }
    enemies_shield_weakness = {
        "rust monster": "wooden shield"
    }

    cursed_weapons = {
        "cursed axe": 4,
        "cursed dagger": 1,
        "cursed bow": 6,
        "explosive bow": 20,
        "jade harpoon": 3,
    }
    blessed_weapons = {
        "magic sword": 2,
        "heart sword": 2
    }
    strength_weapons = {
        "flameblade": 1,
    }
    dexterity_weapons = {
        "kobold scimitar": 1
    }
    exp_weapons = {
        "jungle blade": 0.5
    }
    health_weapons = {
        "heart sword": 8
    }
    luck_weapons = {
        "sword of looting": 5
    }
    steal_weapons = {
        "dagger of stealing": 3
    }
    double_bladed_weapons = ["double bladed sword"]
    defense_weapons = {
        "cross-saber": 5
    }
    offhand_weapons = [
        "feather dagger",
        "light shortsword",
        "dual blade [offhand]"
    ]

    weapons_reload = {}
    world = "farcore"

    if True:

        new_enemies_all = {}

        for x in enemies_all:
            z = enemies_all[x]
            z['drop']["copper trophy"] = max(50 - int(z['exp']/10), 2)
            new_enemies_all[x] = z

        enemies_all = new_enemies_all

        new_enemies_all = {}

        for x in enemies_all:
            z = enemies_all[x]
            z['drop']["bronze trophy"] = max(100 - int(z['exp']/10), 2)
            new_enemies_all[x] = z

        enemies_all = new_enemies_all

        new_enemies_all = {}

        for x in enemies_all:
            z = enemies_all[x]
            z['drop']["silver trophy"] = max(200 - int(z['exp']/10), 2)
            new_enemies_all[x] = z

        enemies_all = new_enemies_all

        new_enemies_all = {}

        for x in enemies_all:
            z = enemies_all[x]
            z['drop']["gold trophy"] = max(500 - int(z['exp']/10), 2)
            new_enemies_all[x] = z

        enemies_all = new_enemies_all

        new_enemies_all = {}

        for x in enemies_all:
            z = enemies_all[x]
            z['drop']["overdrive\'s trophy"] = max(1000 - int(z['exp']/10), 2)
            new_enemies_all[x] = z

        enemies_all = new_enemies_all


        secret_file = open("secrets.txt", "r")
        ss = list(secret_file.readlines())


    def save():
        global pycharm, gp
        if pycharm is False:
            global db

        x = (inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects,
                known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class,
                location, settings, durability_weapon, items_all, weapons_all, shield_all, crystals, offhand_moves, strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons, world)

        f = open("save.txt", "w")

        for i in x:
            f.write(str(i))
            f.write("\n")

        if pycharm is False:
            db['save'] = x
        else:
            with open("save.pickle", 'wb') as file:
                pickle.dump(x, file)


    def load_data():
        global inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects, known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class, location, settings, durability_weapon, items_all, weapons_all, shield_all, crystals, offhand_moves, strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons, world
        global pycharm

        if pycharm is False:
            global db

            dbsave = loads(db.get_raw("save"))

            new_items = {}
            for x in dbsave[23]:
                if x not in items_all:
                    new_items[x] = dbsave[23][x]

            dbsave[23] = items_all
            for x in new_items:
                dbsave[23][x] = new_items[x]

            new_items = {}
            for x in dbsave[24]:
                if x not in weapons_all:
                    new_items[x] = dbsave[24][x]

            dbsave[24] = weapons_all
            for x in new_items:
                dbsave[24][x] = new_items[x]

            new_items = {}
            for x in dbsave[25]:
                if x not in shield_all:
                    new_items[x] = dbsave[25][x]

            dbsave[25] = shield_all
            for x in new_items:
                dbsave[25][x] = new_items[x]

            

        else:
            with open("save.pickle", 'rb') as file:
                load = list(pickle.load(file))


            new_items = {}
            for x in load[23]:
                if x not in items_all:
                    new_items[x] = load[23][x]

            load[23] = items_all.copy()
            for x in new_items:
                load[23][x] = new_items[x]

            new_items = {}
            for x in load[24]:
                if x not in weapons_all:
                    new_items[x] = load[24][x]

            load[24] = weapons_all.copy()
            for x in new_items:
                load[24][x] = new_items[x]

            new_items = {}
            for x in load[25]:
                if x not in shield_all:
                    new_items[x] = load[25][x]

            load[25] = shield_all.copy()
            for x in new_items:
                load[25][x] = new_items[x]

        if pycharm is False:
            while len((inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves,
                        effects,
                        known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max,
                        fighter_class,
                        location, settings, durability_weapon, items_all, weapons_all, shield_all, crystals, offhand_moves, strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons, world)) > len(db['save']):
                z = [inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves,
                        effects,
                        known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max,
                        fighter_class,
                        location, settings, durability_weapon, items_all, weapons_all, shield_all, crystals, offhand_moves, strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons, world]
                y = list(dbsave)
                y.append(z[len(y)])
                db['save'] = y
                dbsave = loads(db.get_raw("save"))

            (inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects,
                known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class,
                location, settings, durability_weapon, items_all, weapons_all, shield_all, crystals, offhand_moves, strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons, world) = dbsave
        else:
            while len((inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves,
                        effects,
                        known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max,
                        fighter_class,
                        location, settings, durability_weapon, items_all, weapons_all, shield_all, crystals, offhand_moves, strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons, world)) > len(load):
                z = [inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves,
                        effects,
                        known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max,
                        fighter_class,
                        location, settings, durability_weapon, items_all, weapons_all, shield_all, crystals, offhand_moves, strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons, world]
                y = list(load)
                y.append(z[len(y)])
                load = y

            (inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects,
                known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class,
                location, settings, durability_weapon, items_all, weapons_all, shield_all, crystals, offhand_moves, strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons, world) = load

        #print((inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects, known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class, location, settings, durability_weapon, items_all, weapons_all, shield_all))
        #input("YES")


    def scrollTxt(text="", spd=0.05, flush=False, end="\n"):
        global settings, clrs_list
        
        clr_code = {
                        "green": '\x1b[38;2;00;160;00m\x1b[1m',
                        "blue": '\x1b[38;2;0;40;255m\x1b[1m',
                        "purple": '\x1b[38;2;130;0;250m\x1b[1m',
                        "red": '\x1b[0;31m\x1b[1m',
                        "orange": '\x1b[38;2;255;90;0m\x1b[1m',
                        "black": '\x1b[38;2;100;100;100m\x1b[1m',
                        
        }
        
        flush2 = flush
        end2 = end
        if settings["color"] != "normal":
            for x in clrs_list:
                text = text.replace(x, clr_code[settings["color"]])
        print(text, flush=flush2, end=end2)


    def lis(string):
        a = []
        for char in string:
            a.append(char)
        return a


    def crollTxt(text="", fvar=3):
        colors = [turquoise, silver, blue, purple, teal, darkgrey, grey, platinum]
        text = text.split()
        nwords = ["a", "the", 'it', 'of', 'are', 'and']

        color = {
            "light": teal,
            "green": green,
            "gold": gold,
            "GP": gold,
            "silver": silver,
            'clear': silver,
            "black": darkgrey,
            "metal": grey,
            "iron": grey,
            "steel": darkgrey,
            "dark": darkgrey,
            "blue": blue,
            "orange": orange,
            "yellow": yellow,
            "purple": purple,
            "red": red,
            "brown": brown,
            "enemy": copper,
            "enemies": copper,
            "loot": gold,
            "sword": silver,
            "weapon": darkgrey,
            "shield": copper,
            "wood": brown,
            "fire": red,
            "damage": orange,
            "kill": red,
            "attack": orange,
            "heal": red,
            "health": red,
            "exp": teal,
            "level": teal,
            "grass": green,
            "blood": red,
            "hill": green,
            "tree": green,
            "boulder": darkgrey,
            "charge": orange,
            "orc": lime,
            "orcs": lime,
            "war": red,
            "torch": brown,
            "firebolt": red,
            "goblin": copper,
            "troll": lime,
            "bonfire": red,
            "potion": silver,
            "ember": orange,
            "water": blue

        }

        new_color = {}

        for x in color:
            new_color[x] = color[x]
            new_color[x + "s"] = color[x]

        color = new_color

        z = 0
        for x in text:
            c = white

            if z == fvar:
                z = 0
                c = random.choice(colors)

            if (((x.lower()).replace(",", "")).replace(".", "")).replace("!", '') in color:
                c = color[(((x.lower()).replace(",", "")).replace(".", "")).replace("!", '')]
                z = 0

            if (((x.lower()).replace(",", "")).replace(".", "")).replace("!", '') in nwords:
                c = white

            print(c + x + " " + white, flush=True, end="")
            z += 1
        print()


    def get_input(commands, lower=True, special=False, invis_commands=[], g=False):
        if special == False:
            if lower is False:
                answer = input()
            else:
                answer = input().lower()

            if answer == "" or answer == " ":
                answer = "-=-=-="

            commands_new = {}
            lcommands = []
            checkCAP = False

            vis_commands = commands.copy()

            for x in invis_commands:
                commands.append(x)

            for x in commands:
                if len(lis(x)) > 1:
                    checkCAP = True

            if checkCAP:

                z = 1
                for i in commands:
                    commands_new[i] = i
                    lcommands.append(i)

                    if lis(i)[0] in lcommands:
                        zcommands = lcommands

                        zed = 0
                        thing_c = lis(i)[0]

                        while True:
                            if thing_c not in zcommands:
                                break
                            zed += 1
                            try:
                                thing_c = thing_c + lis(i)[zed]
                            except:
                                break

                        commands_new[thing_c] = i
                        lcommands.append(thing_c)
                    else:
                        commands_new[lis(i)[0]] = i
                        lcommands.append(lis(i)[0])

                    z += 1
            else:
                lcommands = commands
                for ixi in commands:
                    commands_new[ixi] = ixi

            while answer not in lcommands:
                scrollTxt(f'{red}Invalid{white} answer')
                if g is False:
                    scrollTxt(italic + "Valid Commands: " + str(vis_commands) + normal + '\x1b[1m' +
                                white)
                else:
                    scrollTxt(italic + "Valid Number: " + darkgrey + str(vis_commands[0]) + f"{white}-{darkgrey}" +
                                str(vis_commands[-1]) + normal + '\x1b[1m' +
                                white)
                if "single letter" not in triggers:
                    triggers.append("single letter")
                    scrollTxt(f"You may also just use a {turquoise}SINGLE LETTER{white} of the command")
                    scrollTxt(f'For exampe {red}"a"{white} for {red}apple{white}')
                if lower is False:
                    answer = input()
                else:
                    answer = input().lower()

            return commands_new[answer]
        else:
            selected = "error"


    def effects_add(effect_a, effect_l, effect_n):
        global effects
        if effect_a < 0:
            try:
                effects[effect_n] = [effect_a, effects[effect_n][1]]
            except:
                effects[effect_n] = [effect_a, effect_l]
        else:
            try:
                effects[effect_n] = [max(effects[effect_n][0], effect_a), effects[effect_n][1] + effect_l]
            except:
                effects[effect_n] = [effect_a, effect_l]


    def title3():
        if True:
                    clrs = ["normal", "green", "blue", "purple", "red", "orange", "black"]
                    zx = 0
                    gg = False
                    clr_code = {
                        "green": '\x1b[38;2;00;160;00m\x1b[1m',
                        "blue": '\x1b[38;2;0;40;255m\x1b[1m',
                        "purple": '\x1b[38;2;130;0;250m\x1b[1m',
                        "red": '\x1b[0;31m\x1b[1m',
                        "orange": '\x1b[38;2;255;90;0m\x1b[1m',
                        "black": '\x1b[38;2;100;100;100m\x1b[1m',
                    }

                    for x in clrs:
                        if x != settings["color"] and gg == False:
                            zx += 1
                        else:
                            gg = True

                    

                    try:
                        settings["color"] = clrs[zx]
                    except:
                        settings["color"] = "normal"

                    if settings["color"] != "normal":
                        color_a = clr_code[settings["color"]]
                        bold = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        normal = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        italic = '\x1B[3m'

                        gold = color_a
                        silver = color_a
                        copper = color_a

                        paleyellow = color_a
                        lime = color_a
                        turquoise = color_a
                        teal = color_a

                        yellow = color_a
                        green = color_a
                        blue = color_a
                        purple = color_a
                        brown = color_a
                        red = color_a
                        orange = color_a

                        darkgrey = color_a
                        grey = color_a

                        white = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        platinum = color_a
                        ironc = color_a
                    else:
                        bold = '\x1b[1m'
                        normal = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        italic = '\x1B[3m'

                        gold = '\x1b[38;2;230;190;0m\x1b[1m'
                        silver = '\x1b[38;2;221;221;221m\x1b[1m'
                        copper = '\x1b[38;2;170;44;0m\x1b[1m'

                        paleyellow = '\x1b[38;2;255;255;215m\x1b[1m'
                        lime = '\x1b[38;2;00;255;00m\x1b[1m'
                        turquoise = '\x1b[38;2;0;255;255m\x1b[1m'
                        teal = '\x1b[38;2;0;170;170m\x1b[1m'

                        yellow = '\x1b[38;2;255;255;0m\x1b[1m'
                        green = '\x1b[38;2;00;160;00m\x1b[1m'
                        blue = '\x1b[38;2;0;40;255m\x1b[1m'
                        purple = '\x1b[38;2;130;0;250m\x1b[1m'
                        brown = '\x1b[38;2;135;62;35m\x1b[1m'
                        red = '\x1b[0;31m\x1b[1m'
                        orange = '\x1b[38;2;255;90;0m\x1b[1m'

                        darkgrey = '\x1b[38;2;100;100;100m\x1b[1m'
                        grey = '\x1b[38;2;130;130;130m\x1b[1m'

                        white = '\x1b[38;2;255;255;255m\x1b[1m'
                        platinum = '\x1b[38;2;205;192;255m\x1b[1m'
                        ironc = '\x1b[38;2;255;205;192m\x1b[1m'
        print(f"""{white}
{turquoise}___________                                         
{turquoise}\_   _____/____ {teal}_______   ____{blue}  ___________   ____  
{turquoise} |    __) \__  \\{teal}\\_  __ \\_/ ___\\{blue}/  _ \\_  __ \\_/ __ \\ 
{turquoise} |    |   / __ \\{teal}|  | \\/ \\  \\__{blue}(  <_> )  | \\/\\  ___/ 
{turquoise} \\___/   (____  /{teal}__|     \\___  >{blue}____/|__|    \\___ >
{turquoise}             \\/{teal}            \\/{blue}                  \\/ 
                {white}    - An RPG game -
""")


    def clear(title1=True):
        scrollTxt(white)
        if name == 'nt':
            _ = system('cls')


        else:
            _ = system('clear')

        if title1:
            title3()


    def enter():
        scrollTxt(f'[{turquoise}Enter{white}] to continue')
        input()


    def die():
        global enemies_killed, enemies_all, db, inv, durability_weapon

        if pycharm is False: db["save"] = 'SAVE HAS BEEN DELETED'
        else:
            with open("save.pickle", 'wb') as file:
                pickle.dump("SAVE HAS BEEN DELETED", file)

        scrollTxt(f"You have been {red}slain{white}...")
        print()

        print("_______________________________________")
        print("|                                      |")
        scrollTxt(f"| Here {grey}lies{white} an {blue}Unamed Hero{white}...          |")

        f = "nothing [XD]"
        ff = f
        f7 = 0

        pre = [0, "goblin"]

        for x in enemies_killed:
            f7 += enemies_killed[x] * enemies_all[x]['exp']
            if (enemies_killed[x] * enemies_all[x]['exp']) > pre[0]:
                pre = [(enemies_killed[x] * enemies_all[x]['exp']), x]

        if pre != [0, "goblin"]:
            if pre[0] > 1:
                f = f"{grey}{int(pre[0] / enemies_all[pre[1]]['exp'])} {copper}{pre[1]}s{white}"
                ff = f"{int(pre[0] / enemies_all[pre[1]]['exp'])} {pre[1]}s"
            else:
                f = f"{grey}{int(pre[0] / enemies_all[pre[1]]['exp'])} {copper}{pre[1]}{white}"
                ff = f"{int(pre[0] / enemies_all[pre[1]]['exp'])} {pre[1]}"

        eend = 15 - len(lis(ff))
        eeend = 39 - (len(lis(" final score: " + str(f7+ (len(triggers) * 2)))))

        end2 = ""
        end3 = ""

        for x3 in range(eend):
            end2 = end2 + " "
        for x3 in range(eeend-1):
            end3 = end3 + " "

        scrollTxt(f"| Best know for {red}killing{white} {f}{end2}|")
        scrollTxt(f"| Final Score: {yellow}{f7 + (len(triggers) * 2)}{white}{end3}|")
        print("|______________________________________|")
        enter()
        print()

        print()
        scrollTxt(f"You {blue}save{white} has been {red}deleted{white}, due to this game being {orange}HARDCORE{white}")
        scrollTxt(f"But you made save {teal}1{white} item for the next {darkgrey}run{white}")
        scrollTxt(f"What {purple}item{white} woud you like to {blue}save{white}?")
        answer = get_input(inv)
        print()

        db["saved item"] = answer
        if answer != items_all_copy:
            db["saved item items all"] = items_all[answer]
            if items_all[answer]["weapon"] is True:
                db["saved item weapons all"] = weapons_all[answer]
            if items_all[answer]["shield"] is True:
                db["saved item shield all"] = shield_all[answer]

        real_durability_weapon = {}
        for x in durability_weapon:
            if x == answer:
                real_durability_weapon[x] = durability_weapon[x]
        durability_weapon = real_durability_weapon
            
        db["all weapons stuff"] = (strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons, durability_weapon)
        scrollTxt(f"Item {turquoise}saved{white}!")
        scrollTxt(f"{blue}Save{white} {red}deleted{white}!")
        exit()


    def inventory():
        global offhand_weapons, world, inv, health, weapon, offhand, effects, current_spells, exp, exp_max, strength, lvl, dexterity, max_health, gp, crystals, shield_all, weapons_all, items_all, fighter_class, location, pre_loc, strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons, durability_weapon

        clear()

        scrollTxt(f'{purple}Inventory{white}')
        scrollTxt()
        scrollTxt(f"Health: {red}{health}{white}/{red}{max_health}{white} ❤️")
        print()
        scrollTxt(f'Equiped {grey}Weapon{white}: {blue}{weapon}{white}')
        scrollTxt(f'Equiped {grey}Offhand{white}: {blue}{offhand}{white}')
        scrollTxt()


        imap = {}
        x = 1
        new_t = []
        for i in inv:
            if i not in new_t:
                new_t.append(i)
                nn = 0
                for w in inv:
                    if w == i:
                        nn += 1
                scrollTxt(f'[{red}{x}{white}|', end="", flush=True)
                crollTxt(f" {i} x{nn}", fvar = 0)

                imap[x] = i
                x += 1
                

        scrollTxt()
        scrollTxt(f'[{red}l{white}] to leave')
        scrollTxt()

        commands = ['l']
        for y in range(x):
            if y != 0:
                commands.append(str(y))

        answer = get_input(commands, True)

        if answer != 'l':

            item = imap[int(answer)]
            item_stats = items_all[item]
            print()

            print(blue + item + white)
            scrollTxt(bold + italic + '\x1b[1m' + item_stats['description'] + normal + '\x1b[1m')
            if item_stats["weapon"] is True or item == "healing stone":
                if item in durability_weapon:
                    try:
                        l = weapons_all[item]["durability"]
                    except:
                        l = 20
                    m = durability_weapon[item] 
                    scrollTxt(f"Durability: {darkgrey}{m}{white} / {darkgrey}{l}{white}")
                else:
                    try:
                        asdx = weapons_all[item]["durability"]
                    except:
                        asdx = 20
                    scrollTxt(f"Durability: {gold}{asdx}{white}/{gold}{asdx}{white}")

            scrollTxt()

            commands = ["sell", "exit"]

            scrollTxt('What would you like to do')
            scrollTxt(f"|{gold}Sell{white}| |{orange}Exit{white}|", end="", flush=True)

            if item_stats['consumable'] is True:
                scrollTxt(f' |{purple}Use{white}|', end='', flush=True)

                commands.append('use')

            if item_stats['weapon'] is True or item_stats['shield'] is True:
                scrollTxt(f' |{copper}Equip{white}|', end='', flush=True)

                commands.append('equip')

            if item_stats["weapon"] is True:
                commands.append("scrap")
                scrollTxt(f' |{red}Scr{darkgrey}ap{white}|', end='', flush=True)

            if item == offhand or item == weapon:
                scrollTxt(f' |{teal}Unequip{white}|', end='', flush=True)

                commands.append('unequip')

            if item_stats["fuse"] is True:
                scrollTxt(f' |{green}Infuse{white}|', end='', flush=True)

                commands.append("infuse")

            if item in chatGPT:
                scrollTxt(f' |{turquoise}ChatGPT Des{white}|', end='', flush=True)

                commands.append("chatgpt des")

            scrollTxt()

            answer = get_input(commands, True)
            scrollTxt()

            if answer == 'chatgpt des':
                cgd = chatGPT[item]
                crollTxt(f"{cgd}")

            elif answer == 'use':
                if item not in ["healing stone", "teleportation staff", "monster book", "reykrs book", "andrew dengs book", "nj wolfs book", "map", "guide", "shadow samurias book"]: inv.remove(item)

                if item == 'health potion':
                    if health > max_health:
                        max_healthS = health
                    else:
                        max_healthS = max_health
                    scrollTxt(
                        f'You pour the {yellow}sweet{white} {red}red necture{white} down your mouth. {teal}Relief{white} washes over you'
                    )
                    scrollTxt(f'You healed {red}{min(5 + lvl -1, 10)}{white} health')

                    health += min(5 + lvl -1, 10)

                    if health > max_healthS:
                        health = max_healthS

                if item == 'hardy bread':
                    scrollTxt(
                        f'You munch on the {brown}hardy bread{white}. Its {orange}warm{white} and {lime}savory{white}.'
                    )
                    scrollTxt(f'You healed {red}{5}{white} overflow health')
                    scrollTxt(f"{blue}~note; you can\'t go overflow more than 10~{white}")

                    health += 5
                    if health > max_health + 10:
                        health = max_health + 10

                if item == 'mammoth meat':
                    scrollTxt(
                        f'You gobble down the {red}mammoth meat{white}. Its very {yellow}strechy{white} but also very {darkgrey}filling{white}.'
                    )
                    scrollTxt(f'You healed {red}{5}{white} overflow health')
                    scrollTxt(f"{blue}~note; you can\'t go overflow more than 10~{white}")
                    print()
                    scrollTxt(f"+ {red}5{white} Damage | Last {gold}1{white} Battle")
                    effects_add(5, 1, "damage bonus")

                    health += 5
                    if health > max_health + 10:
                        health = max_health + 10
                
                if item == 'healing stone':
                    if health > max_health:
                        max_healthS = health
                    else:
                        max_healthS = max_health
                    scrollTxt(
                        f'You grasp the {red}red{ironc}pink{white} stone as you feel {red}life{white} flow through you.'
                    )
                    scrollTxt(f'You healed {red}{random.randint(min(1 + lvl -1, 10), min(10 + lvl -1, 20))}{white} health')

                    health += min(5 + lvl -1, 10)

                    if health > max_healthS:
                        health = max_healthS
                    try:
                        durability_weapon["healing stone"] -= 1
                        if durability_weapon["healing stone"] < 1:
                            scrollTxt(f"You {red}healing stone{white} shatters in to a million {darkgrey}pieces{white}")
                            inv.remove(
                                "healing stone"
                            )
                    except:
                        durability_weapon["healing stone"] = 19

                if item == 'hyper heal potion':
                    scrollTxt(
                        f'You pour the {yellow}sour{white} {ironc}pink necture{white} down your mouth. {teal}Relief{white} washes over you'
                    )
                    scrollTxt(f'{red}Health restored to max{white}')

                    health = max_health

                if item == 'magi potion':
                    scrollTxt(
                        f'You uncap the {silver}bottle{white}. The {turquoise}blue liquid{white} takes {paleyellow}sour{white}. Your eyes glow {purple}purple{white} as you feel the {blue}magic{white} wash over you.'
                    )
                    scrollTxt(f'You gained back all your {purple}spells{white}')

                    current_spells = known_spells.copy()

                if item == 'potion of knowledge':
                    scrollTxt(
                        f'You down the {grey}dark potion{white}. It taste {paleyellow}very bitter{white}. You feel {red}uneasy{white}. {purple}Memories{white} of you flash before your {blue}eyes{white}, but they arent your {purple}memories{white}.'
                    )
                    scrollTxt(f'+ {blue}30{white} EXP')

                    exp += 30

                    if exp >= exp_max:
                        scrollTxt("_____________________")
                        scrollTxt("|                   |")
                        scrollTxt(f"| You {blue}LEVELED UP!{white}   |")
                        scrollTxt(f"| + {red}5{white} Max HP        |")
                        scrollTxt(f"| + {turquoise}Level Crystal{white} 🔷|")
                        scrollTxt("|___________________|")

                        lvl += 1
                        crystals += 1
                        max_health += 5

                        exp -= exp_max
                        exp_max = int(exp_max * 1.5)
                        scrollTxt()

                if item == 'lightning cider':
                    scrollTxt(
                        f'You down the {yellow}lighting {gold}cider{white}. Your body {orange}crackles{white} with {paleyellow}energy{white}.'
                    )
                    if random.randint(1, 5) == 5:
                        print()
                        scrollTxt(f"{yellow}LIGHTNING{white} stikes you | - {red}7{white} health")
                        scrollTxt(f"A little known {red}risk{white} of the drink")
                        print()
                        health -= 7
                        if health < 1:
                            die()
                    scrollTxt(f'+ {blue}60{white} EXP')

                    exp += 60

                    if exp >= exp_max:
                        scrollTxt("_____________________")
                        scrollTxt("|                   |")
                        scrollTxt(f"| You {blue}LEVELED UP!{white}   |")
                        scrollTxt(f"| + {red}5{white} Max HP        |")
                        scrollTxt(f"| + {turquoise}Level Crystal{white} 🔷|")
                        scrollTxt("|___________________|")

                        lvl += 1
                        crystals += 1
                        max_health += 5

                        exp -= exp_max
                        exp_max = int(exp_max * 1.5)
                        scrollTxt()

                if item == 'frosted potion':
                    scrollTxt(
                        f"You slurp the {turquoise}ice{teal} blue liquid{white}. Your lips turn {blue}blue{white} as you start {platinum}shivering{white}.")
                    scrollTxt(f"+ {red}5{white} Damage | Lasts {blue}3{white} Battles")
                    scrollTxt(f"+ {green}5{white} Accuracy | Lasts {blue}3{white} Battles")

                    effects_add(5, 3, "damage bonus")
                    effects_add(5, 3, "hit bonus")

                if item == 'ember potion':
                    scrollTxt(
                        f"You gulp down the firey {orange}orange liquid{white}. Your throat {red}burns{white} and you cough out {grey}smoke{white} and {grey}ash{white}")
                    scrollTxt(f"+ {red}3{white} Damage | Lasts {blue}3{white} Battles")
                    scrollTxt(f"+ {green}3{white} Accuracy | Lasts {blue}3{white} Battles")

                    try:
                        effects['damage bonus'] = [effects['damage bonus'][0] + 3, effects['damage bonus'][0] + 3]
                    except:
                        effects['damage bonus'] = [3, 3]

                    try:
                        effects['hit bonus'] = [effects['hit bonus'][0] + 3, effects['damage bonus'][0] + 3]
                    except:
                        effects['hit bonus'] = [3, 3]

                if item == 'potion of rage':
                    scrollTxt(f"You pour the {gold}fizzy{white} {red}red liquid{white} down your throat. You feel immensely {orange}ANGRY{white} it would be {darkgrey}dangerous{white} for anyone to get in your way...")
                    scrollTxt(f"+ {red}10{white} Damage | Lasts {blue}2{white} Battles")
                    scrollTxt(f"- {yellow}2{white} Accuarcy{white} | Lasts {blue}2{white} Battles")
                    effects_add(10, 2, "damage bonus")
                    effects_add(-2, 2, "hit bonus")

                if item == 'tortoise potion':
                    scrollTxt(
                        f"You swallow the {darkgrey}iron grey liquid{white}. It tastse like {green}tortoise{white}?")
                    scrollTxt(f"+ {darkgrey}4{white} Defense | Lasts {blue}3{white} Battles")

                    effects_add(4, 3, "defense bonus")

                if item == "mushroom":
                    scrollTxt(f"You plug your nose and {brown}eat{white} the {copper}mushroom{white}")

                    nn = random.randint(1, 6)
                    if nn == 1:
                        scrollTxt(f"It taste {red}firey hot{white}, it's a {orange}powershroom{white}!")
                        scrollTxt(f"+ {green}2{white} Damage | Lasts {blue}1{white} Battles")
                        effects_add(2, 1, "damage bonus")
                    if nn == 2:
                        scrollTxt(f"It taste {blue}icy cold{white}, it's a {teal}weakenshroom{white}!")
                        scrollTxt(f"- {red}2{white} Damage | Lasts {blue}1{white} Battles")
                        effects_add(-2, 1, "damage bonus")
                    if nn == 3:
                        scrollTxt(f"It taste {green}sour{white}, it's a {lime}focushroom{white}!")
                        scrollTxt(f"+ {green}2{white} Accuracy | Lasts {blue}1{white} Battles")
                        effects_add(2, 1, "hit bonus")
                    if nn == 4:
                        scrollTxt(f"It taste {yellow}bitter{white}, it's a {paleyellow}hazeshroom{white}!")
                        scrollTxt(f"- {red}2{white} Accuracy | Lasts {blue}1{white} Battles")
                        effects_add(-2, 1, "hit bonus")
                    if nn == 5:
                        if health > max_health:
                            max_healthS = health
                        else:
                            max_healthS = max_health
                        scrollTxt(f"It taste {copper}sweet{white}, it's a {red}healshroom{white}!")
                        scrollTxt(f"+ {red}4{white} Health")
                        health += 4
                        if health > max_healthS: health = max_healthS
                    if nn == 6:
                        scrollTxt(f"It taste {grey}salty{white}, it's a {darkgrey}darkshroom{white}!")
                        scrollTxt(f"- {red}2{white} Health")
                        health -= 2

                        if health < 1:
                            scrollTxt(f"You {red}died{white}")
                            die()

                if item == "mushroom soup":
                    scrollTxt(f"You plug your nose and {brown}drink{white} the {copper}mushroom{white} {yellow}soup{white}")

                    nn = random.randint(1, 6)
                    if nn == 1:
                        scrollTxt(f"It taste {red}firey hot{white}, it's a {orange}powershroom soup{white}!")
                        scrollTxt(f"+ {green}3{white} Damage | Lasts {blue}2{white} Battles")
                        effects_add(3, 2, "damage bonus")
                    if nn == 2:
                        scrollTxt(f"It taste {blue}icy cold{white}, it's a {teal}weakenshroom soup{white}!")
                        scrollTxt(f"- {red}3{white} Damage | Lasts {blue}2{white} Battles")
                        effects_add(-3, 2, "damage bonus")
                    if nn == 3:
                        scrollTxt(f"It taste {green}sour{white}, it's a {lime}focushroom soup{white}!")
                        scrollTxt(f"+ {green}3{white} Accuracy | Lasts {blue}2{white} Battles")
                        effects_add(3, 2, "hit bonus")
                    if nn == 4:
                        scrollTxt(f"It taste {yellow}bitter{white}, it's a {paleyellow}hazeshroom soup{white}!")
                        scrollTxt(f"- {red}3{white} Accuracy | Lasts {blue}2{white} Battles")
                        effects_add(-3, 2, "hit bonus")
                    if nn == 5:
                        if health > max_health:
                            max_healthS = health
                        else:
                            max_healthS = max_health
                        scrollTxt(f"It taste {copper}sweet{white}, it's a {red}healshroom soup{white}!")
                        scrollTxt(f"+ {red}6{white} Health")
                        health += 6
                        if health > max_healthS: health = max_healthS
                    if nn == 6:
                        scrollTxt(f"It taste {grey}salty{white}, it's a {darkgrey}darkshroom soup{white}!")
                        scrollTxt(f"- {red}4{white} Health")
                        health -= 4

                        if health < 1:
                            scrollTxt(f"You {red}died{white}")
                            die()

                if item == 'flaming dragon drink':
                    scrollTxt(
                        f"You down the firey {orange}orange liquid{white}. You burp out {red}fire{white}. You feel intense {orange}heat{white} in your forehead.")
                    scrollTxt(f"+ {red}3{white} Damage | Lasts {blue}1{white} Battle")

                    try:
                        effects['damage bonus'] = [max(effects['damage bonus'][0], 3), effects['damage bonus'][1] + 1]
                    except:
                        effects['damage bonus'] = [3, 1]

                if item == 'frost mead':
                    scrollTxt(
                        f"You down the {turquoise}icey{white}. You {blue}shiver{white}. After a while you feel a {teal}cool calm{white} for battle.")
                    scrollTxt(f"+ {green}3{white} Accuracy | Lasts {blue}1{white} Battle")

                    try:
                        effects['hit bonus'] = [max(effects['hit bonus'][0], 3), effects['hit bonus'][1] + 1]
                    except:
                        effects['hit bonus'] = [3, 1]

                if item == "luck potion":
                    scrollTxt(f"You swallow the {gold}golden surup{white}, it taste very {yellow}sweet{white}. You feel extremely {orange}confident{white}")
                    scrollTxt(f"+ {gold}5{white} Luck | Lasts {blue}2{white} Battle")
                    effects_add(5, 2, "luck")

                if item == 'spiders bite drink':
                    scrollTxt(
                        f"You down down the {green}dark green liquid{white}. You feel {lime}nauseous{white}, you {green}throw-up{white}.")
                    scrollTxt(f"+ {red}2{white} Max health | Health is set to {red}1{white}.")

                    max_health += 2
                    health = 1

                if item == 'cove\'s concoction':
                    scrollTxt(
                        f"You take a sip from the {silver}silvery{white} {teal}teal{white} bottle. You feel {yellow}energized{white} for some reason you also feel {orange}weak{white}?")
                    scrollTxt(f"+ {blue}1{white} Dexterity | - {orange}1{white} Strength")

                    dexterity += 1
                    strength -= 1

                if item == 'awl\'s alchemy':
                    scrollTxt(
                        f"You take a sip from the {gold}goldish{white} {purple}purple{white} bottle. You feel {orange}strong{white} for some reason you also feel {darkgrey}tired{white}?")
                    scrollTxt(f"- {blue}1{white} Dexterity | + {orange}1{white} Strength")

                    dexterity -= 1
                    strength += 1

                if item == "crystal potion":
                    scrollTxt(f"You {blue}drink{white} the {turquoise}crystal potion{white} instantly you the {orange}desire{white} to get {gold}stronger{white}")
                    scrollTxt(f"{teal}Exp Bar{white} Reset!")
                    exp_max = 100
                    if exp > exp_max:
                        exp = 99

                if item == "aura of weakening scroll":
                    scrollTxt(f"You learned {darkgrey}AURA OF WEAKENING{white}!")
                    scrollTxt(f"Spell Effect: {italic}Target loses {orange}strength{white} and all targets gain {darkgrey}drain{white}{normal}{bold}")
                    current_spells.append("aura of weakening")
                    known_spells.append("aura of weakening")
                
                if item == "dagger swarm scroll":
                    scrollTxt(f"You learned {darkgrey}DAGGER SWARM{white}!")
                    scrollTxt(f"Spell Effect: {italic}Target takes {red}damage{white} and gains {red}bleed{white}{normal}{bold}")
                    current_spells.append("dagger swarm")
                    known_spells.append("dagger swarm")

                if item == "poison nova scroll":
                    scrollTxt(f"You learned {green}POISON NOVA{white}!")
                    scrollTxt(f"Spell Effect: {italic}All targets gain {green}poison{white}{normal}{bold}")
                    current_spells.append("poison nova")
                    known_spells.append("poison nova")

                if item == "hyper heal scroll":
                    scrollTxt(f"You learned {red}HYPER HEAL{white}!")
                    scrollTxt(f"Spell Effect: {italic}Your {red}health{white} is set back to {blue}full{white}{normal}{bold}")
                    current_spells.append("hyper heal")
                    known_spells.append("hyper heal")

                if item == "ice shards scroll":
                    scrollTxt(f"You learned {teal}ICE SHARDS{white}!")
                    scrollTxt(f"Spell Effect: {italic}All targets take {red}damage{white} and gain {turquoise}freeze{white}.{normal}{bold}")
                    current_spells.append("ice shards")
                    known_spells.append("ice shards")

                if item == "shadow spear scroll":
                    scrollTxt(f"You learned {darkgrey}SHADOW SPEAR{white}!")
                    scrollTxt(f"Spell Effect: {italic}{red}Target{white} takes massive {red}damage{white} and gains {purple}drain{white}{normal}{bold}")
                    current_spells.append("shadow spear")
                    known_spells.append("shadow spear")

                if item == "dark chromatic orb scroll":
                    scrollTxt(f"You learned {darkgrey}DARK{white} {purple}CHROMATIC ORC{white}!")
                    scrollTxt(f"Spell Effect: {italic}{red}Target{white} takes {red}damage{white} and gains {purple}life steal{white}{normal}{bold}")
                    current_spells.append("dark chromatic orb")
                    known_spells.append("dark chromatic orb")
                
                if item == "dark arrows scroll":
                    scrollTxt(f"You learned {darkgrey}DARK{white} {purple}ARROWS{white}!")
                    scrollTxt(f"Spell Effect: {italic}{red}All Targets{white} take {red}damage{white} and gains {purple}drain{white}{normal}{bold}")
                    current_spells.append("dark arrows")
                    known_spells.append("dark arrows")

                if item == "teleportation token":
                    scrollTxt(f"Where would you like to {turquoise}teleport{white}?")
                    if world == "farcore":
                        answer = get_input(list(areas_to_names.keys()))
                        print()

                        scrollTxt(f"{teal}TELEPORTING{white}...")
                        time.sleep(2)

                        scrollTxt(f"You made it to {copper}{answer}{white}")
                        location = areas_to_names[answer]
                        pre_loc = location
                    else:
                        answer = get_input(list(areas_to_fr.keys()))
                        print()

                        scrollTxt(f"{teal}TELEPORTING{white}...")
                        time.sleep(2)

                        scrollTxt(f"You made it to {copper}{answer}{white}")
                        location = areas_to_fr[answer]
                        pre_loc = location

                if item == "world token":
                    scrollTxt(f"Where would you like to {purple}dimension {orange}hop{white}?")
                    answer = get_input(["farcore", "frozite"])
                    print()

                    scrollTxt(f"{orange}WARP{purple}ING{white}...")
                    time.sleep(2)

                    scrollTxt(f"You made it to {blue}{answer}{white}")
                    world = answer
                    if world == "farcore":
                        location = "lockwood"
                    else:
                        location = "white bridge"
                    pre_loc = location

                if item == "dungeon token":
                    amount = 0
                    for obj in triggers:
                        if "dungeon completed" in obj:
                            amount += 1
                            
                    print(f"Entering {darkgrey}dungeon{white}...")
                    time.sleep(3)
                    enter()

                    if amount == 0:
                        crypt_of_the_necromancer()
                    if amount == 1:
                        try:
                            the_furious_jungle()
                        except:
                            print("Dungeon hasn't been added")
                    if amount == 2:
                        try:
                            the_silent_mountain()
                        except:
                            print("Dungeon hasn't been added")
                    if amount == 3:
                        try:
                            cursed_depths()
                        except:
                            print("Dungeon hasn't been added")

                if item == "teleportation staff":
                    scrollTxt(f"Where would you like to {turquoise}teleport{white}?")
                    if world == "farcore":
                        answer = get_input(list(areas_to_names.keys()))
                        print()

                        scrollTxt(f"{teal}TELEPORTING{white}...")
                        time.sleep(2)

                        scrollTxt(f"You made it to {copper}{answer}{white}")
                        location = areas_to_names[answer]
                        pre_loc = location
                    else:
                        answer = get_input(list(areas_to_fr.keys()))
                        print()

                        scrollTxt(f"{teal}TELEPORTING{white}...")
                        time.sleep(2)

                        scrollTxt(f"You made it to {copper}{answer}{white}")
                        location = areas_to_fr[answer]
                        pre_loc = location
                    
                if item == "monster book":
                    scrollTxt(f'You open the {brown}book{white}')
                    scrollTxt(f"What {red}monster{white} would you like to {blue}learn{white} about?")
                    answer = get_input(list(enemies_all.keys()))

                    print()
                    if answer in bosses:
                        scrollTxt(f"{orange}{answer.upper()}{white} [{red}BOSS{white}]")
                    else:
                        lv = enemies_all[answer]["exp"]/10
                        scrollTxt(f"{copper}{answer}{white} [{darkgrey}Lv{white}: {red}{lv}{white}]")
                    gde = enemies_all[answer]["gold"]
                    scrollTxt(f" - Drops {gold}{gde}{white} gp")
                    for thng in enemies_all[answer]["drop"]:
                        if "trophy" not in thng:
                            itm = enemies_all[answer]["drop"][thng]
                            chnc = round(100/itm, 0)
                            scrollTxt(f" - {brown}{thng}{white} [{red}{chnc}{white}%]")

                if item == "guide":
                    scrollTxt(f'You open the {brown}book{white}')
                    print()
                    print()
                    print(f"""{blue}GUIDE{white}
```
___________                                         
\_   _____/____ _______   ____  ___________   ____  
 |    __) \__  \\_  __ \_/ ___\/  _ \_  __ \_/ __ \ 
 |    |   / __ \|  | \/ \  \__(  <_> )  | \/\  ___/ 
 \___/   (____  /__|     \___  >____/|__|    \___ >
             \/            \/                  \/ 
                 - A FULL GUIDE -
```

{blue}Combat | Tips + Info{white}


{blue}Fast Attack and Sweep Attack{white}
- {purple}Fast Attack{white} = {purple}Auto{white} Chooses how to attack | Good for {purple}grinding{white} or if you don't want to spend time choosing how to attak
- {purple}Sweep Attack{white} = Damages {purple}all enemies{white} | Deals {purple}less damage{white}

{blue}{blue}{blue}Dexterity VS Strength Attack{white} 
- {purple}Strength{white} = Uses your strength to attack
- {purple}Dexterity{white} = Uses your dexterity to attack

{blue}{blue}{blue}One Handed Attack VS Two Handed Attack{white}
- {purple}One hand{white} = Automatic if you have a shield, deals {purple}normal damage{white}
- {purple}Two hands{white} = You can choose if you have no shield, deals {purple}double damage{white} but less chance for hitting


{blue}{blue}Game Guide{white}

You {purple}start{white} the {purple}game{white} in a menu that provides the choice of {purple}loading{white} a {purple}save{white}

 ---> Since you are new type "{purple}n{white}"

Next you will have to choose what {purple}class{white} you want

---> My advice for starters is the {purple}warrior class{white}

Then your are prompted with a {purple}test encounter{white}

---> You should choose always to {purple}attack{white} and then {purple}block/dodge{white} and the fight will be over quickly

Finally you will start your adventure in {purple}[Lockwood]{white}
- Go the {purple}market square{white} to upgrade your {purple}weapons & armor{white}
- Talk to a {purple}stranger{white} to trigger a {purple}miniboss{white}
- Go to the {purple}Inn{white} to play {purple}games{white} or buy rare {purple}potions{white} (drinks)

After you are fully upgraded you are ready to start you adventure

{purple}Adveturing Gear{white}

- {purple}Bronze Sword & Shield{white}
- {purple}3 Health potions{white}


{blue}{blue}Common Path/Progression{white}

{purple}Lockwood{white} (start)
    - Get gear

--> {purple}Scarred Plains{white} (east)
    - Fight!

--> {purple}Lost Plains{white} (west x2)
    - Fight!

--> {purple}The Forge{white} (south)
    - Upgrade weapons

--> {purple}Low Grass{white} (east x2)
    - New weapons

--> {purple}Snowy Mountain{white} (west)
    - Boss!

--> {purple}Blessed Lake{white} (south)
    - Level up

--> {purple}Cursed Shores{white} (east)
    - Fight!

--> {purple}Darkwood{white} (south)
    - Get Stronger
                                
--> {purple}Jade Forest{white} (west)
    - Magic Sword

--> {purple}Dragon Cave{white} (south)
    - Boss!!!

---------------------------------------------
PRO TIPS
- Shops change their prices every 5 minutes
- Thief is the best class (just buy a different weapon) 
- Ranger would probably be the second best
- You can grind fight the warrior for gold
- Always run from a copper guardain until your level 2+
- Always have a spare weapon incase your main one breaks
- Most bosses have a chance of dropping spells
- Magi potions give you back your spells
- Luck potions higher the chance of getting items from enemies
- Dexterity = Accuracy = Hit
- Strength = Damage = Power""")
                    
                if item == "map":
                    scrollTxt(f'You open the {brown}map{white}')
                    print()
                    print()

                    print(f"""{turquoise}___________                                         
{turquoise}\_   _____/____ {teal}_______   ____{blue}  ___________   ____  
{turquoise} |    __) \__  \\{teal}\\_  __ \\_/ ___\\{blue}/  _ \\_  __ \\_/ __ \\ 
{turquoise} |    |   / __ \\{teal}|  | \\/ \\  \\__{blue}(  <_> )  | \\/\\  ___/ 
{turquoise} \\___/   (____  /{teal}__|     \\___  >{blue}____/|__|    \\___ >
{turquoise}             \\/{teal}            \\/{blue}                  \\/ 
                {white}- A FULL MAP -

___________  ___________  ___________  ___________
|          | |          | |          | |          |
| {lime}Lost{white}     | | {brown}Lockwood{white} | | {lime}Scarred{white}  | | {blue}Blue{white}     |
| {lime}Plains{white}   | | {brown}Village{white}  | | {lime}Plains{white}   | | {blue}Shores{white}   |
|__________| |__________| |__________| |__________|
___________  ___________  ___________ 
|          | |          | |          | 
| {darkgrey}The{white}      | | {purple}Snowy{white}    | | {lime}Low{white}      |
| {darkgrey}Forge{white}    | | {purple}Mountain{white} | | {lime}Grass{white}    | 
|__________| |__________| |__________|
              ___________  ___________ 
             |          | |          | 
             | {turquoise}Blessed{white}  | | {gold}Cursed{white}   |
             | {turquoise}Lake{white}     | | {gold}Shores{white}   | 
             |__________| |__________|
              ___________  ___________ 
             |          | |          | 
             | {green}Jade{white}     | | {green}Darkwood{white} |
             | {green}Forest{white}   | |          | 
             |__________| |__________|
              ___________ 
             |          |
             | {orange}Dragon{white}   |
             | {orange}Cave{white}     |
             |__________|""")

                if item == "reykrs book":
                    scrollTxt(f'You open the {brown}book{white}')
                    print()
                    print()

                    print(f"""===================
{darkgrey}Reykr's{white} Tip Book 🐺
===================

~ {blue}Dodge{white} and {blue}Block{white}, make use of whichever you can use.

~ Use {darkgrey}Dexterity{white} or {teal}Strength{white} attacks, depending on which of your {purple}stats{white} is higher.
(Check your stats and do what you're best at.)

~ Stock up on {red}Health{white} Potions, you never know when you'll need them.
Make sure you have some in your inventory. If not, buy some with {gold}Gold{white}.

~ Carry around a {blue}spare weapon{white} too, your main one could break during battle.
Do the same with a {blue}spare shield{white} (if you use them).

~ Shops change their {gold}prices{white}, so if something is too {red}expensive{white}, wait til the price lowers!

~ Don't leave {copper}Lockwood{white} until you're ready.
Make sure you've got new, better {darkgrey}gear{white} and plenty of {red}Health{white} Potions.

~ When you DO get out of Lockwood, make sure you know where you want to go.
{purple}Wandering{white} around randomly increases your chances of getting {blue}attacked{white}!
Unless you're looking for a {orange}fight{white}, I'd recommend avoiding unnecessary encounters.

~ A {red}jes{blue}ter{white} might give you stuff for {gold}free{white}, if you tell them to...
You'll have to figure out this one yourself.

~ Not so much of a tip, but my opinions:
{green}Thief{white} and {teal}Ranger{white} are indeed the best classes.
""")

                if item == "andrew dengs book":
                    scrollTxt(f'You open the {brown}book{white}')
                    print()
                    print()

                    print(f"""======================
{blue}AndrewDeng3's{white} Tip Book
======================

Use {green}ranger{white}, it has the most balanced stats

Stat table for classes:

For recommended:
  {green}*{white} means yes definitely
  {yellow}?{white} means maybe
  {red}/{white} means definitly no
__________________________________
|Recommended:  {green}*{white}   {green}*{white}   {yellow}?{white}   {red}/{white}   {yellow}?{white} |
|Character:    T   R   W   M   B |
|Strength:     {yellow}3{white}   {yellow}4{white}   {yellow}4{yellow}   {red}2{white}   {green}5{white} |
|Dexterity:    {green}5{white}   {green}5{white}   {yellow}3{white}   {yellow}3{white}   {yellow}3{white} |
|Health:       {red}15{white}  {yellow}17{white}  {green}20{white}  {red}15{white}  {green}22{white}|
|________________________________|

Use attack more often, and {blue}strength{white} + {blue}two handed{white} = your friend (Good for starting out)
Strength attacks often apply the {red}gash{white} effect to your enemy, which is also very {gold}helpful{white}

Use {blue}dodge{white} when starting the game, and {red}heal wounds{white} if you need to. However, it is a bit risky to {gold}steal{white}.

Also, when playing the game, {blue}do not move{white} around too much, as there is a high chance of you encountering a {red}monster{white} and have to do unnessesary fighting.

Restock your {blue}items{white} every few fights, and keep {blue}extras{white} of pretty much everything on you at all times. You never know what will happen.

Always have a {gold}goal{white} in mind, that way you know what you want to do. Such as buying a new sword or something.

One last tip:{red}
__________________________
|Never gonna GIVE YOU UP |
|Never gonna LET YOU DOWN|
|Never gonna RUN AROUND  |
|and DESERT YOU!         |
|________________________|{white}""")
            
                if item == "shadow samurias book":
                    scrollTxt(f'You open the {brown}book{white}')
                    print()
                    print()
                    crollTxt("""--------------------------
ShadowSamurai69's tip book
--------------------------

Always have at least 10 hp when travelling to another place. You never know when you might encounter a copper giant or a pair of goblins.

Always have a spare weapon in case yours breaks. Fists don't do that much damage.

Thief is by far best class, you can steal gold.from your enemies(if you dont have a shield)

Ranger is second best becasue they have balanced stats and come with a few items.

Do not leave lockwood straight away. You should always grind the warrior for gold and then buy better gear from the market place.

You dont just have to get gear from lockwood. There is a merchant who sells exotic weapons like longbows and tridents in low grass.

When you get a magical weapon like the frosted longsword or the magical sword. Make sure to infuse them or go to the forge to enchant them multiple times. This can be over multiple lives as you ahould choose this weapon to keep in the next life.

When you die don't just stop the repl. If you do then you won't get the chance to bring one of your items into the next game.

Shops change their prices every now and then so make sure to come back to one later if you think the item you want is to o expensive.

Always have at leaat 5 health potions on you. You never know when you might need one. 

My advice is to always get good gear in lockwood, then go to either the mountains or the jungle and get a magical weapon.

Never name your weapon nothing becasue then you cant bring it in to the next life.

Always remember to dodge and block.

This was brought to you by ShadowSamurai69. "Gaming legend"
""")

                if item == "nj wolfs book":
                    scrollTxt(f'You open the {brown}book{white}')
                    print()
                    print()

                    print(f"""===================
Tip Book For {red}Scrubs{white}
===================

Make Sure to Grab {copper}goblin Horns{white}, they give {red}+1{white} to hit.
I would Suggest {darkgrey}Warrior{white} or {green}Ranger{white} they are good starts balanced stats
Remember {blue}Dodge{white} and {blue}Block{white} are your best Friends
Some {orange}Mob Drops{white} add status to weapons, very useful
Make Sure to bring {darkgrey}Weapons/Drops{white} as your item to the next {red}life{white}
In the same place you {teal}level up{white} you can give {gold}coins{white} to your next life
Lots of {red}bosses{white} and mobs have things to infuse def {orange}grind{white} them
Run the {turquoise}Jade Forest{white} has a very useful {darkgrey}item{white} but dont go there until you can fight
Remember to always have backup {blue}claymores{white} or other weapons


{red}Barbarian{white} Is Best. {red}Barbarian{white} Is Bae.
     "{orange}Grog{white} smash {orange}Grog{white} Bash"
      -{orange}Grog{white} The Masher

     "{copper}Bittle{white} Me Makes {copper}Bittle{white} Be"
      - {yellow}Bittle{white} me the swag

-{gold}Lore{white} Master {purple}Nj{white}""")
                
            if answer == 'equip':

                if item_stats['weapon'] is True and item not in offhand_weapons:
                    if len(list(weapons_all[item]["req"].keys())) > 0:
                        meet = False
                        if "class" in weapons_all[item]["req"]:
                            if fighter_class == weapons_all[item]["req"]["class"]:
                                meet= True
                            else:
                                zxc = weapons_all[item]["req"]["class"]
                                scrollTxt(f"This {darkgrey}weapon{white} is only for {purple}{zxc}s{white}")
                        elif "dex" in weapons_all[item]["req"]:
                            
                            if dexterity >= weapons_all[item]["req"]["dex"]:
                                meet= True
                            else:
                                zxc = weapons_all[item]["req"]["dex"]
                                scrollTxt(f"This {darkgrey}weapon{white} is only for people with a {blue}dexterity{white} higher than {green}{zxc-1}{white}")
                        elif "str" in weapons_all[item]["req"]:
                            if strength >= weapons_all[item]["req"]["str"]:
                                meet= True
                            else:
                                zxc = weapons_all[item]["req"]["str"]
                                scrollTxt(f"This {darkgrey}weapon{white} is only for people with a {orange}strength{white} higher than {red}{zxc-1}{white}")
                        
                        if meet is True:
                            scrollTxt(f'{grey}{item}{white} equiped!')

                            if weapons_all[item]["two handed"] is True and fighter_class != "barbarian":
                                offhand = "none"
                                scrollTxt(f"{darkgrey}Weapon{white} is {blue}two-handed{white}")
                                
                            if item in strength_weapons:
                                triggers.append("power weapon equiped")
                                print()
                                am = strength_weapons[item]
                                scrollTxt(f"While equiping this {darkgrey}weapon{white} you gain {red}{am}{white} strength")
                                strength += am

                            if item in dexterity_weapons:
                                triggers.append("power weapon equiped")
                                print()
                                am = dexterity_weapons[item]
                                scrollTxt(f"While equiping this {darkgrey}weapon{white} you gain {green}{am}{white} dexterity")
                                dexterity += am

                            if item in health_weapons:
                                triggers.append("power weapon equiped")
                                print()
                                am = health_weapons[item]
                                scrollTxt(f"While equiping this {darkgrey}weapon{white} you gain {red}{am}{white} max health")
                                max_health += am
                            weapon = item
    
                    else:
                            scrollTxt(f'{grey}{item}{white} equiped!')

                            if weapons_all[item]["two handed"] is True and fighter_class != "barbarian":
                                offhand = "none"
                                scrollTxt(f"{darkgrey}Weapon{white} is {blue}two-handed{white}")
                            if item in strength_weapons:
                                triggers.append("power weapon equiped")
                                print()
                                am = strength_weapons[item]
                                scrollTxt(f"While equiping this {darkgrey}weapon{white} you gain {red}{am}{white} strength")
                                strength += am

                            if item in dexterity_weapons:
                                triggers.append("power weapon equiped")
                                print()
                                am = dexterity_weapons[item]
                                scrollTxt(f"While equiping this {darkgrey}weapon{white} you gain {green}{am}{white} dexterity")
                                dexterity += am

                            if item in health_weapons:
                                triggers.append("power weapon equiped")
                                print()
                                am = health_weapons[item]
                                scrollTxt(f"While equiping this {darkgrey}weapon{white} you gain {red}{am}{white} max health")
                                max_health += am
                            weapon = item

                            if weapon == "dual blade [weapon]":
                                if offhand != "dual blade [offhand]":
                                    offhand = "none"
                else:
                    try:
                        if weapons_all[weapon]["two handed"] and fighter_class != "barbarian":
                            scrollTxt(f"You can\'t equip a {darkgrey}offhand{white}, your weapon is {blue}two handed{white}")
                        else:
                            if item != "dual blade [offhand]":
                                if weapon != "dual blade [weapon]":
                                    scrollTxt(f'{grey}{item}{white} equiped!')
                                    offhand = item
                                else:
                                    scrollTxt(f"You can only equip a {teal}dual blade{white} for your offhand")
                            else:
                                if weapon == "dual blade [weapon]":
                                    scrollTxt(f'{grey}{item}{white} equiped!')
                                    offhand = item
                                else:
                                    scrollTxt(f"You must have a {teal}dual blade{white} equiped as your {darkgrey}weapon{white}")


                    except:
                        if item != "dual blade [offhand]":
                            scrollTxt(f'{grey}{item}{white} equiped!')
                            offhand = item
                        else:
                            scrollTxt(f"You must have a {teal}dual blade{white} equiped as your {darkgrey}weapon{white}")

            if answer == "unequip":
                scrollTxt(f'{grey}{item}{white} unequiped!')

                if item == offhand:
                    offhand = 'none'
                elif item == weapon:
                    if "power weapon equiped" in triggers:
                        if item in strength_weapons:
                            am = strength_weapons[item]
                            strength -= am

                        if item in dexterity_weapons:
                            am = dexterity_weapons[item]
                            dexterity -= am

                        if item in health_weapons:
                            am = health_weapons[item]
                            max_health -= am
                        triggers.remove("power weapon equiped")
                    if weapon == "dual blade [weapon]":
                        offhand = "none"
                    weapon = "none"

            if answer == "sell":
                amount_sell = item_stats["selling price"]
                print(f"+ {gold}{amount_sell}{white} GP")
                print(f"- {red}{item}{white}")

                gp += amount_sell
                inv.remove(item)
                if item == offhand:
                    offhand = 'none'
                if item == weapon:
                    weapon = "none"

                if item in durability_weapon:
                    durability_weapon.pop(item)
            
            if answer == "scrap":
                scra = max(math.floor(items_all[item]["selling price"]/10), 1)
                print(f"+ {blue}{scra}{white} {darkgrey}metal scrap{white}")
                print(f"- {red}{item}{white}")
                inv.remove(item)
                if item == offhand:
                    offhand = 'none'
                if item == weapon:
                    weapon = "none"

                if item in durability_weapon:
                    durability_weapon.pop(item)
                for h in (1, scra):
                    inv.append("metal scrap")
                if scra == 1: inv.remove("metal scrap")

            if answer == "infuse":
                ww = []
                for x in inv:
                    if items_all[x]["weapon"] and "staff" not in x:
                        ww.append(x)

                print(f"What {darkgrey}weapon{white} would you like to {green}infuse{white}?")

                for x in ww:
                    if x != ww[len(ww) - 1]:
                        print(f"{random.choice([darkgrey, grey, silver, platinum])}{x}{white}, ", end="")
                    else:
                        print(f"{random.choice([darkgrey, grey, silver, platinum])}{x}{white}", end="")
                print()

                answer = get_input(ww)

                if item != "sharpening stone" and item != "shrinker":

                    print()

                    istats = items_all[answer].copy()
                    wstats = weapons_all[answer].copy()

                    is_chosen = False
                    if weapon == answer: is_chosen = True

                    if is_chosen: weapon = "none"
                    inv.remove(answer)

                    duramount = 0
                    duracheck = False
                    if answer in durability_weapon:
                        duramount = durability_weapon[answer]
                        duracheck = True
                        durability_weapon.pop(answer)


                    if item == "troll heart": power_bonus = f"{green}poison"
                    if item == "goblin horn": power_bonus = f"{blue}goblin horn"
                    if item == "orc tooth": power_bonus = f"{orange}orc tooth"
                    if item == "master ruby": power_bonus = f"{red}ruby"
                    if item == "yeti eye": power_bonus = f"{turquoise}frosted"
                    if item == "lightning stone": power_bonus = f"{yellow}lightning"
                    if item == "jade": power_bonus = f"{purple}life steal"
                    if item == "dragon scale": power_bonus = f"{paleyellow}dragon scale"
                    if item == "skull": power_bonus = f"{silver}skull"
                    if item == "mutant jaguar tooth": power_bonus = f"{red}jaguar tooth"
                    if item == "ogre nail": power_bonus = f"{yellow}ogre{darkgrey} nail"
                    if item == "acid goo": power_bonus = f"{lime}infected{white}"
                    if item == "rock core": power_bonus = f"{darkgrey}rocky{white}"
                    print(f"Your {darkgrey}{answer}{white} is now a {power_bonus}{white} {darkgrey}{answer}{white}")
                    

                    if item == "troll heart": power_bonus = f"poison"
                    if item == "goblin horn": power_bonus = f"goblin horn"
                    if item == "orc tooth": power_bonus = f"orc tooth"
                    if item == "yeti eye": power_bonus = f"frosted"
                    if item == "lightning stone": power_bonus = f"lightning" 
                    if item == "jade": power_bonus = f"life steal"
                    if item == "master ruby": power_bonus = f"ruby"
                    if item == "dragon scale": power_bonus = item
                    if item == "mutant jaguar tooth": power_bonus = f"jaguar tooth"
                    if item == "skull": power_bonus = item
                    if item == "ogre nail": power_bonus = item
                    if item == "acid goo": power_bonus = "infected"
                    if item == "rock core": power_bonus = "rocky"

                    wname = power_bonus + " " + answer

                    inv.append(wname)
                    if is_chosen: weapon = wname

                    istats['name'] = wname
                    istats['description'] = istats[
                                                'description'] + f"\n{green}Fused{white} with a {item}. Named {darkgrey}{wname}{white}."
                    istats['selling price'] += int(item_stats['selling price']/2)
                    items_all[wname] = istats

                    if item == "troll heart":
                        if wstats["special"] is False:
                            wstats['special'] = "poison"
                            wstats['special text'] = f"Ugly {green}green{white} blood {lime}oozes{white} out of their {red}wound{white}"
                        else:
                            try:
                                wstats['special'].append("poison")
                                wstats['special text'].append(f"Ugly {green}green{white} blood {lime}oozes{white} out of their {red}wound{white}")
                            except:
                                wstats["special"] = [wstats["special"], "poison"]
                                wstats['special text'] = [wstats["special text"], f"Ugly {green}green{white} blood {lime}oozes{white} out of their {red}wound{white}"]
                    if item == "acid goo":
                        if wstats["special"] is False:
                            wstats['special'] = "acid"
                            wstats['special text'] = f"{lime}Radoactive{white} goo covered the {red}enemy{white} causing a {orange}deadly burn{white}."
                        else:
                            try:
                                wstats['special'].append("acid")
                                wstats['special text'].append(f"{lime}Radoactive{white} goo covered the {red}enemy{white} causing a {orange}deadly burn{white}.")
                            except:
                                wstats["special"] = [wstats["special"], "acid"]
                                wstats['special text'] = [wstats["special text"], f"{lime}Radoactive{white} goo covered the {red}enemy{white} causing a {orange}deadly burn{white}."]
                    if item == "goblin horn":
                        wstats["hit"] += 1
                        scrollTxt(f"+ {green}1{white} accuracy")
                    if item == "orc tooth":
                        wstats["damage"] += 1
                        scrollTxt(f"+ {red}1{white} damage")
                    if item == "ogre nail":
                        wstats["damage"] += 3
                        scrollTxt(f"This {darkgrey}weapon{white} is {blue}two-handed{white}")
                        wstats["two handed"] = True
                        offhand = "none"
                        scrollTxt(f"+ {red}3{white} damage")
                    if item == "rock core":
                        scrollTxt(f"+ {darkgrey}4{white} Defense | When Equiping this {red}Weapon{white}")
                        if "cross-saber" not in wname: defense_weapons[wname] = 4
                    if item == "mutant jaguar tooth":
                        strength_weapons[wname] = 2

                        strength += 2
                        triggers.append("power weapon equiped")

                        scrollTxt(f"gives {red}2{white} strength when equiped")
                    if item == "master ruby":
                        wstats["damage"] += 2
                        scrollTxt(f"+ {red}2{white} damage")
                    if item == "yeti eye":
                        scrollTxt(f"+ {teal}freeze{white} ability")
                        if wstats["special"] is False:
                            wstats['special'] = "freeze"
                            wstats['special text'] = f"Their body slightly {turquoise}frosts{white} over. Leaving it {blue}blueish{white}."
                        else:
                            try:
                                wstats['special'].append("freeze")
                                wstats['special text'].append(f"Their body slightly {turquoise}frosts{white} over. Leaving it {blue}blueish{white}.")
                            except:
                                wstats["special"] = [wstats["special"], "freeze"]
                                wstats['special text'] = [wstats["special text"], f"Their body slightly {turquoise}frosts{white} over. Leaving it {blue}blueish{white}."]
                    if item == "lightning stone":
                        scrollTxt(f"+ {orange}lightning{white} ability")
                        if wstats["special"] is False:
                            wstats['special'] = "shock"
                            wstats['special text'] = f"The {red}enemies{white} body {paleyellow}crackles{white} with {yellow}electricity{white}."
                        else:
                            try:
                                wstats['special'].append("shock")
                                wstats['special text'].append(f"The {red}enemies{white} body {paleyellow}crackles{white} with {yellow}electricity{white}.")
                            except:
                                wstats["special"] = [wstats["special"], "shock"]
                                wstats['special text'] = [wstats["special text"], f"The {red}enemies{white} body {paleyellow}crackles{white} with {yellow}electricity{white}."]
                    if item == "jade":
                        scrollTxt(f"+ {purple}life steal{white} ability")
                        if wstats["special"] is False:
                            wstats['special'] = "life steal"
                            wstats['special text'] = f"The {red}enemy{white} turns a {darkgrey}shadowly grey{white} as it\'s {red}lifeforce{white} is being {purple}drained{white}"
                        else:
                            try:
                                wstats['special'].append("life steal")
                                wstats['special text'].append(f"The {red}enemy{white} turns a {darkgrey}shadowly grey{white} as it\'s {red}lifeforce{white} is being {purple}drained{white}")
                            except:
                                wstats["special"] = [wstats["special"], "life steal"]
                                wstats['special text'] = [wstats["special text"], f"The {red}enemy{white} turns a {darkgrey}shadowly grey{white} as it\'s {red}lifeforce{white} is being {purple}drained{white}"]
                    if item == "dragon scale":
                        scrollTxt(f"+ {orange}dragon burn{white} ability")
                        if wstats["special"] is False:
                            wstats['special'] = "dragon burn"
                            wstats['special text'] = f"The {copper}enemy{white} ignites on {red}fire{white}. {paleyellow}White hot flames{white} ingulf everything."
                        else:
                            try:
                                wstats['special'].append("dragon burn")
                                wstats['special text'].append(f"The {copper}enemy{white} ignites on {red}fire{white}. {paleyellow}White hot flames{white} ingulf everything.")
                            except:
                                wstats["special"] = [wstats["special"], "dragon burn"]
                                wstats['special text'] = [wstats["special text"], f"The {copper}enemy{white} ignites on {red}fire{white}. {paleyellow}White hot flames{white} ingulf everything."]
                    if item == "skull":
                        scrollTxt(f"+ {darkgrey}drain{white} ability")
                        if wstats["special"] is False:
                            wstats['special'] = "drain"
                            wstats['special text'] = f"The {red}target{white} wound turns {darkgrey}grey{white} and {purple}shrivels{white}"
                        else:
                            try:
                                wstats['special'].append("drain")
                                wstats['special text'].append(f"The {red}target{white} wound turns {darkgrey}grey{white} and {purple}shrivels{white}")
                            except:
                                wstats["special"] = [wstats["special"], "drain"]
                                wstats['special text'] = [wstats["special text"], f"The {red}target{white} wound turns {darkgrey}grey{white} and {purple}shrivels{white}"]

                    weapons_all[wname] = wstats
                    print()

                    if duracheck:
                        durability_weapon[wname] = duramount

                    inv.remove(item)

                    answer = item

                    if answer in blessed_weapons:
                        blessed_weapons[wname] = blessed_weapons[answer]
                    if answer in cursed_weapons:
                        cursed_weapons[wname] = cursed_weapons[answer]
                    if answer in strength_weapons:
                        strength_weapons[wname] = strength_weapons[answer]
                    if answer in dexterity_weapons:
                        dexterity_weapons[wname] = dexterity_weapons[answer]
                    if answer in health_weapons:
                        health_weapons[wname] = health_weapons[answer]
                    if answer in luck_weapons:
                        luck_weapons[wname] = luck_weapons[answer]
                    if answer in steal_weapons:
                        steal_weapons[wname] = steal_weapons[answer]
                    if answer in double_bladed_weapons:
                        double_bladed_weapons.append(answer)
                    if answer in defense_weapons:
                        defense_weapons[wname] = defense_weapons[answer]
                    if answer in offhand_weapons:
                        offhand_weapons.append(answer)
                else:
                    if item == "sharpening stone":
                        print()
                        scrollTxt(f"{darkgrey}Weapon{white} durability set to {blue}full{white}!")
                        if answer in durability_weapon.keys():
                            durability_weapon.pop(answer)
                        inv.remove("sharpening stone")
                    elif item == "shrinker":
                        print()

                        if "shrunken" not in answer:
                        
                            if weapons_all[answer]['two handed'] is True:

                                nweapon_name = "shrunken " + answer
                                if answer == weapon: weapon = nweapon_name
                                weapons_all["shrunken " + answer] = weapons_all[answer].copy()
                                items_all["shrunken " + answer] = items_all[answer].copy()
                                weapons_all[nweapon_name]["two handed"] = False
                                items_all[nweapon_name]["name"] = nweapon_name
                                inv.remove(answer)
                                inv.append(nweapon_name)
                                inv.remove('shrinker')
                                scrollTxt(f"Weapon {lime}shrunk{white}!")
                            elif answer != offhand_weapons:
                                nweapon_name = "shrunken " + answer
                                if answer == weapon: weapon = nweapon_name
                                weapons_all["shrunken " + answer] = weapons_all[answer].copy()
                                items_all["shrunken " + answer] = items_all[answer].copy()
                                weapons_all[nweapon_name]["two handed"] = False
                                items_all[nweapon_name]["name"] = nweapon_name
                                inv.remove(answer)
                                inv.append(nweapon_name)
                                offhand_weapons.append(nweapon_name)
                                inv.remove('shrinker')
                                scrollTxt(f"Weapon {lime}shrunk{white}!")
                            else:
                                scrollTxt(f"Your {darkgrey}weapon{white} cannot be {green}shrunken{white}.")
                        else:
                            scrollTxt(f"Your {darkgrey}weapon{white} cannot be {green}shrunken{white}.")

        if answer != "exit":
            enter()

        if answer != 'l':
            inventory()

        else:
            clear()


    def randomize(target, change_amount):
        ntarget = {}

        for x in target:
            try:
                z = target[x] - 100
                ntarget[x] = target[x] + random.randint(-change_amount, change_amount)

            except:
                ntarget[x] = target[x]

        return ntarget


    def combat(enemy, dam_multiplier=1, enemies_damaged = []):
        global effects, clrs_list, health, inv, weapon, offhand, dexterity, strength, max_health, gp, effects, special_moves, shield_moves, known_spells, current_spells, enemies_killed, exp, exp_max, lvl, fighter_class, crystals, weapons_reload

        save()
        enemies = {}
        y = {}

        effects_applied = []

        begin_health = health

        enemies_checks = list(enemies_all.keys())

        for i in enemy:
            

            for x in enemies_checks:
                if x in i and len(list(i)) - 4 < len(list(x)):
                    try:
                        y[x] += 1
                    except:
                        y[x] = 1

                    new_enemy = enemies_all[x].copy()
                    if x not in multimove:
                        new_enemy["damage"] += int(lvl/3)
                        new_enemy["dex"] += int(lvl/3)
                        new_enemy["str"] += int(lvl/3)
                        new_enemy["health"] += int(lvl/3)
                    else:
                        nda = []
                        nde = []

                        for l in new_enemy["damage"]:
                            try:
                                nda.append((l + int(lvl/3)))
                            except:
                                nda.append(l)
                        for l in new_enemy["dex"]:
                            nde.append((l + int(lvl/3)))

                        new_enemy["damage"] = nda
                        new_enemy["dex"] = nde
                        new_enemy["str"] += int(lvl/3)
                        new_enemy["health"] += int(lvl/3)
                    

                    enemies[i] = new_enemy
        clear()

        battle = ""
        battle2 = ""
        

        for i in y:

            if battle != "":
                battle = "" + battle + white + " and the "

            if y[i] > 1:
                battle = "" + battle + red + str(y[i]) + grey + " " + i + "s"
            else:
                battle = "" + battle + teal + "lone" + grey + " " + i

        for i in y:

            if battle2 != "":
                battle2 = "" + battle2+ " and the "

            if y[i] > 1:
                battle2 = "" + battle2 +  str(y[i]) + " " + i + "s"
            else:
                battle2 = "" + battle2 + "lone" + " " + i

        turn = 'player'

        blocking = []

        metahi_bonus = 0
        metadam_bonus = 0
        metade_bonus = 0

        hurt = []
        uhurt = []

        luck_amount = 0

        if "damage bonus" in effects:
            effects_applied.append("damage bonus")
            effects['damage bonus'][1] -= 1
            metadam_bonus = effects['damage bonus'][0]
            if effects['damage bonus'][1] == 0:
                effects.pop("damage bonus")

        if "hit bonus" in effects:
            effects_applied.append("hit bonus")
            effects['hit bonus'][1] -= 1
            metahi_bonus = effects['hit bonus'][0]
            if effects['hit bonus'][1] == 0:
                effects.pop("hit bonus")

        if "defense bonus" in effects:
            effects_applied.append("defense bonus")
            effects["defense bonus"][1] -= 1
            metade_bonus = effects["defense bonus"][0]
            if effects['defense bonus'][1] == 0:
                effects.pop("defense bonus")

        if weapon in defense_weapons:
            metade_bonus += defense_weapons[weapon]


        if "luck" in effects:

            effects['luck'][1] -= 1
            luck_amount = effects["luck"][0]
            if effects['luck'][1] == 0:
                effects.pop("luck")

        if weapon in luck_weapons:
            luck_amount += luck_weapons[weapon]

        turn1 = True

        if enemies_damaged != []:
            current_num = 0
            for x in enemies:
                enemies[x]["health"] -= enemies_damaged[current_num]
                current_num += 1

        while True:
            y = {}
            enemies_checks = list(enemies_all.keys())
            enemy = enemies.keys()
            for i in enemy:
                for x in enemies_checks:
                    if x in i and len(list(i)) - 4 < len(list(x)):
                        try:
                            y[x] += 1
                        except:
                            y[x] = 1
            battle = ""
            battle2 = ""
            

            for i in y:

                if battle != "":
                    battle = "" + battle + white + " and the "

                if y[i] > 1:
                    battle = "" + battle + red + str(y[i]) + grey + " " + i + "s"
                else:
                    battle = "" + battle + teal + "lone" + grey + " " + i

            for i in y:

                if battle2 != "":
                    battle2 = "" + battle2+ " and the "

                if y[i] > 1:
                    battle2 = "" + battle2 +  str(y[i]) + " " + i + "s"
                else:
                    battle2 = "" + battle2 + "lone" + " " + i

            clear()
            #input(len("| " + "Battle " + "of the " + battle + " |"))
            lt = int(max(len(list("| " + "Battle " + "of the " + battle2 + " |")) - 19, 0)/2)
            p1 = ""
            for x in range(lt):
                p1 += " "
            boss1 = False
            for b in enemy:
                c1 = False
                for o in bosses:
                    if o in b:
                        c1 = True
                if c1: boss1 = True

            if boss1:
                scrollTxt(f"{p1}X== {red}BOSS BATTLE{white} ==X")


            scrollTxt("| " + purple + "Battle " + blue + "of the " + battle + white + " |")
            p2 = ""
            p3 = ""   
            lt = int(max(len(list("| " + "Battle " + "of the " + battle2 + " |")) - 24, 0)/2)
            for x in range(lt):
                p2 += " "
            lt = int(max(len(list("| " + "Battle " + "of the " + battle2 + " |")) - 27, 0)/2)
            for x in range(lt):
                p3 += " "
            if turn1:
                turn1 = False
                if dam_multiplier > 1:
                    scrollTxt(f"{p2}~{blue}You have the advantage{white}~")
                elif dam_multiplier < 1:
                    scrollTxt(f"{p3}~{yellow}You have the disadvantage{white}~")
                
            scrollTxt()

            

            if turn == 'player':
                if health > 0:
                    unhurt = []
                    def_buff_effect = {}
                    for ix in uhurt:
                        if ix[0] == "player":
                            try:
                                if def_buff_effect[ix[1]] >= effects_stack[ix[1]]:
                                    asdfg = True
                                else:
                                    asdfg = False
                                    def_buff_effect[ix[1]] += 1
                            except:
                                asdfg = False
                                def_buff_effect[ix[1]] = 1

                            if ix[2] > 1:
                                    unhurt.append([ix[0], ix[1], ix[2] - 1])

                            if asdfg is False:
                                if ix[1] == "bleed":
                                    scrollTxt(f"You {red}bleed{white} | -{red}1{white} health")
                                    health -= 1

                                if ix[1] == "burn":
                                    scrollTxt(f"You {orange}burn{white} | -{orange}2{white} health")
                                    health -= 2

                                if ix[1] == "poison":
                                    scrollTxt(f"You {green}fester{white} | -{red}1{white} health")
                                    health -= 1

                                if ix[1] == "force drain":
                                    scrollTxt(f"Your {red}life-force{white} is {darkgrey}drained{white} | -{red}1{white} max health")
                                    max_health -= 1

                                if ix[1] == "life steal":
                                    scrollTxt(f"Your {red}life force{white} is stolen | -{red}1{white} health | + {red}1{white} enemy health")
                                    health -= 1

                                    for enms in enemies:
                                        if "life steal" in enemies[enms]["elemental"]:
                                            enemies[enms]["health"] += 1

                                if ix[1] == "silence waves":
                                    scrollTxt(f"You {turquoise}silence{silver} effect{white} | -{red}3{white} ❤️, -{orange}1{white} str")
                                    effects_add(-1, 0, "damage bonus")
                                    health -= 3
                                
                                if ix[1] == "echo blast":
                                    scrollTxt(f"You {teal}echo{darkgrey} effect{white} | -{red}5{white} ❤️, -{orange}1{white} dex")
                                    effects_add(-1, 0, "dex bonus")
                                    health -= 5
                                
                                if ix[1] == "drain":
                                    scrollTxt(f"You {grey}weaken{white} | -{red}1{white} str")
                                    effects_add(-1, 0, "damage bonus")

                                if ix[1] == "freeze":
                                    scrollTxt(f"You {teal}freeze{white} | -{red}1{white} defense")
                                    effects_add(-1, 0, "defense bonus")

                                if ix[1] == "acid":
                                    scrollTxt(f"You {lime}acid{white}{orange} burn{white} | - {red}2{white} ❤️, -{red}1{white} defense")
                                    effects_add(-1, 0, "defense bonus")
                                    health -= 2
                                
                                if ix[1] == "confusion":
                                    scrollTxt(f"You are {yellow}confused{white} | -{red}1{white} dex")
                                    effects_add(-1, 0, "dex bonus")

                                if ix[1] == "shock" and random.randint(1, 3) == 1:
                                    scrollTxt(f"{yellow}SHOCK{white} | You drop your {darkgrey}weapon{white}")
                                    weapon = "none"

                                if ix[1] == "rust":
                                    if "rusty" not in weapon and weapon != "none":
                                        scrollTxt(f"{copper}RUST{white} | Your weapon {copper}rusts{white} over")
                                        inv.remove(weapon)
                                        wstats = weapons_all[weapon].copy()
                                        istats = items_all[weapon].copy()
                                        weapon = "rusty " + weapon
                                        inv.append(weapon)
                                        wstats["damage"] -= 1
                                        wstats["hit"] -= 1
                                        wstats["sweep"] -= 0.1
                                        istats["name"] = weapon
                                        istats["selling price"] = max(0, istats["selling price"] - 5)
                                        istats["description"] = istats["description"] + f"\nVery {copper}rusty{white} looks like the {blue}owner{white} negelcted it for many {darkgrey}years{white}"

                                        weapons_all[weapon] = wstats
                                        items_all[weapon] = istats

                    try:
                        if "damage bonus" not in effects_applied and effects["damage bonus"] < 1:
                            effects_applied.append("damage bonus")
                            if "damage bonus" in effects:
                                effects['damage bonus'][1] -= 1
                                metadam_bonus = effects['damage bonus'][0]
                        
                        if "hit bonus" not in effects_applied and effects["hit bonus"] < 1:
                            effects_applied.append("hit bonus")
                            if "hit bonus" in effects:
                                effects['hit bonus'][1] -= 1
                                metahi_bonus = effects['hit bonus'][0]

                        if "defense bonus" not in effects_applied and effects["defense bonus"] < 1:
                            
                            if "defense bonus" in effects:
                                effects_applied.append("defense bonus")
                                effects["defense bonus"][1] -= 1
                                metade_bonus = effects["defense bonus"][0]     
                    except:
                        pass

                    # input(effects)

                    uhurt = unhurt
                    scrollTxt(grey + "Your Health: " + red + str(health) + white)

                    scrollTxt()

                    if health <= 0:
                        scrollTxt(f"You have {red}DIED{white}")
                        print()
                        die()

                    if weapon in weapons_reload:

                        if "staff" in weapon or len(current_spells) != 0 :
                            scrollTxt(
                                f"|{red}Prep/Reload weapon{white}| |{blue}Use Item{white}| |{purple}Magic{white}|")

                            answer = get_input(['prep weapon', 'use item', 'magic'], True)
                        else:
                            scrollTxt(
                                f"|{red}Prep/Reload weapon{white}| |{blue}Use Item{white}|")

                            answer = get_input(['prep weapon', 'use item'], True)

                    else:
                        if "staff" in weapon or len(current_spells) != 0 :
                            scrollTxt(
                                f"|{red}Attack{white}| |{orange}Fast Attack {white}[{green}Auto Chooses{white}]| |{blue}Use Item{white}| |{purple}Magic{white}|")

                            answer = get_input(['attack', "fast attack", 'use item', 'magic'], True)
                        else:
                            scrollTxt(
                                f"|{red}Attack{white}| |{orange}Fast Attack {white}[{green}Auto Chooses{white}| |{blue}Use Item{white}|")

                            answer = get_input(['attack', 'fast attack', 'use item'], True)

                    damage_bonus = metadam_bonus
                    hit_bonus = metahi_bonus
                    def attack_or_fast(answer, damage_bonus, hit_bonus):
                     global effects, clrs_list, health, inv, weapon, offhand, dexterity, strength, max_health, gp, effects, special_moves, shield_moves, known_spells, current_spells, enemies_killed, exp, exp_max, lvl, fighter_class, crystals, weapons_reload
                     if answer == 'attack' or answer == "fast attack":
                        fast_a = False
                        if answer == "fast attack": fast_a = True

                        scrollTxt(f'You get ready to {copper}attack{white}...')

                        scrollTxt()

                        scrollTxt_enemies = ""
                        keys_of_e = []

                        for i in enemies:
                            scrollTxt_enemies = scrollTxt_enemies + f"|{lime}{i}{white}| "
                            keys_of_e.append(i)

                        if fast_a is False:
                            if len(keys_of_e) != 1:
                                scrollTxt(f"Would you like to make a {teal}sweep{white} attack? [{green}y/n{white}]")
                                answer = get_input(['yes', 'no'],
                                                    True)
                            else:
                                answer = "no"

                            scrollTxt("")

                            if answer == "yes":
                                sweep_attk = True
                            else:
                                sweep_attk = False

                                if len(enemies.keys()) != 1:

                                    scrollTxt("Who would you like to attack?")

                                    scrollTxt(scrollTxt_enemies)

                                    answer = get_input(keys_of_e, True)
                                    scrollTxt()

                                    target = enemies[answer]
                                    tname = answer
                                else:
                                    target = enemies[keys_of_e[0]]
                                    tname = keys_of_e[0]

                            handed = 1

                            try:
                                chock = weapons_all[weapon]['two handed']
                            except:
                                chock = False
                            if offhand == 'none' and chock is False:
                                scrollTxt(
                                    f"|{teal}One Handed Attack{white}| |{turquoise}Two Handed Attack{white}|"
                                )

                                answer = get_input(["one", 'two'], True)

                                if answer == "two":
                                    handed = 1.5

                                scrollTxt()

                            scrollTxt(
                                f"|{platinum}Dexterity Attack{white}| |{copper}Strength Attack{white}|"
                            )

                            answer = get_input(['dexterity attack', 'strength attack'],
                                                True)
                            scrollTxt()

                            try:
                                if answer == "dexterity attack":
                                    hit_bonus += min(dexterity, int(weapons_all[weapon]["hit"] * 3))
                                else:
                                    damage_bonus += min(strength, int(weapons_all[weapon]["damage"] * 0.75))
                            except:
                                if answer == "dexterity attack":
                                    hit_bonus += dexterity / 2
                                else:
                                    damage_bonus += strength / 3


                        else:
                            target = enemies[keys_of_e[0]]
                            tname = keys_of_e[0]
                            handed = 1
                            sweep_attk = False

                            if random.randint(1, 2) == 1:
                                hit_bonus += dexterity
                            else:
                                damage_bonus += strength

                        if True:
                            if weapon != 'none':
                                lklk = weapons_all[weapon]['hit']
                            else:
                                lklk = dexterity

                            if weapon != 'none':
                                ykyk = weapons_all[weapon]['damage']
                            else:
                                ykyk = strength * 0.7

                            nat_hit = random.randint(1, 20)

                            hit = min(int(
                                nat_hit + hit_bonus +
                                lklk - handed), 20)
                            

                            if fighter_class != "barbarian":
                                mmHit = hit
                            else:
                                mmHit = random.randint(15, 20)

                            try:
                                ccrit = weapons_all[weapon]["crit"]
                            except:
                                ccrit = 0
                            if nat_hit > 19 - ccrit:
                                mmHit = 20
                                hit = 20
                                damage = int(
                                    int(int((ykyk * 2) * (mmHit / 20) + damage_bonus) * handed) * dam_multiplier)

                            else:
                                damage = int(int(int((ykyk) * (mmHit / 20) + damage_bonus) * handed) * dam_multiplier)

                            level_hit = ""

                            if nat_hit >= 5:
                                level_hit = red + "Weak Hit" + white

                            else:
                                level_hit = paleyellow + "Miss" + white

                            if nat_hit >= 10:
                                level_hit = brown + "Solid Hit" + white

                            if nat_hit >= 15:
                                level_hit = blue + "Strong Hit" + white

                            try:
                                ccrit = weapons_all[weapon]["crit"]
                            except:
                                ccrit = 0
                            if nat_hit >= 20 - ccrit:
                                level_hit = gold + "CRITICAL STRIKE" + white
                                if weapon == "vorpal sword":
                                    level_hit = red + f"DREAD{darkgrey}STRIKE" + white
                                    damage = 100

                            if sweep_attk:
                                x6 = 10
                            else:
                                x6 = target['armor']

                            try:
                                if enemies_weapon_weakness[tname][0] in weapon:
                                    damage += enemies_weapon_weakness[tname][1]
                            except:
                                pass

                            if hit > x6:
                                

                                if sweep_attk == False:
                                    enemies[tname]['health'] -= damage

                                    if handed == 1.5:
                                        ifs = "s"
                                    else:
                                        ifs = ""

                                    if weapon != "none":
                                        neapon = weapon
                                    else:
                                        neapon = "fist" + ifs

                                    if "bow" in neapon: adv = f"fire an {darkgrey}arrow{white} with your"
                                    
                                    else: adv = "swing your"

                                    scrollTxt(
                                        f"You {adv} {darkgrey}{neapon}{white} at {copper}{tname}{white}"
                                    )

                                    try:
                                        if random.randint(1, weapons_all[weapon]['speed']) == 1:
                                            scrollTxt(
                                                f"Your {orange}speed{white} allows you to {blue}hit{white} the {red}enemy{white} again!")
                                            scrollTxt("")
                                            scrollTxt(level_hit +
                                                        f" | You dealt {red}{damage}{white} damage")

                                            level_hit = ""
                                            nat_hit = random.randint(1, 20)
                                            hit = min(int(nat_hit + hit_bonus + lklk - handed), 20)

                                            if nat_hit >= 5:
                                                level_hit = red + "Weak Hit" + white

                                            else:
                                                level_hit = paleyellow + "Miss" + white

                                            if nat_hit >= 10:
                                                level_hit = brown + "Solid Hit" + white

                                            if nat_hit >= 15:
                                                level_hit = blue + "Strong Hit" + white

                                            if nat_hit >= 20:
                                                level_hit = gold + "CRITICAL STRIKE" + white

                                            if fighter_class != "barbarian":
                                                mmHit = hit
                                            else:
                                                mmHit = random.randint(15, 20)
                                            if nat_hit > 19:
                                                mmHit = 20
                                                hit = 20
                                                damage = int((ykyk * 2) *
                                                                (mmHit / 20) + damage_bonus) * handed

                                            else:
                                                damage = int((ykyk) *
                                                                (mmHit / 20) + damage_bonus) * handed

                                            scrollTxt(level_hit +
                                                        f" | You dealt {red}{damage}{white} damage")
                                            scrollTxt("")
                                            enemies[tname]['health'] -= damage
                                        elif weapon in double_bladed_weapons:
                                            scrollTxt(
                                                f"Your {darkgrey}weapon{white} is {orange}double bladed{white} this allows you to {blue}hit{white} the {red}enemy{white} again!")
                                            scrollTxt("")
                                            scrollTxt(level_hit +
                                                        f" | You dealt {red}{damage}{white} damage")

                                            level_hit = ""
                                            nat_hit = random.randint(1, 20)
                                            hit = min(int(nat_hit + hit_bonus + lklk - handed), 20)

                                            if nat_hit >= 5:
                                                level_hit = red + "Weak Hit" + white

                                            else:
                                                level_hit = paleyellow + "Miss" + white

                                            if nat_hit >= 10:
                                                level_hit = brown + "Solid Hit" + white

                                            if nat_hit >= 15:
                                                level_hit = blue + "Strong Hit" + white

                                            if nat_hit >= 20:
                                                level_hit = gold + "CRITICAL STRIKE" + white

                                            if fighter_class != "barbarian":
                                                mmHit = hit
                                            else:
                                                mmHit = 20
                                            if nat_hit > 19:
                                                damage = int((ykyk * 2) *
                                                                (mmHit / 20) + damage_bonus) * handed

                                            else:
                                                damage = int((ykyk) *
                                                                (mmHit / 20) + damage_bonus) * handed

                                            scrollTxt(level_hit +
                                                        f" | You dealt {red}{damage}{white} damage")
                                            scrollTxt("")
                                            enemies[tname]['health'] -= damage
                                        else:
                                            scrollTxt(level_hit +
                                                        f" | You dealt {red}{damage}{white} damage")
                                    except:
                                        scrollTxt(level_hit +
                                                    f" | You dealt {red}{damage}{white} damage")
                                    try:
                                        if "damage to all" in weapons_all[weapon]:
                                            print()
                                            dta = weapons_all[weapon]["damage to all"]
                                            scrollTxt(f"You also deal {orange}{dta}{white} to all the {red}enemies{white}")
                                            
                                            for enen in enemies:
                                                if enen != tname:
                                                    enemies[enen]["health"] -= dta 
                                    except:
                                        pass
                                    try:
                                        if weapons_all[weapon]["special"] != False:
                                            print()
                                            
                                            try:
                                                eff = 0
                                                for ef in weapons_all[weapon]["special"]:
                                                    hurt.append([tname, ef, effects_length[ef]])
                                                    scrollTxt(weapons_all[weapon]["special text"][eff])
                                                    eff += 1

                                            except:
                                                hurt.append([tname, weapons_all[weapon]["special"], effects_length[weapons_all[weapon]["special"]]])
                                                scrollTxt(weapons_all[weapon]["special text"])
                                    except:
                                        pass

                                    try:
                                        if enemies_weapon_weakness[tname][0] in weapon:
                                            print()
                                            scrollTxt(f"You {red}attack{white} was {gold}super effective{white}")
                                    except:
                                        pass


                                else:

                                    for x5 in enemies:
                                        if weapon != 'none':
                                            hkhk = weapons_all[weapon]["sweep"]
                                        else:
                                            hkhk = 0.7

                                        enemies[x5]['health'] -= (int((damage * hkhk) / int(len(keys_of_e))))

                                    if handed == 1.5:
                                        ifs = "s"
                                    else:
                                        ifs = ""

                                    if weapon != "none":
                                        neapon = weapon
                                    else:
                                        neapon = "fist" + ifs

                                    if "bow" in neapon: adv = f"fire an {darkgrey}arrow{white} with your"
                                    else: adv = "swing your"

                                    scrollTxt(
                                        f"You {adv} {darkgrey}{neapon}{white} at {copper}every enemy{white}"
                                    )

                                    scrollTxt(level_hit +
                                                f" | You dealt {red}{(int((damage * hkhk) / int(len(keys_of_e))))}{white} damage to everyone")

                                    try:
                                        if weapons_all[weapon]["special"] != False:
                                            print()
                                            try:
                                                eff = 0
                                                for ef in weapons_all[weapon]["special"]:
                                                    for x4 in enemies:
                                                        hurt.append([x4, ef, effects_length[ef]])
                                                    scrollTxt(weapons_all[weapon]["special text"][eff])
                                                    eff += 1
                                            except:
                                                for x4 in enemies:
                                                    hurt.append([x4, weapons_all[weapon]["special"], effects_length[weapons_all[weapon]["special"]]])
                                                scrollTxt(weapons_all[weapon]["special text"])
                                    except:
                                        pass

                                try:
                                    ca = cursed_weapons[weapon]
                                    health -= ca
                                    if "explosive" not in weapon:

                                        scrollTxt(f"- {darkgrey}{ca}{white} 🖤 [{purple}CURSED{white}]")
                                    else:
                                        scrollTxt(f"- {red}{ca}{white} ❤️ [{orange}EXPLOSIVE{white}]")

                                    if health < 1:
                                        print()
                                        scrollTxt(f"Your {purple}{weapon}{white} {red}killed{white} you")
                                        die()

                                except:
                                    pass

                                try:
                                    if health > max_health:
                                        max_healthS = health
                                    else:
                                        max_healthS = max_health
                                    ca = blessed_weapons[weapon]
                                    health += ca
                                    scrollTxt(f"+ {blue}{ca}{white} 💙 [{turquoise}BLESSED{white}]")
                                    
                                    if health > max_healthS:
                                        health = max_healthS

                                except:
                                    pass

                                if weapon in steal_weapons:
                                    print()
                                    try:
                                        op = enemies[tname]["gold"]
                                        scrollTxt(f"You steal {gold}{int((op)/steal_weapons[weapon])}{white} gp from {copper}{tname}{white}")
                                        gp += int((op)/steal_weapons[weapon])
                                    except:
                                        tname = random.choice(list(enemies.keys()))
                                        op = enemies[tname]["gold"]
                                        scrollTxt(f"You steal {gold}{int((op)/steal_weapons[weapon])}{white} gp from {copper}{tname}{white}")
                                        gp += int((op)/steal_weapons[weapon])

                                        
                                try:
                                        durability_weapon[weapon] -= 1

                                        if durability_weapon[weapon] < 1:
                                            durability_weapon.pop(weapon)
                                            if "magic" in weapon: print(f"Your {blue}weapon{white} fades into {platinum}mist{white}")
                                            else: print(f"Your {darkgrey}weapon{white} broke!")
                                            inv.remove(weapon)
                                            if weapon in offhand_weapons:
                                                offhand = "none"  
                                            else:
                                                weapon = "none"
                                            

                                            

                                except:
                                    try:
                                        durability_weapon[weapon] = weapons_all[weapon]['durability'] - 1
                                    except:
                                        pass

                                try:
                                    if weapons_all[weapon]['reload'] > 0: weapons_reload[weapon] = weapons_all[weapon]["reload"]
                                except:
                                    pass

                                

                                enter()
                            else:
                                if handed == 1.5:
                                        ifs = "s"
                                else:
                                        ifs = ""
                                if weapon != "none":
                                    neapon = weapon
                                else:
                                    neapon = "fist" + ifs
                                if "bow" in neapon: adv = f"fire an {darkgrey}arrow{white} with your"
                                else: adv = "swing your"
                                scrollTxt(
                                    level_hit +
                                    f" | You {adv} {darkgrey}{neapon}{white} but {red}miss{white}"
                                )

                                enter()

                    attack_or_fast(answer, damage_bonus, hit_bonus)

                    if answer == "prep weapon":
                        print()
                        if "bow" in weapon: 
                            rm = "reload"
                            ra = "ed"
                        else: 
                            rm = "prepare"
                            ra = "d"
                        
                        scrollTxt(f"You {orange}{rm}{white} your {darkgrey}{weapon}{white} for {blue}use{white}")

                        weapons_reload[weapon] -= 1
                        if weapons_reload[weapon] <= 0:
                            weapons_reload.pop(weapon)
                            scrollTxt(f"Your {darkgrey}{weapon}{white} is fully {turquoise}{rm}{ra}{white}!")
                        else:
                            scrollTxt(f"Your {darkgrey}{weapon}{white} still needs to be {turquoise}{rm}{ra}{white} for {red}{weapons_reload[weapon]}{white} more turns")

                        enter()

                    if answer == 'magic':

                        scrollTxt(f'You get ready to use a {teal}spell{white}...')

                        scrollTxt()

                        scrollTxt_enemies = ""
                        keys_of_e = []

                        for i in enemies:
                            scrollTxt_enemies = scrollTxt_enemies + f"|{lime}{i}{white}| "
                            keys_of_e.append(i)

                        if len(enemies.keys()) != 1:

                            scrollTxt("Who would you like to attack?")

                            scrollTxt(scrollTxt_enemies)

                            answer = get_input(keys_of_e, True)
                            scrollTxt()

                            target = enemies[answer]
                            tname = answer
                        else:
                            target = enemies[keys_of_e[0]]
                            tname = keys_of_e[0]

                        handed = 1

                        if 'staff' in weapon:
                            scrollTxt(
                                f"|{platinum}basic{white}|", end="", flush=True
                            )

                        for x1 in current_spells:
                            scrollTxt(f" |{platinum}{x1}{white}|", end="", flush=True)

                        print()

                        ccurrent_spells = current_spells.copy()
                        if "staff" in weapon:
                            ccurrent_spells.append("basic")

                        answer = get_input(ccurrent_spells,
                                            True)
                        scrollTxt()

                        chosen_spell = answer

                        if "staff" in weapon:
                            hit_bonus += staffs_all[weapon]["hit bonus"]
                            damage_bonus += staffs_all[weapon]["damage bonus"]

                        crit = False

                        if True:
                            multi_dam = False
                            if chosen_spell == "basic":

                                hit = min(int(random.randint(staffs_all[weapon]['hit'], 20) - handed), 20)

                                if hit > 19:
                                    damage = int(
                                        (staffs_all[weapon]['damage'] * 2) * (hit / 15)) * handed

                                else:
                                    damage = int(staffs_all[weapon]['damage'] * (hit / 15)) * handed
                                    crit = True

                                mtxt = staffs_all[weapon]["norm text"]

                                if staffs_all[weapon]['multi']: multi_dam = True

                            elif "hyper" not in weapon:
                                current_spells.remove(chosen_spell)

                            if chosen_spell == "magic missile":
                                hit = min(int(
                                    ((random.randint(5, 20) - 0) + hit_bonus) - handed), 20)

                                if hit > 19:
                                    damage = int((3 * 2) *
                                                    (hit / 15) + damage_bonus) * handed

                                else:
                                    damage = int((3) *
                                                    (hit / 15) + damage_bonus) * handed
                                    crit = True

                                mtxt = spells_all[chosen_spell]
                                multi_dam = True

                            if chosen_spell == "dark chromatic orb":
                                hit = min(int(
                                    random.randint(5, 20) + hit_bonus - handed), 20)

                                if hit > 19:
                                    damage = int((6 * 2) *
                                                    (hit / 15) + damage_bonus) * handed

                                else:
                                    damage = int((6) *
                                                    (hit / 15) + damage_bonus) * handed
                                    crit = True

                                mtxt = spells_all[chosen_spell]
                                multi_dam = False

                                hurt.append([tname, "life steal", 5])

                            if chosen_spell == "dark arrows":
                                hit = min(int(
                                    random.randint(5, 20) + hit_bonus - handed), 20)

                                if hit > 19:
                                    damage = int((8 * 2) *
                                                    (hit / 15) + damage_bonus) * handed

                                else:
                                    damage = int((8) *
                                                    (hit / 15) + damage_bonus) * handed
                                    crit = True

                                mtxt = spells_all[chosen_spell]
                                multi_dam = True

                                for pl in enemies:
                                    hurt.append([pl, "drain", 5])
                            
                            if chosen_spell == "ice shards":
                                hit = min(int(
                                    ((random.randint(1, 20) - 1) + hit_bonus) - handed), 20)

                                if hit > 19:
                                    damage = int((4 * 2) *
                                                    (hit / 15) + damage_bonus) * handed

                                else:
                                    damage = int((4) *
                                                    (hit / 15) + damage_bonus) * handed
                                    crit = True

                                mtxt = spells_all[chosen_spell]
                                multi_dam = True

                                for x779 in enemies:
                                    hurt.append([x779, "freeze", 2])

                            if chosen_spell == "firebolt":
                                hit = min(int(
                                    ((random.randint(1, 20) - 1) + hit_bonus) - handed), 20)

                                if hit > 19:
                                    damage = int((9 * 2) *
                                                    (hit / 15) + damage_bonus) * handed

                                else:
                                    damage = int((9) *
                                                    (hit / 15) + damage_bonus) * handed
                                    crit = True

                                mtxt = spells_all[chosen_spell]
                                hurt.append([tname, "burn", 1])
                            if chosen_spell == "tornado burst":
                                hit = min(int(
                                    ((random.randint(1, 20) - 1) + hit_bonus) - handed), 20)

                                if hit > 19:
                                    damage = int((20 * 2) *
                                                    (hit / 15) + damage_bonus) * handed

                                else:
                                    damage = int((20) *
                                                    (hit / 15) + damage_bonus) * handed
                                    crit = True

                                mtxt = spells_all[chosen_spell]
                                hurt.append([tname, "crunch", 3])

                            if chosen_spell == "shadow spear":
                                hit = min(int(
                                    ((random.randint(1, 20) - 1) + hit_bonus) - handed), 20)

                                if hit > 19:
                                    damage = int((12 * 2) *
                                                    (hit / 15) + damage_bonus) * handed

                                else:
                                    damage = int((12) *
                                                    (hit / 15) + damage_bonus) * handed
                                    crit = True

                                mtxt = spells_all[chosen_spell]
                                hurt.append([tname, "drain", 4])

                            if chosen_spell == "dagger swarm":
                                hit = min(int(
                                    random.randint(2, 20) + hit_bonus - handed), 20)

                                if hit > 19:
                                    damage = int((5 * 2) *
                                                    (hit / 15) + damage_bonus) * handed

                                else:
                                    damage = int((5) *
                                                    (hit / 15) + damage_bonus) * handed
                                    crit = True

                                mtxt = spells_all[chosen_spell]
                                hurt.append([tname, "bleed", 5])

                            if chosen_spell == "blurr mind":
                                hit = min(int(random.randint(7, 20) + hit_bonus - handed), 20)

                                if hit > 19:
                                    damage = int((2 * 2) *
                                                    (hit / 15) + damage_bonus) * handed

                                else:
                                    damage = int((2) *
                                                    (hit / 15) + damage_bonus) * handed
                                    crit = True

                                mtxt = spells_all[chosen_spell]
                            try:
                                if hit < 1:
                                    hit = 1
                                    #input("T-T")
                            except:
                                pass
                            if chosen_spell in ["shield of the magi", "aura of weakening", "poison nova", "hyper heal"]:
                                hit = False
                                damage = 0
                                mtxt = spells_all[chosen_spell]
                                #input("CHECK")

                            level_hit = ""

                            if hit != False:

                                if hit >= 5:
                                    level_hit = red + "Weak Hit" + white

                                else:
                                    level_hit = paleyellow + "Miss" + white

                                if hit >= 10:
                                    level_hit = brown + "Solid Hit" + white

                                if hit >= 15:
                                    level_hit = blue + "Strong Hit" + white

                                if hit >= 20:
                                    level_hit = gold + "CRITICAL STRIKE" + white

                            checkHIT = False

                            try:
                                if hit >= target['armor']: checkHIT = True
                            except:
                                pass

                            if hit == False: checkHIT = True

                            if checkHIT:
                                if multi_dam == False:
                                    enemies[tname]['health'] -= damage

                                    scrollTxt(
                                        f"{mtxt}"
                                    )
                                    #input(hit)
                                    if hit != False:
                                        #input("CHECK SDF")
                                        scrollTxt(level_hit +
                                                    f" | You dealt {red}{damage}{white} damage")

                                    if chosen_spell == "blurr mind":
                                        scrollTxt(
                                            f"You {red}opponent{white} wobbles around, {yellow}dazed{white}, their mind {grey}blurred{white}")
                                        enemies[tname]["dex"] -= 2

                                    if chosen_spell == "aura of weakening":
                                        scrollTxt(
                                            f"You {red}opponents{white} staggers their body {darkgrey}withered{white} and {paleyellow}weak{white}")
                                        for x in enemies:
                                            hurt.append([x, "drain", 3])
                                        enemies[tname]["str"] -= 1
                                        

                                    if chosen_spell == "poison nova":
                                        scrollTxt(f"Your {red}oppenents{white} all are {green}poisoned{white}.")
                                        for x in enemies:
                                            hurt.append([x, "poison", 10])

                                    if chosen_spell == "hyper heal":
                                        scrollTxt(f"You healed to {red}max health{white} (+ {blue}{max_health - health}{white} 💙)")
                                        health = max_health

                                    if chosen_spell == "shield of the magi":
                                        blocking.append(["shield of the magi", 7 , 3])
                                    enter()

                                else:
                                    #input(
                                        # "CHECK MULTI"
                                    #)
                                    for x99 in enemies:
                                        enemies[x99]['health'] -= damage

                                    scrollTxt(
                                        f"{mtxt}"
                                    )
                                    if hit != False:
                                        scrollTxt(level_hit +
                                                    f" | You dealt {red}{damage}{white} damage to everyone")

                                    enter()

                            else:
                                scrollTxt(
                                    level_hit +
                                    f" | Your {purple}spell{white} {red}missed{white}"
                                )
                                if chosen_spell != "basic":
                                    current_spells.append(chosen_spell)

                                enter()

                    if answer == "use item":
                        inventory()
                        try:
                            if "damage bonus" not in effects_applied and effects["damage bonus"] < 1:
                                effects_applied.append("damage bonus")
                                if "damage bonus" in effects:
                                    effects['damage bonus'][1] -= 1
                                    metadam_bonus = effects['damage bonus'][0]
                            
                            if "hit bonus" not in effects_applied and effects["hit bonus"] < 1:
                                effects_applied.append("hit bonus")
                                if "hit bonus" in effects:
                                    effects['hit bonus'][1] -= 1
                                    metahi_bonus = effects['hit bonus'][0]

                            if "defense bonus" not in effects_applied and effects["defense bonus"] < 1:
                                
                                if "defense bonus" in effects:
                                    effects_applied.append("defense bonus")
                                    effects["defense bonus"][1] -= 1
                                    metade_bonus = effects["defense bonus"][0] 
                        except:
                            pass  
                    scrollTxt()

                    reactions = []
                    ranswer = []

                    scrollTxt(orange + "REACTION TURN" + white)
                    scrollTxt()

                    if offhand != "none":
                        if offhand not in offhand_weapons:
                            reactions = shield_moves
                        else:
                            reactions = offhand_moves
                    else:
                        reactions = special_moves

                    for i in reactions:
                        if i != "prep weapon" or i == "prep weapon" and weapon in weapons_reload:
                            scrollTxt(f"|{grey}{i}{white}|", end=" ", flush=True)

                            ranswer.append(i)
                    scrollTxt()

                    answer = get_input(ranswer, True)
                    scrollTxt()

                    if answer == 'block':
                        blocking.append([offhand, shield_all[offhand]["block"], 1])
                        scrollTxt(f"You raise your {copper}{offhand}{white} and get ready to block")

                    if answer == "prep weapon":
                        print()
                        if "bow" in weapon: 
                            rm = "reload"
                            ra = "ed"
                        else: 
                            rm = "prepare"
                            ra = "d"
                        
                        scrollTxt(f"You {orange}{rm}{white} your {darkgrey}{weapon}{white} for {blue}use{white}")

                        weapons_reload[weapon] -= 1
                        if weapons_reload[weapon] <= 0:
                            weapons_reload.pop(weapon)
                            scrollTxt(f"Your {darkgrey}{weapon}{white} is fully {turquoise}{rm}{ra}{white}!")
                        else:
                            scrollTxt(f"Your {darkgrey}{weapon}{white} still needs to be {turquoise}{rm}{ra}{white} for {red}{weapons_reload[weapon]}{white} more turns")

                    if answer == "use item":
                        inventory()
                        try:
                            if "damage bonus" not in effects_applied and effects["damage bonus"] < 1:
                                effects_applied.append("damage bonus")
                                if "damage bonus" in effects:
                                    effects['damage bonus'][1] -= 1
                                    metadam_bonus = effects['damage bonus'][0]
                            
                            if "hit bonus" not in effects_applied and effects["hit bonus"] < 1:
                                effects_applied.append("hit bonus")
                                if "hit bonus" in effects:
                                    effects['hit bonus'][1] -= 1
                                    metahi_bonus = effects['hit bonus'][0]

                            if "defense bonus" not in effects_applied and effects["defense bonus"] < 1:
                                
                                if "defense bonus" in effects:
                                    effects_applied.append("defense bonus")
                                    effects["defense bonus"][1] -= 1
                                    metade_bonus = effects["defense bonus"][0] 
                        except:
                            pass 

                    if answer == "shield bash":
                        scrollTxt_enemies = ""

                        keys_of_e = []

                        for i in enemies:
                            keys_of_e.append(i)

                        for i in enemies:
                            scrollTxt_enemies = scrollTxt_enemies + f"|{lime}{i}{white}| "

                        if len(enemies.keys()) != 1:

                            scrollTxt("Who would you like to attack?")

                            scrollTxt(scrollTxt_enemies)

                            answer = get_input(keys_of_e, True)
                            scrollTxt()

                            target = enemies[answer]
                            tname = answer
                        else:
                            target = enemies[keys_of_e[0]]
                            tname = keys_of_e[0]

                        if "kinetic shield" not in offhand:
                            scrollTxt(f"You bash your {copper}{offhand}{white} against {green}{tname}{white}")
                            dam = shield_all[offhand]["damage"]
                            scrollTxt(f"You deal {red}{dam}{white} damage")
                        else:
                            scrollTxt(f"You blast out {purple}purple energy{white} out of your {darkgrey}{offhand}{white} against {green}{tname}{white}")
                            power = ""

                            startc = False
                            for char in offhand:
                                if char == "[":
                                                            startc = True
                                elif char == "]":
                                                            startc = False
                                elif startc is True:
                                                            power += char

                            dam = shield_all[offhand]["damage"] + int(power)
                            scrollTxt(f"You deal {red}{dam}{white} damage")

                            inv.remove(offhand)
                            offhand = "kinetic shield [0]"
                            
                            inv.append("kinetic shield [0]")

                        enemies[tname]["health"] -= shield_all[offhand]["damage"]

                    if answer == "dodge":
                        if fighter_class == "thief":
                            blocking.append(["dodge", 1.5 + min(math.ceil(dexterity/3), 3), 1])
                        else:
                            blocking.append(["dodge", 1.5 + min(math.ceil(dexterity/3), 3), 1])

                        scrollTxt(f"You get ready to {teal}dodge{white}")

                    if answer == "heal wounds":
                        hw = random.randint(1, 3)
                        scrollTxt(f"You healed {red}{hw}{white} health")

                        health = min(health + hw, max_health)

                    if answer == 'winded dodge':
                        scrollTxt(f"You get ready to {teal}dodge{white}, your body becomes like {grey}wind{white} 💨")
                        scrollTxt(f"+ {green}1{white} Accuracy")

                        blocking.append(["dodge", min(dexterity, 6), 1])

                        metahi_bonus += 1

                    if answer == 'ocean calm':
                        scrollTxt(
                            f"You take in a deep {silver}breath{white}. You feel the {turquoise}ocean calm{white} 🌊.")

                        scrollTxt(f"+ {green}1{white} Accuracy")
                        scrollTxt(f"+ {red}1{white} Damage")

                        metadam_bonus += 1
                        metahi_bonus += 1

                    if answer == "steal gold":
                        scrollTxt_enemies = ""

                        keys_of_e = []

                        for i in enemies:
                            keys_of_e.append(i)

                        for i in enemies:
                            scrollTxt_enemies = scrollTxt_enemies + f"|{lime}{i}{white}| "

                        if len(enemies.keys()) != 1:

                            scrollTxt("Who would you like to steal from?")

                            scrollTxt(scrollTxt_enemies)

                            answer = get_input(keys_of_e, True)
                            scrollTxt()

                            target = enemies[answer]
                            tname = answer
                        else:
                            target = enemies[keys_of_e[0]]
                            tname = keys_of_e[0]

                        print(f"You swipe some {gold}GP{white} from {tname}")
                        get_gold = int(target["gold"] / 3)
                        print(f"+ {gold}{get_gold}{white} GP")
                        gp += get_gold

                    if answer == "rage":
                        print(f"You {red}rage{white} and grow {orange}STRONGER{white}!")
                        print(f"+{teal}3{white} Damage, -{red}1{white} Dex")
                        metadam_bonus += 3
                        metahi_bonus -= 1

                    if answer == "lucky dance":
                        print(f"You do a little {blue}dance{white} and sing a {gold}lucky song{white}")
                        print(f"+{gold}2{white} Luck")
                        luck_amount += 2
                        
                    if answer == "jellify":
                        print(f"You {purple}cast{white} a simple {blue}jellify{white} spell")
                        scrollTxt_enemies = ""

                        keys_of_e = []

                        for i in enemies:
                            keys_of_e.append(i)

                        for i in enemies:
                            scrollTxt_enemies = scrollTxt_enemies + f"|{lime}{i}{white}| "

                        if len(enemies.keys()) != 1:

                            scrollTxt("Who would you like to jellify?")

                            scrollTxt(scrollTxt_enemies)

                            answer = get_input(keys_of_e, True)
                            scrollTxt()

                            target = enemies[answer]
                            tname = answer
                        else:
                            target = enemies[keys_of_e[0]]
                            tname = keys_of_e[0]

                        try:

                            enemies[tname]["dex"] -= 2
                        except:
                            ndex = []
                            for o in enemies[tname]['dex']:
                                ndex.append(o - 2)

                            enemies[tname]["dex"] = ndex
                        print(f"{copper}{tname}{white} dex {red}-2{white}")
                        print(f"{copper}{tname}{white} dex: {blue}{target['dex']}{white}")

                    if answer == "inflict":
                        scrollTxt_enemies = ""

                        keys_of_e = []

                        for i in enemies:
                            keys_of_e.append(i)

                        for i in enemies:
                            scrollTxt_enemies = scrollTxt_enemies + f"|{lime}{i}{white}| "

                        if len(enemies.keys()) != 1:

                            scrollTxt(f"Who would you like to {red}inflict{white}?")

                            scrollTxt(scrollTxt_enemies)

                            answer = get_input(keys_of_e, True)
                            scrollTxt()

                            target = enemies[answer]
                            tname = answer
                        else:
                            target = enemies[keys_of_e[0]]
                            tname = keys_of_e[0]

                        scrollTxt(f"You inflicted {red}BLEED{white} on {copper}{tname}{white}")
                        hurt.append([tname, "bleed", 2])
                        hurt.append([tname, "bleed", 2])
                        hurt.append([tname, "bleed", 2])

                    if answer == "cursed drain":
                        scrollTxt_enemies = ""

                        keys_of_e = []

                        for i in enemies:
                            keys_of_e.append(i)

                        for i in enemies:
                            scrollTxt_enemies = scrollTxt_enemies + f"|{lime}{i}{white}| "

                        if len(enemies.keys()) != 1:

                            scrollTxt(f"Who would you like to {red}curse{white}?")

                            scrollTxt(scrollTxt_enemies)

                            answer = get_input(keys_of_e, True)
                            scrollTxt()

                            target = enemies[answer]
                            tname = answer
                        else:
                            target = enemies[keys_of_e[0]]
                            tname = keys_of_e[0]

                        scrollTxt(f"You inflict {purple}DRA{darkgrey}IN{white} on {copper}{tname}{white}")
                        hurt.append([tname, "drain", 2])
                        hurt.append([tname, "drain", 2])
                        hurt.append([tname, "drain", 2])

                    if answer == "exp drain":
                        scrollTxt_enemies = ""

                        keys_of_e = []

                        for i in enemies:
                            keys_of_e.append(i)

                        for i in enemies:
                            scrollTxt_enemies = scrollTxt_enemies + f"|{lime}{i}{white}| "

                        if len(enemies.keys()) != 1:

                            scrollTxt(f"Who would you like to {turquoise}drain{white}?")

                            scrollTxt(scrollTxt_enemies)

                            answer = get_input(keys_of_e, True)
                            scrollTxt()

                            target = enemies[answer]
                            tname = answer
                        else:
                            target = enemies[keys_of_e[0]]
                            tname = keys_of_e[0]

                        xp_gain_am = int(enemies[tname]["exp"] / 3)
                        scrollTxt(f"You steal {turquoise}{xp_gain_am}{white} XP from {copper}{tname}{white}.")
                        exp += xp_gain_am
                        if exp >= exp_max:
                            print()
                            scrollTxt("_____________________")
                            scrollTxt("|                   |")
                            scrollTxt(f"| You {blue}LEVELED UP!{white}   |")
                            scrollTxt(f"| + {red}5{white} Max HP        |")
                            scrollTxt(f"| + {turquoise}Level Crystal{white} 🔷|")
                            scrollTxt("|___________________|")

                            lvl += 1
                            crystals += 1
                            max_health += 5

                            exp -= exp_max
                            exp_max = int(exp_max * 1.5)
                            scrollTxt()

                    real_weapon = weapon
                    weapon = offhand
                    attack_or_fast(answer, damage_bonus, hit_bonus)
                    weapon = real_weapon
                    
                    if answer != 'attack' and answer != "fast attack" and answer != "use item": enter()

                    turn = "enemies"
                else:
                    if "totem of undying" not in inv:
                        die()
                    else:
                        scrollTxt(f"You {red}died{white} but your {gold}totem of undying{white} saves you!")
                        print()
                        scrollTxt(f"- {darkgrey}totem of undying{white}")
                        health = max_health
                        inv.remove("totem of undying")
                        enter()

            if turn == 'enemies':
                removeE = []
                adddE = {}
                for i in enemies:
                    clear()
                    scrollTxt("| " + purple + "Battle " + blue + "of the " + battle + white + " |")
                    scrollTxt()
                    scrollTxt(f"{copper}{i}{white}s Turn")
                    ehealth = enemies[i]["health"]
                    
                    removeEFCT = []
                    nhurt = []
                    def_buff_effect = {}
                    for ix in hurt:
                        if ix[0] == i:
                            try:
                                if def_buff_effect[ix[1]] >= effects_stack[ix[1]]:
                                    asdfg = True
                                else:
                                    asdfg = False
                                    def_buff_effect[ix[1]] += 1
                            except:
                                asdfg = False
                                def_buff_effect[ix[1]] = 1

                            if ix[2] > 1:
                                nhurt.append([ix[0], ix[1], ix[2] - 1])
                            
                            if asdfg == False:

                                if ix[1] == "bleed":
                                    scrollTxt(f"{red}Bleed{white} Effect| -{red}1{white} health")
                                    ehealth -= 1
                                    enemies[i]["health"] -= 1
                                
                                if ix[1] == "hyper bleed":
                                    scrollTxt(f"{ironc}Hyper{red} Bleed{white} Effect| -{red}2{white} health")
                                    ehealth -= 2
                                    enemies[i]["health"] -= 2

                                if ix[1] == "burn":
                                    scrollTxt(f"{orange}Burn{white} Effect | -{orange}2{white} health")
                                    ehealth -= 2
                                    enemies[i]["health"] -= 2

                                if ix[1] == "dragon burn":
                                    scrollTxt(f"{orange}Dragon Burn{white} Effect | -{orange}4{white} health")
                                    ehealth -= 4
                                    enemies[i]["health"] -= 4

                                if ix[1] == "poison":
                                    scrollTxt(f"{green}Fester{white} Effect | -{red}1{white} health")
                                    ehealth -= 1
                                    enemies[i]["health"] -= 1

                                if ix[1] == "life steal":
                                    if health > max_health:
                                        max_healthS = health
                                    else:
                                        max_healthS = max_health
                                    scrollTxt(f"{purple}Life {darkgrey}steal{white} Effect | Enemy: -{red}1{white} 🖤 | You: + {red}1{white} 💙")
                                    ehealth -= 1
                                    enemies[i]["health"] -= 1
                                    health += 1
                                    if health > max_healthS:
                                        health = max_healthS

                                if ix[1] == "drain":
                                    scrollTxt(f"{grey}Weaken{white} Effect | -{red}1{white} str")
                                    try:
                                        enemies[i]["str"] -= 1
                                    except:
                                        ndex = []
                                        for o in enemies[i]['str']:
                                            ndex.append(o - 1)

                                        enemies[i]["str"] = ndex

                                if ix[1] == "freeze":
                                    scrollTxt(f"{teal}Freeze{white} Effect | -{red}1{white} dex")
                                    try:

                                        enemies[i]["dex"] -= 1
                                    except:
                                        ndex = []
                                        for o in enemies[i]['dex']:
                                            ndex.append(o - 1)

                                        enemies[i]["dex"] = ndex

                                if ix[1] == "hyper freeze":
                                    scrollTxt(f"{turquoise}Hyper Freeze{white} Effect | -{red}2{white} dex")
                                    try:

                                        enemies[i]["dex"] -= 2
                                    except:
                                        ndex = []
                                        for o in enemies[i]['dex']:
                                            ndex.append(o - 2)

                                        enemies[i]["dex"] = ndex

                                if ix[1] == "crunch":
                                    scrollTxt(f"{orange}Crunch{white} Effect | -{red}1{white} Defense")
                                    enemies[i]["armor"] -= 1

                                if ix[1] == "dirtify":
                                    scrollTxt(f"{brown}Dirt{white} Effect | -{red}2{white} Defense")
                                    enemies[i]["armor"] -= 2

                                if ix[1] == "acid":
                                    scrollTxt(f"{lime}Acid{white} Effect | -2 ❤️, -{red}1{white} Defense")
                                    enemies[i]["armor"] -= 1
                                    ehealth -= 2
                                    enemies[i]["health"] -= 2

                                if ix[1] == "lightning":
                                    scrollTxt(f"{yellow}LIGHTNING{white} Effect | -{red}1{white} defense : -{red}1{white} damage : -{green}1{white} accuracy")
                                    enemies[i]["armor"] -= 1
                                    try:

                                            enemies[i]["dex"] -= 1
                                    except:
                                            ndex = []
                                            for o in enemies[i]['dex']:
                                                ndex.append(o - 1)

                                            enemies[i]["dex"] = ndex
                                    try:
                                            enemies[i]["str"] -= 1
                                    except:
                                            ndex = []
                                            for o in enemies[i]['str']:
                                                ndex.append(o - 1)

                                            enemies[i]["str"] = ndex

                                if ix[1] == "shock" and enemies[i]["damage"] != 0:
                                    if i not in bosses:
                                        if random.randint(1, 3) == 4:
                                            scrollTxt(f"{yellow}SHOCK{white} | Dropped {darkgrey}Weapon{white}")
                                            if i not in multimove:

                                                enemies[i]["damage"] = 0
                                                enemies[i]["attack"] = f"The {copper}{i}{white} punches you!"
                                            else:
                                                len_attacks = 0
                                                for ting in enemies[i]["damage"]:
                                                    len_attacks += 1
                                                new_damage_m = []
                                                new_attack_m =[]
                                                for x0x in range(1, len_attacks):
                                                    new_damage_m.append(0)
                                                for x0x in range(1, len_attacks):
                                                    new_attack_m.append(f"The {copper}{i}{white} punches you!")
                                                enemies[i]["damage"] = new_damage_m
                                                enemies[i]["attack"] = new_attack_m

                                        else:
                                            scrollTxt(f"{yellow}SHOCK{white} | Nothing happened")
                                    else:
                                        scrollTxt(f"{yellow}SHOCK{white} | -{red}1{white} damage : -{green}1{white} accuracy")
                                        try:

                                            enemies[i]["dex"] -= 1
                                        except:
                                            ndex = []
                                            for o in enemies[i]['dex']:
                                                ndex.append(o - 1)

                                            enemies[i]["dex"] = ndex
                                        try:
                                            enemies[i]["str"] -= 1
                                        except:
                                            ndex = []
                                            for o in enemies[i]['str']:
                                                ndex.append(o - 1)

                                            enemies[i]["str"] = ndex

                        else:
                            nhurt.append(ix)
                                    
                    hurt = nhurt

        

                    scrollTxt(f"{copper}{i}{white} {grey}Health{white}: {red}{ehealth}{white}")
                    scrollTxt()

                    if ehealth > 0:
                        check_multi = False
                        for p in multimove:
                            if p in i:
                                check_multi = True

                        if check_multi:
                            

                            attack = random.randint(0, len(enemies[i]['attack']) - 1)
                            ehit = random.randint(1, 20) + enemies[i]['dex'][attack]

                            #input(blocking)
                            for x7 in blocking:
                                if x7[0] == 'dodge':
                                    ehit -= x7[1]
                                    x7[1] -= random.randint(0, 1)
                            #input(blocking)
                            try:
                                edamage = int(enemies[i]['damage'][attack] + enemies[i]['str'] * (ehit / 20))
                            except:
                                edamage = 0

                            level_hit = ""

                            if ehit >= 5:
                                level_hit = red + "Weak Hit" + white

                            else:
                                level_hit = paleyellow + "Miss" + white

                            if ehit >= 10:
                                level_hit = brown + "Solid Hit" + white

                            if ehit >= 15:
                                level_hit = blue + "Strong Hit" + white

                            if ehit >= 20:
                                level_hit = gold + "CRITICAL STRIKE" + white

                            if enemies[i]['damage'][attack] == "heal":
                                scrollTxt("{}".format(enemies[i]["attack"][attack]))
                                hpl = random.randint(max(int(enemies_all[i]['health'] / 15), 2), max(int(enemies_all[i]['health'] / 3), 3))
                                scrollTxt(f"{copper}{i}{white} heals {red}{hpl}{white} HP")
                                enemies[i]['health'] += hpl
                            elif enemies[i]['damage'][attack] == "dam buff":
                                scrollTxt("{}".format(enemies[i]["attack"][attack]))
                                enemies[i]["str"] += int(enemies[i]["str"] / 1.5)
                                rand_var = int(enemies[i]["str"] / 1.5)
                                scrollTxt(f"{copper}{i}{white} gets {red}{rand_var}{white} STRONGER")
                            elif enemies[i]['damage'][attack] == "steal":
                                scrollTxt("{}".format(enemies[i]["attack"][attack]))
                                gpl = min(random.randint(int((enemies[i]["exp"]/10)), int((enemies[i]["exp"]/10) + 5)), gp)
                                scrollTxt(f"{copper}{i}{white} steals {red}{gpl}{white} GP")
                                gp -= gpl
                            elif enemies[i]["damage"][attack] == "summon":
                                scrollTxt("{}".format(enemies[i]["attack"][attack]))
                                adddE[enemies[i]["elemental"][attack] + str(len(enemies))] = enemies_all[enemies[i]["elemental"][attack]]
                            


                            else:
                                if offhand != "none":

                                    try:
                                        guardshield = shield_all[offhand]["guard"]
                                        if i in enemies_shield_weakness.keys():
                                            if enemies_shield_weakness[i] in offhand: 
                                                guardshield *= 2
                                                

                                    except:
                                        guardshield = min(dexterity + strength, 9)

                                    if ehit > guardshield + metade_bonus:
                                        scrollTxt("{}".format(enemies[i]["attack"][attack]))

                                        remo = []
                                        #input(blocking)
                                        for ysdf in blocking:
                                            if ysdf[0] != "dodge":
                                                if "kinetic shield" not in offhand:
                                                    if type(ysdf[1]) == type(1):
                                                        shield_bl = ysdf[1]
                                                        if i in enemies_shield_weakness.keys():
                                                            if enemies_shield_weakness[i] in offhand: 
                                                                shield_bl *= 2
                                                            
                                                        scrollTxt(
                                                        f"You blocked {green}{shield_bl}{white} damage with your {turquoise}{ysdf[0]}{white}")
                                                        edamage -= shield_bl
                                                        ysdf[1] -= 1
                                                    else:
                                                        scrollTxt(
                                                        f"You blocked {green}{int(ysdf[1])}{white} percent of the damage with your {turquoise}{ysdf[0]}{white}")
                                                        edamage -= int(edamage * int(ysdf[1]) / 100)

                                                else:
                                                    scrollTxt(f"You absorbed {purple}{int(edamage/4)}{white} damage with your {darkgrey}kinetic shield{white}")
                                                    power = ""
                                                    #power = int(power) + int(edamage/4)
                                                    

                                                    startc = False
                                                    for char in offhand:
                                                        if char == "[":
                                                            startc = True
                                                        elif char == "]":
                                                            startc = False
                                                        elif startc is True:
                                                            power += char
                                                    
                                                    power = int(power) + int(float(edamage/4))
                                                    edamage -= int(edamage/4)

                                                    inv.remove(offhand)
                                                    offhand = "kinetic shield [" + str(power) + "]"
                                                    inv.append(offhand)

                                                    kistats = items_all["kinetic shield [0]"].copy()
                                                    
                                                    kistats["name"] = offhand
                                                    kistats["description"] = f'A {blue}large{white} round shield, covered in a {darkgrey}dark material{white} that feels like {orange}rubber{white}, when it takes a hit it {purple}shimmers purple{white}.\nAbsorbed {purple}{power}{white} energy'

                                                    items_all[offhand] = kistats
                                                    shield_all[offhand] = shield_all['kinetic shield [0]'].copy()

                                                    

                                            remo.append(ysdf)
                                        #input(blocking)

                                        if edamage <= 0:
                                            edamage = 1

                                        scrollTxt(f"{level_hit} | {copper}{i}{white} dealt {red}{edamage}{white} damage")
                                        if enemies[i]["elemental"][attack] != "none":
                                            print()
                                            xcv = enemies[i]["elemental"][attack]
                                            crollTxt(f"You gain {xcv}", 2)
                                            uhurt.append(["player", xcv, effects_length[xcv]])
                                        health -= edamage
                                        
                                        if offhand not in offhand_weapons:
                                            if edamage > shield_all[offhand]["break"]:
                                                print()
                                                inv.remove(offhand)
                                                offhand = "none"
                                                scrollTxt(f"The {red}hit{white} was to much for your {darkgrey}shield{white}, it {orange}shattered{white} into {paleyellow}pieces{white}")

                                    else:
                                        scrollTxt("{} but your shield blocks you!".format(enemies[i]["attack"][attack]))

                                else:

                                    if ehit > min(dexterity + strength, 10) + metade_bonus:
                                        scrollTxt("{}".format(enemies[i]["attack"][attack]))

                                        remo = []

                                        for ysdf in blocking:
                                            if ysdf[0] != "dodge":
                                                scrollTxt(
                                                    f"You blocked {green}{ysdf[1]}{white} damage with your {turquoise}{ysdf[0]}{white}")
                                                edamage -= ysdf[1]
                                                ysdf[1] -= 1
                                            remo.append(ysdf)

                                        if edamage <= 0:
                                            edamage = 1

                                        scrollTxt(f"{level_hit} | {copper}{i}{white} deals {red}{edamage}{white} damage")
                                        if enemies[i]["elemental"][attack] != "none":
                                            print()
                                            xcv = enemies[i]["elemental"][attack]
                                            crollTxt(f"You gain {xcv}", 2)
                                            uhurt.append(["player", xcv, effects_length[xcv]])
                                        health -= edamage

                                    else:
                                        scrollTxt("{} but misses!".format(enemies[i]["attack"][attack]))

                        else:

                            ehit = random.randint(1, 20) + enemies[i]['dex']
                            #input(blocking)
                            for x7 in blocking:
                                if x7[0] == 'dodge':
                                    ehit -= x7[1]
                                    x7[1] /= 2
                            #input(blocking)
                            edamage = int(enemies[i]['damage'] + enemies[i]['str'] * (ehit / 20))

                            level_hit = ""

                            if ehit >= 5:
                                level_hit = red + "Weak Hit" + white

                            else:
                                level_hit = paleyellow + "Miss" + white

                            if ehit >= 10:
                                level_hit = brown + "Solid Hit" + white

                            if ehit >= 15:
                                level_hit = blue + "Strong Hit" + white

                            if ehit >= 20:
                                level_hit = gold + "CRITICAL STRIKE" + white

                            if offhand != "none":
                                try:
                                    guardshield = shield_all[offhand]["guard"]
                                    if i in enemies_shield_weakness.keys():
                                            if enemies_shield_weakness[i] in offhand: 
                                                guardshield *= 2
                                except:
                                    guardshield = min(dexterity + strength, 9)
                                if ehit > guardshield + metade_bonus:
                                    scrollTxt("{}".format(enemies[i]["attack"]))

                                    remo = []

                                    for ysdf in blocking:
                                        if ysdf[0] != "dodge":
                                            if "kinetic shield" not in offhand:
                                                    if type(ysdf[1]) == type(1):
                                                        shield_bl = ysdf[1]
                                                        if i in enemies_shield_weakness.keys():
                                                            if enemies_shield_weakness[i] in offhand: 
                                                                shield_bl *= 2
                                                            
                                                        scrollTxt(
                                                        f"You blocked {green}{shield_bl}{white} damage with your {turquoise}{ysdf[0]}{white}")
                                                        edamage -= shield_bl
                                                        ysdf[1] -= 1
                                                    else:
                                                        scrollTxt(
                                                        f"You blocked {green}{int(ysdf[1])}{white} percent of the damage with your {turquoise}{ysdf[0]}{white}")
                                                        edamage -= int(edamage * int(ysdf[1]) / 100)
                                            else:
                                                    scrollTxt(f"You absorbed {purple}{int(edamage/4)}{white} damage with your {darkgrey}kinetic shield{white}")
                                                    power = ""

                                                    

                                                    startc = False
                                                    for char in offhand:
                                                        if char == "[":
                                                            startc = True
                                                        elif char == "]":
                                                            startc = False
                                                        elif startc is True:
                                                            power += char
                                                    
                                                    power = int(power) + int(edamage/4)
                                                    edamage -= int(edamage/4)

                                                    inv.remove(offhand)
                                                    offhand = "kinetic shield [" + str(power) + "]"
                                                    inv.append(offhand)

                                                    kistats = items_all["kinetic shield [0]"].copy()
                                                    
                                                    kistats["name"] = offhand
                                                    kistats["description"] = f'A {blue}large{white} round shield, covered in a {darkgrey}dark material{white} that feels like {orange}rubber{white}, when it takes a hit it {purple}shimmers purple{white}.\nAbsorbed {purple}{power}{white} energy'

                                                    items_all[offhand] = kistats
                                                    shield_all[offhand] = shield_all["kinetic shield [0]"].copy()
                                        remo.append(ysdf)

                                    #blocking = nblo.copy()
                                    

                                    if edamage < 1:
                                        edamage = 0

                                    scrollTxt(f"{level_hit} | {copper}{i}{white} deals {red}{edamage}{white} damage")
                                    if enemies[i]["elemental"] != "none":
                                        print()
                                        xcv = enemies[i]["elemental"]
                                        crollTxt(f"You gain {xcv}", 2)
                                        uhurt.append(["player", xcv, effects_length[xcv]])
                                    health -= edamage

                                    if offhand not in offhand_weapons:
                                        if edamage > shield_all[offhand]["break"]:
                                                print()
                                                inv.remove(offhand)
                                                offhand = "none"
                                                scrollTxt(f"The {red}hit{white} was to much for your {darkgrey}shield{white}, it {orange}shattered{white} into {paleyellow}pieces{white}")

                                else:
                                    scrollTxt("{} but your shield blocks you!".format(enemies[i]["attack"]))

                            else:

                                if ehit > min(dexterity + strength, 10) + metade_bonus:
                                    scrollTxt("{}".format(enemies[i]["attack"]))

                                    remo = []
                                    #nblo = []

                                    for ysdf in blocking:
                                        if ysdf[0] != "dodge":
                                            scrollTxt(
                                                f"You blocked {green}{ysdf[1]}{white} damage with your {turquoise}{ysdf[0]}{white}")
                                            edamage -= ysdf[1]
                                            #ysdf[1] -= 1
                                        remo.append(ysdf)
                                        #nblo.append(ysdf)

                                    #blocking = nblo.copy()

                                    if edamage <= 0:
                                        edamage = 1

                                    scrollTxt(f"{level_hit} | {copper}{i}{white} deals {red}{edamage}{white} damage")
                                    if enemies[i]["elemental"] != "none":
                                        xcv = enemies[i]["elemental"]
                                        print()
                                        scrollTxt(f"You were {red}inflicted{white} with {darkgrey}{xcv}{white}")
                                        uhurt.append(["player", xcv, effects_length[xcv]])
                                    health -= edamage

                                else:
                                    scrollTxt("{} but misses!".format(enemies[i]["attack"]))

                    else:
                        removeE.append(i)
                        scrollTxt("" + enemies[i]['death'])
                        scrollTxt()

                        ge = enemies[i]["gold"]
                        ee = enemies[i]['exp']

                        scrollTxt(f"You got {gold}{ge}{white} gold!")
                        if weapon in exp_weapons:
                            scrollTxt(f"You got {turquoise}{ee + int(ee*0.5)}{white} exp | {teal}{ee*0.5}{white} extra xp from your {darkgrey}{weapon}{white}")
                            exp += ee + ee*0.5
                        else:
                            scrollTxt(f"You got {turquoise}{ee}{white} exp")
                            exp += ee

                        gp += ge

                       

                        if exp >= exp_max:
                            scrollTxt("_____________________")
                            scrollTxt("|                   |")
                            scrollTxt(f"| You {blue}LEVELED UP!{white}   |")
                            scrollTxt(f"| + {red}5{white} Max HP        |")
                            scrollTxt(f"| + {turquoise}Level Crystal{white} 🔷|")
                            scrollTxt("|___________________|")

                            lvl += 1
                            crystals += 1
                            max_health += 5

                            exp -= exp_max
                            exp_max = int(exp_max * 1.5)
                            scrollTxt()

                        

                        for sdf in enemies[i]['drop']:
                            if random.randint(1, max(enemies[i]['drop'][sdf] - luck_amount, 1)) == 1:
                                if "trophy" in sdf and sdf not in triggers:
                                    print()
                                    triggers.append(sdf)
                                    inv.append(sdf)
                                    scrollTxt(f"{gold}Congradulations{white} you managed to get a {orange}trophy{white}!")
                                    if "copper" in sdf:
                                        scrollTxt(f"You got a {brown}{sdf}{white} [{darkgrey}Tier{white} {turquoise}I{white}] !")
                                        crollTxt(decode_string(ss[0], skey[3]))
                                    elif "bronze" in sdf:
                                        scrollTxt(f"You got a {copper}{sdf}{white} [{darkgrey}Tier{white} {turquoise}II{white}] !! ⭐️")
                                        crollTxt(decode_string(ss[1], skey[3]))
                                    elif "silver" in sdf:
                                        scrollTxt(f"You got a {silver}{sdf}{white} [{darkgrey}Tier{white} {turquoise}III{white}] !!! 🌟")
                                        crollTxt(decode_string(ss[2], skey[3]))
                                    elif "gold" in sdf:
                                        scrollTxt(f"You got a {gold}{sdf}{white} [{darkgrey}Tier{white} {turquoise}IV{white}] !!!! 💫")
                                        crollTxt(decode_string(ss[3], skey[3]))
                                    else:
                                        scrollTxt(f"You got a {blue}{sdf}{white} [{darkgrey}Tier{white} {turquoise}V{white}] !!!!! ✨")
                                        crollTxt(decode_string(ss[4], skey[3]))
                                else:
                                    if sdf in weapons_all.keys():
                                        if random.randint(1, 5) == 1:
                                            modifier = random.choice(["cursed", "rusty", "blessed", "polished", "damaged", "renforced"])
                                            nsdf = modifier + " " + sdf
                                            wstats = weapons_all[sdf].copy()
                                            istats = items_all[sdf].copy()

                                            if modifier == "cursed":
                                                cursed_weapons[nsdf] = random.randint(1, 5)
                                                io = f"\n{purple}Cursed{white} Effect | Take {red}damage{white} when wielding"
                                            elif modifier == "rusty":
                                                wstats["damage"] -= 1
                                                wstats["hit"] -= 1
                                                io = f"\n{copper}Rusty{white} Effect | Less {red}damage{white}, Less {blue}accuarcy{white}"
                                            elif modifier == "blessed":
                                                blessed_weapons[nsdf] = random.randint(1, 5)
                                                io = f"\n{blue}Blessed{white} Effect | {red}Heal{white} when wielding"
                                            elif modifier == "polished":
                                                wstats["durability"] += 10
                                                io = f"\n{gold}Polished{white} Effect | Increased {darkgrey}durability{white}"
                                            elif modifier == "damaged":
                                                wstats["durability"] -= 10
                                                if wstats["durability"] < 5:
                                                    wstats["durability"] = 5
                                                io = f"\n{red}Damaged{white} Effect | Less {darkgrey}durability{white}"
                                            elif modifier == "renforced":
                                                wstats["damage"] += 1
                                                wstats["hit"] += 1
                                                io = f"\n{orange}Renforced{white} Effect | More {red}damage{white}, More {blue}accuarcy{white}"
                                            istats['description'] = istats['description'] + io
                                            items_all[nsdf] = istats
                                            weapons_all[nsdf] = wstats

                                            print()
                                            scrollTxt(f"The {i} dropped a {copper}{nsdf}{white}")

                                            inv.append(nsdf)

                                        else:
                                            print()
                                            scrollTxt(f"The {i} dropped a {copper}{sdf}{white}")

                                            inv.append(sdf)

                                    else:
                                        print()
                                        scrollTxt(f"The {i} dropped a {copper}{sdf}{white}")

                                        inv.append(sdf)
                    enter()

                nblocking = []
                for ysdf in blocking:
                    if ysdf[2] - 1 != 0:
                        nblocking.append([ysdf[0], ysdf[1], ysdf[2] - 1])
                
                blocking = nblocking

                for u in removeE:
                    for x2 in enemies_checks:
                        if x2 in u:
                            try:
                                enemies_killed[x2] += 1
                            except:
                                enemies_killed[x2] = 1
                    enemies.pop(u)
                for u in adddE:
                    enemies[u] = adddE[u]
                if len(enemies) < 1:
                    if len(enemy) > 1: 
                        scrollTxt(f"You have {blue}defeated{white} all the {copper}enemies{white}")
                        print()
                        dt = int((begin_health - health)/3)
                        if dt > 0:
                            scrollTxt(f"You gained back {red}{dt}{white} ❤️")
                            health += dt
                            print()
                        enter()
                    else:
                        
                        dt = int((begin_health - health)/2)
                        if dt > 0:
                            print()
                            scrollTxt(f"You gained back {red}{dt}{white} ❤️")
                            health += dt
                            print()
                            enter()
                    clear()
                    break
                else:
                    turn = 'player'

            neffects = {}

            for x in effects:
                #input(x)
                #input(effects[x])
                if effects[x][1] >= 1:
                    neffects[x] = effects[x]

            effects = neffects
            #input(effects)


    def playaudio(filename):
        import urllib.request
        import urllib.parse
        url = 'https://wind-and-water-or-rpg-or-pyserver.overdrivereplit.repl.co/update'
        data = {'music': filename}
        data = urllib.parse.urlencode(data).encode("utf-8")
        urllib.request.urlopen(urllib.request.Request(url, data))


    def Shop(shop_items, prices, name, sp=15):
        global time_triggers, triggers, gp, inv

        current_GMT = time.gmtime()
        current_time = calendar.timegm(current_GMT)

        scrollTxt(f"Welcome to {name}")
        scrollTxt("")

        try:
            time_passed = current_time - time_triggers[name]
        except:
            time_passed = 0
            time_triggers[name] = current_time

        if time_passed >= 120:
            new_prices = []
            for i in prices:
                new_prices.append(int(i * (random.randint(8 , 12) / 10)))

            prices = new_prices
            time_triggers[name] = current_time

        scrollTxt(f"GP: {gold}{gp}{white}")

        for x in range(0, len(prices)):
            z1 = sp - len(lis(shop_items[x]))

            f1 = ""
            f2 = ""

            for x10 in range(math.ceil(z1 / 2)):
                f2 += " "
            for x10 in range(math.floor(z1 / 2)):
                f1 += " "

            scrollTxt(f"[{f2}{grey}{shop_items[x]}{white}{f1}] | [{prices[x]}{gold} gp{white}]")

        scrollTxt(f"[{blue}leave{white}] to leave")

        print()

        shop_items.append("leave")
        answer = get_input(shop_items, True)
        print()

        if answer != "leave":

            num = 0
            z = 0
            for i in shop_items:
                if i == answer:
                    num = z
                z += 1

            if gp >= prices[num]:
                inv.append(answer)
                scrollTxt(f"Thanks for your {gold}purchase{white}")
                print()

                scrollTxt(f"+ {teal}{answer}{white} | - {gold}{prices[num]}{white}")
                gp -= prices[num]
            else:
                scrollTxt(f"You don't have {red}enough{white}.")
            enter()
            clear()
            Shop(shop_items, prices, name, sp)

        else:
            scrollTxt("You leave...")
            enter()


    def calScore():
        global enemies_killed, enemies_all

        f7 = 0

        for x in enemies_killed:
            f7 += enemies_killed[x] * enemies_all[x]['exp']

        f7 += len(triggers) * 2

        return f7


    def printStats():
        global effects
        print(f"- {turquoise}LEVEL {lvl}{white} -")
        scrollTxt(f"Level Crystals: {turquoise}{crystals}{white} 🔷")
        scrollTxt(f"Health: {red}{health}{white}/{red}{max_health}{white} ❤️")
        scrollTxt(f"GP: {gold}{gp}{white} 🔶")
        scrollTxt(f"Score: {yellow}{calScore()}{white} ⚜️")
        scrollTxt(f"Exp: {teal}{exp}{white}/{teal}{exp_max}{white} 🌀")
        print()
        print("---------------------")
        print()
        scrollTxt(f"Strength: {orange}{strength}{white}")
        scrollTxt(f"Dexterity: {green}{dexterity}{white}")
        print()
        print("---------------------")
        if len(effects) > 0:
            print()
            for x in effects:
                print(f"{blue}{x}{white} | Length: {darkgrey}{effects[x][1]}{white}")
            print()
            print("---------------------")
        print()
        scrollTxt(f"Progression: {purple}{int((len(triggers)/72)*100)}%{white}")

        enter()


    def usual_options(answer):
        global bold, normal, italic, gold, silver, copper, paleyellow, lime, turquoise, teal, yellow, green, blue, purple, brown, red, orange, darkgrey, grey, white, platinum, ironc
        global items_all
        global settings

        if answer == "inv":
            inventory()
        if answer == 'stats':
            printStats()

        if answer == "save":
            scrollTxt(f"{turquoise}Saving{white} Data...")
            save()
            time.sleep(1)
            scrollTxt(f"Like the game? Leave a ❤️...")
            time.sleep(1)
            scrollTxt(f"{green}>>Save Complete<<{white}")
            enter()

        if answer == "settings":
            while True:
                clear()

                len_clr = {
                    "purple": "   ",
                    "normal": "   ",
                    "blue": "     ",
                    "green": "    ",
                    "red": "      ",
                    "orange": "   ",
                    "black": "    "
                }
                if settings["print out des"]:
                    z = f"{green}ON{white}"
                else:
                    z = f"{red}OFF{white}"

                print(f"What would you like {green}change{white}?")
                print(
                    f"    * POD  [{z}]       {italic}Changes if the description of an area is printed even if you have already been there{normal}{bold}")
                if settings["surroundings"]:
                    z = f"{green}ON{white}"
                else:
                    z = f"{red}OFF{white}"
                print(f"    * SRND [{z}]       {italic}Prints out the areas surrounding the area your in{normal}{bold}")
                if settings["minimap"]:
                    z = f"{green}ON{white}"
                else:
                    z = f"{red}OFF{white}"
                print(f"    * MMAP [{z}]       {italic}Prints a minimap{normal}{bold}")
                if settings["auto saving"]:
                    z = f"{green}ON{white}"
                else:
                    z = f"{red}OFF{white}"
                print(f"    * AUSV [{z}]       {italic}Auto Saves when you travel{normal}{bold}")
                z = settings["color"]
                bn = len_clr[settings["color"]]
                print(f"    * CLR  [{z}]{bn}{italic}Changes the screen color{normal}{bold}")
                print(f"[{orange}l{white}] - Leave")

                change = get_input(["pod", "srnd", 'mmap', "ausv", "clr", "leave"])
                print()

                if change == "pod":
                    if settings["print out des"]:
                        settings["print out des"] = False
                    else:
                        settings["print out des"] = True
                if change == "srnd":
                    if settings["surroundings"]:
                        settings["surroundings"] = False
                    else:
                        settings["surroundings"] = True
                if change == "mmap":
                    if settings["minimap"]:
                        settings["minimap"] = False
                    else:
                        settings["minimap"] = True
                if change == "ausv":
                    if settings["auto saving"]:
                        settings["auto saving"] = False
                    else:
                        settings["auto saving"] = True

                if change == "clr":
                    
                    clrs = ["normal", "green", "blue", "purple", "red", "orange", "black"]
                    zx = 0
                    gg = False
                    clr_code = {
                        "green": '\x1b[38;2;00;160;00m\x1b[1m',
                        "blue": '\x1b[38;2;0;40;255m\x1b[1m',
                        "purple": '\x1b[38;2;130;0;250m\x1b[1m',
                        "red": '\x1b[0;31m\x1b[1m',
                        "orange": '\x1b[38;2;255;90;0m\x1b[1m',
                        "black": '\x1b[38;2;100;100;100m\x1b[1m',
                    }

                    for x in clrs:
                        if x != settings["color"] and gg == False:
                            zx += 1
                        else:
                            gg = True

                    

                    try:
                        settings["color"] = clrs[zx + 1]
                    except:
                        settings["color"] = "normal"

                    if settings["color"] != "normal":
                        color_a = clr_code[settings["color"]]
                        bold = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        normal = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        italic = '\x1B[3m'

                        gold = color_a
                        silver = color_a
                        copper = color_a

                        paleyellow = color_a
                        lime = color_a
                        turquoise = color_a
                        teal = color_a

                        yellow = color_a
                        green = color_a
                        blue = color_a
                        purple = color_a
                        brown = color_a
                        red = color_a
                        orange = color_a

                        darkgrey = color_a
                        grey = color_a

                        white = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        platinum = color_a
                        ironc = color_a
                    else:
                        bold = '\x1b[1m'
                        normal = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        italic = '\x1B[3m'

                        gold = '\x1b[38;2;230;190;0m\x1b[1m'
                        silver = '\x1b[38;2;221;221;221m\x1b[1m'
                        copper = '\x1b[38;2;170;44;0m\x1b[1m'

                        paleyellow = '\x1b[38;2;255;255;215m\x1b[1m'
                        lime = '\x1b[38;2;00;255;00m\x1b[1m'
                        turquoise = '\x1b[38;2;0;255;255m\x1b[1m'
                        teal = '\x1b[38;2;0;170;170m\x1b[1m'

                        yellow = '\x1b[38;2;255;255;0m\x1b[1m'
                        green = '\x1b[38;2;00;160;00m\x1b[1m'
                        blue = '\x1b[38;2;0;40;255m\x1b[1m'
                        purple = '\x1b[38;2;130;0;250m\x1b[1m'
                        brown = '\x1b[38;2;135;62;35m\x1b[1m'
                        red = '\x1b[0;31m\x1b[1m'
                        orange = '\x1b[38;2;255;90;0m\x1b[1m'

                        darkgrey = '\x1b[38;2;100;100;100m\x1b[1m'
                        grey = '\x1b[38;2;130;130;130m\x1b[1m'

                        white = '\x1b[38;2;255;255;255m\x1b[1m'
                        platinum = '\x1b[38;2;205;192;255m\x1b[1m'
                        ironc = '\x1b[38;2;255;205;192m\x1b[1m'
                    

                    
                if change == "leave":
                    break


    def cups():
        global gp

        clear()
        if gp > 0:
            scrollTxt(f"How much would you like to {green}bet{white}?")
            commands = []
            for x in range(1, gp + 1):
                commands.append(str(x))
            how_much = get_input(commands, g= True)
            scrollTxt("")
        else:
            scrollTxt(f"Looks like you {red}don\'t{white} have any {gold}coins{white}...")
            scrollTxt(f"You are playing for {purple}zero stakes{white}")
            how_much = 0
            print()

        scrollTxt("🫙 🫙 🫙")
        scrollTxt(f"Which cup has the {gold}coin{white} [🔶]")
        cup = get_input(["left", "middle", "right"])
        print()

        ccup = random.choice(['left', 'middle', 'right'])

        l = ['left', 'middle', 'right']

        for i in l:
            if i == ccup:
                scrollTxt("🔶 ", end="", flush=True)
            else:
                scrollTxt("🫙 ", end="", flush=True)

        print()

        if cup == ccup:
            scrollTxt(f"Correct! ✅")
            scrollTxt(f"+ {how_much} [🔶]")
            gp += int(how_much)
        else:
            scrollTxt(f"Wrong! ❌")
            scrollTxt(f"- {red}{how_much}{white} [🔶]")
            gp -= int(how_much)

        save()


    def dice():
        global gp

        clear()
        if gp > 0:
            scrollTxt(f"How much would you like to {red}bet{white}?")
            commands = []
            for x in range(1, gp + 1):
                commands.append(str(x))
            how_much = int(get_input(commands, g= True))
            scrollTxt("")
        else:
            scrollTxt(f"Looks like you {red}don\'t{white} have any {gold}coins{white}...")
            scrollTxt(f"You are playing for {purple}zero stakes{white}")
            print()
            how_much = 0

        scrollTxt("                 -  🎲  - ")
        scrollTxt(f"Which {blue}number{white} will the {purple}dice{white} land on?")
        dice_guess = int(get_input(["1", "2", "3", "4","5", "6"], g= True))
        print()

        dice = random.randint(1, 6)
        dice_to_emoji = {
            "1": "1️⃣",
            "2": "2️⃣",
            "4": "4️⃣",
            "3": "3️⃣",
            "5": "5️⃣",
            "6": "6️⃣"
        }

        dice_emo = dice_to_emoji[str(dice)]
        level_close = f"{red}incorrect{white} ❌"
        if dice_guess in range(dice - 1, dice + 2):
            level_close = f"{blue}close{white} 🟦"
        if dice_guess == dice:
            level_close = f"{green}correct{white} ✅"
        scrollTxt(f"The 🎲 landed on a {dice_emo}")
        scrollTxt(f"You were {level_close}")
        print()

        if dice_guess == dice:
            print(f"+ {gold}{how_much * 2}{white} 🔶")
            gp += how_much * 2
        elif dice_guess in range(dice - 1, dice + 2):
            print(f"+ {gold}{int(how_much / 2)}{white} 🔶")
            gp += int(how_much  / 2)
        else:
            print(f"- {red}{how_much}{white} 🔶")
            gp -= how_much

        save()


    def minimap():
        if True:
                    clrs = ["normal", "green", "blue", "purple", "red", "orange", "black"]
                    zx = 0
                    gg = False
                    clr_code = {
                        "green": '\x1b[38;2;00;160;00m\x1b[1m',
                        "blue": '\x1b[38;2;0;40;255m\x1b[1m',
                        "purple": '\x1b[38;2;130;0;250m\x1b[1m',
                        "red": '\x1b[0;31m\x1b[1m',
                        "orange": '\x1b[38;2;255;90;0m\x1b[1m',
                        "black": '\x1b[38;2;100;100;100m\x1b[1m',
                    }

                    for x in clrs:
                        if x != settings["color"] and gg == False:
                            zx += 1
                        else:
                            gg = True

                    

                    try:
                        settings["color"] = clrs[zx]
                    except:
                        settings["color"] = "normal"

                    if settings["color"] != "normal":
                        color_a = clr_code[settings["color"]]
                        bold = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        normal = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        italic = '\x1B[3m'

                        gold = color_a
                        silver = color_a
                        copper = color_a

                        paleyellow = color_a
                        lime = color_a
                        turquoise = color_a
                        teal = color_a

                        yellow = color_a
                        green = color_a
                        blue = color_a
                        purple = color_a
                        brown = color_a
                        red = color_a
                        orange = color_a

                        darkgrey = color_a
                        grey = color_a

                        white = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        platinum = color_a
                        ironc = color_a
                    else:
                        bold = '\x1b[1m'
                        normal = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        italic = '\x1B[3m'

                        gold = '\x1b[38;2;230;190;0m\x1b[1m'
                        silver = '\x1b[38;2;221;221;221m\x1b[1m'
                        copper = '\x1b[38;2;170;44;0m\x1b[1m'

                        paleyellow = '\x1b[38;2;255;255;215m\x1b[1m'
                        lime = '\x1b[38;2;00;255;00m\x1b[1m'
                        turquoise = '\x1b[38;2;0;255;255m\x1b[1m'
                        teal = '\x1b[38;2;0;170;170m\x1b[1m'

                        yellow = '\x1b[38;2;255;255;0m\x1b[1m'
                        green = '\x1b[38;2;00;160;00m\x1b[1m'
                        blue = '\x1b[38;2;0;40;255m\x1b[1m'
                        purple = '\x1b[38;2;130;0;250m\x1b[1m'
                        brown = '\x1b[38;2;135;62;35m\x1b[1m'
                        red = '\x1b[0;31m\x1b[1m'
                        orange = '\x1b[38;2;255;90;0m\x1b[1m'

                        darkgrey = '\x1b[38;2;100;100;100m\x1b[1m'
                        grey = '\x1b[38;2;130;130;130m\x1b[1m'

                        white = '\x1b[38;2;255;255;255m\x1b[1m'
                        platinum = '\x1b[38;2;205;192;255m\x1b[1m'
                        ironc = '\x1b[38;2;255;205;192m\x1b[1m'
        if location == "lockwood":
            print(f"""██|{green}██{white}|██|██
██|██|██
   ██|██
   ██|██
   ██""")
        if location == "snowy mountain":
            print(f"""██|██|██|██
██|{green}██{white}|██
   ██|██
   ██|██
   ██""")
        if location == "orc layer":
            print(f"""{green}██{white}|██|██|██
██|██|██
   ██|██
   ██|██
   ██""")
        if location == "troll & goblin encamp":
            print(f"""██|██|{green}██{white}|██
██|██|██
   ██|██
   ██|██
   ██""")
        if location == "the forge":
            print(f"""██|██|██|██
{green}██{white}|██|██
   ██|██
   ██|██
   ██""")
        if location == "merchant":
            print(f"""██|██|██|██
██|██|{green}██{white}
   ██|██
   ██|██
   ██""")
        if location == "merchant 2":
            print(f"""██|██|██|{green}██{white}
██|██|██
   ██|██
   ██|██
   ██""")
        if location == "shrine":
            print(f"""██|██|██|██
██|██|██
   {green}██{white}|██
   ██|██
   ██""")
        if location == "bandit hideout":
            print(f"""██|██|██|██
██|██|██
   ██|{green}██{white}
   ██|██
   ██""")
        if location == "magic forest":
            print(f"""██|██|██|██
██|██|██
   ██|██
   {green}██{white}|██
   ██""")
        if location == "dragon worshipers":
            print(f"""██|██|██|██
██|██|██
   ██|██
   ██|{green}██{white}
   ██""")
        if location == "dragon cave":
            print(f"""██|██|██|██
██|██|██
   ██|██
   ██|██
   {green}██{white}""")


    def minimap_frozite():
        if True:
                    clrs = ["normal", "green", "blue", "purple", "red", "orange", "black"]
                    zx = 0
                    gg = False
                    clr_code = {
                        "green": '\x1b[38;2;00;160;00m\x1b[1m',
                        "blue": '\x1b[38;2;0;40;255m\x1b[1m',
                        "purple": '\x1b[38;2;130;0;250m\x1b[1m',
                        "red": '\x1b[0;31m\x1b[1m',
                        "orange": '\x1b[38;2;255;90;0m\x1b[1m',
                        "black": '\x1b[38;2;100;100;100m\x1b[1m',
                    }

                    for x in clrs:
                        if x != settings["color"] and gg == False:
                            zx += 1
                        else:
                            gg = True

                    

                    try:
                        settings["color"] = clrs[zx]
                    except:
                        settings["color"] = "normal"

                    if settings["color"] != "normal":
                        color_a = clr_code[settings["color"]]
                        bold = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        normal = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        italic = '\x1B[3m'

                        gold = color_a
                        silver = color_a
                        copper = color_a

                        paleyellow = color_a
                        lime = color_a
                        turquoise = color_a
                        teal = color_a

                        yellow = color_a
                        green = color_a
                        blue = color_a
                        purple = color_a
                        brown = color_a
                        red = color_a
                        orange = color_a

                        darkgrey = color_a
                        grey = color_a

                        white = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        platinum = color_a
                        ironc = color_a
                    else:
                        bold = '\x1b[1m'
                        normal = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        italic = '\x1B[3m'

                        gold = '\x1b[38;2;230;190;0m\x1b[1m'
                        silver = '\x1b[38;2;221;221;221m\x1b[1m'
                        copper = '\x1b[38;2;170;44;0m\x1b[1m'

                        paleyellow = '\x1b[38;2;255;255;215m\x1b[1m'
                        lime = '\x1b[38;2;00;255;00m\x1b[1m'
                        turquoise = '\x1b[38;2;0;255;255m\x1b[1m'
                        teal = '\x1b[38;2;0;170;170m\x1b[1m'

                        yellow = '\x1b[38;2;255;255;0m\x1b[1m'
                        green = '\x1b[38;2;00;160;00m\x1b[1m'
                        blue = '\x1b[38;2;0;40;255m\x1b[1m'
                        purple = '\x1b[38;2;130;0;250m\x1b[1m'
                        brown = '\x1b[38;2;135;62;35m\x1b[1m'
                        red = '\x1b[0;31m\x1b[1m'
                        orange = '\x1b[38;2;255;90;0m\x1b[1m'

                        darkgrey = '\x1b[38;2;100;100;100m\x1b[1m'
                        grey = '\x1b[38;2;130;130;130m\x1b[1m'

                        white = '\x1b[38;2;255;255;255m\x1b[1m'
                        platinum = '\x1b[38;2;205;192;255m\x1b[1m'
                        ironc = '\x1b[38;2;255;205;192m\x1b[1m'
        if location == "white bridge":
            scrollTxt(f"""    ██
    ██|██
    ██       {blue}World Map{white}
 ██|{turquoise}██{white}|██|██
    ██|██
    ██""")
        if location == "monk cliffs":
            scrollTxt(f"""    ██
    ██|██
    ██       {blue}World Map{white}
 {turquoise}██{white}|██|██|██
    ██|██
    ██""")
        if location == "goliaths burrow":
            scrollTxt(f"""    ██
    ██|██
    ██       {blue}World Map{white}
 ██|██|██|██
    {turquoise}██{white}|██
    ██""")
        if location == "core-sail arena":
            scrollTxt(f"""    ██
    ██|██
    ██       {blue}World Map{white}
 ██|██|██|██
    ██|██
    {turquoise}██{white}""")
        if location == "sunken graveyard":
            scrollTxt(f"""    ██
    ██|██
    ██       {blue}World Map{white}
 ██|██|{turquoise}██{white}|██
    ██|██
    ██""")
        if location == "frosted cave":
            scrollTxt(f"""    ██
    ██|██
    {turquoise}██{white}       {blue}World Map{white}
 ██|██|██|██
    ██|██
    ██""")
        if location == "dead lake":
            scrollTxt(f"""    ██
    {turquoise}██{turquoise}|██
    ██      {blue}World Map{white}
 ██|██|██|██
    ██|██
    ██""")
           

    def forge_weapon():
        global inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects, known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class, location, settings, durability_weapon, items_all, weapons_all, shield_all, strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons
        triggers.append("forged weapon")

        ww = []
        for x in inv:
            if items_all[x]["weapon"] and x not in staffs_all:
                ww.append(x)

        print(f"What {darkgrey}weapon{white} would you like to {orange}forge{white}?")

        for x in ww:
            if x != ww[len(ww) - 1]:
                print(f"{random.choice([darkgrey, grey, silver, platinum])}{x}{white}, ", end="")
            else:
                print(f"{random.choice([darkgrey, grey, silver, platinum])}{x}{white}", end="")
        print()

        answer = get_input(ww)

        print()

        istats = items_all[answer].copy()
        wstats = weapons_all[answer].copy()

        is_chosen = False
        duracheck = False
        duramount = 0
        if answer in durability_weapon:
            duramount = durability_weapon[answer]
            durability_weapon.pop(answer)
            duracheck = True
            
        if weapon == answer: is_chosen = True

        if is_chosen: weapon = "none"
        inv.remove(answer)

        bonuses = [f"{red}Attack up{white}", f"{green}Sweep Range Increase{white}", f"{blue}Accuracy Up{white}",
                    f"{turquoise}Combo Hit Increase{white}", f"{orange}Durability Up{white}"]
        bonus = random.choice(bonuses)
        print(f"Your {darkgrey}{answer}{white} got the {bonus} bonus!")
        print()

        print(f"What would you like to {blue}call{white} your {darkgrey}weapon{white}?")
        wname = input("> ").lower()

        inv.append(wname)
        if is_chosen: weapon = wname

        istats['name'] = wname
        istats['description'] = istats[
                                    'description'] + f"\n{purple}Enchanted{white} with {bonus}. Named {darkgrey}{wname}{white}."
        istats['selling price'] += 20
        items_all[wname] = istats

        if "Attack up" in bonus:
            wstats["damage"] += 3
        if "Sweep Range" in bonus:
            wstats['sweep'] += 0.5
        if "Accuracy Up" in bonus:
            wstats["hit"] += 3
        if "Combo Hit" in bonus:
            wstats['speed'] = max(1, wstats['speed'] - 1)
            if wstats['speed'] > 15: wstats["speed"] = 15
        if "Durability Up" in bonus:
            wstats["durability"] += 10
            

        weapons_all[wname] = wstats

        if duracheck:
            durability_weapon[wname] = duramount
            if "Durability Up" in bonus:
                durability_weapon[wname] += 10
        if answer in blessed_weapons:
            blessed_weapons[wname] = blessed_weapons[answer]
        if answer in cursed_weapons:
            cursed_weapons[wname] = cursed_weapons[answer]
        if answer in strength_weapons:
            strength_weapons[wname] = strength_weapons[answer]
        if answer in dexterity_weapons:
            dexterity_weapons[wname] = dexterity_weapons[answer]
        if answer in health_weapons:
            health_weapons[wname] = health_weapons[answer]
        if answer in luck_weapons:
            luck_weapons[wname] = luck_weapons[answer]
        if answer in steal_weapons:
            steal_weapons[wname] = steal_weapons[answer]
        if answer in double_bladed_weapons:
            double_bladed_weapons.append(answer)
        if answer in offhand_weapons:
            offhand_weapons.append(answer)
        if answer in defense_weapons:
            defense_weapons[wname] = defense_weapons[answer]

        enter()


    def forge_shield():
        global inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects, known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class, location, settings, durability_weapon, items_all, weapons_all, shield_all

        ww = []
        for x in inv:
            if items_all[x]["shield"]:
                ww.append(x)

        print(f"What {darkgrey}shield{white} would you like to {orange}forge{white}?")

        for x in ww:
            if x != ww[len(ww) - 1]:
                print(f"{random.choice([darkgrey, grey, silver, platinum])}{x}{white}, ", end="")
            else:
                print(f"{random.choice([darkgrey, grey, silver, platinum])}{x}{white}", end="")
        print()

        answer = get_input(ww)

        print()

        istats = items_all[answer].copy()
        wstats = shield_all[answer].copy()

        is_chosen = False
        if offhand == answer: is_chosen = True

        if is_chosen: offhand = "none"
        inv.remove(answer)

        bonuses = [f"{red}Block Up{white}", f"{green}Guard Increase{white}", f"{blue}Break point Increase{white}", f"{orange}Shield bash Damage Up{white}"]
        bonus = random.choice(bonuses)
        print(f"Your {darkgrey}{answer}{white} got the {bonus} bonus!")
        print()

        print(f"What would you like to {blue}call{white} your {darkgrey}shield{white}?")
        wname = input("> ").lower()

        inv.append(wname)
        if is_chosen: offhand = wname

        istats['name'] = wname
        istats['description'] = istats[
                                    'description'] + f"\n{purple}Enchanted{white} with {bonus}. Named {darkgrey}{wname}{white}."
        istats['selling price'] += 10
        items_all[wname] = istats

        if "Block up" in bonus:
            if type(wstats["block"]) == type(1):
                wstats["block"] += 2
            else:
                wstats["block"] = str(int(wstats['block']) + 5)
        if "Guard Increase" in bonus:
            wstats['guard'] += 4
        if "Break point Increase" in bonus:
            wstats["break"] += 6 
        if "Shield bash Damage Up" in bonus:
            wstats['damage'] += 3

        shield_all[wname] = wstats

        enter()


    def view_weapon():
        scrollTxt(f"What {darkgrey}weapon{white} would you like to {white}view{white} ?")
        answer = get_input(list(weapons_all.keys()))
        print()

        print()
        scrollTxt(f"{blue}{answer}{white}")
        z = items_all[answer]["description"]
        x = weapons_all[answer]
        y = {
            "bleed": 5,
            "poison": 6,
            "burn": 8,
            "shock": 10,
            "drain": 7,
            "freeze": 7,
            "life steal": 8,
            "dragon burn": 12,
            "crunch": 7,
            "lightning": 15,
            "hyper bleed": 8,
            "hyper freeze": 8,
            "dirtify": 9,
            "acid": 10
        }
        ws = int(((((x["damage"]/(1))) * (5 - (x['reload'] * 1.4) + (x["hit"] / 2))) + (x["hit"]) + min(15, (x["durability"]/2)) + max(0, (20 - (x["speed"] * 1.5))) + (x["damage"] * x["sweep"])))
        if x["special"] != False: 
            if type(x["special"]) == type(["this", "is", 'a', "list"]):
                    for sp in x["special"]:
                        ws += y[sp]
            else:
                ws += y[x["special"]] 
        if "crit" in x: ws += int(x["damage"] * (x["crit"] / 10))

        scrollTxt(f"{italic}{z}{normal}{white}")
        print()
        scrollTxt(f"{turquoise}Weapon{white} {darkgrey}Score{white}: {teal}{ws}{white}")
        print()
        d = x["damage"]
        h = x["hit"]
        r = x['reload']

        scrollTxt(f"Damage: {orange}{d}{white}")
        scrollTxt(f"Hit: {blue}{h}{white}")
        scrollTxt(f"Reload time: {green}{r}{white} turns")

        enter()


    def make_weapon():
        global items_all, weapons_all

        istats = {
            'name': input(f"What would you like to {blue}name{white} your {darkgrey}weapon{white}\n"),
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description': input(f"\nWhat would you like the {turquoise}description{white} of the {darkgrey}weapon{white} to be\n"),
            'selling price': 5,
            'fuse': False
        }
    
        wstats = {'hit': 4, 'damage': 5, 'special': False, "special text": "", "speed": 5, "sweep": 1, "durability": 15, "reload": 0}

        print()

        wstats['hit'] = int(input(f"What would you like the {orange}hit{white} to be [Heavy weapons = -3 to -1] [Light Weapons = 2 to 4]\n"))
        print()
        wstats['damage'] = int(input(f"What would you like the {red}damage{white} to be [Wooden Sword = 5] [Steel Sword = 10]\n"))
        print()
        scrollTxt(f"What {purple}effect{white} would you like your {darkgrey}weapon{white} to have")
        wstats['special'] = get_input(["bleed", "burn", "poison", "drain", 'freeze'])
        print()
        wstats["special text"] = input(f"What should the {green}game{white} say when you cause the {blue}effect{white}\n")
        print()
        wstats["speed"] = int(input(f"What should be the {yellow}chance{white} of landing a {turquoise}combo hit{white} be [50% = 2] [10% = 10]\n"))
        print()
        wstats["durability"] = int(input(f"What should the {teal}duarability{white} of the {darkgrey}weapon{white} be [Normal weapon = 10-30]\n"))
        
        print()

        scrollTxt(f"{turquoise}Creating{white} Weapon...")
        weapons_all[istats["name"]] = wstats
        x = weapons_all[istats["name"]]
        y = {
            "bleed": 17,
            "poison": 18,
            "burn": 20,
            "drain": 18,
            "freeze": 18
        }
        ws = int(((((x["damage"]/(1))) * (5 - (x['reload'] * 1.4) + (x["hit"] / 2))) + (x["hit"]) + min(15, (x["durability"]/2)) + max(0, (20 - (x["speed"] * 1.5))) + (x["damage"] * x["sweep"])))
        if x["special"] != False: ws += y[x["special"]] - 5
        istats["selling price"] = ws*2
        items_all[istats["name"]] = istats
        time.sleep(2)

        n = istats["name"]
        
        d = istats["description"]
        scrollTxt(f"{blue}{n}{white}")
        scrollTxt(f"{italic}{d}{white}")
        print()

        scrollTxt(f"Weapon Score: {yellow}{ws}{white}")
        scrollTxt(f"Cost: {red}{ws*2}{white} 🔶")


    # Credit to @BluDev
    def loading_animation(message, length=100, sleep = 0):
        for i in range(51):
            sys.stdout.write('\r')
            sys.stdout.write(f"{message}: {i*2}% |{'█' * i}{' ' * (50 - i)}|")
            sys.stdout.flush()
            time.sleep(length*0.01)
            clear()
        print()
        time.sleep(sleep)


    def snowy_mountain():
        global inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects, known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class, location, settings, durability_weapon, items_all, weapons_all, shield_all, crystals
        
        mini_location = "climbing faze 1"
        ft = 0
        hydration = 100
        energy = 100

        clear()
        dot = ""
        for x in range(9):
            scrollTxt(f"Loading {turquoise}Snowy{white} {purple}Mountain{white}{dot}")
            dot += "."
            if dot == "....":
                dot = ""
            time.sleep(0.2)
            clear()
        clear()

        loading_animation(f"Creating {darkgrey}Enemies{white}", 5, 0)
        loading_animation(f"Loading {blue}Weapons{white}", 5, 0)
        loading_animation(f"Generating {brown}Terrain{white}", 5, 0)
        
        clear()

        scrollTxt(f"Welcome to {turquoise}Snowy{white} {purple}Mountain{white}")
        enter()

        if mini_location == "climbing faze 1":
            while ft < 99:
                
                clear()

                if energy < 0:
                    scrollTxt(f"You have no {yellow}energy{white} left and you {red}die{white}")
                    die()

                if hydration < 0:
                    scrollTxt(f"You die of {blue}thirst{white}")
                    die()

                scrollTxt(f"{blue}{100 - ft}{white} ft Left")
                scrollTxt(f"[{darkgrey}Climb{white}] [{purple}Check Stats{white}] [{blue}Drink Water{white}] [{red}Heal{white}]")
                scrollTxt(f"What would {turquoise}you{white} like to do?")
                answer = get_input(["climb", "check stats", "drink water", 'heal'])
                print()

                if answer == "climb":
                    scrollTxt(f"You {red}struggle{white} to {brown}climb{white} the {purple}mountain{white} slowly you put one {blue}hand{white} above the other")
                    amount = 12
                    if "climbing gear" in inv: amount -= 2
                    if "rope" in inv: amount -= 1

                    if random.randint(1, amount) in range(1, dexterity + strength):
                        cl_amount = random.randint(5, 20)
                        if "climbing gear" in inv: cl_amount += 5
                        if "rope" in inv: cl_amount += 3

                        scrollTxt(f"You made it up {green}{cl_amount}{white} ft!")
                        ft += cl_amount

                    else:
                        scrollTxt(f"You {red}struggle{white} to find a {darkgrey}grip{white} and fall!")
                        fl_amount = random.randint(5, 10)
                        if "climbing gear" in inv: fl_amount -= 2
                        if "rope" in inv: fl_amount -= 1

                        scrollTxt(f'You fell {red}{min(fl_amount, ft)}{white} ft')
                        scrollTxt(f"You lost {red}{int(min(fl_amount, ft)/2)}{white} health")
                        health -= int(min(fl_amount, ft)/2)

                        ft -= fl_amount

                        if health < 0:
                            print()
                            scrollTxt(f"You {red}died{white}")
                            die()

                    elamount = random.randint(5, 10)
                    hlamount = random.randint(10, 15)
                    print()
                    scrollTxt(f"You lost {yellow}{elamount}{white} energy")
                    scrollTxt(f"You lost {blue}{hlamount}{white} hydration")
                    

                    energy -= elamount
                    hydration -= hlamount

                    if random.randint(1, 5) == 1 and "rope" in inv:
                        print()
                        scrollTxt(f"You {brown}rope{white} snapped in half")
                        inv.remove("rope")

                    enter()

                if answer == "check stats":
                    scrollTxt(f"Energy: {yellow}{energy}{white} ⚡️")
                    scrollTxt(f"Hydration: {blue}{hydration}{white} 💧")
                    enter()

                if answer == "drink water":
                    if "water bottle" in inv:
                        scrollTxt(f"You use a {blue}water bottle{white}")
                        scrollTxt(f"+ {turquoise}50{white} Hydration")
                        hydration = min(hydration + 50, 100)
                        inv.remove("water bottle")
                    else:
                        scrollTxt(f"You {red}don\'t{white} have a water bottle")

                    enter()

                if answer == "heal":
                    if "health potion" in inv:
                        scrollTxt(f"You use a {red}health potion{white}")
                        scrollTxt(f"+ {red}10{white} Health")
                        scrollTxt(f"+ {yellow}50{white} Energy")
                        health = min(health + 10, max_health)
                        energy = min(energy + 50, 100)
                        inv.remove("health potion")
                    else:
                        scrollTxt(f"You {red}don\'t{white} have a health potion")

                    enter()
            mini_location = "break 1"

            clear()
            scrollTxt(f"After {blue}hours{white} of {darkgrey}climbing{white} you finally made it to a small {orange}cave{white} to take a break")
            enter()

        if mini_location == "break 1":
            print()
            scrollTxt(f"You find {teal}yourself{white} in a {green}damp cave{white}. In the middle of the {darkgrey}cave{white} inserted in a {grey}rock{white} is a {copper}rusty sword{white} the scene seems {orange}off{white}...")
            scrollTxt(f"As you approach the {darkgrey}blade{white} you feel a sense of deep {red}forebodeing{white}")
            scrollTxt(f"[{turquoise}Take out the Blade{white}] [{turquoise}Leave it alone{white}]")
            scrollTxt(f"What would {blue}you{white} like to do?")
            answer = get_input(["take out blade", 'leave it alone'])
            print()

            if answer == "take out blade":
                scrollTxt(f"Slowly you take out the {copper}rusted{white} {darkgrey}broadsword{white}")
                scrollTxt(f"{brown}+ Rusty Sword{white}")
                inv.append("rusty sword")

                print()

                time.sleep(1)

                scrollTxt(f"Right when you {red}dislodge{white} the {darkgrey}blade{white} you hear a deep {orange}rummbling{white} sound...")
                scrollTxt(f"You turn around only to {blue}bump{white} into a {green}FUGI MONSTER{white}")
                scrollTxt(f'Its {brown}mushroomlike{white} face twisted with {red}anger{white} it charges at you!')
                enter()

                combat(["fungi monster"])

                scrollTxt(f"After {blue}defeated{white} the {green}fungi monster{white} you take a long {orange}rest{white}")
                health = max_health
                scrollTxt(f"{red}Health Restored to Max{white}")

                enter()

            if answer == "leave it alone":
                scrollTxt(f'You leave the {copper}rusty sword{white} alone. It doesn\'t seem to be {gold}worth{white} anything')
                scrollTxt(f"You take a long {blue}rest{white}...")
                time.sleep(1)

                health = max_health
                scrollTxt(f"{red}Health Restored to Max{white}")

                enter()

            print()
            scrollTxt(f"You get up and continue {darkgrey}climbing{white} up the {purple}mountain")
            enter()
            
            clear()

            mini_location = "climbing faze 2"

        if mini_location == "climbing faze 2":
            ft = 0 
            while ft < 99:
                
                clear()

                if energy < 0:
                    scrollTxt(f"You have no {yellow}energy{white} left and you {red}die{white}")
                    die()

                if hydration < 0:
                    scrollTxt(f"You die of {blue}thirst{white}")
                    die()

                scrollTxt(f"{blue}{100 - ft}{white} ft Left")
                scrollTxt(f"[{darkgrey}Climb{white}] [{purple}Check Stats{white}] [{blue}Drink Water{white}] [{red}Heal{white}]")
                scrollTxt(f"What would {turquoise}you{white} like to do?")
                answer = get_input(["climb", "check stats", "drink water", 'heal'])
                print()

                if answer == "climb":
                    scrollTxt(f"You {red}struggle{white} to {brown}climb{white} the {purple}mountain{white} slowly you put one {blue}hand{white} above the other")
                    amount = 12
                    if "climbing gear" in inv: amount -= 2
                    if "rope" in inv: amount -= 1

                    if random.randint(1, amount) in range(1, dexterity + strength):
                        cl_amount = random.randint(5, 20)
                        if "climbing gear" in inv: cl_amount += 5
                        if "rope" in inv: cl_amount += 3

                        scrollTxt(f"You made it up {green}{cl_amount}{white} ft!")
                        ft += cl_amount

                    else:
                        scrollTxt(f"You {red}struggle{white} to find a {darkgrey}grip{white} and fall!")
                        fl_amount = random.randint(5, 10)
                        if "climbing gear" in inv: cl_amount -= 2
                        if "rope" in inv: cl_amount -= 1

                        scrollTxt(f'You fell {red}{min(fl_amount, ft)}{white} ft')
                        scrollTxt(f"You lost {red}{int(min(fl_amount, ft)/2)}{white} health")
                        health -= int(min(fl_amount, ft)/2)

                        ft -= fl_amount

                        if health < 0:
                            print()
                            scrollTxt(f"You {red}died{white}")
                            die()

                    elamount = random.randint(5, 10)
                    hlamount = random.randint(10, 15)
                    print()
                    scrollTxt(f"You lost {yellow}{elamount}{white} energy")
                    scrollTxt(f"You lost {blue}{hlamount}{white} hydration")
                    

                    energy -= elamount
                    hydration -= hlamount

                    if random.randint(1, 5) == 1 and "rope" in inv:
                        print()
                        scrollTxt(f"You {brown}rope{white} snapped in half")
                        inv.remove("rope")

                    enter()


                if answer == "check stats":
                    scrollTxt(f"Energy: {yellow}{energy}{white} ⚡️")
                    scrollTxt(f"Hydration: {blue}{hydration}{white} 💧")
                    enter()

                if answer == "drink water":
                    if "water bottle" in inv:
                        scrollTxt(f"You use a {blue}water bottle{white}")
                        scrollTxt(f"+ {turquoise}50{white} Hydration")
                        hydration = min(hydration + 50, 100)
                        inv.remove("water bottle")
                    else:
                        scrollTxt(f"You {red}don\'t{white} have a water bottle")

                    enter()

                if answer == "heal":
                    if "health potion" in inv:
                        scrollTxt(f"You use a {red}health potion{white}")
                        scrollTxt(f"+ {red}10{white} Health")
                        scrollTxt(f"+ {yellow}50{white} Energy")
                        health = min(health + 10, max_health)
                        energy = min(energy + 50, 100)
                        inv.remove("health potion")
                    else:
                        scrollTxt(f"You {red}don\'t{white} have a health potion")

                    enter()
            mini_location = "peak"

            clear()
            scrollTxt(f"After {blue}days{white} of {darkgrey}climbing{white} to make it to the {purple}peak{white}...")
            enter()
            print()

        if mini_location == "peak":
            scrollTxt(f"""
    As {blue}you{white} stand atop the {purple}snowy mountain peak{white}, a sense of {gold}triumph{white} and {turquoise}wonder{white} washes over you.
You've {orange}conquered{white} the formidable slopes, overcoming {yellow}physical challenges{white} and pushing beyond your {teal}limits{white}. 
The {silver}crisp mountain air{white} fills your {ironc}lungs{white}, rejuvenating your {turquoise}spirit{white} and heightening your {blue}senses{white}.

    Looking around, you are greeted by a {blue}breathtaking{white} panorama that {darkgrey}stretches{white} as far as the {teal}eye{white} can see. 
A {turquoise}pristine{white} blanket of {silver}glistening white snow{white} coats the {brown}landscape{white}, shimmering under the {yellow}radiant sunlight{white}. 
The jagged peaks of neighboring mountains pierce the {orange}horizon{white}, standing tall as {grey}guardians{white} of this {teal}frozen realm{white}.

    The {blue}silence{white} surrounding you is {gold}profound{white}, broken only by the occasional {silver}whisper of the wind{white} and the distant echoes of nature's voice. 
It's as if {green}time{white} has momentarily stood {teal}still{white}, allowing you to savor this {purple}rare{white} moment of {grey}solitude{white} and {grey}serenity{white}. 
The {turquoise}tranquility{white} envelopes you, granting a respite from the {red}chaos{white} of everyday life.
""")
            time.sleep(2)
            triggers.append("mountain peak")

            exp += 60
            scrollTxt(f"+ {blue}60{white} EXP 🌀")

            if exp >= exp_max:
                        scrollTxt("_____________________")
                        scrollTxt("|                   |")
                        scrollTxt(f"| You {blue}LEVELED UP!{white}   |")
                        scrollTxt(f"| + {red}5{white} Max HP        |")
                        scrollTxt(f"| + {turquoise}Level Crystal{white} 🔷|")
                        scrollTxt("|___________________|")

                        lvl += 1
                        crystals += 1
                        max_health += 5

                        exp -= exp_max
                        exp_max = int(exp_max * 1.5)
                        scrollTxt()

            enter()

            print()

            health = max_health

            scrollTxt(f"Sadly the {paleyellow}peace{white} is {darkgrey}short-lived{white}")
            scrollTxt(f"A {red}deafening{white} {orange}ROAR{white} shatters your {blue}ears{white}")
            scrollTxt(f"{teal}Icicles{white} drop from a {darkgrey}cave{white} near by as a {orange}huge{white} {turquoise}YETI{white} lumbers out!")
            scrollTxt(f"Turning around you {blue}draw{white} you {copper}{weapon}{white}")
            scrollTxt(f"The {red}BOSS{white} is here")
            enter()

            combat(["yeti", "snow minion"])

            scrollTxt(f'{red}Blood{white} drips from many {orange}cuts{white} as you stagger around')
            time.sleep(0.5)
            scrollTxt(f"[{red}LACK OF OXYGEN{white}]")
            time.sleep(0.5)
            scrollTxt(f"[{red}BLOOD LOSS{white}]")
            time.sleep(0.5)
            scrollTxt(f"[{red}EXHAUSTION{white}]")
            time.sleep(0.5)
            print()

            scrollTxt(f"You see a {blue}faint{white} {paleyellow}light{white} in the distance")
            scrollTxt(f"[{turquoise}CLIMB DOWN MOUNTAIN{white}] [{turquoise}FOLLOW LIGHT{white}]")
            scrollTxt(f"What do you {blue}do{white}?")
            answer = get_input(["climb down", "follow light"])
            print()

            if answer == "climb down":
                scrollTxt(f"You atemp to {darkgrey}climb{white} down the {purple}mountain")

                ft = 0 
                while ft < 199:
                    
                    clear()

                    if energy < 0:
                        scrollTxt(f"You have no {yellow}energy{white} left and you {red}die{white}")
                        die()

                    if hydration < 0:
                        scrollTxt(f"You die of {blue}thirst{white}")
                        die()

                    scrollTxt(f"{blue}{100 - ft}{white} ft Left")
                    scrollTxt(f"[{darkgrey}Climb{white}] [{purple}Check Stats{white}] [{blue}Drink Water{white}] [{red}Heal{white}]")
                    scrollTxt(f"What would {turquoise}you{white} like to do?")
                    answer = get_input(["climb", "check stats", "drink water", 'heal'])
                    print()

                    if answer == "climb":
                        scrollTxt(f"You {red}struggle{white} to {brown}climb{white} the {purple}mountain{white} slowly you put one {blue}hand{white} above the other")
                        amount = 12
                        if "climbing gear" in inv: amount -= 2
                        if "rope" in inv: amount -= 1

                        if random.randint(1, amount) in range(1, dexterity + strength):
                            cl_amount = random.randint(5, 20)
                            if "climbing gear" in inv: cl_amount += 5
                            if "rope" in inv: cl_amount += 3

                            scrollTxt(f"You made it down {green}{cl_amount}{white} ft!")
                            ft += cl_amount

                        else:
                            scrollTxt(f"You {red}struggle{white} to find a {darkgrey}grip{white} and fall!")
                            fl_amount = random.randint(5, 10)
                            if "climbing gear" in inv: cl_amount -= 2
                            if "rope" in inv: cl_amount -= 1

                            scrollTxt(f'You fell {red}{min(fl_amount, ft)}{white} ft')
                            scrollTxt(f"You lost {red}{int(min(fl_amount, ft)/2)}{white} health")
                            health -= int(min(fl_amount, ft)/2)

                            ft += fl_amount

                            if health < 0:
                                print()
                                scrollTxt(f"You {red}died{white}")
                                die()

                        elamount = random.randint(5, 10)
                        hlamount = random.randint(10, 15)
                        print()
                        scrollTxt(f"You lost {yellow}{elamount}{white} energy")
                        scrollTxt(f"You lost {blue}{hlamount}{white} hydration")
                        

                        energy -= elamount
                        hydration -= hlamount

                        if random.randint(1, 5) == 1 and "rope" in inv:
                            print()
                            scrollTxt(f"You {brown}rope{white} snapped in half")
                            inv.remove("rope")

                        enter()


                    if answer == "check stats":
                        scrollTxt(f"Energy: {yellow}{energy}{white} ⚡️")
                        scrollTxt(f"Hydration: {blue}{hydration}{white} 💧")
                        enter()

                    if answer == "drink water":
                        if "water bottle" in inv:
                            scrollTxt(f"You use a {blue}water bottle{white}")
                            scrollTxt(f"+ {turquoise}50{white} Hydration")
                            hydration = min(hydration + 50, 100)
                            inv.remove("water bottle")
                        else:
                            scrollTxt(f"You {red}don\'t{white} have a water bottle")

                        enter()

                    if answer == "heal":
                        if "health potion" in inv:
                            scrollTxt(f"You use a {red}health potion{white}")
                            scrollTxt(f"+ {red}10{white} Health")
                            scrollTxt(f"+ {yellow}50{white} Energy")
                            health = min(health + 10, max_health)
                            energy = min(energy + 50, 100)
                            inv.remove("health potion")
                        else:
                            scrollTxt(f"You {red}don\'t{white} have a health potion")

                        enter()

                clear()
                scrollTxt(f"You made it back to {orange}base camp{white}")
                enter()
                clear()

            if answer == "follow light":
                scrollTxt(f"You follow the {paleyellow}light{white}")
                scrollTxt(f"You hear a {yellow}sizzling{white} sound as you drift {blue}asleep{white}...")
                time.sleep(2)

                scrollTxt(f"You wake in {orange}base camp{white} but you feel {orange}fuzzy{white}")
                scrollTxt(f"- {red}5{white} Max Health")

                max_health -= 5
                
                health -= 5
                if health < 1:
                    health = 1
                enter()
                clear()


    def bandit_hideout():
        global inv, health, max_health, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects, known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class, location, settings, durability_weapon, items_all, weapons_all, shield_all
        
        mini_location = "2 bandits"

        while True:
            clear()
            preloc = mini_location
            if mini_location == "2 bandits":
                scrollTxt(f"You are at the {orange}entrance{white} to the {yellow}bandit hideout{white}")
                scrollTxt(f"There are {blue}2{white} {darkgrey}gaurds{white} holding {yellow}scimitars{white}")
                scrollTxt(f"[{turquoise}Sneak Past{white}] [{turquoise}Fight the Guards{white}]")
                scrollTxt(f"What would you like to {blue}do{white}?")
                answer = get_input(["fight guards", "sneak past"])
                print()

                if answer == "sneak past":
                    if random.randint(1, 5) in range(1, dexterity):
                        scrollTxt(f"You make it {blue}past{white} the {darkgrey}guards{white}")

                    else:
                        scrollTxt(f"You are {red}noticed{white} and the {darkgrey}bandit guards{white} charge at you!")
                        enter()

                        combat(["bandit", "bandit 2"], 0.9)       
                else:
                    scrollTxt(f"You {orange}charge{white} at the {yellow}bandit guards{white}!")
                    enter()

                    combat(["bandit", "bandit 2"], 1.1)

                scrollTxt(f"You walk into the {yellow}hideout{white}")
                enter()
                mini_location = "arrows trap"

            elif mini_location == "arrows trap":
                scrollTxt(f"Inside this {blue}room{white} is a bunch of mounted {darkgrey}arrow{white} {orange}cannons{white}")
                scrollTxt(f"They are {red}firing{white} heavy {grey}iron{white} arrows at high {yellow}speeds{white}")
                scrollTxt(f"[{turquoise}Run Through{white}] [{turquoise}Use Shield{white}]")
                scrollTxt(f"What do {blue}you{white} do?")

                answer = get_input(["run through", "use shield"])
                print()

                if answer == "run through":
                    scrollTxt(f"You run through the {darkgrey}arrows{white}")
                    scrollTxt(f"Many of them {orange}strike{white} you causing {red}wounds{white}")
                    scrollTxt(f" - {red}3{white} Health")
                    health -= 3

                    if health < 1:
                        print()
                        scrollTxt(f"You {red}died{white}")
                        die()
                else:
                    if offhand != "none" and offhand not in offhand_weapons:
                        scrollTxt(f"You use your {darkgrey}shield{white} to block all the {orange}arrows{white}")
                        scrollTxt(f"By the {blue}end{white} your {darkgrey}shield{white} is {red}chipped{white} and {red}dented{white}")
                        istats = items_all[offhand].copy()
                        sstats = shield_all[offhand].copy()

                        istats["description"] = istats["description"] + f"\nChipped from {darkgrey}iron arrows{white}"
                        sstats["break"] = int(sstats["break"] * 0.75)

                        new_name = "chipped " + offhand
                        items_all[new_name] = istats
                        shield_all[new_name] = sstats

                        inv.remove(offhand)
                        offhand = new_name
                        inv.append(new_name)
                    else:
                        scrollTxt(f"You don\'t have a {darkgrey}shield{white}")
                        enter()
                        print()

                        scrollTxt(f"You run through the {darkgrey}arrows{white}")
                        scrollTxt(f"Many of them {orange}strike{white} you causing {red}wounds{white}")
                        scrollTxt(f" - {red}3{white} Health")
                        health -= 3

                        if health < 1:
                            print()
                            scrollTxt(f"You {red}died{white}")
                            die()

                print()

                scrollTxt(f"You continue {teal}south{white} down the {darkgrey}hall{white}.")
                enter()

                mini_location = "3 bandits"

            elif mini_location == "3 bandits":
                if "[bandit base] 3 bandits" not in triggers:
                    triggers.append("[bandit base] 3 bandits")
                    scrollTxt(f"Inside this {blue}room{white} there is a large {brown}table{white} full of {paleyellow}playing cards{white} and {orange}dice{white}, three {yellow}bandits{white} are huddled around the {brown}table{white}.")
                    scrollTxt(f"They all turn and {turquoise}look{white} at you, their faces {yellow}light{white} up with {red}alarm{white} and they {orange}charge{white} at you")
                    enter()

                    combat(["bandit", "bandit 2", "bandit 3"])
                    scrollTxt(f"After {gold}defeating{white} the {yellow}bandits{white} you find a {darkgrey}key{white} that opens the {brown}doors{white}")
                    scrollTxt(f"Do you {blue}travel{white} {teal}east{white} or {teal}south{white}?")
                    answer = get_input(["east", "south"])
                    print()

                    if answer == "east": 
                        scrollTxt(f"You walk to the {teal}east{white} room")
                        enter()
                        mini_location = "treasure"
                    else:
                        scrollTxt(f"You walk to the {teal}south{white} room")
                        enter()
                        mini_location = "lazer trap"
                else:
                    scrollTxt(f"This {blue}room{white} is {purple}empty{white}. Some {brown}playing cards{white} and {copper}dice{white} are on a {brown}table{white}")
                    scrollTxt(f"Do you {blue}travel{white} {teal}east{white} or {teal}south{white}?")
                    answer = get_input(["east", "south"])
                    print()

                    if answer == "east": 
                        scrollTxt(f"You walk to the {teal}east{white} room")
                        enter()
                        mini_location = "treasure"
                    else:
                        scrollTxt(f"You walk to the {teal}south{white} room")
                        enter()
                        mini_location = "lazer trap"
                    
            elif mini_location == "treasure":
                if "[bandit base] treasure" not in triggers:
                    scrollTxt(f"This {blue}room{white} contains a pile of {gold}gold coins{white} and a {yellow}scimitar{white} lying on the {darkgrey}floor{white}")
                    scrollTxt(f'Do you take the {gold}coins{white} [{green}y{white}/{red}n{white}]')
                    answer = get_input(["yes", "no"])
                    print()

                    if answer == "yes":
                        scrollTxt(f"+ {gold}10{white} GP")
                        gp += 10

                        print()

                    scrollTxt(f'Do you take the {grey}scimitar{white} [{green}y{white}/{red}n{white}]')
                    answer = get_input(["yes", "no"])
                    print()

                    if answer == "yes":
                        scrollTxt(f"+ {grey}scimitar{white}")
                        inv.append("scimitar")

                        print()

                    scrollTxt(f'The {blue}room{white} is now {red}empty{white}')
                    scrollTxt(f"You go to the {brown}room{white} to the {teal}west{white}")
                    enter()

                    mini_location = "3 bandits"

                else:
                    scrollTxt(f'The {blue}room{white} is {red}empty{white}')
                    scrollTxt(f"You go to the {brown}room{white} to the {teal}west{white}")
                    enter()

                    mini_location = "3 bandits"

            elif mini_location == "lazer trap":
                scrollTxt(f"This {blue}room{white} has a a row of {turquoise}intricately{white} set {red}lazers{white}")
                scrollTxt(f"[{turquoise}Run through{white}] [{turquoise}Use a mirror{white}]")
                scrollTxt(f"What would {green}you{white} like to do?")
                answer = get_input(["run through", "use a mirror"])
                print()

                if answer == "run through":
                    if random.randint(1, 6) in range(1, dexterity):
                        scrollTxt(f"You {teal}dodge{white} and {darkgrey}weave{white} through the {red}lazers{white}")
                        scrollTxt(f"After a few {green}minutes{white} you make to the {orange}end{white}")
                        #enter()

                    else:
                        scrollTxt(f"After a few {teal}seconds{white} you are {yellow}zapped{white} by a {red}lazer{white}")
                        scrollTxt(f"- {red}3{white} ❤️")
                        health -= 3
                        #enter()

                else:
                    if "mirror" in inv:
                        scrollTxt(f"You use a {darkgrey}mirror{white} to mess with the {red}lazers{white}")
                        scrollTxt(f"After the {red}lazers{white} are {orange}disrupted{white} you walk through {green}easier{white}")
                        #enter()
                    else:
                        scrollTxt(f"You don\'t have a {gold}mirror{white}")
                        enter()

                        print()

                        if random.randint(1, 6) in range(1, dexterity):
                            scrollTxt(f"You {teal}dodge{white} and {darkgrey}weave{white} through the {red}lazers{white}")
                            scrollTxt(f"After a few {green}minutes{white} you make to the {orange}end{white}")
                            #enter()

                        else:
                            scrollTxt(f"After a few {teal}seconds{white} you are {yellow}zapped{white} by a {red}lazer{white}")
                            scrollTxt(f"- {red}3{white} ❤️")
                            health -= 3
                            #enter()

                print()
                scrollTxt(f"You continue {teal}west{white} to the next {blue}room{white}")
                enter()
                mini_location = "bandit lord"

            elif mini_location == "bandit lord":
                scrollTxt(f"You have {teal}reached{white} the {blue}FINAL ROOM{white}")
                scrollTxt(f"This {darkgrey}room{white} is full of {gold}gold coins{white}")
                scrollTxt(f"In the {grey}middle{white} is a {orange}large bandit{white} holding a even large {red}MASTER SCIMITAR{white}")
                scrollTxt(f"The {yellow}bandit lord{white} turns around to {teal}face{white} you")
                enter()

                combat(["bandit lord"])
                print()

                scrollTxt(f"You have {green}finished{white} the {orange}BANDIT HIDEOUT{white}!")
                scrollTxt(f"Although the {red}SHARK FANGS{white} will likely be back...")
                scrollTxt(f"You {darkgrey}leave{white} the {yellow}hideout{white}")
                enter()
                break
        
            if preloc != mini_location:
                if "health potion" in inv:
                    scrollTxt(f'Would you like to use a {red}health potion{white}? [{green}y{white}/{red}n{white}]')
                    answer = get_input(['yes', "no"])
                    print()

                    if answer == "yes":
                        inv.remove("health potion")
                        scrollTxt(f"+ {red}5{white} ❤️")
                        health += 5
                    
                    enter()


    def jade_forest():
        global inv, health, max_health, triggers, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects, known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class, location, settings, durability_weapon, items_all, weapons_all, shield_all, offhand_weapons, offhand
        mini_location = "entrance"

        while True:
            clear()
            preloc = mini_location

            if mini_location == "entrance":
                scrollTxt(f"You are {darkgrey}standing{white} at the {blue}entrance{white} to the {teal}Jade Forest{white}")
                scrollTxt(f"Two {teal}Jade minions{white} stand {darkgrey}guarding{white} to only path in.")
                enter()
                print()

                scrollTxt(f"You draw your {orange}weapon{white} and {orange}charge{white} the {teal}jade minions{white}!")
                enter()

                combat(["jade minion 1", "jade minion 2"])
                
                scrollTxt(f"The {green}forest{white} now splits off in {brown}2 paths{white}")
                scrollTxt(f"[{orange}1{white}] This path is full of {purple}thorns{white} and {darkgrey}rocks{white}")
                scrollTxt(f"[{orange}2{white}] This path it {yellow}lighter{white} and is {brown}beaten out{white}.")
                scrollTxt(f"Which {brown}path{white} do you take?")
                answer = get_input(["1", "2"])
                print()

                scrollTxt(f"You walk along your {orange}chosen path{white}...")
                enter()

                if answer == "1":
                    mini_location = "jade knight"
                else:
                    mini_location = "jade"

            elif mini_location == "jade knight":
                scrollTxt(f"You enter a {copper}clearing{white} instead of it being {yellow}lighter{white} you find it to be {darkgrey}darker{white}")
                scrollTxt(f"In the middle your find a {darkgrey}knight{white} clad in {turquoise}jade armor{white} holding a {turquoise}jade sword{white}")
                scrollTxt(f"[{turquoise}Attack{white}] [{turquoise}Walk past{white}]")
                scrollTxt(f"What would {blue}you{white} like to do?")

                answer = get_input(["attack", "walk past"])
                print()

                if answer == "attack":
                    scrollTxt(f"You {orange}charge{white} at the {darkgrey}knight{white} in {turquoise}jade{white}")
                    enter()

                    combat(["jade knight"], 1.2)

                else:
                    scrollTxt(f"You atempt to {blue}walk{white} past the {teal}jade knight{white} but when your take a {orange}step{white} closer the {darkgrey}knight{white} bolts towards you!")
                    enter()

                    combat(["jade knight"], 0.9)

                scrollTxt(f"After dealing with the {teal}jade knight{white} you continue {red}deeper{white} into the {green}forest{white}")
                enter()

                mini_location = "pool"
            
            elif mini_location == "jade":
                scrollTxt(f"You come to a {brown}clearing{white} in the path.")
                scrollTxt(f"In the middle your see a {teal}Jade stone{white} imbeded in a {darkgrey}rock{white}")
                scrollTxt(f"[{turquoise}Use weapon{white}] [{turquoise}Leave it{white}]")
                answer = get_input(["use weapon", "leave it"])
                print()

                if answer == "use weapon":
                    scrollTxt(f"You use your {darkgrey}{weapon}{white} to hack at the {teal}jade rock{white}")
                    wdamage = weapons_all[weapon]["damage"]
                    amount = int(30/wdamage)
                    try:
                        durability_weapon[weapon] -= amount

                        if durability_weapon[weapon] < 1:
                            durability_weapon.pop(weapon)
                            print(f"Your {darkgrey}weapon{white} broke!")
                            inv.remove(weapon)
                            if weapon in offhand_weapons:
                                offhand = "none"  
                            else:
                                weapon = "none"

                    except:
                        durability_weapon[weapon] = weapons_all[weapon]['durability'] - 1

                    scrollTxt(f"+ {teal}Jade{white}")
                    inv.append("jade")

                else:
                    scrollTxt(f"You decide that it might {red}break{white} your {darkgrey}weapon{white} and you {blue}leave{white}")

                print()

                scrollTxt(f"You continue {darkgrey}deeper{white} into the {green}forest{white}")
                mini_location = "pool"            
                
            elif mini_location == "pool":
                scrollTxt(f'You find a {turquoise}crystal clear{white} {blue}pool{white}.')
                scrollTxt(f"The {blue}water{white} seems to beckon your {orange}closer{white}")
                scrollTxt(f"[{turquoise}Drink the Water{white}] [{turquoise}Leave it alone{white}]")
                answer = get_input(["drink the water", "leave it alone"])
                print()

                if answer == "drink the water":
                    scrollTxt(f"You take a sip of the {blue}water{white}")
                    scrollTxt(f"It turns out to be {teal}Jade water{white}!")
                    scrollTxt(f"+ {red}3{white} Max HP ❤️")
                    max_health += 3

                    enter()

                    print()

                    scrollTxt(f'As you {blue}drink{white} from the {turquoise}pool{white} your here a {silver}bubbling{white} sound')
                    scrollTxt(f"A huge mass of {darkgrey}drowned bodies{white} shaped into a {orange}grotesque monster{white} rises from the {blue}pool{white}")
                    enter()

                    combat(["drowned monstrosity"])
                    scrollTxt(f"{brown}Disguested{white} and {green}disturbed{white} your leave")
                else:
                    scrollTxt(f"You leave the {blue}water{white} alone")

                print()
                scrollTxt(f"The {brown}path{white} splits into the {orange}two{white} directions{white}")
                scrollTxt(f"Would you like to {blue}go{white} {darkgrey}left{white} or {darkgrey}right{white}")
                answer = get_input(["left", "right"])
                print()

                scrollTxt(f'Your turn {teal}{answer}{white}')
                enter()

                if answer == "left": mini_location = "puzzle"
                if answer == "right": mini_location = "riddle"

            elif mini_location == "riddle":
                scrollTxt(f"You see a tall {brown}wooden sphinx{white}, it talks with out moving its {red}mouth{white}")
                scrollTxt(f"This is what is says: Answer my {turquoise}riddle{white} or fear my {darkgrey}wrath{white}")
                scrollTxt(f"Here is the {gold}riddle{white}")
                print()
                time.sleep(1)

                scrollTxt(f"Through me, {gold}kings{white} and {darkgrey}knights{white} claim their right, {red}gems{white} and {gold}gold{white} shining {yellow}bright{white}. I'm {blue}circular{white}, with a face and hands, {darkgrey}ticking{white} away as {orange}history{white} expands. What am I?")
                answer = input("> ").lower()
                print()

                if answer in ["clock", "a clock", "clocks", "timepiece"]:
                    scrollTxt(f"{green}Correct{white}!")
                    scrollTxt(f"The {brown}sphinx{white} lets your go past")
                    scrollTxt(f"You continue into the {green}forest{white}")
                    enter()

                    mini_location = "jade guardian"
                else:
                    scrollTxt(f"{red}INNCORRECT{white} [{blue}Ans: Clock{white}]")
                    scrollTxt(f"The {brown}wooden{white} sphinx slams a massive {darkgrey}claw{white} down!")
                    scrollTxt(f" - 5 ❤️")
                    health -= 5
                    if health < 1:
                        die()
                    scrollTxt(f"You continue into the {green}forest{white}")
                    enter()

                    mini_location = "jade guardian"

            elif mini_location == "puzzle":
                scrollTxt(f"You see a tall {brown}wooden sphinx{white}, it talks with out moving its {red}mouth{white}")
                scrollTxt(f"This is what is says: Answer my {turquoise}riddle{white} or fear my {darkgrey}wrath{white}")
                scrollTxt(f"Here is the {gold}riddle{white}")
                print()
                time.sleep(1)

                scrollTxt(f"I am taken from a {darkgrey}mine{white}, and shut up in a {brown}wooden case{white}, from which I am never released. Yet, I am used by many to help them {blue}see{white} the {green}world{white}. What am I")
                answer = input("> ").lower()
                print()

                if answer in ["pencil", "a pencil", "pencils", "idk"]:
                    scrollTxt(f"{green}Correct{white}!")
                    scrollTxt(f"The {brown}sphinx{white} lets your go past")
                    scrollTxt(f"You continue into the {green}forest{white}")
                    enter()

                    mini_location = "jade guardian"
                else:
                    scrollTxt(f"{red}INNCORRECT{white} [{blue}Ans: PENCIL{white}]")
                    scrollTxt(f"The {brown}wooden{white} sphinx slams a massive {darkgrey}claw{white} down!")
                    scrollTxt(f" - 5 ❤️")
                    health -= 5
                    if health < 1:
                        die()
                    scrollTxt(f"You continue into the {green}forest{white}")
                    enter()

                    mini_location = "jade guardian"


            elif mini_location == "jade guardian":
                scrollTxt(f"You are now in the {blue}center{white} of the {teal}Jade Forest{white}.")
                scrollTxt(f"The {yellow}sun{white} illuminates a {turquoise}crystal blue{white} {darkgrey}broad sword{white}. It seems to {orange}glow{white} in the {paleyellow}light{white}")
                scrollTxt(f"Sadly it\'s not {darkgrey}unguarded{white}, a huge {teal}Jade monster{white} made of {darkgrey}metal parts{white} and {teal}crystalized jade{white} stands in front of the {blue}blade{white}")
                scrollTxt(f"It\'s {orange}core{white} starts to {yellow}glow{white} as a humming noise {red}intensifies{white}")
                scrollTxt(f"It picks up a {turquoise}jade scythe{white} and {orange}lumbers{white} toward you!")
                enter()

                combat(["jade guardian"])
                scrollTxt(f"With the {teal}Jade guardian{white} now in pecies, the {blue}magic sword{white} is all your!")
                scrollTxt(f"[{turquoise}Take Sword{white}] [{turquoise}Leave{white}]")
                scrollTxt(f"What would {blue}you{white} like to do?")
                answer = get_input(["take sword", "leave"])
                print()

                if answer == "leave":
                    scrollTxt(f"You {darkgrey}tread{white} back out the {green}forest{white} you don\'t {orange}encounter{white} any {copper}enemies{white}")
                    scrollTxt(f"You made it {blue}out{white}!")
                    enter()
                else:
                    scrollTxt(f"You approach the {blue}glowing sword{white}...")
                    time.sleep(1)
                    print()
                    scrollTxt(f"You place your {orange}hand{white} on the {darkgrey}blade{white}")
                    scrollTxt(f"{green}Time{white} seems to {darkgrey}slow{white}")
                    time.sleep(1)
                    print()
                    scrollTxt(f"The {blue}blade{white} seems to force you to take your {orange}hand{white} off it")
                    scrollTxt(f"You are exterting lots of {paleyellow}effort{white} keeping your {orange}hand{white} on")
                    for x in range(health):
                        print("- 🖤")
                        time.sleep(1)

                    print()
                    scrollTxt(f"Finally your use your last {orange}strength{white} and rip the {blue}blade{white} from the {darkgrey}rock{white}")
                    health = 1
                    scrollTxt(f"+ {blue}magic sword{white}")
                    inv.append("magic sword")
                    enter()

                    clear()

                    scrollTxt(f"You {darkgrey}tread{white} back out the {green}forest{white} you don\'t {orange}encounter{white} any {copper}enemies{white}")
                    scrollTxt(f"You made it {blue}out{white}!")
                    enter()   

                break

            if preloc != mini_location:
                print()
                if "health potion" in inv:
                    scrollTxt(f'Would you like to use a {red}health potion{white}? [{green}y{white}/{red}n{white}]')
                    answer = get_input(['yes', "no"])
                    print()

                    if answer == "yes":
                        inv.remove("health potion")
                        scrollTxt(f"+ {red}5{white} ❤️")
                        health += 5
                    
                    enter()

    
    def darkwood():
        global inv, health, max_health, triggers, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects, known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class, location, settings, durability_weapon, items_all, weapons_all, shield_all
        mini_loc = "dragon worshipers"

        while True:
            clear()
            pre_loc = mini_loc

            if mini_loc == "dragon worshipers":
                scrollTxt(f"You see {purple}cloaked{white} figure wearing a {red}horrible dragon{white} mask. A {darkgrey}shadowy spear{white} in hand.")
                scrollTxt(f"This person is a {red}dragon worshiper{white}, someone who devotes his/her {orange}life{white} to the {purple}dark dragon{white}")
                scrollTxt(f"You draw your {blue}{weapon}{white}")
                enter()

                combat(["dragon worshiper"])
                scrollTxt(f"You continue {darkgrey}deeper{white} into the {green}forest{white}")
                mini_loc = "forest horror"

            elif mini_loc == "forest horror":
                scrollTxt(f"You come to a {brown}clearing{white}")
                scrollTxt(f"Would you like to {red}rest up{white} or {blue}stay alert{white}?")
                answer = get_input(["rest up", "stay alert"])
                print()

                if answer == "rest up":
                    scrollTxt(f"You {red}rest{white} for about an {teal}hour{white}")
                    time.sleep(1)
                    scrollTxt(f"~{red}Health replenished{white}~")
                    health = max_health

                    print()

                    scrollTxt(f"Sadly you {yellow}fail{white} to notice the {green}horrible creature{white} that jumps at you!")
                    enter()

                    combat(["forest horror"], 0.8)

                else:
                    scrollTxt(f'You stay {yellow}alert{white}, so you notice the {green}horrible creature{white} as it trys to {darkgrey}jump{white} on you')
                    scrollTxt(f"You draw your {blue}{weapon}{white}")
                    enter()

                    combat(["forest horror"], 1.2)
                scrollTxt(f"You continue {darkgrey}deeper{white} into the {green}forest{white}")

                mini_loc = "dragon worshipers x3"

            elif mini_loc == "dragon worshipers x3":
                scrollTxt(f"You find a group of {purple}dragon worshipers{white} huddled around a {orange}fire{white}")
                scrollTxt(f"Would you like to {orange}charge attack{white} or try to {darkgrey}push one into the fire{white}?") 
                answer =get_input(["charge attack", "push one into the fire"])
                print()

                if answer == "charge attack":
                    scrollTxt(f"You {orange}charge{white} at the {purple}dragon worshipers{white}")
                    enter()

                    combat(["dragon worshiper 1", "dragon worshiper 2", "dragon worshiper 3"], 1.2)
                else:
                    if random.randint(1, 10) in range(1, dexterity + strength):
                        scrollTxt(f"You push one of the {purple}dragon worshipers{white} into the {yellow}fire{white}")
                        scrollTxt(f"The rest {red}attack{white} you!")
                        enter()

                        combat(["dragon worshiper 1", "dragon worshiper 2"])
                scrollTxt(f"You continue {darkgrey}deeper{white} into the {green}forest{white}")
                mini_loc = "cursed merchant"

            elif mini_loc == "cursed merchant":
                scrollTxt(f'You find another {brown}clearing{white}')
                scrollTxt(f"In the center your find a {darkgrey}short figure{white} drapped in {purple}purple robes{white}")
                scrollTxt(f'"My name is {blue}Notlik{white}, I am the {orange}cursed merchant{white}", says {blue}Notlik{white}')
                Shop(["cursed dagger", "cursed axe", "cursed bow"], [100, 120, 140], f"{darkgrey}The cursed shop{white}")
                scrollTxt(f"Would your like to view your {turquoise}inventory{white}? [{green}y{white}/{red}no{white}]")
                answer =get_input(["yes", "no"])
                if answer == "yes":
                    inventory()

                print()
                scrollTxt(f"You continue {darkgrey}deeper{white} into the {green}forest{white}")
                mini_loc = "boss battle"

            elif mini_loc == "boss battle":
                scrollTxt(f"You are at the {red}beating heart{white} or {darkgrey}darkwood{white}")
                time.sleep(0.5)
                scrollTxt(f"Here you find a what seems to be a {blue}large man{white} hunched over a {red}red tablet{white}")
                time.sleep(0.5)
                scrollTxt(f"He {darkgrey}cackles{white} throwing off his {purple}robe{white} revealing him to be quite a {orange}short fellow{white}")
                time.sleep(0.5)
                scrollTxt(f"He then waves around a {orange}massive{white} {red}DRAGON SCALE CLAYMORE{white} that is almost double his {blue}size{white}")
                time.sleep(0.5)
                scrollTxt(f"Finally he {paleyellow}charges{white} at you!")
                enter()

                combat(["dragon lord"]) 

                print()

                scrollTxt(f"The {orange}Dragon lord{white} staggers and slams down the {red}red tablet{white} breaking it into a million pieces")
                scrollTxt(f"He {yellow}screams{white} as his body morphes info a {brown}giaganic tree monster{white}")
                scrollTxt(f"This time when he {paleyellow}laughes{white} it shakes the {green}forest{white}!")
                scrollTxt(f"He is now the {brown}DREADWOOD{white}")
                enter()

                combat(["the dreadwood"])

                scrollTxt(f"The {green}forest{white} seems much {yellow}lighter{white}")
                scrollTxt(f"You find your way out with out any {red}trouble{white}!")
                enter()
                break    
            if pre_loc != mini_loc:
                print()
                scrollTxt(f"The {green}forest{white} seems to {grey}shift{white} and {darkgrey}blurr{white}")
                if "health potion" in inv:
                    scrollTxt(f'Would you like to use a {red}health potion{white}? [{green}y{white}/{red}n{white}]')
                    answer = get_input(['yes', "no"])
                    print()

                    if answer == "yes":
                        inv.remove("health potion")
                        scrollTxt(f"+ {red}5{white} ❤️")
                        health += 5
                    
                    enter()


    def dungeon():
        global inv, health, max_health, triggers, weapon, offhand, dexterity, strength, gp, special_moves, shield_moves, effects, known_spells, current_spells, triggers, time_triggers, enemies_killed, lvl, exp, exp_max, fighter_class, location, settings, durability_weapon, items_all, weapons_all, shield_all


        def dungeon_map(mini_location):
            if mini_location == "1":
                print(f"""██ - {darkgrey}██{white} - ██
-         -
██   ██ - ██     Dungeon Map
-    -    -
██   ██   ██""")

            if mini_location == "2":
                print(f"""{darkgrey}██{white} - ██ - ██
-         -
██   ██ - ██     Dungeon Map
-    -    -
██   ██   ██""")

            if mini_location == "3":
                print(f"""██ - ██ - ██
-         -
{darkgrey}██{white}   ██ - ██     Dungeon Map
-    -    -
██   ██   ██""")

            if mini_location == "4":
                print(f"""██ - ██ - ██
-         -
██   ██ - ██     Dungeon Map
-    -    -
{darkgrey}██{white}   ██   ██""")

            if mini_location == "5":
                print(f"""██ - ██ - ██
-         -
██   ██ - ██     Dungeon Map
-    -    -
██   {darkgrey}██{white}   ██""")

            if mini_location == "6":
                print(f"""██ - ██ - ██
-         -
██   ██ - ██     Dungeon Map
-    -    -
██   ██   {darkgrey}██{white}""")

            if mini_location == "7":
                print(f"""██ - ██ - ██
-         -
██   ██ - {darkgrey}██{white}     Dungeon Map
-    -    -
██   ██   ██""")

            if mini_location == "8":
                print(f"""██ - ██ -{darkgrey} ██{white}
-         -
██   ██ - ██     Dungeon Map
-    -    -
██   ██   ██""")

            if mini_location == "9":
                print(f"""██ - ██ - ██
-         -
██   {darkgrey}██{white} - ██     Dungeon Map
-    -    -
██   ██   ██""")
                            

        mini_location = "1"
        pre_loc = mini_location
        rtriggers = []

        while True:
            clear()

            dungeon_map(mini_location)
            print()

            if mini_location == "1":
                scrollTxt(f"This {orange}room{white} contains a pile of {paleyellow}bones{white}")
                scrollTxt(f"You see two massive {silver}skulls{white} like that of a {brown}beast{white}")
                scrollTxt(f"{blue}Commands{white}: {teal}Inv{white}, {platinum}Stats{white}, {silver}Touch Bones{white}, {darkgrey}Leave room{white}")
                answer = get_input(["inv", "stats", "touch bones", "leave room"])
                print()

                if answer == "inv":
                    inventory()
                    #enter()

                if answer == "stats":
                    printStats()
                    enter()

                if answer == "touch bones":
                    rtriggers.append("touched bones")
                    scrollTxt(f"You grab one of the {paleyellow}bones{white}...")
                    time.sleep(1)
                    scrollTxt(f"As you do, it flings out of your {darkgrey}hand{white}, {red}cutting{white} you")
                    scrollTxt(f"You look to see, the {paleyellow}bones{white} cobble together to form two {copper}skeleton soldiers{white}")
                    enter()

                    combat(["skeleton soldier 1", "skeleton soldier 2"])

                if answer == "leave room":
                    scrollTxt(f"There are two {brown}doors{white}")
                    scrollTxt(f"One to your {orange}west{white} and the other to your {orange}east{white}")
                    answer = get_input(["west", "east"])
                    print()

                    if "touched bones" not in rtriggers:
                        scrollTxt(f"As you head to the {brown}door{white} you notice that the {paleyellow}bones{white} are gone")
                        scrollTxt(f"You then turn to see two {copper}skeleton soldiers{white} blocking the exit")
                        enter()

                        combat(["skeleton soldier 1", "skeleton soldier 2"])

                    scrollTxt(f"You take the {brown}door{white} to the {orange}{answer}")

                    if answer == "west":
                        mini_location = "2"
                    else:
                        mini_location = "8"
                    enter()

            elif mini_location == '2':
                scrollTxt(f"This {orange}room{white} has pile of {red}red ooze{white} blocking the {darkgrey}hall{white}")
                scrollTxt(f"It smells {green}terrible{white}...")
                scrollTxt(f"{blue}Commands{white}: {teal}Inv{white}, {platinum}Stats{white}, {silver}Walk through ooze{white}, {darkgrey}Jump over{white}")
                answer = get_input(["inv", "stats", "walk through ooze", "jump over"])
                print()

                if answer == "inv":
                    inventory()
                    #enter()

                if answer == "stats":
                    printStats()
                    enter()

                if answer == "walk through ooze":
                    scrollTxt(f'Uhhhhh...')
                    time.sleep(1)
                    scrollTxt(f"Well you walk through the {red}ooze{white}...")
                    time.sleep(1)

                    scrollTxt(f"Your feet got {orange}burned{white} from the {lime}acid{white}")
                    scrollTxt(f"- 3 ❤️")
                    health -= 1
                    print()

                    if health < 1:
                        scrollTxt(f"This {red}kills{white} you!")
                        die()

                    scrollTxt(f"You continue to the next {darkgrey}room{white}")
                    scrollTxt(f"Would you like to go {turquoise}east{white} or {turquoise}south{white}?")
                    answer = get_input(["east", "south"])
                    print()
                    if answer == "east":
                        mini_location = "1"
                    else:
                        mini_location = "3"
                    enter()
                    mini_location = "3"
                if answer == "jump over":
                    if random.randint(1, 12) in range(1, dexterity + strength):
                        scrollTxt(f"You gracefully {teal}leap{white} across the {red}red ooze{white}!")
                        scrollTxt(f"You continue to the next {darkgrey}room{white}")
                        scrollTxt(f"Would you like to go {turquoise}east{white} or {turquoise}south{white}?")
                        answer = get_input(["east", "south"])
                        print()
                        if answer == "east":
                            mini_location = "1"
                        else:
                            mini_location = "3"
                    else:
                        scrollTxt(f"You make it only {red}half-way{white}...")

                        scrollTxt(f"You got {orange}burned{white} from the {lime}acid{white}"
                                    )
                        scrollTxt(f"- 5 ❤️")
                        health -= 5
                        print()

                        if health < 1:
                            scrollTxt(f"This {red}kills{white} you!")
                            die()

                        scrollTxt(f"You continue to the next {darkgrey}room{white}")
                        scrollTxt(f"Would you like to go {turquoise}east{white} or {turquoise}south{white}?")
                        answer = get_input(["east", "south"])
                        print()
                        if answer == "east":
                            mini_location = "1"
                        else:
                            mini_location = "3"
                    enter()
                    #mini_location = "3"
            
            elif mini_location == "3":
                scrollTxt(f"This {orange}room{white} has {yellow}friendly looking{white} {darkgrey}bearded{white} merchant")
                scrollTxt(f'"Hullo I\'m the {darkgrey}Dungeon Merchant{white}", says the {blue}Dungeon merchant{white}')
                scrollTxt(f"{blue}Commands{white}: {teal}Inv{white}, {platinum}Stats{white}, {silver}Merchant{white}, {darkgrey}Leave room{white}")
                answer = get_input(["inv", "stats", "merchant", "leave room"])
                print()

                if answer == "inv":
                    inventory()
                    #enter()

                if answer == "stats":
                    printStats()
                    enter()

                if answer == "merchant":
                    Shop(["plate shield", "great sword", "great axe"], [70, 70, 70], f"{darkgrey}The Dungeon Merchant{white}")
                
                if answer == "leave room":
                    scrollTxt(f"Would you like to go the to {blue}south{white} room or the {blue}north{white} room?")
                    answer =get_input(["north", "south"])
                    print()

                    scrollTxt(f"You open the {brown}door{white} to the {orange}{answer}{white}")
                    if answer == "north":
                        mini_location = "2"
                    else:
                        mini_location = "4"
                    enter()

            elif mini_location == "4":
                if "fought cube" not in rtriggers:
                    rtriggers.append("fought cube")

                    scrollTxt(f"The floor here is {purple}clean{white}... too {purple}clean{white}")
                    scrollTxt(f"You turn to see your {blue}answer{white}, a huge {green}gelatinous cube{white}!")
                    enter()

                    combat(["gelatinous cube"])
                    clear()
                    dungeon_map(mini_location)
                    print()

                scrollTxt(f"The floor here is {silver}clean{white}, very {silver}clean{white}")
                scrollTxt(f"{blue}Commands{white}: {teal}Inv{white}, {platinum}Stats{white}, {darkgrey}Leave room{white}")
                answer = get_input(["inv", "stats", "leave room"])
                print()

                if answer == "inv":
                    inventory()
                    #enter()

                if answer == "stats":
                    printStats()
                    enter()

                if answer == "leave room":
                    scrollTxt(f"Your {red}only{white} option is to go {orange}north{white}")
                    enter()

                    mini_location = "3"
                
            elif mini_location == "8":
                scrollTxt(f"This {orange}room{white} contains an array of {copper}rusty weapons{white}")
                if "attacked bug" not in rtriggers:
                    
                    scrollTxt(f"A large {darkgrey}bug-like creature{white} with even large {red}mandables{white} is in the corner of the {orange}room{white}")
                    scrollTxt(f"{blue}Commands{white}: {teal}Inv{white}, {platinum}Stats{white}, {silver}Attack bug{white}, {darkgrey}Leave room{white}")
                    answer = get_input(["inv", "stats", "attack bug", "leave room"])

                else:
                    scrollTxt(f"{blue}Commands{white}: {teal}Inv{white}, {platinum}Stats{white}, {darkgrey}Leave room{white}")
                    answer = get_input(["inv", "stats", "leave room"])
                print()

                if answer == "inv":
                    inventory()
                    #enter()

                if answer == "stats":
                    printStats()
                    enter()

                if answer == "attack bug":
                    rtriggers.append("attacked bug")
                    scrollTxt(f'You charge at the {copper}rusty bug{white}!')
                    enter()

                    combat(["rust monster"])

                if answer == "leave room":
                    scrollTxt(f"Would you like to go the to {blue}south{white} room or the {blue}west{white} room?")
                    answer = get_input(["west", "south"])
                    print()

                    scrollTxt(f"You open the {brown}door{white} to the {orange}{answer}{white}")
                    if answer == "west":
                        mini_location = "1"
                    else:
                        mini_location = "7"
                    enter()

            elif mini_location == "7":
                if "fought lich" not in rtriggers:
                    rtriggers.append("fought lich")

                    scrollTxt(f"You hear a {blue}voice{white} echo across the {orange}room{white}")
                    scrollTxt(f'"WHO {red}DARES{white} ENTER THE {darkgrey}LAIR{white} OF THE {gold}UNDEAD KING{white}!", the {blue}voice{white} says')
                    time.sleep(1)

                    scrollTxt(f"See a horrible {paleyellow}skeleton frame{white} holding a {turquoise}glowing blue staff{white}, walking towards you!")
                    enter()

                    combat(["lich"])
                    clear()
                    dungeon_map(mini_location)
                    print()


                scrollTxt(f"This {orange}room{white} is mostly empty. Its {green}smells{white} as if something {red}died{white} here.")
                scrollTxt(f"{blue}Commands{white}: {teal}Inv{white}, {platinum}Stats{white}, {darkgrey}Leave room{white}")
                answer = get_input(["inv", "stats", "leave room"])
                print()

                if answer == "inv":
                    inventory()
                    #enter()

                if answer == "stats":
                    printStats()
                    enter()

                if answer == "leave room":
                    scrollTxt(f"Would you like to go the to {blue}south{white} room, the {blue}west{white} room, or the {blue}north{white} room?")
                    answer = get_input(["west", "north", "south"])
                    print()

                    scrollTxt(f"You open the {brown}door{white} to the {orange}{answer}{white}")
                    if answer == "west":
                        mini_location = "9"
                    elif answer == "north":
                        mini_location = '8'
                    else:
                        mini_location = "6"
                    enter()

            elif mini_location == "6":
                if "open chest [dungeon]" not in triggers:
                    triggers.append("open chest [dungeon]")
                    scrollTxt(f"This {orange}room{white} is mostly empty but contains a single {brown}chest{white}")

                    scrollTxt(f"{blue}Commands{white}: {teal}Inv{white}, {platinum}Stats{white}, {brown}Open Chest{white}, {darkgrey}Leave room{white}")
                    answer = get_input(["inv", "stats", "open chest", "leave room"])
                    print()

                    if answer == "inv":
                        inventory()
                        #enter()

                    if answer == "stats":
                        printStats()
                        enter()

                    if answer == "open chest":
                        scrollTxt(f"As you open the {gold}chest{white} it {red}bites{white} you!")
                        scrollTxt(f"It\'s a {darkgrey}chest mimic{white}!")
                        enter()

                        combat(["chest mimic"])
                else:
                    scrollTxt(f"This {orange}room{white} is mostly empty, you see {darkgrey}scratch{white} marks on the wall")

                    scrollTxt(f"{blue}Commands{white}: {teal}Inv{white}, {platinum}Stats{white}, {darkgrey}Leave room{white}")
                    answer = get_input(["inv", "stats", "leave room"])
                    print()

                    if answer == "inv":
                        inventory()
                        #enter()

                    if answer == "stats":
                        printStats()
                        enter()

                if answer == "leave room":
                    scrollTxt(f"Your {red}only{white} option is to go {orange}north{white}")
                    enter()

                    mini_location = "7"

            elif mini_location == "9":
                if "open chest 2 [dungeon]" not in triggers:
                    triggers.append("open chest 2 [dungeon]")
                    scrollTxt(f"This {orange}room{white} is completly {darkgrey}empty{white} save a single {brown}chest{white}")

                    scrollTxt(f"{blue}Commands{white}: {teal}Inv{white}, {platinum}Stats{white}, {brown}Open Chest{white}, {darkgrey}Leave room{white}")
                    answer = get_input(["inv", "stats", "open chest", "leave room"])
                    print()

                    if answer == "inv":
                        inventory()
                        #enter()

                    if answer == "stats":
                        printStats()
                        enter()

                    if answer == "open chest":
                        scrollTxt(f"You open the {gold}chest{white}")
                        time.sleep(1)
                        scrollTxt(f"You found a {orange}phoenix shield{white}!")
                        inv.append("phoenix shield")
                        enter()

                else:
                    scrollTxt(f"This {orange}room{white} is mostly empty, you see {darkgrey}scratch{white} marks on the wall")

                    scrollTxt(f"{blue}Commands{white}: {teal}Inv{white}, {platinum}Stats{white}, {darkgrey}Leave room{white}")
                    answer = get_input(["inv", "stats", "leave room"])
                    print()

                    if answer == "inv":
                        inventory()
                        #enter()

                    if answer == "stats":
                        printStats()
                        enter()

                if answer == "leave room":
                    scrollTxt(f"Would you like to go the to {blue}south{white} room, or the {blue}east{white} room?")
                    answer = get_input(["east", "south"])
                    print()

                    scrollTxt(f"You open the {brown}door{white} to the {orange}{answer}{white}")
                    if answer == "east":
                        mini_location = "7"
                    else:
                        mini_location = "5"
                    enter()

            elif mini_location == "5":
                scrollTxt(f"The {darkgrey}doors{white} shut behind you...")
                time.sleep(1)
                scrollTxt(f"Piles of {gold}gold{white} and {red}gems{white} decorate the floor")
                time.sleep(1)

                scrollTxt(f"A large {darkgrey}black dragon{white} with {purple}glowing purple{white} streaks sits on the piles of {gold}gold{white}...")
                time.sleep(1)

                scrollTxt(f"You draw your {orange}{weapon}{white}, and the {red}FINAL BOSS FIGHT{white} has begun!")
                enter()

                combat(["the dark dragon"])

                scrollTxt(f"You stagger to the {orange}exit{white} barely {blue}alive{white}")
                scrollTxt(f"You open the {darkgrey}dungeon gate{white} and find yourself in the {lime}Overworld{white} once again")
                scrollTxt(f"{blue}~Dungeon Completed~{white}")
                print()
                scrollTxt(f"{darkgrey}~Tokens Obtained~{white}")
                inv.append("dungeon token")
                inv.append("world token")
                enter()

                break
            if pre_loc != mini_location:
                rtriggers = []
    

    def crypt_of_the_necromancer():
        mini_loc = "1"
        pre_loc = mini_loc 
        rtriggers = []


        def crypt_map(loc):
            if loc == "1":
                print(f"""     {darkgrey}██{white} - ██
     -    - 
██ - ██ - ██  Dungeon Map
     -    
     ██ - ██""")
                
            if loc == "2":
                print(f"""     ██ - {darkgrey}██{white}
     -    - 
██ - ██ - ██  Dungeon Map
     -    
     ██ - ██""")
                
            if loc == "3":
                print(f"""     ██ - ██
     -    - 
{darkgrey}██{white} - ██ - ██  Dungeon Map
     -    
     ██ - ██""")
                
            if loc == "4":
                print(f"""     ██ - ██
     -    - 
██ - {darkgrey}██{white} - ██  Dungeon Map
     -    
     ██ - ██""")
                
            if loc == "5":
                print(f"""     ██ - ██
     -    - 
██ - ██ - {darkgrey}██{white}  Dungeon Map
     -    
     ██ - ██""")
                
            if loc == "6":
                print(f"""     ██ - ██
     -    - 
██ - ██ - ██  Dungeon Map
     -    
    {darkgrey}██{white} - ██""")
                
            if loc == "7":
                print(f"""     ██ - ██
     -    - 
██ - ██ - ██  Dungeon Map
     -    
     ██ - {darkgrey}██{white}""")
            

        while True:
            clear()

            crypt_map(mini_loc)
            print()

            if mini_loc == "1":
                scrollTxt(f"This {blue}room{white} contains piles and piles of {paleyellow}bones{white} and {silver}skulls{white}.")
                scrollTxt(f"The {silver}bones{white} seem to be {ironc}fresh{white}...")
                if "defeated skeletons" not in rtriggers:
                    scrollTxt(f"Commands | {silver}take skull{white} / {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                    answer = get_input(["take skull", "leave", "stats", "inv"])
                else:
                    scrollTxt(f"Commands | {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                    answer = get_input([ "leave", "stats", "inv"])
                print()

                if answer == "take skull":
                    inv.append("skull")
                    scrollTxt(f"You pick up a {paleyellow}skull{white}")
                    scrollTxt(f"+ {silver}skull{white}")
                    print()
                    time.sleep(1)

                    scrollTxt(f"The {silver}bones{white} start to rattle as they sense a {red}stranger{white}...")
                    print()

                    scrollTxt(f"The move together to form {orange}4{white} {silver}skeletons{white}")
                    enter()

                    combat(["skeleton 1", "skeleton 2", "skeleton 3", "skeleton 4"])
                    scrollTxt(f"The {silver}bones{white} are now more scattered across the {blue}room{white}")
                    enter()

                    rtriggers.append("defeated skeletons")

                if answer == "leave":
                    if 'defeated skeletons' not in rtriggers:
                        scrollTxt(f"The {silver}bones{white} start to rattle as they sense a {red}stranger{white}...")
                        print()

                        scrollTxt(f"The move together to form {orange}4{white} {silver}skeletons{white}")
                        enter()

                        combat(["skeleton 1", "skeleton 2", "skeleton 3", "skeleton 4"])
                        scrollTxt(f"The {silver}bones{white} are now more scattered across the {blue}room{white}")
                        enter()

                    print()

                    scrollTxt(f"Directions | {purple}south{white} / {darkgrey}east{white}")
                    answer = get_input(["south", "east"])
                    print()

                    if answer == "south":
                        mini_loc = "4"
                    else:
                        mini_loc = "2"

                if answer == "inv":
                    inventory()

                if answer == "stats":
                    printStats()

            elif mini_loc == "3":
                scrollTxt(f"This {blue}room{white} contains heap and heaps of {gold}treasure{white}")
                scrollTxt(f"You also can make out a {red}huge ruby{white}!")
                if "take treasure" not in triggers:
                    scrollTxt(f"Commands | {silver}take ruby{white} / {gold}take treasure{white} / {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                    answer = get_input(["take ruby", "take treasure", "leave", "stats", "inv"])
                else:
                    scrollTxt(f"Sadly your {brown}backpack{white} is too full to fit anything else")
                    scrollTxt(f"Commands | {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                    answer = get_input([ "leave", "stats", "inv"])
                print()

                if answer == "take ruby":
                    triggers.append("take treasure")
                    scrollTxt(f"You pick up the {red}giant ruby{white}")
                    scrollTxt(f"+ {red}master ruby{white}")
                    inv.append("master ruby")
                    enter()

                if answer == "take treasure":
                    triggers.append("take treasure")
                    scrollTxt(f"You put tons of {gold}gold{white} into your {brown}backpack{white}")
                    scrollTxt(f"+ {gold}50{white} 🔶")
                    gp += 50
                    enter()


                if answer == "leave":

                    print()

                    scrollTxt(f"Directions | {purple}south{white} / {darkgrey}east{white}")
                    answer = get_input(["east"])
                    print()

                    mini_loc = "4"

                if answer == "inv":
                    inventory()

                if answer == "stats":
                    printStats()

            elif mini_loc == "2":
                if "giant rats" not in triggers:
                    triggers.append("giant rats")
            
                    scrollTxt(f"This {blue}room{white} a group of {darkgrey}giant rats{white}!")
                    scrollTxt(f"They all {red}charge{white} at you!")
                    enter()
                    print()

                    combat(["giant rat 1", "giant rat 2", "giant rat 3", "giant rat 4", "giant rat 5"])
                else:
                    scrollTxt(f"This {blue}room{white} is empty")

               
                    scrollTxt(f"Commands | {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                    answer = get_input([ "leave", "stats", "inv"])
                    print()


                    if answer == "leave":
                        scrollTxt(f"Directions | {purple}south{white} / {darkgrey}west{white}")
                        answer = get_input(["south", "west"])
                        print()

                        if answer == "south":
                            mini_loc = "5"
                        else:
                            mini_loc = "1"

                    if answer == "inv":
                        inventory()

                    if answer == "stats":
                        printStats()
            
            elif mini_loc == "4":
                if "zombies" not in triggers:
                    triggers.append("zombies")
            
                    scrollTxt(f"This {blue}room{white} a horde of {green}zombies{white}!")
                    scrollTxt(f"They hobble toward {blue}you{white}!")
                    enter()
                    print()

                    combat(["zombie", "zombie 2", "zombie 3"])
                else:
                    scrollTxt(f"This {blue}room{white} is empty")

               
                    scrollTxt(f"Commands | {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                    answer = get_input([ "leave", "stats", "inv"])
                    print()


                    if answer == "leave":
                        scrollTxt(f"Directions | {red}north{white} / {purple}south{white} / {silver}east{white} / {darkgrey}west{white}")
                        answer = get_input(["north", "east", "south", "west"])
                        print()

                        if answer == "north":
                            mini_loc = "1"
                        if answer == "south":
                            mini_loc = "6"
                        if answer == "east":
                            mini_loc = "5"
                        if answer == "west":
                            mini_loc = "3"

                    if answer == "inv":
                        inventory()

                    if answer == "stats":
                        printStats()

            elif mini_loc == "5":
                if "lich mini boss" not in triggers:
                    triggers.append("lich mini boss")
            
                    scrollTxt(f"You see a frail {silver}skeleton like{white} figure holding a {purple}glowing purple{white} {darkgrey}staff{white}")
                    scrollTxt(f"With a wave of the {purple}staff{white} the doors shut behind you!")
                    enter()
                    

                    combat(["lich"])
                else:
                    scrollTxt(f"This {blue}room{white} is empty")

               
                    scrollTxt(f"Commands | {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                    answer = get_input([ "leave", "stats", "inv"])
                    print()


                    if answer == "leave":
                        scrollTxt(f"Directions | {red}north{white} / {purple}south{white} / {darkgrey}west{white}")
                        answer = get_input(["north", "south", "west"])
                        print()

                        if answer == "north":
                            mini_loc = "2"
                        if answer == "south":
                            mini_loc = "7"
                        if answer == "west":
                            mini_loc = "4"

                    if answer == "inv":
                        inventory()

                    if answer == "stats":
                        printStats()

            elif mini_loc == "6":
                if "death knight mini boss" not in triggers:
                    triggers.append("death knight mini boss")
            
                    scrollTxt(f"You see a {silver}ghostly{white} {darkgrey}iron knight{white} with {orange}glowing orange{white} eyes")
                    scrollTxt(f"The {darkgrey}death knight{white} unsheathes a {red}gleeming red{white} blade with {silver}skulls{white} on it")
                    enter()
                    

                    combat(["death knight"])
                else:
                    scrollTxt(f"This {blue}room{white} is empty")

               
                    scrollTxt(f"Commands | {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                    answer = get_input([ "leave", "stats", "inv"])
                    print()


                    if answer == "leave":
                        scrollTxt(f"Directions | {red}north{white} / {purple}south{white} / {darkgrey}west{white}")
                        answer = get_input(["north", "east"])
                        print()

                        if answer == "north":
                            mini_loc = "4"
                        if answer == "east":
                            mini_loc = "7"

                    if answer == "inv":
                        inventory()

                    if answer == "stats":
                        printStats()

            elif mini_loc == "7":
                scrollTxt(f"The {darkgrey}doors{white} shut behind you...")
                time.sleep(1)
                print()
                scrollTxt(f"{orange}Illliuminated{white} atop a gold {gold}throne{white} sits a {silver}skeleton{white}")
                scrollTxt(f"Adorned with a {gold}golden crown{white} and a {green}glowing green{white} staff")
                time.sleep(1)
                print()

                scrollTxt(f"The {purple}necromancer{white}\'s pale {lime}green{white} eyes stare directly at you")
                time.sleep(1)
                print()

                scrollTxt(f"You draw your {orange}{weapon}{white}, and the {red}BOSS FIGHT{white} has begun!")
                enter()

                combat(["necromancer"])

                scrollTxt(f"You stagger to the {orange}exit{white} barely {blue}alive{white}")
                scrollTxt(f"You open the {darkgrey}dungeon gate{white} and find yourself in the {lime}Overworld{white} once again")
                scrollTxt(f"{blue}~Dungeon Completed~{white}")
                print()
                scrollTxt(f"{purple}~LEGENDARY ITEM OBTAINED~{white}")
                print()
                print()
                scrollTxt(f"{darkgrey}~Next Token Obtained~{white}")
                print()
                inv.append("dungeon token")
                inv.append("kinetic shield [0]")
                triggers.append("dungeon completed [crypt of the necromancer]")
                enter()

                break

            if pre_loc != mini_loc:
                rtriggers = []


    def the_furious_jungle():
        mini_loc = "1"
        pre_loc = mini_loc 
        rtriggers = []

        def jungle_map(loc):
            if loc == "1":
                print(f"""     {lime}██{white}
     |
██ - ██ - ██  Jungle Map
     |    | 
     ██ - ██ - ██
""")
                
            if loc == "2":
                print(f"""     ██
     |
{lime}██{white} - ██ - ██  Jungle Map
     |    | 
     ██ - ██ - ██
""")
                
            if loc == "3":
                print(f"""     ██
     |
██ - {lime}██{white} - ██  Jungle Map
     |    | 
     ██ - ██ - ██
""")
                
            if loc == "4":
                print(f"""     ██
     |
██ - ██ - {lime}██{white}  Jungle Map
     |    | 
     ██ - ██ - ██
""")
                
            if loc == "5":
                print(f"""     ██
     |
██ - ██ - ██  Jungle Map
     |    | 
     {lime}██{white} - ██ - ██
""")
                
            if loc == "6":
                print(f"""     ██
     |
██ - ██ - ██  Jungle Map
     |    | 
     ██ - {lime}██{white} - ██
""")
                
            if loc == "7":
                print(f"""     ██
     |
██ - ██ - ██  Jungle Map
     |    | 
     ██ - ██ - {lime}██{white}
""")
            

        while True:
            clear()

            jungle_map(mini_loc)
            print()

            if mini_loc == "1":
                scrollTxt(f"This {blue}room{white} contains {red}2{white} {lime}kobolds{white} branshings {darkgrey}scimitars{white}")
                enter()
                combat(["kobold 1", "kobold 2"])
                scrollTxt(f"The {blue}room{white} is empty for {red}now{white}...")
                scrollTxt(f"Commands | {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                answer = get_input([ "leave", "stats", "inv"])
                print()


                if answer == "leave":
                    scrollTxt(f"Directions | {purple}south{white}")
                    answer = get_input(["south"])
                    print()

                    if answer == "south":
                        mini_loc = "3"

                if answer == "inv":
                    inventory()

                if answer == "stats":
                    printStats()

            elif mini_loc == "6":
                scrollTxt(f"This {blue}room{white} contains a {darkgrey}merchant{white} carring a small {brown}backpack{white}")
                scrollTxt(f"Commands | {silver}merchant{white} / {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                answer = get_input(["merchant", "leave", "stats", "inv"])
                print()


                if answer == "leave":
                    scrollTxt(f"Directions | {purple}north{white} / {darkgrey}east{white} / {red}west{white}")
                    answer = get_input(["north", "east", "west"])
                    print()

                    if answer == "north":
                        mini_loc = "4"
                    elif answer == "east":
                        mini_loc = "7"
                    elif answer == "west":
                        mini_loc = "5"

                if answer == "merchant":
                    scrollTxt(f"You walk up to the {darkgrey}merchant{white}")
                    Shop(["hyper heal potion", "tortoise potion", "heart sword"], [10, 10, 120], f"{green}Lost{white} Merchant", sp = 20)

                if answer == "inv":
                    inventory()

                if answer == "stats":
                    printStats()

            elif mini_loc == "4":
                scrollTxt(f"This {blue}room{white} contains a {red}growling{white} 10ft long {lime}MUTANT JAGUAR{white}!")
                enter()
                combat(["mutant jaguar"])
                scrollTxt(f"The {blue}room{white} is empty for {red}now{white}...")
                scrollTxt(f"Commands | {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                answer = get_input([ "leave", "stats", "inv"])
                print()


                if answer == "leave":
                    scrollTxt(f"Directions | {purple}south{white} / {darkgrey}west{white}")
                    answer = get_input(["south", "west"])
                    print()

                    if answer == "south":
                        mini_loc = "6"
                    else:
                        mini_loc = "3"

                if answer == "inv":
                    inventory()

                if answer == "stats":
                    printStats()

            elif mini_loc == "5":
                scrollTxt(f"This {blue}room{white} contains {red}2{white} {brown}bugbears{white} holding {darkgrey}huge axes{white}")
                enter()
                combat(["bugbear", "bugbear 2"])
                scrollTxt(f"The {blue}room{white} is empty for {red}now{white}...")
                scrollTxt(f"Commands | {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                answer = get_input([ "leave", "stats", "inv"])
                print()


                if answer == "leave":
                    scrollTxt(f"Directions | {purple}south{white} / {darkgrey}east{white}")
                    answer = get_input(["north", "east"])
                    print()

                    if answer == "north":
                        mini_loc = "3"
                    else:
                        mini_loc = "6"

                if answer == "inv":
                    inventory()

                if answer == "stats":
                    printStats()

            elif mini_loc == "3":
                scrollTxt(f"This {blue}room{white} has a statue of a {orange}sphinx{white} made out of {lime}mossy{white} {darkgrey}stone{white}")
                scrollTxt(f"Commands | {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                answer = get_input([ "leave", "stats", "inv"])
                print()


                if answer == "leave":
                    scrollTxt(f'The {orange}sphinx{white} rummbles and {blue}tells{white} you a riddle...')
                    scrollTxt(f"""I\'m hidden in the {green}jungle\'s{white} deep,
A slithering {red}creature{white}, not for sleep.
Patterned skin, scales shine so {gold}bright{white},
{lime}Venomous{white} bite, causing a fright.
What am I, in {purple}shadows{white} I creep?
""")
                    answer = input("> ").lower()
                    print()

                    if answer in ["python", "snake", "rattlesnake", "a python", "a snake"]:
                        scrollTxt(f"Correct ✅")
                        scrollTxt(f"The {orange}sphinx{white} allows you to pass")
                    else:
                        scrollTxt(f"Incorrect ❌")
                        scrollTxt(f"A {green}huge python{white} materializes blocking the {brown}path{white}.")
                        enter()
                        combat(["huge python"])
                    print()
                              
                    scrollTxt(f"Directions | {purple}south{white} / {darkgrey}east{white} / {red}north{white} / {silver}west{white}")
                    answer = get_input(["north", "east", "west", "south"])
                    print()

                    if answer == "north":
                        mini_loc = "3"
                    elif answer == "east":
                        mini_loc = "4"
                    elif answer == "west":
                        mini_loc = "2"
                    else:
                        mini_loc = "5"

                if answer == "inv":
                    inventory()

                if answer == "stats":
                    printStats()

            elif mini_loc == "2":
                scrollTxt(f"{yellow}Sunlight{white} pours throught an opening in the {lime}Jungle{white}")
                if "jungle staff" not in triggers:
                    scrollTxt(f"The {gold}light{white} shimmers refelcting off a {brown}wooden staff{white} with a {green}glowing green crystal{white}")
                    scrollTxt(f"Commands | {silver}take staff{white} / {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                    answer = get_input([ "take staff" , "leave", "stats", "inv"])
                else:
                    scrollTxt(f"Commands | {red}leave{white} / {purple}inv{white} / {darkgrey}stats{white}")
                    answer = get_input(["leave", "stats", "inv"])
                print()

            
                if answer == "take staff":
                    scrollTxt(f"You carefully life the {brown}wooden staff{white} out of a {green}mossy{white} {darkgrey}stone{white}")
                    scrollTxt(f"+ {green}earth {brown}staff{white}")
                    enter()

                    inv.append("earth staff")


                if answer == "leave":
                    scrollTxt(f"Directions | {darkgrey}east{white}")
                    answer = get_input(["east"])
                    print()

                    mini_loc = "3"

                if answer == "inv":
                    inventory()

                if answer == "stats":
                    printStats()

            elif mini_loc == "7":
                scrollTxt(f"The {green}Jungle{white} closes in on you...")
                time.sleep(1)
                print()
                scrollTxt(f"A massive {lime}mossy{white} {darkgrey}stone{white} golem stands in front a large {silver}rock{white}")
                scrollTxt(f"Imbeded in the {silver}stone{white} is a {brown}wooden{white} sword covered in {purple}vines{white}")
                time.sleep(1)
                print()

                scrollTxt(f"The {darkgrey}Golems{white}\'s pale {turquoise}blue{white} eyes stare directly at you")
                time.sleep(1)
                print()

                scrollTxt(f"You draw your {orange}{weapon}{white}, and the {red}BOSS FIGHT{white} has begun!")
                enter()

                combat(["guardian of the jungle"])

                scrollTxt(f"You stagger to the {orange}exit{white} barely {blue}alive{white}")
                scrollTxt(f"You exit the {green}Jungle{white} and find yourself in the {lime}Overworld{white} once again")
                scrollTxt(f"{blue}~Dungeon Completed~{white}")
                print()
                scrollTxt(f"{purple}~LEGENDARY ITEM OBTAINED~{white}")
                print()
                print()
                scrollTxt(f"{darkgrey}~Next Token Obtained~{white}")
                print()
                inv.append("dungeon token")
                inv.append("flameblade")
                triggers.append("dungeon completed [furious jungle]")
                enter()

                break

            if pre_loc != mini_loc:
                rtriggers = []


    def manage_inv():
        global inv
        inv_sort = {}
        for x in inv:
            if x not in inv_sort:
                inv_sort[x] = 1
            else:
                inv_sort[x] += 1
        inv = []

        for x in inv_sort:
            for i in range(1, inv_sort[x] + 1): inv.append(x)

        
    if False: input(str(100 - (100 / ( (20 + int(input("Enemy Dex: ")) - int(input("Dodge Amount: ")) ) / (20 + int(input("Enemy Dex: ")) - int(input("Dodge Amount: ")) - (int(input("Block Ability: ")) + int(input("Dodge amout: ")) - int(input("Enemy Dex: ")) ) )))))
    if False:
        input(f"Items: {len(items_all)}")
        input(f"Weapons: {len(weapons_all)}")
        input(f"Shields: {len(shield_all)}")
        input(f"Enemies: {len(enemies_all)}")

    clear(False)
    scrollTxt(f"{grey}Overdrive{white}{turquoise}Games{white} presents...")
    time.sleep(1)

    clear(False)

    title3()

    enter()

    ce = False

    try:
        scrollTxt(f"Would you like to {orange}load{white} a {turquoise}save{white} [{green}y/n{white}]")
        answer = get_input(['yes', 'no'])
        scrollTxt()

        if answer == "yes":
            clear()
            load_data()
            
            
        
            scrollTxt(f"Loading {turquoise}Save{white}...")
            time.sleep(1)
            scrollTxt(f"{green}>>Save Loaded<<{white}")
            enter()
            clear()
            if location == "jade forest": location = "magic forest"
            

            if True:
                    clrs = ["normal", "green", "blue", "purple", "red", "orange", "black"]
                    zx = 0
                    gg = False
                    clr_code = {
                        "green": '\x1b[38;2;00;160;00m\x1b[1m',
                        "blue": '\x1b[38;2;0;40;255m\x1b[1m',
                        "purple": '\x1b[38;2;130;0;250m\x1b[1m',
                        "red": '\x1b[0;31m\x1b[1m',
                        "orange": '\x1b[38;2;255;90;0m\x1b[1m',
                        "black": '\x1b[38;2;100;100;100m\x1b[1m',
                    }

                    for x in clrs:
                        if x != settings["color"] and gg == False:
                            zx += 1
                        else:
                            gg = True

                    

                    try:
                        settings["color"] = clrs[zx]
                    except:
                        settings["color"] = "normal"

                    if settings["color"] != "normal":
                        color_a = clr_code[settings["color"]]
                        bold = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        normal = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        italic = '\x1B[3m'

                        gold = color_a
                        silver = color_a
                        copper = color_a

                        paleyellow = color_a
                        lime = color_a
                        turquoise = color_a
                        teal = color_a

                        yellow = color_a
                        green = color_a
                        blue = color_a
                        purple = color_a
                        brown = color_a
                        red = color_a
                        orange = color_a

                        darkgrey = color_a
                        grey = color_a

                        white = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        platinum = color_a
                        ironc = color_a
                    else:
                        bold = '\x1b[1m'
                        normal = '\x1b[0m' + '\x1b[38;2;255;255;255m'
                        italic = '\x1B[3m'

                        gold = '\x1b[38;2;230;190;0m\x1b[1m'
                        silver = '\x1b[38;2;221;221;221m\x1b[1m'
                        copper = '\x1b[38;2;170;44;0m\x1b[1m'

                        paleyellow = '\x1b[38;2;255;255;215m\x1b[1m'
                        lime = '\x1b[38;2;00;255;00m\x1b[1m'
                        turquoise = '\x1b[38;2;0;255;255m\x1b[1m'
                        teal = '\x1b[38;2;0;170;170m\x1b[1m'

                        yellow = '\x1b[38;2;255;255;0m\x1b[1m'
                        green = '\x1b[38;2;00;160;00m\x1b[1m'
                        blue = '\x1b[38;2;0;40;255m\x1b[1m'
                        purple = '\x1b[38;2;130;0;250m\x1b[1m'
                        brown = '\x1b[38;2;135;62;35m\x1b[1m'
                        red = '\x1b[0;31m\x1b[1m'
                        orange = '\x1b[38;2;255;90;0m\x1b[1m'

                        darkgrey = '\x1b[38;2;100;100;100m\x1b[1m'
                        grey = '\x1b[38;2;130;130;130m\x1b[1m'

                        white = '\x1b[38;2;255;255;255m\x1b[1m'
                        platinum = '\x1b[38;2;205;192;255m\x1b[1m'
                        ironc = '\x1b[38;2;255;205;192m\x1b[1m'
        else:
            clear()

            scrollTxt(f"Creating {turquoise}Save{white}...")
            time.sleep(1)
            scrollTxt(f"{green}>>Save Created<<{white}")
            enter()
            clear()
            ce = True
            createError
    except:
        if ce is False:
            scrollTxt(f"[{red}Save failed to load{white}]")
            enter()
        clear()
        scrollTxt()

        scrollTxt(f"{white}Choose a {blue}class{white}")
        scrollTxt(f"[{green}Thief{white}]{grey}      - Medium strength | Lots of dexterity | Dagger | Potions{white}")
        scrollTxt(f"[{teal}Ranger{white}]{grey}     - Good strength | Good dexterity | Short Bow & Items{white}")
        scrollTxt(f"[{orange}Warrior{white}]{grey}    - Good strength | Good dexterity | Sword & Shield{white}")
        scrollTxt(
            f"[{purple}Mage{white}]{grey}       - Weak strength | Ok dexterity | Quartz Staff | Spells {white}")
        scrollTxt(
            f"[{red}Barbarian{white}]{grey}  - Lots of strength | Ok dexterity | Axe & Goblin Shield | CAN'T DODGE!{white}")

        answer = get_input(['thief', 'warrior', 'mage', "barbarian", "ranger"], invis_commands=["monk"])
        scrollTxt()

        fighter_class = answer

        scrollTxt("")

        answer = fighter_class

        if answer == "thief":
            strength = 3
            dexterity = 5

            max_health = 15
            health = max_health

            gp = 10

            known_spells = []

            inv = ['dagger', 'health potion', 'health potion', 'potion of knowledge']
            special_moves.append("steal gold")

        if answer == "warrior":
            strength = 4
            dexterity = 3

            max_health = 20
            health = max_health

            gp = 5

            known_spells = []

            inv = ['wooden sword', 'wooden shield', 'health potion']
            offhand = "wooden shield"
            special_moves.append("inflict")
            shield_moves.append("inflict")

        if answer == "mage":
            strength = 2
            dexterity = 3

            max_health = 15
            health = max_health

            gp = 5

            inv = ['quartz staff', 'magi potion', "health potion"]
            special_moves.append("jellify")
            shield_moves.append("jellify")

        if answer == "barbarian":
            strength = 5
            dexterity = 3

            max_health = 22
            health = max_health

            gp = 2

            known_spells = []

            inv = ['axe', 'goblin shield', 'health potion']
            special_moves.remove("dodge")

            special_moves.append("rage")
            shield_moves.append("rage")

            if "winded dodge" in special_moves:
                special_moves.remove("winded dodge")
                shield_moves.remove("winded dodge")

            offhand = "goblin shield"

        if answer == "ranger":
            strength = 4
            dexterity = 5

            max_health = 17
            health = max_health

            gp = 2

            known_spells = []

            inv = ['short bow', 'rope', 'torch', 'water bottle']
            special_moves.append("winded dodge")
            special_moves.remove("dodge")

        if answer == "monk":
            strength = 5
            dexterity = 5

            max_health = 25
            health = max_health

            gp = 0

            known_spells = []
            #crystals = 10

            inv = ['health potion', 'ember potion']

            special_moves.append("ocean calm")
            shield_moves.append("ocean calm")

            offhand = "none"

            fighter_class = "monk"

        current_spells = known_spells.copy()

        try:
            if fighter_class != "monk": weapon = inv[0]
        except:
            weapon = "none"
        scrollTxt(f"{orange}Strength{white} | {strength}")
        scrollTxt(f"{blue}Dexterity{white} | {dexterity}")
        scrollTxt(f"{red}Health{white} | {health}")
        print()
        scrollTxt(f"{gold}Gold{white} | {gp}")
        print()
        scrollTxt(f"{grey}Inv{white} | {inv}")
        scrollTxt(f"{purple}Spells{white} | {known_spells}")


        try:
            if os.environ['REPL_OWNER'] == "NoteitDOWN4352":
                print()
                scrollTxt(f"You got {darkgrey}note-it-downs saber{white}!")
                inv.append("note-it-downs saber")
            if os.environ['REPL_OWNER'] == "OverdriveReplit":
                print()
                scrollTxt(f"You got {darkgrey}note-it-downs saber{white}!")
                inv.append("lightning spear")

            if os.environ['REPL_OWNER'] == "chromebot":
                print()
                scrollTxt(f"You got {darkgrey}steel sword{white}!")
                inv.append("steel sword")

            if os.environ['REPL_OWNER'] in ["NathanPang1", "Nathan Pang"]:
                print()
                scrollTxt(f"You got {teal}Nathans Jade Claymore{white}!")
                inv.append("nathans jade claymore")
                
            if os.environ['REPL_OWNER'] in "PiggyReplit":
                print()
                scrollTxt(f"You got {brown}Warhog blade{white}!")
                inv.append("warhog blade")
            if os.environ["REPL_OWNER"] == "LucasPingPong":
                print()
                scrollTxt(f"You got {darkgrey}cotopia staff{white}!")
                inv.append(f"cotopia staff")


                
        except:
            pass

        try:
            if db['coins'] > 0:
                gp += db["coins"]
                print()
                cg = db['coins']
                scrollTxt(f"You got {gold}{cg}{white} gold from a previous {blue}run{white}!")
                db["coins"] = 0
        except:
            pass

        try:
            if db['saved item'] != "none":
                inv.append(db["saved item"])
                print()
                cg = db['saved item']
                scrollTxt(f"You got a {darkgrey}{cg}{white} from a previous {blue}run{white}!")
                db["saved item"] = "none"

                try:
                    if db["saved item items all"] != "none":
                        items_all[cg] = loads(db.get_raw("saved item items all"))
                        db["saved item items all"] = "none"
                except:
                    pass

                try:
                    if db["saved item weapons all"] != "none":
                        weapons_all[cg] = loads(db.get_raw("saved item weapons all"))
                        db["saved item weapons all"] = "none"
                except:
                    pass

                try:
                    if db["saved item shield all"] != "none":
                        shield_all[cg] = loads(db.get_raw("saved item shield all"))
                        db["saved item shield all"] = "none"
                except:
                    pass

                
                try:
                    (strength_weapons, dexterity_weapons, health_weapons, steal_weapons, defense_weapons, luck_weapons, double_bladed_weapons, offhand_weapons, durability_weapon) = loads(db.get_raw("all weapons stuff"))
                except:
                    pass
        except:
            pass

        print()
        scrollTxt(f"Would you like a {orange}starter chest{white}? [{green}y{white}/{red}n{white}]")
        scrollTxt(f"Gives small amount of {blue}items{white} (reconmended for {darkgrey}new players{white})")
        answer = get_input(["yes", "no"])
        print()

        if answer == "yes":
            scrollTxt(f"You open the {brown}chest{white} 🎁")
            print()
            scrollTxt(f" + 5 {red}health potions{white} 🔻")
            scrollTxt(f" + 1 {gold}luck potion{white} ⚱️")
            scrollTxt(f" + 1 {copper}bronze sword{white} 🗡️")
            scrollTxt(f" + 1 {copper}bronze shield{white} 🛡️")
            for num in range(1, 5): inv.append("health potion")
            inv.append("luck potion")
            inv.append("bronze sword")
            inv.append("bronze shield")
        else:
            scrollTxt(f"Looks like you a {orange}TRUE HARDCORE{white} {darkgrey}PLAYER{white}!")
        print()

        enter() 
        clear()

        scrollTxt(f"Here is a test {copper}encounter{white} [{purple}s{white} to {blue}skip{white}]")
        a = input()

        if testing == False and a != "s":
            combat(['goblin'])
        clear()

        save()
    
    while True:
        manage_inv()
                
        if "power guantlets" in inv:
            inv.remove("power guantlets")
            inv.append("power gauntlets")
        if "flame blade" in inv:
            inv.remove("flame blade")
            inv.append("flameblade")
        if "platnium" in inv:
            inv.remove("platnium shield")
            inv.append("platinum shield")
      
        if "frozent katana" in inv:
                inv.remove("frozent katana")

        weapons_all["power gauntlets"]["damage"] = strength
        weapons_all["power gauntlets"]["hit"] = dexterity
        enemies_all["you"]["health"] = max_health
        try:
            enemies_all["you"]["damage"] = int(weapons_all[weapon]["damage"] * 1.2)
        except:
            enemies_all["you"]["damage"] = strength
        try:
            enemies_all["you"]["dex"]= dexterity + weapons_all[weapon]["hit"]
        except:
            enemies_all["you"]["dex"] = dexterity
        enemies_all["you"]["str"] = strength
        enemies_all["you"]["gold"] = gp
        try:
            enemies_all["you"]["armor"] = int(shield_all[offhand]["guard"] * 1.2)
        except:
            enemies_all["you"]["armor"] = min(dexterity*2, 12)
        enemies_all["you"]["exp"] = exp_max
        try:
            if weapons_all[weapon]["special"] != False and type([1, 2,3]) != (weapons_all[weapon]["special"]): enemies_all['you']["elemental"] = weapons_all[weapon]["special"]
            if enemies_all['you']["elemental"] in ["hyper bleed", "hyper freeze", "dragon burn", "crunch", "lightning"]: enemies_all['you']["elemental"] = "none"
        except:
            pass
        #input(items_all)
        clear()
        if settings["auto saving"]: save()

        pre_loc = location

        if world == "farcore":

            if location == "lockwood":
                scrollTxt(f"~[{green}LOCKWOOD{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding {green}lockwood{white} is open {lime}grass plains{white} to the {teal}east{white} and {teal}west{white}, a {purple}purple snowy mountain{white} to the {teal}south{white} and the {blue}ocean{white} to the {teal}north{white}{normal}{bold}")
                    scrollTxt("")

                if "lockwood" not in triggers:
                    triggers.append("lockwood")
                    scrollTxt(
                        f"{italic}People mull around the {brown}town{white}. There is a large {brown}wooden tavern{white} labeled {grey}'The Black Boar'{white}. {paleyellow}Merchants{white} shout out from tents set up in the {red}Market Square{white}. {normal}{bold}")
                    scrollTxt(f"{blue}~Tip: Check out the bookstore | In market square~{white}")

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}People mull around the {brown}town{white}. There is a large {brown}wooden tavern{white} labeled {grey}'The Black Boar'{white}. {paleyellow}Merchants{white} shout out from tents set up in the {red}Market Square{white}. {normal}{bold}")

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {green}Inv : Stats : Settings : Save | Inn : Converse : Market Square : Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", 'inn', 'converse', 'market square', 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "inn":
                    while True:
                        clear()
                        scrollTxt("")
                        scrollTxt(f"~[{grey}THE BLACK BOAR{white}]~")
                        scrollTxt("")
                        scrollTxt(
                            f"The {brown}tavern{white} is filled with {yellow}cheerful{white} {turquoise}music{white}. People sit around tables playing {purple}cups{white}. A {paleyellow}bartender{white} is serving a {orange}Flaming Dragon{white} to someone.")
                        scrollTxt(f"{turquoise}What would you like to do{white}?")
                        scrollTxt(f"> {green}Inv : Stats : Settings : Save | Bards : Games : Bartender : Leave{white}")
                        answer = get_input(['inv', 'stats', 'settings', "save", 'bards', 'games', 'bartender', "leave"])
                        print()

                        usual_options(answer)

                        if answer == "bards":
                            scrollTxt(f"You walk over to the {orange}bards{white} playing {blue}music{white}.")
                            scrollTxt(f"Would you like to {gold}tip{white} them? [{green}y/n{white}]")
                            answer = get_input(['yes', 'no'])
                            scrollTxt(f"")

                            if answer == "yes":
                                scrollTxt(f"- {gold}1{white} GP")
                            else:
                                scrollTxt(f"You walk away...")

                            enter()

                        if answer == 'games':
                            scrollTxt(f"You walk over to the {blue}people{white} playing {silver}cups{white}.")
                            scrollTxt(f"Would you like to {teal}join{white} them? [{green}y/n{white}]")
                            answer = get_input(['yes', 'no'])
                            scrollTxt(f"")

                            if answer == "yes":
                                scrollTxt(f"You play {silver}cups{white}")
                                enter()

                                cups()

                            else:
                                scrollTxt("You walk away...")

                            enter()

                        if answer == "leave":
                            scrollTxt(f"You walk out of the {darkgrey}inn{white}...")
                            enter()
                            break

                        if answer == "bartender":
                            scrollTxt(f"What would you like to {blue}buy{white}?")
                            Shop(["flaming dragon drink", 'spiders bite drink', 'frost mead'], [6, 7, 5],
                                    f"{darkgrey}The Black Boar{white}", 20)

                elif answer == "market square":
                    scrollTxt(f"You walk over to the {red}Market Square{white}")
                    enter()

                    clear()

                    while True:
                        clear()
                        clear()
                        scrollTxt("")
                        scrollTxt(f"~[{orange}MARKET SQUARE{white}]~")
                        scrollTxt("")
                        scrollTxt(
                            f"{paleyellow}Merchants{white} are everywhere with tents {red}shouting{white} out what they are {yellow}selling{white}.")
                        scrollTxt(f"{turquoise}Which merchant would you like to go to{white}?")
                        scrollTxt(f"{green}> Weapons Smith : Shield Smith : Potions Master : Staff Crafter : Book Store : Leave{white}")
                        answer = get_input(["weapons smith", 'shield smith', 'potions master', 'staff crafter', "book store", 'leave'])
                        print()

                        if answer == "weapons smith":
                            scrollTxt(f"You walk over to the {darkgrey}weapons smith{white}...")
                            Shop(["wooden sword", 'bronze sword', 'iron sword', 'steel sword'], [10, 30, 60, 100],
                                    f"{grey}Greybeards{white} {silver}Smith{white} Shop")
                        if answer == "shield smith":
                            scrollTxt(f"You walk over to the {darkgrey}shield smith{white}...")
                            Shop(["wooden shield", 'bronze shield', 'iron shield', 'steel shield'], [7, 25, 55, 80],
                                    f"{brown}Tara's{white} {copper}Shields{white}")
                        if answer == "potions master":
                            scrollTxt(f"You walk over to the {red}potions master{white}...")
                            Shop(["health potion", 'potion of knowledge', 'magi potion', 'ember potion'], [2+lvl, 15, 5, 20],
                                    f"{red}THE POTION {orange}MASTER{white}", 20)
                        if answer == "staff crafter":
                            scrollTxt(f"You walk over to the {copper}staff crafter{white}...")
                            Shop(["quartz staff", 'sapphire staff', 'ruby staff', 'citrine staff'], [50, 70, 100, 150],
                                    f"{turquoise}Sub-natural Staffs{white}")
                        if answer == "book store":
                            scrollTxt(f"You walk over to the {brown}book store{white}")
                            Shop(["map", "guide", "monster book", "reykrs book", "andrew dengs book", "nj wolfs book", "shadow samurias book"], [10, 8, 10, 6, 6, 6, 6], f"{brown}Books{white} n {copper}Brooks{white}", 20)
                        if answer == "leave":
                            scrollTxt(f"You leave the {red}Market Square{white}...")
                            enter()
                            break

                elif answer == "converse":
                    scrollTxt(f"You walk over to the {orange}town square{white}")
                    enter()

                    while True:
                        clear()
                        scrollTxt(f"~[{brown}TOWN SQUARE{white}]~")
                        scrollTxt("")
                        if "the stranger" not in triggers:
                            scrollTxt(
                                f"People {paleyellow}buzz{white} around the {brown}town square{white} you see a group of {gold}noble men{white} grouped around in a tight {blue}circle{white}, you see an old {purple}wizard{white} and and a {teal}mysterious stranger{white}")
                            scrollTxt(f"{turquoise}What would you like to do{white}?")
                            scrollTxt(f"{green}> Noble men : Wizard : Stranger : Leave{white}")
                            answer = get_input(["noble men", "wizard", 'stranger', 'leave'])
                        else:
                            scrollTxt(
                                f"People {paleyellow}buzz{white} around the {brown}town square{white} you see a group of {gold}noble men{white} grouped around in a tight {blue}circle{white}, you see an old {purple}wizard{white} and and a {teal}bold warrior{white} who is challenging anyone to a duel")
                            scrollTxt(f"{turquoise}What would you like to do{white}?")
                            scrollTxt(f"{green}> Noble men : Wizard : Warrior : Leave{white}")
                            answer = get_input(["noble men", "wizard", 'warrior', 'leave'])
                        print()

                        if answer == "leave":
                            scrollTxt("You walk away...")
                            enter()

                            break

                        if answer == "noble men":
                            scrollTxt(f"You walk over to the {gold}noble men{white}")

                            if fighter_class == "thief":
                                if "nobles killed" not in triggers:
                                    if "lockwood nobles" not in triggers:
                                        triggers.append("lockwood nobles")
                                    scrollTxt(f'"{paleyellow}*snicker* Look its peasant thief, how disgusting{white}"')
                                    scrollTxt(f"{turquoise}What would you like to do{white}?")
                                    scrollTxt(f"{green}> Fight : Leave{white}")
                                    answer = get_input(["fight", 'leave'])
                                    print()

                                    if answer == "fight":
                                        combat(['noble', 'noble 2'])
                                        triggers.append("nobles killed")
                                        scrollTxt(f"You throw their {red}bodies{white} in a ditch...")
                                        enter()

                                    if answer == "leave":
                                        scrollTxt("You leave")
                                        enter()
                                else:
                                    scrollTxt("All the rest of the nobles run!")
                                    enter()

                            if fighter_class == "barbarian":
                                if "nobles killed" not in triggers:
                                    if "lockwood nobles" not in triggers:
                                        triggers.append("lockwood nobles")
                                    scrollTxt(f'"{paleyellow}*snicker* Look its a stupid barbarian{white}"')
                                    scrollTxt(f"{turquoise}What would you like to do{white}?")
                                    scrollTxt(f"{green}> Fight : Leave{white}")
                                    answer = get_input(["fight", 'leave'])
                                    print()

                                    if answer == "fight":
                                        combat(['noble', 'noble 2'])
                                        triggers.append("nobles killed")
                                        scrollTxt(f"You throw their {red}bodies{white} in a ditch...")
                                        enter()

                                    if answer == "leave":
                                        scrollTxt("You leave")
                                        enter()
                                else:
                                    scrollTxt("All the rest of the nobles run!")
                                    enter()

                            if fighter_class == "mage":
                                scrollTxt(f"The {gold}nobles{white} run from you, afraid of {purple}magic{white}")
                                enter()

                            if fighter_class == "warrior" or fighter_class == "ranger" or fighter_class == "monk":
                                if "lockwood nobles" not in triggers:
                                    triggers.append("lockwood nobles")
                                    scrollTxt(
                                        f'"{paleyellow}Welcome {blue}{fighter_class}{paleyellow}, would you like to buy a {silver}rapier{paleyellow} for {gold}25{white} GP? {white}[{green}y/n{white}]"')
                                    answer = get_input(['yes', 'no'])
                                    print()

                                    if answer == "yes":
                                        if gp > 24:
                                            scrollTxt(f"{silver}+ rapier{white} | - {gold}25{white} GP")
                                            gp -= 25
                                            inv.append("rapier")
                                        else:
                                            scrollTxt("You dont have enough")

                                    scrollTxt("You leave")
                                    enter()
                                else:
                                    scrollTxt(
                                        f'"{paleyellow}Hello again {blue}{fighter_class}{paleyellow}, would you like to buy another {silver}rapier{paleyellow} for {gold}20{white} GP? {white}[{green}y/n{white}]"')
                                    answer = get_input(['yes', 'no'])
                                    print()

                                    if answer == "yes":
                                        if gp > 19:
                                            scrollTxt(f"{silver}+ rapier{white} | - {gold}20{white} GP")
                                            gp -= 20
                                            inv.append("rapier")
                                        else:
                                            scrollTxt("You dont have enough")

                                    scrollTxt("You leave")
                                    enter()

                        if answer == "wizard":
                            if "lockwood wizard" not in triggers:
                                triggers.append("lockwood wizard")
                                scrollTxt(f"You walk up to the {purple}Wizard{white}")

                                scrollTxt(
                                    f'"{teal}Well hello here, would you like to buy a {purple}rare spell{teal} Ive made? I call it {platinum}blurr mind{white}. It will cost you {gold}35{white} GP{teal} though{white}" [{green}y/n{white}]')
                                answer = get_input(["yes", 'no'])
                                print()

                                if answer == "yes":
                                    if gp > 34:
                                        scrollTxt(f"{purple}+ blurr mind{white} | - {gold}35{white} GP")
                                        gp -= 35
                                        known_spells.append("blurr mind")
                                        current_spells.append("blurr mind")
                                    else:
                                        scrollTxt(f"You dont have {red}enough{white}")

                                scrollTxt("You leave")
                                enter()

                            else:
                                if gp > 34:
                                    scrollTxt(f"You walk up to the {purple}Wizard{white}")

                                    scrollTxt(f'"{teal}Well hello nice to see you again{white}')
                                    scrollTxt(f"Would you like to buy that {purple}spell{white} I made?")
                                    answer = get_input(["yes", 'no'])
                                    print()

                                    if answer == "yes":
                                        scrollTxt(f"{purple}+ blurr mind{white} | - {gold}35{white} GP")
                                        gp -= 35
                                        known_spells.append("blurr mind")
                                        current_spells.append("blurr mind")

                                    scrollTxt("You leave")
                                    enter()

                                scrollTxt(f"You walk up to the {purple}Wizard{white}")

                                scrollTxt(f'"{teal}Well hello nice to see you again{white}')

                                scrollTxt("You leave")
                                enter()

                        if answer == "stranger":
                            if "the stranger" not in triggers:
                                triggers.append("the stranger")
                                scrollTxt("You walk up to the stranger")
                                scrollTxt(
                                    f'"{darkgrey}You look like a fighter, I challenge you to a duel to the death. Defeat me and you may read the words written on my cloak{white}"')
                                scrollTxt(
                                    f"He {blue}turns{white} around and {grey}unsheathe{white} his {silver}blade{white}")
                                enter()

                                combat(['the stranger'])
                                scrollTxt("You read the words on the cloak")
                                scrollTxt(f"""
    In the middle of {teal}JADE FOREST{white} lies a {blue}MAGIC SWORD{white} that will slay the {orange}DRAGON{white} that plauges this {brown}LAND{white}.""")
                                enter()

                        if answer == "warrior":
                            scrollTxt(f"You walk up to the {orange}warrior{white} ready to {blue}duel.")
                            scrollTxt(f"You both draw you {grey}weapon{white} and {red}fight{white}!")
                            enter()

                            combat(['warrior'])
                            scrollTxt(
                                f"You think he is {red}dead{white} but by {purple}magic{white} he pulls himself up and grins at you")
                            scrollTxt(
                                f'"{orange}By a curse or blessing depending on how you see it, I cant be killed. I wish to fight you again, later{white}"')
                            scrollTxt("You walk away")
                            enter()

                elif answer == "leave":
                    scrollTxt(f"Where would you like to {blue}go{white}?")
                    scrollTxt(f"{teal}East : South : West{white}")
                    answer = get_input(['east', 'south', 'west'])
                    scrollTxt("")

                    print(f"You travel {orange}{answer}{white} for many {darkgrey}hours{white}")

                    if answer == "west":
                        location = "orc layer"
                    if answer == "south":
                        location = "snowy mountain"
                    if answer == "east":
                        location = "troll & goblin encamp"
                    enter()

            elif location == "orc layer":
                scrollTxt(f"~[{green}LOST PLAINS{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding the {green}lost plains{white} is {brown}Lockwood{white} to the {teal}east{white} and the {blue}ocean{white} to the {teal}west{white} and the {teal}north{white}, more {lime}green plains{white} although you can also make out a {darkgrey}small castle{white} to the {teal}south{white}{normal}{bold}")
                    scrollTxt("")

                if "orcs killed" not in triggers:

                    if "orc layer" not in triggers:
                        triggers.append("orc layer")
                        scrollTxt(
                            f"{italic}{grey}Smoke{white} rises from a {red}fire{white} in the {silver}distance{white}. Large {brown}leather tents{white} surround the {red}fire{white}, an {copper}ORC CAMP{white}. {normal}{bold}"
                        )

                    elif settings["print out des"] is True:
                        scrollTxt(
                            f"{italic}{grey}Smoke{white} rises from a {red}fire{white} in the {silver}distance{white}. Large {brown}leather tents{white} surround the {red}fire{white}, an {copper}ORC CAMP{white}. {normal}{bold}"
                        )

                    scrollTxt(f"{turquoise}What would you like to do{white}?")
                    scrollTxt(f"> {green}Inv : Stats : Settings : Save | Invade ORC CAMP : Leave{white}")
                    answer = get_input(["inv", 'stats', 'settings', "save", "invade orc camp", 'leave'])
                    scrollTxt("")

                    usual_options(answer)

                    if answer == "invade orc camp":
                        print("")
                        scrollTxt(f"You decide to invade the {orange}orc camp{white}.")
                        scrollTxt(
                            f"Upon getting a close {blue}view{white} you see that there are {red}2{white} {copper}orcs{white} and {red}1{white} {copper}ORC WARLORD{white}")
                        print()
                        scrollTxt(f"How do you {turquoise}procede{white}?")
                        scrollTxt(f"    * [{orange}CA{white}] - Charge and attack")
                        scrollTxt(f"    * [{blue}OBO{white}] - Take them down one by one")
                        scrollTxt(f"    * [{green}LA{white}] - Look around for other options")
                        scrollTxt(f"    * [{yellow}RL{white}] - Run and leave")

                        answer = get_input(["ca", 'obo', 'la', 'rl'])
                        print()

                        if answer == "ca":
                            scrollTxt(
                                f"You decide that the {gold}best{white} option is to {orange}charge{white} and {turquoise}take{white} on all the {copper}orcs{white} at once!")
                            enter()
                            combat(["orc 1", 'orc 2', 'orc warlord'], 1.5)

                        if answer == "obo":
                            scrollTxt(
                                f"You decide that the {gold}best{white} option is to take each of the {lime}orcs{white} on {blue}one{white} at a time.")
                            eleft = ['orc 1', 'orc 2', 'orc warlord']
                            while len(eleft) > 0:
                                if random.randint(1, 5) in range(1, dexterity):
                                    print(
                                        f"You are {turquoise}able{white} to {green}locate{white} and {red}corner{white} one {lime}orc{white}!")
                                    enter()
                                    echose = random.choice(eleft)
                                    combat([echose])
                                    eleft.remove(echose)
                                else:
                                    print(
                                        f"You are {red}spotted{white} and the rest of the {lime}orcs{white} charge at you!")
                                    enter()
                                    combat(eleft)
                                    eleft = []

                                print()

                            triggers.append("orcs killed")

                        if answer == "la":
                            crollTxt(
                                "You decide that none of the other options are the best and you should look for other ways of attacking")
                            crollTxt("After doing a thorough search of the area you find 2 things")
                            crollTxt(f"[{orange}FIRE{white}]     - A large tree that can be lit on fire")
                            crollTxt(f"[{darkgrey}BOULDER{white}]     - A large boulder that could be rolled down the hill")
                            print()
                            crollTxt("What would you like to do?")
                            answer = get_input(["fire", "boulder"])
                            print()

                            if answer == "fire":
                                if "firebolt" not in known_spells and "torch" not in inv:
                                    crollTxt("You fail to find a way to light the tree on fire")
                                else:
                                    if "firebolt" in known_spells:
                                        crollTxt("You use FIREBOLT to light the tree on fire")
                                        crollTxt("2 orcs die before the rest escape")
                                        crollTxt("You charge at the ORC WARLORD")
                                        enter()
                                        combat(["orc warlord"])
                                    else:
                                        inv.remove("torch")
                                        crollTxt("You throw your torch at the tree and light it on fire")
                                        crollTxt("1 orc dies before the rest escape")
                                        crollTxt("You charge at the rest of the orcs")
                                        enter()
                                        combat(["orc warlord", "orc 1"])
                                    triggers.append("orcs killed")

                                enter()
                            if answer == "boulder":
                                if random.randint(1, 6) in range(1, strength):
                                    crollTxt("You successfully roll the boulder down the hill!")
                                    crollTxt("This kills the orc warlord before the other orcs scatter")
                                    crollTxt("You charge at the rest of the orcs")
                                    enter()
                                    combat(["orc 1", "orc 2"])
                                    enter()
                                    triggers.append("orcs killed")
                                else:
                                    crollTxt("You are too weak the roll the boulder down the hill")
                                    enter()

                        if answer == "rl":
                            crollTxt("You run away from the orc camp")
                            enter()
                else:
                    if "orc layer" not in triggers:
                        triggers.append("orc layer")
                        scrollTxt(
                            f"{italic}{grey}Smoke{white} rises from a {darkgrey}new{white} {red}fire{white} in the {silver}distance{white}. Large {darkgrey}dark{white} {brown}leather tents{white} surround the {red}fire{white}, an {copper}mess{white}. {normal}{bold}"
                        )

                    elif settings["print out des"] is True:
                        scrollTxt(
                            f"{italic}{grey}Smoke{white} rises from a {darkgrey}new{white} {red}fire{white} in the {silver}distance{white}. Large {darkgrey}dark{white} {brown}leather tents{white} surround the {red}fire{white}, an {copper}mess{white}. {normal}{bold}"
                        )

                    scrollTxt(f"{turquoise}What would you like to do{white}?")
                    scrollTxt(f"> {green}Inv : Stats : Settings : Save | Invade ORC CAMP | Leave{white}")
                    answer = get_input(["inv", 'stats', 'settings', "save", "invade orc camp", 'leave'])
                    scrollTxt("")

                    usual_options(answer)

                    if answer == "invade orc camp":
                        print("")
                        scrollTxt(f"You decide to invade the {orange}orc camp{white}.")
                        scrollTxt(
                            f"Upon getting a close {blue}view{white} you see that there are {red}3{white} {copper}orcs{white} and {red}1{white} {copper}ORC WARLORD{white}")
                        print()
                        scrollTxt(f"How do you {turquoise}procede{white}?")
                        scrollTxt(f"    * [{orange}CA{white}] - Charge and attack")
                        scrollTxt(f"    * [{blue}OBO{white}] - Take them down one by one")
                        scrollTxt(f"    * [{yellow}RL{white}] - Run and leave")

                        answer = get_input(["ca", 'obo', 'rl'])
                        print()

                        if answer == "ca":
                            scrollTxt(
                                f"You decide that the {gold}best{white} option is to {orange}charge{white} and {turquoise}take{white} on all the {copper}orcs{white} at once!")
                            enter()
                            combat(["orc 1", 'orc 2', 'orc 3', 'orc warlord'], 1.2)

                        if answer == "obo":
                            scrollTxt(
                                f"You decide that the {gold}best{white} option is to take each of the {lime}orcs{white} on {blue}one{white} at a time.")
                            eleft = ['orc 1', 'orc 2', 'orc 3', 'orc warlord']
                            while len(eleft) > 0:
                                if random.randint(1, 6) in range(1, dexterity):
                                    print(
                                        f"You are {turquoise}able{white} to {green}locate{white} and {red}corner{white} one {lime}orc{white}!")
                                    enter()
                                    echose = random.choice(eleft)
                                    combat([echose])
                                    eleft.remove(echose)
                                else:
                                    print(
                                        f"You are {red}spotted{white} and the rest of the {lime}orcs{white} charge at you!")
                                    enter()
                                    combat(eleft)
                                    eleft = []

                                print()

                            triggers.append("orcs killed")


                        if answer == "rl":
                            crollTxt("You run away from the orc camp")
                            enter()

                if answer == "leave":
                    scrollTxt(f"Where would you like to {blue}go{white}?")
                    scrollTxt(f"{teal}East : South{white}")
                    answer = get_input(['east', 'south'])
                    scrollTxt("")

                    print(f"You travel {orange}{answer}{white} for many {darkgrey}hours{white}")

                    if answer == "east":
                        location = "lockwood"
                    if answer == "south":
                        location = "the forge"
                    enter()

            elif location == "troll & goblin encamp":
                scrollTxt(f"~[{green}SCARRED PLAINS{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding the {green}scarred plains{white} is {darkgrey}Lockwood{white} to the {teal}west{white}, more {lime}grassy plains{white} to the {teal}south{white}, strange {blue}blue sandy shores{white} to the {teal}east{white} and the {blue}ocean{white} surrounds to the {teal}north{white}{normal}{bold}")
                    scrollTxt("")

                if "goblins & troll killed" not in triggers:

                    if "troll & goblin encamp" not in triggers:
                        triggers.append("troll & goblin encamp")
                        scrollTxt(
                            f"{italic}The {silver}wind{white} wistles in your ear as you survey the {green}land{white}. You notice a {darkgrey}skull shaped rock{white} in the distance emitting an {orange}orange{white} glow like that from a {red}fire{white}. {normal}{bold}")

                    elif settings["print out des"] is True:
                        scrollTxt(
                            f"{italic}The {silver}wind{white} wistles in your ear as you survey the {green}land{white}. You notice a {darkgrey}skull shaped rock{white} in the distance emitting an {orange}orange{white} glow like that from a {red}fire{white}. {normal}{bold}")

                    scrollTxt(f"{turquoise}What would you like to do{white}?")
                    scrollTxt(f"> {green}Inv : Stats : Settings : Save | Check out skull rock : Leave{white}")
                    answer = get_input(["inv", 'stats', 'settings', "save", "check out skull rock", 'leave'])
                    scrollTxt("")

                    usual_options(answer)

                    if answer == "check out skull rock":
                            print("")
                            crollTxt("You decide to investigate the skull rock...")
                            time.sleep(0.5)
                            crollTxt("When you reach the skull rock you hear chanting")
                            crollTxt("In the middle of the skull rock is a large bonfire, surrounding it is a bunch of goblins and a troll !")
                            print()
                            scrollTxt(f"How do you {turquoise}procede{white}?")
                            scrollTxt(f"    * [{orange}CA{white}] - Charge and attack")
                            scrollTxt(f"    * [{blue}OBO{white}] - Take them down one by one")
                            scrollTxt(f"    * [{green}LA{white}] - Look around for other options")
                            scrollTxt(f"    * [{yellow}RL{white}] - Run and leave")

                            answer = get_input(["ca", 'obo', 'la', 'rl'])
                            print()

                            if answer == "ca":
                                scrollTxt(
                                    f"You decide that the {gold}best{white} option is to {orange}charge{white} and {turquoise}take{white} on all the {copper}enemies{white} at once!")
                                enter()
                                combat(["goblin 1", 'goblin 2', 'troll'], 1.5)

                            if answer == "obo":
                                scrollTxt(
                                    f"You decide that the {gold}best{white} option is to take each of the {lime}goblins{white} on {blue}one{white} at a time.")
                                eleft = ['goblin 1', 'goblin 2', 'troll']
                                while len(eleft) > 0:
                                    if random.randint(1, 6) in range(1, dexterity):
                                        print(
                                            f"You are {turquoise}able{white} to {green}locate{white} and {red}corner{white} one {lime}goblin{white}!")
                                        enter()
                                        echose = random.choice(eleft)
                                        combat([echose])
                                        eleft.remove(echose)
                                    else:
                                        print(
                                            f"You are {red}spotted{white} and the rest of the {lime}goblins{white} charge at you!")
                                        enter()
                                        combat(eleft)
                                        eleft = []

                                    print()

                                triggers.append("goblins & troll killed")

                            if answer == "la":
                                crollTxt(
                                    "You decide that none of the other options are the best and you should look for other ways of attacking")
                                crollTxt("After doing a thorough search of the area you find 2 things")
                                crollTxt(f"[{orange}EXPLODE{white}]     - A large explosive barrel")
                                crollTxt(f"[{darkgrey}PUSH{white}]     - Try to push the troll into the fire")
                                print()
                                crollTxt("What would you like to do?")
                                answer = get_input(["explode", "push"])
                                print()

                                if answer == "explode":
                                    if "firebolt" not in known_spells and "torch" not in inv and "bow" not in weapon:
                                        crollTxt("You fail to find a way to hit the barrel")
                                    else:
                                        if "firebolt" in known_spells:
                                            crollTxt("You use FIREBOLT to light the barrel on fire")
                                            crollTxt("2 goblins die in the explosion")
                                            crollTxt("You charge at the troll")
                                            enter()
                                            combat(["troll"])
                                        else:
                                            inv.remove("torch")
                                            crollTxt("You throw your torch at the barrel and light it on fire")
                                            crollTxt("2 goblins dies before the rest escape")
                                            crollTxt("You charge at the troll")
                                            enter()
                                            combat(["troll"])
                                        triggers.append("goblins & troll killed")

                                    enter()
                                if answer == "push":
                                    if random.randint(1, 6) in range(1, dexterity):
                                        crollTxt("You successfully push the troll into the fire !")
                                        crollTxt("This instantly kills it")
                                        crollTxt("You charge at the rest of the goblins")
                                        enter()
                                        combat(["goblin 1", "goblin 2"])
                                        enter()
                                        triggers.append("goblins & troll killed")
                                    else:
                                        crollTxt("You are noticed and the enemies charge at you!")
                                        enter()
                                        combat(["goblin 1", "goblin 2", 'troll'], 0.8)
                                        triggers.append("goblins & troll killed")
                                        enter()

                            if answer == "rl":
                                crollTxt("You run away from the skull rock")
                                enter()
                else:
                    if "troll & goblin encamp" not in triggers:
                        triggers.append("troll & goblin encamp")
                        scrollTxt(
                            f"{italic}You see a slightly {darkgrey}cracked{white} {grey}rock{white} that resembles a {red}skull{white} its glowing {orange}orange{white} from what seems to be a {red}fire{white} {normal}{bold}")

                    elif settings["print out des"] is True:
                        scrollTxt(
                            f"{italic}You see a slightly {darkgrey}cracked{white} {grey}rock{white} that resembles a {red}skull{white} its glowing {orange}orange{white} from what seems to be a {red}fire{white} {normal}{bold}")

                    scrollTxt(f"{turquoise}What would you like to do{white}?")
                    scrollTxt(f"> {green}Inv : Stats : Settings : Save | Check out skull rock : Leave{white}")
                    answer = get_input(["inv", 'stats', 'settings', "save", "check out skull rock", 'leave'])
                    scrollTxt("")

                    usual_options(answer)

                    if answer == "check out skull rock":
                            print("")
                            crollTxt("You decide to investigate the skull rock...")
                            time.sleep(0.5)
                            crollTxt("When you reach the skull rock you hear chanting")
                            crollTxt("In the middle of the skull rock is a large bonfire, surrounding it is a bunch of goblins and a troll !")
                            print()
                            scrollTxt(f"How do you {turquoise}procede{white}?")
                            scrollTxt(f"    * [{orange}CA{white}] - Charge and attack")
                            scrollTxt(f"    * [{blue}OBO{white}] - Take them down one by one")
                            scrollTxt(f"    * [{yellow}RL{white}] - Run and leave")

                            answer = get_input(["ca", 'obo', 'rl'])
                            print()

                            if answer == "ca":
                                scrollTxt(
                                    f"You decide that the {gold}best{white} option is to {orange}charge{white} and {turquoise}take{white} on all the {copper}enemies{white} at once!")
                                enter()
                                combat(["goblin 1", 'goblin 2', 'goblin 3', 'troll'], 1.3)

                            if answer == "obo":
                                scrollTxt(
                                    f"You decide that the {gold}best{white} option is to take each of the {lime}goblins{white} on {blue}one{white} at a time.")
                                eleft = ['goblin 1', 'goblin 2', 'goblin 3', 'troll']
                                while len(eleft) > 0:
                                    if random.randint(1, 7) in range(1, dexterity):
                                        print(
                                            f"You are {turquoise}able{white} to {green}locate{white} and {red}corner{white} one {lime}goblin{white}!")
                                        enter()
                                        echose = random.choice(eleft)
                                        combat([echose])
                                        eleft.remove(echose)
                                    else:
                                        print(
                                            f"You are {red}spotted{white} and the rest of the {lime}goblins{white} charge at you!")
                                        enter()
                                        combat(eleft)
                                        eleft = []

                                    print()

                                triggers.append("goblins & troll killed")

                            

                            if answer == "rl":
                                crollTxt("You run away from the skull rock")
                                enter()

                if answer == "leave":
                    scrollTxt(f"Where would you like to {blue}go{white}?")
                    scrollTxt(f"{teal}South : West : East{white}")
                    answer = get_input(['west', 'south', "east"])
                    scrollTxt("")

                    print(f"You travel {orange}{answer}{white} for many {darkgrey}hours{white}")

                    if answer == "south":
                        location = "merchant"
                    if answer == "west":
                        location = "lockwood"
                    if answer == "east":
                        location = "merchant 2"
                    enter()
            
            elif location == "the forge":
                scrollTxt(f"~[{green}THE FORGE{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding {green}the forge{white} is open {lime}grass plains{white} to the {teal}north{white}, a {purple}purple snowy mountain{white} to the {teal}east{white} and the {blue}ocean{white} to the {teal}south{white} and {teal}west{white}{normal}{bold}")
                    scrollTxt("")

                if "the forge" not in triggers:
                    triggers.append("the forge")
                    crollTxt("You are greeted by a burly blacksmith.")
                    crollTxt('"Welcome to the forge, here you can upgrade your weapons and look at other weapons", says the blacksmith.')
                    print()
                    crollTxt("You hear the sound of people hammering on exquisite weapons and shields. People surround models of rare weapons")

                elif settings["print out des"] is True:
                    crollTxt("You hear the sound of people hammering on exquisite weapons and shields. People surround models of rare weapons")

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {green}Inv : Stats : Settings : Save | Look at Weapons : Forge a Shield : Forge a Weapon : Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", 'look at weapons', 'forge a shield', 'forge a weapon', 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "look at weapons":
                    view_weapon()
                if answer == "forge a shield":
                    crollTxt('You walk up to the nearest shield forgery.')
                    crollTxt(f'"That will be {10 + (lvl*10)} gold " says the smith')
                    yn = get_input(["yes", "no"])

                    if yn == "yes":
                        if gp >= 10 + (lvl*10):
                            gp -= 10 + (lvl*10)
                            crollTxt(f"-{10 + (lvl*10)} gold")
                            print()
                            forge_shield()
                        else:
                            crollTxt("You don\'t have enough gold")
                            enter()

                    else:
                        crollTxt("You leave the shield forgery")
                        enter()
                if answer == "forge a weapon":
                    cost_w = 20
                    for i in triggers:
                        if i == "forged weapon":
                            cost_w *= 1.4
                    for i in inv:
                        for x in items_all[i]["description"].split():
                            if "Enchanted" in x:
                                cost_w *= 1.7

                    cost_w = int(cost_w)
                            
                    scrollTxt(f'You walk up to the nearest {darkgrey}weapon{orange} forgery{white}.')
                    scrollTxt(f'"That will be {gold}{cost_w}{white} gold and {darkgrey}{int(cost_w/20)}{white} metal scraps" says the {red}smith{white}')
                    yn = get_input(["yes", "no"])

                    if yn == "yes":
                        am_of_scraps = 0
                        for itm in inv:
                            if itm == "metal scrap": am_of_scraps += 1
                        if gp >= cost_w and am_of_scraps >= int(cost_w/20):
                            gp -= cost_w
                            scrollTxt(f"-{gold}{cost_w}{white} gold")
                            scrollTxt(f"- {darkgrey}{ int(cost_w/20)}{white} metal scraps")
                            removeinv = []
                            am_of_scraps = int(cost_w/20)
                            for itm in inv:
                                if itm == "metal scrap" and am_of_scraps > 0:
                                    am_of_scraps -= 1
                                    removeinv.append("metal scrap")

                            for itm in removeinv:
                                inv.remove(itm)
                            scrollTxt(f"")
                            print()
                            forge_weapon()
                        else:
                            scrollTxt(f"You don\'t have enough {red}items{white}")
                            enter()

                    else:
                        crollTxt("You leave the weapon forgery")
                        enter()

                if answer == "leave":
                    scrollTxt(f"Where would you like to {blue}go{white}?")
                    scrollTxt(f"{teal}North : East{white}")
                    answer = get_input(['north', 'east'])
                    scrollTxt("")

                    print(f"You travel {orange}{answer}{white} for many {darkgrey}hours{white}")

                    if answer == "north":
                        location = "orc layer"
                    if answer == "east":
                        location = "snowy mountain"
                    enter()

            elif location == "merchant":
                scrollTxt(f"~[{green}LOW-GRASS{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding {green}low grass{white} is more {lime}grass plains{white} to the {teal}north{white}, a {purple}purple snowy mountain{white} to the {teal}west{white}, a {yellow}desert{white} to the south, and the {blue}ocean{white} to the {teal}east{white}{normal}{bold}")
                    scrollTxt("")

                if "merchant" not in triggers:
                    triggers.append("merchant")
                    scrollTxt(
                        f"{italic}The {lime}grass{white} sways in the gentle {silver}breeze{white}. You can make out a {darkgrey}merchant{white} the distance{white}.{normal}{bold}")

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}The {lime}grass{white} sways in the gentle {silver}breeze{white}. You can make out a {darkgrey}merchant{white} the distance{white}. {normal}{bold}")

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {green}Inv : Stats : Settings : Save | Merchant : Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", 'merchant', 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "merchant":
                    crollTxt('You walk up the the merchant.\nHe has a huge backpack full of shields, swords, and potions. He is also wearing a large red pointy hat. \n“Hello there, the name\'s Cove, I\'ve been supplying adventurers with gear since 12th of Emberwane, Year of the Ebon Moon!”, says Cove.')
                    enter()

                    Shop(["water bottle", 'torch', 'mirror', 'rope', 'cove\'s concoction', "scale shield", "trident", "longbow", "crossbow"], [5, 5, 10, 10, 10, 80, 120, 120, 130],
                                    f"{red}Cove\'s{white} {darkgrey}Collection{white}", 20)
                    
                elif answer == "leave":
                    scrollTxt(f"Where would you like to {blue}go{white}?")
                    scrollTxt(f"{teal}North : South : West{white}")
                    answer = get_input(['north', 'south', 'west'])
                    scrollTxt("")

                    print(f"You travel {orange}{answer}{white} for many {darkgrey}hours{white}")

                    if answer == "south":
                        location = "bandit hideout"
                    if answer == "west":
                        location = "snowy mountain"
                    if answer == "north":
                        location = "troll & goblin encamp"
                    enter()
            
            elif location == "merchant 2":
                scrollTxt(f"~[{green}BLUE SHORES{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding {green}blue shores{white} is {lime}grassy plains{white} to the east, and the {blue}ocean{white} {teal}everywhere else{white}{normal}{bold}")
                    scrollTxt("")

                if "merchant 2" not in triggers:
                    triggers.append("merchant 2")
                    scrollTxt(
                        f"{italic}The {yellow}sand{white} here appears {blue}blue{white}, great {darkgrey}jagged rocks{white} block some of your {turquoise}view{white}. You can make out a {darkgrey}merchant{white} the distance{white}.{normal}{bold}")

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}The {yellow}sand{white} here appears {blue}blue{white}, great {darkgrey}jagged rocks{white} block some of your {turquoise}view{white}. You can make out a {darkgrey}merchant{white} the distance{white}.{normal}{bold}")

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {green}Inv : Stats : Settings : Save | Merchant : Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", 'merchant', 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "merchant":
                    crollTxt('You walk up the the merchant.\nShe has a huge backpack full of shields, spears, and potions. She is also wearing a large purple pointy hat. \n“My name\'s Awl, have you met by brother? His name is Cove, he also sells items.”, says Awl.')
                    enter()

                    Shop(['awl\'s alchemy', "luck potion", "spear", "rune shield", "guardian shield"], [10, 20, 25, 85, 90],
                                    f"{red}Awl's{white} Articles{darkgrey}{white}", 20)
                    
                elif answer == "leave":
                    print(f"You travel {orange}west{white} for many {darkgrey}hours{white}")

                    location = "troll & goblin encamp"
                    enter()       
            
            elif location == "snowy mountain":
                scrollTxt(f"~[{green}SNOWY MOUNTAIN{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding the {green}snowy mountain{white} is open {lime}grass plains{white} to the {teal}north{white}, {teal}west{white}, and {teal}east{white}, and a {blue}lake{white} to the {teal}south{white}")
                    scrollTxt("")

                if "snowy mountian" not in triggers:
                    triggers.append("snowy mountian")
                    scrollTxt(
                        f"{italic}The {blue}cold{white} {silver}snowy wind{white} whips your face. The great {purple}purple mountain{white} looms above you. Casting an ominous {darkgrey}shadow{white} upon you\n{italic}[{red}WARNING{white}] Ment for those at a {green}high{white} level!{normal}{bold}")

                elif settings["print out des"] is True:
                        scrollTxt(f"{italic}The {blue}cold{white} {silver}snowy wind{white} whips your face. The great {purple}purple mountain{white} looms above you. Casting an ominous {darkgrey}shadow{white} upon you\n{italic}[{red}WARNING{white}] Ment for those at a {green}high{white} level!{normal}{bold}")

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {green}Inv : Stats : Settings : Save | Gear Up : Converse : Start Climbing : Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", 'gear up', 'converse', 'start climbing', 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "leave":
                    scrollTxt(f"Where would you like to {blue}go{white}?")
                    scrollTxt(f"{teal}North: East : South : West{white}")
                    answer = get_input(['north', 'east', 'south', 'west'])
                    scrollTxt("")

                    print(f"You travel {orange}{answer}{white} for many {darkgrey}hours{white}")

                    if answer == "north":
                        location = "lockwood"
                    if answer == "east":
                        location = "merchant"
                    if answer == "west":
                        location = "the forge"
                    if answer == "south":
                        location = "shrine"
                    enter()

                if answer == "gear up":
                    scrollTxt(f"You walk up a {darkgrey}climbing{white} store")
                    enter()
                    Shop(["climbing gear", "rope", 'water bottle'], [20, 6, 3], f"{turquoise}Snowcap{white} Shop")

                if answer == "converse":
                    scrollTxt(f'You see {green}three people{white}\nWho would you like to {blue}talk{white} to? [A B C]')
                    tt = get_input(['a', 'b', 'c'])

                    if tt == 'a':
                        clear()
                        scrollTxt(f"{blue}I\'m going to climb this mountain no matter what. HAHAHAHHAHA{white}")
                        enter()
                    elif tt == "b":
                        clear()
                        scrollTxt(f"{darkgrey}Did you know out of the 200 people that atempt this climb every year only 5 survive. I would reconmend you have lots of water, some rope, and climbing gear{white}")
                        enter()
                    elif tt == "c":
                        clear()
                        scrollTxt(f"{orange}Methinks ther is a monster up ther. Me tinks it not wise to clim!{white}")
                        enter()

                if answer == "start climbing":
                    snowy_mountain()

            elif location == "shrine":
                scrollTxt(f"~[{green}BLESSED LAKE{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding the {green}blessed lake{white} is an {yellow}sandy shores{white} to the {teal}east{white}, a {purple}purple snowy mountain{white} to the {teal}north{white}, the {green}forest{white} to the {teal}south{white}, and the {blue}ocean{white} to the {teal}west{white}{normal}{bold}")
                    scrollTxt("")

                if "shrine" not in triggers:
                    triggers.append("shrine")
                    scrollTxt(
                        f"{italic}You gaze upon the vast {blue}lake{white}. A small {paleyellow}island{white} lies in the middle of the {teal}lake{white}. And upon the {paleyellow}island{white} is a large {darkgrey}stone statue{white}.{normal}{bold}")

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}You gaze upon the vast {blue}lake{white}. A small {paleyellow}island{white} lies in the middle of the {teal}lake{white}. And upon the {paleyellow}island{white} is a large {darkgrey}stone statue{white}.{normal}{bold}")
                
                if "island is important" not in triggers:
                    triggers.append("island is important")
                    scrollTxt(f"~{blue}island is important{white}~")
                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {green}Inv : Stats : Settings : Save | Examine Island : Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", 'examine island', 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "examine island":
                    scrollTxt(f"You must somehow get {darkgrey}across{white} the {blue}lake{white}")
                    scrollTxt(f"You {green}notice{white} a {ironc}ferry boat{white} nearby")
                    scrollTxt(f"[{turquoise}Swim Across{white}] [{turquoise}Ferry Boat{white}]")
                    scrollTxt(f"What do {blue}you{white} do?")
                    answer = get_input(["swim across", "ferry boat"])
                    print()

                    made_across = True

                    if answer == "swim across":
                        if random.randint(1, 10) in range(1, dexterity + strength) or inv == []:
                            scrollTxt(f"You make it {green}safely{white} across to the {yellow}island{white}")
                            enter()
                        else:
                            item = random.choice(inv)
                            scrollTxt(f"As you are {blue}swimming{white} your {darkgrey}{item}{white} floats away")
                            scrollTxt(f"Do you {orange}retrieve{white} it? [{green}y{white}/{red}n{white}]")
                            yn = get_input(["yes", "no"])
                            print()

                            if yn == "yes":
                                nitem = random.choice(inv)
                                scrollTxt(f"You {orange}retrieve{white} your {darkgrey}{item}{white} but your {darkgrey}{nitem}{white} floats away")
                                scrollTxt(f"Do you {orange}retrieve{white} it? [{green}y{white}/{red}n{white}]")
                                yn = get_input(["yes", "no"])
                                print()

                                if yn == "yes":
                                    item = random.choice(inv)
                                    scrollTxt(f"You {orange}retrieve{white} your {darkgrey}{item}{white} but your {darkgrey}{item}{white} floats away")
                                    scrollTxt(f"You make it {green}safely{white} across")
                                    scrollTxt(f"{red}- {item}{white}")
                                    inv.remove(item)
                                else:
                                    inv.remove(nitem)
                                    scrollTxt(f"You make it {green}safely{white} across")
                                    scrollTxt(f"{red}- {nitem}{white}")
                            else:
                                inv.remove(item)
                                scrollTxt(f"You make it {green}safely{white} across")
                                scrollTxt(f"{red}- {item}{white}")
                    elif answer == "ferry boat":
                        scrollTxt(f"The {ironc}ferry boat{white} costs {gold}5{white} GP")
                        scrollTxt(f"Would {blue}you{white} like to {gold}pay{white}?")
                        answer = get_input(["yes", "no"])
                        print()

                        if answer == "no":
                            scrollTxt(f"You {red}leave{white}...")
                            made_across = False
                            enter()

                        else:
                            if gp >= 5:
                                scrollTxt(f"You make it {green}across{white} on the {ironc}ferry boat{white}")
                                scrollTxt(f"- {gold}5{white} GP")
                                gp -= 5
                            else:
                                scrollTxt(f"You don\'t have {red}enough{white}...")
                                enter()

                                made_across = False
                    
                    if made_across is True:
                        while True:
                            clear()
                            scrollTxt(f"Upon {green}reaching{white} the {darkgrey}statue{white} you find that there is a {blue}slot{white} in the {darkgrey}state{white} that fits to shape of a {turquoise}Level Crystal{white} 🔷")
                            scrollTxt(f"There is another {darkgrey}slot{white} that is in the shape of a {gold}gold coin{white}")
                            scrollTxt(f"[{turquoise}Put in Crystal{white}] [{turquoise}Put in Coin{white}] [{turquoise}Leave{white}]")
                            scrollTxt(f"What would {blue}you{white} like to do?")
                            answer = get_input(["put in crystal", "put in coin", "leave"])
                            print()

                            if answer == "put in crystal":
                                if crystals > 0:
                                    scrollTxt(f"You put in a {turquoise}Level Crystal{white} 🔷")
                                    time.sleep(2)

                                    clear()

                                    while True:
                                        clear()
                                        cost = {
                                            "strength boon": 1,
                                            "dexterity boon": 1,
                                            "health boon": 1,
                                            "crystal dagger": 1,
                                            "crystal potion": 3
                                        }
                                        print(f"You have {turquoise}{crystals}{white} Level Cystals")
                                        print(f"- {turquoise}Strength{white} Boon  -  [ {teal}1 level crystal{white} ]")
                                        print(f"- {turquoise}Dexterity{white} Boon -  [ {teal}1 level crystal{white} ]")
                                        print(f"-  {turquoise}Health{white} Boon   -  [ {teal}1 level crystal{white} ]")
                                        print(f"- {turquoise}Crystal{white} Dagger -  [ {teal}1 level crystal{white} ]")
                                        print(f"- {turquoise}Crystal{white} Potion -  [ {teal}3 level crystal{white} ]")
                                        print(f"[{purple}l{white}] to leave")
                                        print()
                                        scrollTxt(f"What would {blue}you{white} like to buy?")
                                        answer = get_input(["strength boon", "dexterity boon", "health boon", "crystal dagger", "crystal potion", "leave"])
                                        print()

                                        if answer == "leave":
                                            break
                                            

                                        else:
                                            

                                            if crystals >= cost[answer]:
                                                crystals -= cost[answer]
                                                if answer == "strength boon":
                                                    scrollTxt(f"You feel {orange}STRENGTH{white} surge through {blue}you{white}")
                                                    scrollTxt(f"+ {orange}1{white} Strength")
                                                    strength += 1
                                                elif answer == "dexterity boon":
                                                    scrollTxt(f"You feel {blue}DEXTERITY{white} surge through {blue}you{white}")
                                                    scrollTxt(f"+ {blue}1{white} Dexterity")
                                                    dexterity += 1
                                                elif answer == "health boon":
                                                    scrollTxt(f"You feel {red}HEALTH{white} surge through {blue}you{white}")
                                                    scrollTxt(f"+ {red}3{white} Max Health")
                                                    max_health += 3
                                                    health += 3
                                                else:
                                                    scrollTxt(f"You got a {turquoise}{answer}{white}")
                                                    inv.append(answer)

                                                enter()
                                            else:
                                                scrollTxt(f"You don\'t have {red}enough{white}")
                                                enter()

                                else:
                                    scrollTxt(f"You {red}don\'t{white} have any {turquoise}crystals{white}...")
                                    enter()
                            elif answer == "put in coin":
                                if gp > 0:
                                    scrollTxt(f"This will {blue}save{white} half of any {gold}coins{white} you put in for {orange}future{white} runs!")
                                    scrollTxt(f'How many {gold}coins{white} would you like to put in?')
                                    cc = []
                                    for ggp in range(1, gp + 1):
                                        cc.append(str(ggp))
                                    answer = get_input(commands = cc, g = True)
                                    print()
                                    scrollTxt(f"{gold}Coins{white} {darkgrey}Saved{white}!")
                                    try:
                                        db["coins"] += int(int(answer)/2)
                                    except:
                                        db["coins"] = int(int(answer)/2)
                                    enter()
                                    gp -= int(answer)
                                else:
                                    scrollTxt(f"You have no {gold}coins{white}...")
                                    enter()
                            else:
                                scrollTxt(f"You leave the {yellow}island{white}")
                                enter()
                                break

                elif answer == "leave":
                    scrollTxt(f"Where would you like to {blue}go{white}?")
                    scrollTxt(f"{teal}North: East: South{white}")
                    answer = get_input(['east', 'south', 'north'])
                    scrollTxt("")

                    print(f"You travel {orange}{answer}{white} for many {darkgrey}hours{white}")

                    if answer == "north":
                        location = "snowy mountain"
                    if answer == "south":
                        location = "magic forest"
                    if answer == "east":
                        location = "bandit hideout"
                    enter()

            elif location == "bandit hideout":
                scrollTxt(f"~[{green}CURSED SHORES{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding the {green}cursed shores{white} is a {blue}lake{white} to the {teal}west{white}, open {lime}grassy plains{white} to the {teal}north{white}, a {green}forest{white} to the {teal}south{white} and the {blue}ocean{white} to the {teal}east{white}{normal}{bold}")
                    scrollTxt("")

                if "bandit hideout" not in triggers:
                    triggers.append("bandit hideout")
                    scrollTxt(
                        f"{italic}The {yellow}sand{white} here is a {paleyellow}yellowish{white}-{red}red{white}. It\'s also home to the {orange}Shark Fang\'s hideout{white}, a netourious group of {darkgrey}bandits{white}.{normal}{bold}")

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}The {yellow}sand{white} here is a {paleyellow}yellowish{white}-{red}red{white}. It\'s also home to the {orange}Shark Fang\'s hideout{white}, a netourious group of {darkgrey}bandits{white}.{normal}{bold}")

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {green}Inv : Stats : Settings : Save | Raid Hideout : Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", 'raid hideout', 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "raid hideout":
                    scrollTxt(f"With {red}caution{white} you aproach the {darkgrey}formidable{white} {yellow}bandit base{white}...")
                    enter()
                    bandit_hideout()

                elif answer == "leave":
                    scrollTxt(f"Where would you like to {blue}go{white}?")
                    scrollTxt(f"{teal}North : South : West{white}")
                    answer = get_input(['north', 'south', 'west'])
                    scrollTxt("")

                    print(f"You travel {orange}{answer}{white} for many {darkgrey}hours{white}")

                    if answer == "north":
                        location = "merchant"
                    if answer == "south":
                        location = "dragon worshipers"
                    if answer == "west":
                        location = "shrine"
                    enter()

            elif location == "magic forest":
                scrollTxt(f"~[{green}JADE FOREST{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}{italic}Surrounding the {green}jade forest{white} is a {blue}lake{white} to the {teal}north{white}, more {green}forest{white} to the {teal}east{white}, a {darkgrey}cave{white} to the {teal}south{white} and the {blue}ocean{white} to the {teal}west{white}{normal}{bold}{normal}{bold}")
                    scrollTxt("")

                if "jade forest" not in triggers:
                    triggers.append("jade forest")
                    scrollTxt(
                        f"{italic}Beautiful {teal}teal willow{white} {lime}trees{white} sway gracefully in the {silver}wind{white}. Strange {green}creatures{white} have been sighted here.{normal}{bold}")

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}Beautiful {teal}teal willow{white} {lime}trees{white} sway gracefully in the {silver}wind{white}. Strange {green}creatures{white} have been sighted here.{normal}{bold}")

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {green}Inv : Stats : Settings : Save | Explore Forest : Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", 'explore forest', 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "explore forest":
                    scrollTxt(f"You feel a sense of {turquoise}wonder{white} as you walk towards the {teal}Jade forest{white}...")
                    enter()
                    jade_forest()

                elif answer == "leave":
                    scrollTxt(f"Where would you like to {blue}go{white}?")
                    scrollTxt(f"{teal}North : South : East{white}")
                    answer = get_input(['north', 'south', 'east'])
                    scrollTxt("")

                    print(f"You travel {orange}{answer}{white} for many {darkgrey}hours{white}")

                    if answer == "north":
                        location = "shrine"
                    if answer == "east":
                        location = "dragon worshipers"
                    if answer == "south":
                        location = "dragon cave"
                    enter()

            elif location == "dragon worshipers":
                scrollTxt(f"~[{green}DARKWOOD{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}{italic}Surrounding {green}darkwood{white} is a {red}red sandy shores{white} to the {teal}north{white}, more {green}forest{white} to the {teal}west{white}, and the {blue}ocean{white} to the {teal}west{white} and {teal}south{white}{normal}{bold}{normal}{bold}")
                    scrollTxt("")

                if "darkwood" not in triggers:
                    triggers.append("darkwood")
                    scrollTxt(
                        f"{italic}{purple}Infected{white} {darkgrey}dark{white} {green}pine trees{white} seems to wail in the {silver}wind{white}. No one has every been {orange}sane{white} after entering {darkgrey}darkwood{white}.{normal}{bold}")

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}{purple}Infected{white} {darkgrey}dark{white} {green}pine trees{white} seems to wail in the {silver}wind{white}. No one has every been {orange}sane{white} after entering {darkgrey}darkwood{white}.{normal}{bold}")

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {green}Inv : Stats : Settings : Save | Enter Forest : Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", 'enter forest', 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "enter forest":
                    scrollTxt(f"You feel a sense of {orange}dread{white} as you walk towards the {darkgrey}dark forest  {white}...")
                    enter()
                    darkwood()

                elif answer == "leave":
                    scrollTxt(f"Where would you like to {blue}go{white}?")
                    scrollTxt(f"{teal}North : West{white}")
                    answer = get_input(['north', 'west'])
                    scrollTxt("")

                    print(f"You travel {orange}{answer}{white} for many {darkgrey}hours{white}")

                    if answer == "north":
                        location = "bandit hideout"
                    if answer == "west":
                        location = "magic forest"
                    enter()

            elif location == 'dragon cave':
                scrollTxt(f"~[{green}DRAGON CAVE{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}{italic}Surrounding {green}dragon cave{white} is the {turquoise}jade forest{white} to the {teal}north{white} and the {blue}ocean{white} surrounding every other {teal}direction{white} {normal}{bold}{normal}{bold}")
                    scrollTxt("")

                if "dragon cave" not in triggers:
                    triggers.append("dragon cave")
                    scrollTxt(
                        f"{italic}The {orange}dragon cave{white} has been the stuff of {gold}legend{white} and {purple}myths{white} for ages. A few poor {darkgrey}adventures{white} die every trying to slay the {red}dragon{white}{normal}{bold}")

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}The {orange}dragon cave{white} has been the stuff of {gold}legend{white} and {purple}myths{white} for ages. A few poor {darkgrey}adventures{white} die every trying to slay the {red}dragon{white}{normal}{bold}")

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {green}Inv : Stats : Settings : Save | Enter Cave : Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", 'enter cave', 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "enter cave":
                    scrollTxt(f"Pick up your {darkgrey}weapon{white} take a deep {platinum}breath{white} for it may be your {red}last{white}")
                    enter()
                    dungeon()

                elif answer == "leave":
                    scrollTxt(f"Where would you like to {blue}go{white}?")
                    scrollTxt(f"{teal}North{white}")
                    answer = get_input(['north'])
                    scrollTxt("")

                    print(f"You travel {orange}{answer}{white} for many {darkgrey}hours{white}")

                    if answer == "north":
                        location = "magic forest"
                    enter()

            if pre_loc != location:
                clear()
                travel_encounters = ["ambush", "stranger", "terrain", "chest", "guardian", "teleport"]
                if "weird merchant [1]" not in triggers or "weird merchant [2]" not in triggers or "weird merchant [3]" not in triggers: travel_encounters.append("weird merchant")
                encounter = random.choice(travel_encounters)

                if encounter == "ambush":
                    ambush_enemies = {
                        "pair of goblins": ["goblin 1", "goblin 2"],
                        "crazed troll": ["troll"],
                        "angry orc": ["orc"],
                        "bandit": ["bandit"]
                    }

                    enemy = random.choice(list(ambush_enemies.keys()))
                    scrollTxt(f"As you are {blue}traveling{white} your are {orange}ambushed{white} by a {copper}{enemy}{white}!")
                    enter()

                    combat(ambush_enemies[enemy])

                    scrollTxt(f"You are able to {green}defeat{white} the {copper}{enemy}{white} and you continue along the {brown}path{white}.")
                    enter()

                elif encounter == "stranger":
                    scrollTxt(f"You find a {brown}dirty{white} old {green}hermit{white} waving at you")
                    scrollTxt(f"He offers you a {yellow}ambiguously colored{white} {copper}mushroom{white} in enchange for {gold}1{white} gold")
                    answer = get_input(["yes", "no"])
                    print()

                    if answer == "yes":
                        if gp > 0:
                            gp -= 1
                            scrollTxt(f"{red}-1{white} {gold}Gold{white}")
                            scrollTxt(f"{green}+ mushroom{white}")
                            inv.append("mushroom")
                        else:
                            scrollTxt(f"You don\'t have {red}enough{white}")
                    else:
                        scrollTxt(f"You shrug and leave the {green}hermit{white}")
                    
                    print()
                    scrollTxt(f"You continue along the {brown}path{white}")
                    enter()

                elif encounter == "terrain":
                    scrollTxt(f'You come to a point on the {brown}path{white} where there is a {darkgrey}sheer{white} drop-off.')
                    if "rope" in inv:
                        scrollTxt(f"Options: {grey}Climb Down{white} | {yellow}Take another path{white} | {brown}Use Rope{white}")
                        scrollTxt(f"What would {blue}you{white} like to do?")
                        answer = get_input(["climb down", "take another path", "use rope"])
                    else:
                        scrollTxt(f"Options: {grey}Climb Down{white} | {yellow}Take another path{white}")
                        scrollTxt(f"What would {blue}you{white} like to do?")
                        answer = get_input(["climb down", "take another path"])
                    print()

                    if answer == "climb down":
                        if random.randint(1, 20) in range(1, dexterity + strength):
                            scrollTxt(f"You climb down {green}successfully{white}!")
                            scrollTxt(f"You continue along the {brown}path{white}")
                            enter()
                        else:
                            scrollTxt(f"You {red}fall{white} while {darkgrey}climbing{white} down!")
                            scrollTxt(f"-{red}4{white} Health")
                            health -= 4
                            if health < 1:
                                scrollTxt(f"You {red}died")
                                die()
                            scrollTxt(f"You {orange}shake{white} yourself off and continue along the {brown}path{white}")
                            enter()
                    if answer == "take another path":
                        scrollTxt(f'You take another {brown}path{white}')
                        enter()
                        clear()
                        travel_encounters = ["ambush", "stranger", "chest", "guardian", "teleport", "tips"]
                        encounter = random.choice(travel_encounters)

                        if encounter == "ambush":
                            ambush_enemies = {
                                "pair of goblins": ["goblin 1", "goblin 2"],
                                "crazed troll": ["troll"],
                                "angry orc": ["orc"],
                                "bandit": ["bandit"]
                            }

                            enemy = random.choice(list(ambush_enemies.keys()))
                            scrollTxt(f"As you are {blue}traveling{white} your are {orange}ambushed{white} by a {copper}{enemy}{white}!")
                            enter()

                            combat(ambush_enemies[enemy])

                            scrollTxt(f"You are able to {green}defeat{white} the {copper}{enemy}{white} and you continue along the {brown}path{white}.")
                            enter()

                        if encounter == "stranger":
                            scrollTxt(f"You find a {brown}dirty{white} old {green}hermit{white} waving at you")
                            scrollTxt(f"He offers you a {yellow}ambiguously colored{white} {copper}mushroom{white} in enchange for {gold}1{white} gold")
                            answer = get_input(["yes", "no"])
                            print()

                            if answer == "yes":
                                if gp > 0:
                                    gp -= 1
                                    scrollTxt(f"{red}-1{white} {gold}Gold{white}")
                                    scrollTxt(f"{green}+ mushroom{white}")
                                    inv.append("mushroom")
                                else:
                                    scrollTxt(f"You don\'t have {red}enough{white}")
                            else:
                                scrollTxt(f"You shrug and leave the {green}hermit{white}")
                            
                            print()
                            scrollTxt(f"You continue along the {brown}path{white}")
                            enter()

                    

                            if answer == "use rope":
                                    scrollTxt(f'You {green}easily{white} scale down the {darkgrey}cliff{white}')
                                    if random.randint(1, 4) == 4:
                                        scrollTxt(f"Sadly you {brown}rope{white} snaps from the {red}effort{white}")
                                        inv.remove("rope")
                                    scrollTxt(f"You continue along the {brown}path{white}")

                        if encounter == "chest":
                            scrollTxt(f"A small wedge in a {darkgrey}rock{white} catches you {blue}eye{white}")
                            scrollTxt(f"Upon closer {teal}inspection{white} you find a {gold}chest{white}")
                            scrollTxt(f'Would you like to {green}try{white} to open it?')
                            answer = get_input(["yes", "no"])
                            print()

                            if answer == "yes":
                                if random.randint(1, 3) == 1:
                                    scrollTxt(f"You try to open the {brown}chest{white} but it snaps it's {yellow}teeth{white} at you")
                                    scrollTxt(f"It\'s a {darkgrey}chest mimic{white}!")
                                    enter()
                                    combat(["chest mimic"])
                                    scrollTxt(f"You are {orange}shaken up{white} but continue along the {brown}path{white}")
                                    enter()
                                else:
                                    if random.randint(1, 5) in range(1, strength):
                                        scrollTxt(f"You are able to {green}open{white} the {gold}chest{white}")
                                        scrollTxt(f"You find {gold}5{white} GP")
                                        gp += 5
                                        scrollTxt(f"You continue along the {brown}path{white} in a {green}good{white} mood")
                                        enter()
                                    else:
                                        scrollTxt(f"You are {red}unable{white} to {blue}open{white} the {gold}chest{white}")
                                        scrollTxt(f"You continue along the {brown}path{white} in a {red}bad{white} mood")
                                        enter()
                            else:
                                scrollTxt(f"You decide it's better left {red}alone{white} and you continue along the {brown}path{white}")
                                enter()

                        if encounter == "guardian":
                            if lvl < 3: guardian = f"{copper}copper guardian{white}"
                            elif lvl > 9: guardian = f"{grey}steel guardian{white}"
                            elif lvl > 6: guardian = f"{darkgrey}iron guardian{white}"
                            else: guardian = f"{silver}silver guardian{white}"

                            scrollTxt(f'You encounter a huge {guardian}!')
                            scrollTxt(f"It {red}charges{white} at you")
                            scrollTxt(f"Do you {blue}RUN{white} or {orange}FIGHT{white} ?")
                            answer = get_input(["fight", "run"])
                            print()

                            if answer == "fight":
                                scrollTxt(f"You draw you {darkgrey}weapon{white} and {red}charge{white}!")
                                enter()

                                if lvl < 3: guardian = f"copper guardian"
                                elif lvl > 9: guardian = f"steel guardian"
                                elif lvl > 6: guardian = f"iron guardian"
                                else: guardian = f"silver guardian"

                                combat([guardian], 1.5)
                                scrollTxt(f"You stagger along the {brown}path{white}, {yellow}exhausted{white}")
                                enter()

                            else:
                                scrollTxt(f"You {turquoise}narrowly{white} escape the {copper}guardain{white} but not before it {orange}strikes{white} you")
                                scrollTxt(f"- {red}3{white} Health")

                                health -= 3

                                if health < 1:
                                    scrollTxt(f"This {red}kills{white} you 💀")
                                    die()

                                enter()
                        
                        if encounter == "teleport":
                            scrollTxt(f"You are {blue}traveling{white} along the {copper}path{white} when a {darkgrey}cloaked figure{white} appears right in front of you")
                            scrollTxt(f"The {darkgrey}teleportator{white} offer to sell you the {orange}power{white} of {turquoise}teleportation{white} in a small {darkgrey}token{white} for {gold}10{white} GP [{green}y{white}/{red}n{white}]")
                            answer = get_input(["yes", "no"])
                            print()

                            if answer == "yes":
                                if gp > 9:
                                    scrollTxt(f"+ {darkgrey}teleportation token{white}")
                                    scrollTxt(f"- {gold}10{white} GP")
                                    inv.append("teleportation token")
                                    gp -= 10
                                else:
                                    scrollTxt(f"You don\'t have {red}enough{white}")
                            
                                print()

                            scrollTxt(f"The {darkgrey}figure{white} then offers to sell you the {orange}permanent power{white} of {turquoise}teleportation{white} for {gold}170{white} GP [{green}y{white}/{red}n{white}]")
                            answer = get_input(["yes", "no"])
                            print()

                            if answer == "yes":
                                if gp >= 170:
                                    scrollTxt(f"+ {darkgrey}teleportation staff{white}")
                                    scrollTxt(f"- {gold}170{white} GP")
                                    inv.append("teleportation staff")
                                    gp -= 170
                                else:
                                    scrollTxt(f"You don\'t have {red}enough{white}")
                            
                                print()

                            scrollTxt(f"You continue along the {copper}path{white}")
                            enter()

                        if encounter == "tips":
                            scrollTxt(f"You find a {paleyellow}Wise Old Man{white}!")
                            rtips = ["Drink magi potions to replenish spells", "Shops chance prices every 5 min", "Luck potions are really usefull", "The BLESSED LAKE is very important"]
                            crollTxt('\"' + random.choice(rtips) + '\" says the Wise Old Man')
                            scrollTxt(f"You continue along the {copper}path{white}")
                            enter()
                    if answer == "use rope":
                            scrollTxt(f'You {green}easily{white} scale down the {darkgrey}cliff{white}')
                            if random.randint(1, 4) == 4:
                                scrollTxt(f"Sadly you {brown}rope{white} snaps from the {red}effort{white}")
                                inv.remove("rope")
                            scrollTxt(f"You continue along the {brown}path{white}")
                            enter()

                elif encounter == "chest":
                    scrollTxt(f"A small wedge in a {darkgrey}rock{white} catches you {blue}eye{white}")
                    scrollTxt(f"Upon closer {teal}inspection{white} you find a {gold}chest{white}")
                    scrollTxt(f'Would you like to {green}try{white} to open it?')
                    answer = get_input(["yes", "no"])
                    print()

                    if answer == "yes":
                        if random.randint(1, 3) == 1:
                            scrollTxt(f"You try to open the {brown}chest{white} but it snaps it's {yellow}teeth{white} at you")
                            scrollTxt(f"It\'s a {darkgrey}chest mimic{white}!")
                            enter()
                            combat(["chest mimic"])
                            scrollTxt(f"You are {orange}shaken up{white} but continue along the {brown}path{white}")
                            enter()
                        else:
                            if random.randint(1, 5) in range(1, strength):
                                scrollTxt(f"You are able to {green}open{white} the {gold}chest{white}")
                                scrollTxt(f"You find {gold}5{white} GP")
                                gp += 5
                                scrollTxt(f"You continue along the {brown}path{white} in a {green}good{white} mood")
                                enter()
                            else:
                                scrollTxt(f"You are {red}unable{white} to {blue}open{white} the {gold}chest{white}")
                                scrollTxt(f"You continue along the {brown}path{white} in a {red}bad{white} mood")
                                enter()
                    else:
                        scrollTxt(f"You decide it's better left {red}alone{white} and you continue along the {brown}path{white}")
                        enter()

                elif encounter == "guardian":
                    if lvl < 3: guardian = f"{copper}copper guardian{white}"
                    elif lvl > 9: guardian = f"{grey}steel guardian{white}"
                    elif lvl > 6: guardian = f"{darkgrey}iron guardian{white}"
                    else: guardian = f"{silver}silver guardian{white}"

                    scrollTxt(f'You encounter a huge {guardian}!')
                    scrollTxt(f"It {red}charges{white} at you")
                    scrollTxt(f"You you {blue}RUN{white} or {orange}FIGHT{white} ?")
                    answer = get_input(["fight", "run"])
                    print()

                    if answer == "fight":
                        scrollTxt(f"You draw you {darkgrey}weapon{white} and {red}charge{white}!")
                        enter()

                        if lvl < 3: guardian = f"copper guardian"
                        elif lvl > 9: guardian = f"steel guardian"
                        elif lvl > 6: guardian = f"iron guardian"
                        else: guardian = f"silver guardian"

                        combat([guardian], 1.5)
                        scrollTxt(f"You stagger along the {brown}path{white}, {yellow}exhausted{white}")
                        enter()

                    else:
                        scrollTxt(f"You {turquoise}narrowly{white} escape the {copper}guardain{white} but not before it {orange}strikes{white} you")
                        scrollTxt(f"- {red}3{white} Health")

                        health -= 3

                        if health < 1:
                            scrollTxt(f"This {red}kills{white} you 💀")
                            die()

                        enter()

                elif encounter == "teleport":
                    scrollTxt(f"You are {blue}traveling{white} along the {copper}path{white} when a {darkgrey}cloaked figure{white} appears right in front of you")
                    scrollTxt(f"The {darkgrey}teleportator{white} offer to sell you the {orange}power{white} of {turquoise}teleportation{white} in a small {darkgrey}token{white} for {gold}10{white} GP [{green}y{white}/{red}n{white}]")
                    answer = get_input(["yes", "no"])
                    print()

                    if answer == "yes":
                        if gp > 9:
                            scrollTxt(f"+ {darkgrey}teleportation token{white}")
                            scrollTxt(f"- {gold}10{white} GP")
                            inv.append("teleportation token")
                            gp -= 10
                        else:
                            scrollTxt(f"You don\'t have {red}enough{white}")
                    
                        print()

                    scrollTxt(f"The {darkgrey}figure{white} then offers to sell you the {orange}permanent power{white} of {turquoise}teleportation{white} for {gold}170{white} GP [{green}y{white}/{red}n{white}]")
                    answer = get_input(["yes", "no"])
                    print()

                    if answer == "yes":
                        if gp >= 170:
                            scrollTxt(f"+ {darkgrey}teleportation staff{white}")
                            scrollTxt(f"- {gold}170{white} GP")
                            inv.append("teleportation staff")
                            gp -= 170
                        else:
                            scrollTxt(f"You don\'t have {red}enough{white}")
                    
                        print()

                    scrollTxt(f"You continue along the {copper}path{white}")
                    enter()

                elif encounter == "weird merchant":
                    if "weird merchant [1]" not in triggers:
                        sel_item = "tazer"
                        sel_txt = f"{darkgrey}tazer{white}"
                        sel_cost = 25
                        triggers.append("weird merchant [1]")

                    elif "weird merchant [2]" not in triggers:
                        sel_item = "combo gloves"
                        sel_txt = f"{red}oversized boxing gloves{white}"
                        sel_cost = 45
                        triggers.append("weird merchant [2]")

                    elif "weird merchant [3]" not in triggers:
                        sel_item = "the stick to rule them all"
                        sel_txt = f"{brown}small thin ugly stick{white}"
                        sel_cost = 60
                        triggers.append("weird merchant [3]")

                    scrollTxt(f"You find a {red}jest{white}{blue}er{white} holding what appears to be a {sel_item}???!?!?!")
                    scrollTxt(f"You draw your {darkgrey}weapon{white} but the {red}jest{white}{blue}er{white} offers you the {sel_item}")
                    scrollTxt(f"The {sel_item} cost {gold}{sel_cost}{white} GP")
                    scrollTxt(f"Would you like to {orange}buy{white} it? [{green}y{white}/{red}n{white}]")
                    answer = get_input(["yes", "no"], invis_commands=["give me it for free!"])
                    
                    if answer == "yes":
                        if gp >= sel_cost:
                            scrollTxt(f"You got {blue}{sel_item}{white}!")
                            scrollTxt(f"- {gold}{sel_cost}{white} GP")
                            gp -= sel_cost
                            inv.append(sel_item)
                        else:
                            scrollTxt(f'You don\'t have {red}enough{white}!')

                    if answer == "give me it for free!":
                        scrollTxt(f"For some {red}reason{white} the {red}jest{white}{blue}er{white} gives you it for {gold}FREE{white}")
                        scrollTxt(f"You got {blue}{sel_item}{white}!")
                        inv.append(sel_item)

                    print()
                    scrollTxt(f"You continue along the {brown}path{white}...")
                    enter()
        
        
        elif world == "frozite":
            if location == "white bridge":
                scrollTxt(f"~[{blue}WHITE BRIDGE{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap_frozite()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding {blue}white bridge{white} is open {blue}ice tundura{white} to the {teal}north{white}, {teal}east{white}, and {teal}south{white}, a {purple}burrow{white} to the {teal}south{white} and great {darkgrey}mountains{white} to the {teal}west{white}.{normal}{bold}")
                    scrollTxt("")

                if "white bridge" not in triggers:
                    triggers.append("white bridge")
                    scrollTxt(
                        f"{italic}Folk covered in {brown}warm clothes{white} talk to each {teal}other{white} inside the {darkgrey}protective walls{white} of {silver}white bridge{white}. There is a {orange}cozy tavern{white}, it\'s name covered in {teal}snow{white}. Wandering {turquoise}traders{white} are offering {brown}goods{white} in the {darkgrey}shops{white}. {normal}{bold}")

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}Folk covered in {brown}warm clothes{white} talk to each {teal}other{white} inside the {darkgrey}protective walls{white} of {silver}white bridge{white}. There is a {orange}cozy tavern{white}, it\'s name covered in {teal}snow{white}. Wandering {turquoise}traders{white} are offering {brown}goods{white} in the {darkgrey}shops{white}. {normal}{bold}")

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {green}Inv : Stats : Settings : Save | Tavern : Encounter : Shops : Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", 'tavern', 'encounter', 'shops', 'leave'], invis_commands=["give me gold", "keynote"])
                scrollTxt("")

                usual_options(answer)

                if answer == "tavern":
                    while True:
                        clear()
                        scrollTxt("")
                        scrollTxt(f"~[{grey}Frosted Inn{white}]~")
                        scrollTxt("")
                        scrollTxt(
                            f"The {brown}tavern{white} is filled with {ironc}peaceful{white} {white}music{white}. People gather round playing {purple}dice{white}. A {turquoise}keeper{white} is serving a {yellow}Lightning Cider{white} to someone.")
                        scrollTxt(f"{turquoise}What would you like to do{white}?")
                        scrollTxt(f"> {green}Inv : Stats : Settings : Save | Bards : Dice : Keeper : Leave{white}")
                        answer = get_input(['inv', 'stats', 'settings', "save", 'bards', 'dice', 'keeper', "leave"])
                        print()

                        usual_options(answer)

                        if answer == "bards":
                            scrollTxt(f"You walk over to the {orange}bards{white} playing {blue}music{white}.")
                            scrollTxt(f"Would you like to {gold}tip{white} them? [{green}y{white}/{red}n{white}]")
                            answer = get_input(['yes', 'no'])
                            scrollTxt(f"")

                            if answer == "yes":
                                scrollTxt(f"How much would you like to {red}give{white}?")
                                commands = []
                                for x in range(1, gp + 1):
                                    commands.append(str(x))
                                how_much = int(get_input(commands, g= True))
                                scrollTxt("")

                                scrollTxt(f"- {gold}{how_much}{white} GP")
                                gp -= how_much
                                if how_much > 5:
                                    print()
                                    scrollTxt(f"One of the {brown}bards{white} whispers into your ear, '{gold}secret treasure{white} lies buried in {teal}white bridge{white}. just type \"{darkgrey}give me gold{white}\"'")
                                else:
                                    print()
                                    scrollTxt(f"One of the {brown}bards{white} whispers into your ear, '{gold}secret treasure{white} lies buried in {teal}white bridge{white}. just type \"{darkgrey}keynote{white}\"'")

                            else:
                                scrollTxt(f"You {teal}walk{white} away...")
                                scrollTxt(f"The {brown}bards{white} frown at you 😠")

                            enter()

                        if answer == 'dice':
                            scrollTxt(f"You walk over to the {blue}people{white} playing {darkgrey}dice{white}.")
                            scrollTxt(f"Would you like to {purple}join{white} them? [{green}y{white}/{red}n{white}]")
                            answer = get_input(['yes', 'no'])
                            scrollTxt(f"")

                            if answer == "yes":
                                scrollTxt(f"You play {darkgrey}dice{white}")
                                enter()

                                dice()

                            else:
                                scrollTxt(f"You {blue}walk{white} away...")

                            enter()

                        if answer == "leave":
                            scrollTxt(f"You walk out of the {darkgrey}tavern{white}...")
                            enter()
                            break

                        if answer == "keeper":
                            scrollTxt(f"What would you like to {blue}buy{white}?")
                            Shop(["mushroom soup", 'hardy bread', 'lightning cider'], [5, 10, 20],
                                    f"{darkgrey}The Frosted Inn{white}", 20)

                elif answer == "shops":
                    scrollTxt(f"You walk over to the {darkgrey}Shops{white}")
                    enter()

                    clear()

                    while True:
                        clear()
                        clear()
                        scrollTxt("")
                        scrollTxt(f"~[{blue}SHOPS{white}]~")
                        scrollTxt("")
                        scrollTxt(
                            f"Traders from across the {lime}world{white} are gathers here to sell {purple}rare items{white} and {darkgrey}weapons{white}.")
                        scrollTxt(f"{teal}Which merchant would you like to go to{white}?")
                        scrollTxt(f"{green}> Blacksmith : Alchemist : Wizard : Leave{white}")
                        answer = get_input(["blacksmith", 'alchemist', "wizard", 'leave'])
                        print()

                        if answer == "blacksmith":
                            scrollTxt(f"You walk over to the {darkgrey}blacksmith{white}...")
                            Shop(["steel broadsword", 'frozen katana', 'platinum shield'], [120, 150, 200],
                                    f"The {darkgrey}Smithery{white}")
                     
                        if answer == "alchemist":
                            scrollTxt(f"You walk over to the {purple}alchemist{white}...")
                            Shop(["hyper heal potion", 'magi potion', 'frosted potion'], [15, 10, 30],
                                    f"{darkgrey}Storm{white} brewery", 20)
                        if answer == "wizard":
                            scrollTxt(f"You walk over to the {copper}staff crafter{white}...")
                            Shop(["frost staff", 'gold staff', 'dread staff'], [200, 300, 400],
                                    f"{turquoise}Crystalized{white} Magic")
                       
                        if answer == "leave":
                            scrollTxt(f"You leave the {teal}shops{white}...")
                            enter()
                            break

                elif answer == "encounter":
                    scrollTxt(f"You mull around the {brown}village{white} looking {blue}around{white}>")
                    enter()

                    while True:
                        clear()
                        scrollTxt(f"~[{teal}VILLAGE HUB{white}]~")
                        scrollTxt("")
                        if "cloaked sick" not in triggers:
                            scrollTxt(f"You see [{red}A{white}] A person huddled in a {darkgrey}ragged cloak{white}. [{red}B{white}] A group of {purple}Spike Gang Members{white}. [{red}C{white}] An old man holding a {yellow}citrine staff{white}.")
                            scrollTxt(f"Who would you like to {brown}talk{white} to?")
                            scrollTxt(f"{green}> A : B : C : Leave{white}")
                            answer = get_input(["a", "b", 'c', 'leave'])
                        else:
                            scrollTxt(f"You see [{red}B{white}] A group of {purple}Spike Gang Members{white}. [{red}C{white}] An old man holding a {yellow}citrine staff{white}.")
                            scrollTxt(f"Who would you like to {brown}talk{white} to?")
                            scrollTxt(f"{green}> B : C : Leave{white}")
                            answer = get_input(["b", 'c', 'leave'])
                        print()

                        if answer == "leave":
                            scrollTxt(f"You walk {blue}away{white}...")
                            enter()

                            break

                        if answer == "b":
                            scrollTxt(f"You walk over to the {red}Spike gang members{white}")

                            if "gang killed" not in triggers:
                                if "spike gang" not in triggers:
                                    triggers.append("spike gang")
                                scrollTxt(f'"{darkgrey}*growl* Get lost stranger{white}"')
                                scrollTxt(f"{turquoise}What would you like to do{white}?")
                                scrollTxt(f"{green}> Fight : Leave{white}")
                                answer = get_input(["fight", 'leave'])
                                print()

                                if answer == "fight":
                                    combat(['spike gang runt', 'spike gang runt 2', "spike gang leader"])
                                    triggers.append("gang killed")
                                    scrollTxt(f"You cover their {red}bodies{white} in {teal}snow{white} to hide the {blue}evidence{white}...")
                                    enter()

                                if answer == "leave":
                                    scrollTxt(f"You {red}leave{white}")
                                    enter()
                            else:
                                scrollTxt(f"The {red}remaining{white} gang members flee in {blue}terror{white}")
                                enter()


                        if answer == "c":
                            if "frozite wizard" not in triggers:
                                triggers.append("frozite wizard")
                                scrollTxt(f"You walk up to the {teal}Wizard stranger{white}")

                                scrollTxt(
                                    f'"Well hello where, would you like to buy a {red}crazy spell{white} I\'ve made? I call it {darkgrey}tornado {red}burst{white}. It will cost you {gold}50{white} GP though{white}" [{green}y{white}/{red}n{white}]')
                                answer = get_input(["yes", 'no'])
                                print()

                                if answer == "yes":
                                    if gp > 49:
                                        scrollTxt(f"+ {darkgrey}tornado {red}burst{white} | - {gold}50{white} GP")
                                        gp -= 50
                                        known_spells.append("tornado burst")
                                        current_spells.append("tornado burst")
                                    else:
                                        scrollTxt(f"You dont have {red}enough{white}")

                                scrollTxt(f"You {red}leave{white}")
                                enter()

                            else:
                                scrollTxt(f"You walk up to the {teal}Wizard stranger{white}")

                                scrollTxt(
                                    f'"Well hello {lime}pear{white}, nice to see you again')
                                scrollTxt(f"Do you want to buy the {purple}spell{white}?")
                                answer = get_input(["yes", 'no'])
                                print()

                                if answer == "yes":
                                    if gp > 49:
                                        scrollTxt(f"+ {darkgrey}tornado {red}burst{white} | - {gold}50{white} GP")
                                        gp -= 50
                                        known_spells.append("tornado burst")
                                        current_spells.append("tornado burst")
                                    else:
                                        scrollTxt(f"You dont have {red}enough{white}")

                                scrollTxt(f"You {red}leave{white}")
                                enter()

                        if answer == "a":
                            scrollTxt(f"You walk up the the person in a {darkgrey}dark cloak{white}")
                            print()
                            if "cloaked sick" not in triggers:
                                scrollTxt(f'\"*cough* bring me a {red}{italic}healing stone{normal}{bold}{white}... please I\'m {darkgrey}dying{white}\", whispers the {purple}cloaked stranger{white}')
                                scrollTxt(f"What would you {red}say{white}?")
                                scrollTxt(f"[{orange}I don't care{white}] [{blue}Sorry{white}] [{teal}Too bad{white}] [{turquoise}I'll find it{white}]", end="", flush=True)
                                if "healing stone" in inv:
                                    scrollTxt(f" [{platinum}I have it, here{white}] [{purple}I have it but you can\'t have it{white}]",end="", flush=True)
                                print()
                                answer = get_input(["i don't care", "sorry", "too bad", "i'll find it", "i have it, here", "i have it but you can't"])
                                if answer in ["i don't care", "too bad", "i have it but you can't"]:
                                    print()
                                    scrollTxt(f"The {darkgrey}figure{white} shakes his head sadly.")
                                    scrollTxt(f"'Such is how the {lime}world{white} treats the {red}sick{white}', he mutters")
                                if answer in ["sorry"]:
                                    print()
                                    scrollTxt(f'"DON\'T APPOLIGIZE BRING ME IT", the figure {red}screams{white}')
                                if answer in ["i'll find it"]:
                                    print()
                                    scrollTxt(f'"Thank you, please {teal}hurry{white}", the {purple}figure{white} tells you')
                                if answer in ["i have it, here"]:
                                    triggers.append("cloaked sick")
                                    print()
                                    scrollTxt(f'You hand the {purple}the figure{white} the {red}red stone{white}')
                                    inv.remove('healing stone')
                                    scrollTxt(f"- {red}healing stone{white}")
                                    print()
                                    scrollTxt(f'"You have my {blue}blessing{white} sadly that is all I can give", sighs the {purple}figure{white}')
                                    scrollTxt(f"+ {red}1{white} strength")
                                    scrollTxt(f"+ {blue}1{white} dexterity")
                                    dexterity += 1
                                    strength += 1
                                    
                                enter()

                elif answer == "keynote" and "keynote" not in triggers:
                    triggers.append("keynote")
                    scrollTxt(f"You start {brown}digging{white} around {silver}white bridge{white}...")
                    time.sleep(2)
                    scrollTxt(f"You found {gold}20{white} gp and a {teal}frosted potion{white}!")
                    enter()
                    gp += 20
                    inv.append('frosted potion')
                elif answer == "give me gold" and "give me gold" not in triggers:
                    triggers.append("give me gold")
                    scrollTxt(f"You start {brown}digging{white} around {silver}white bridge{white}...")
                    time.sleep(2)
                    scrollTxt(f"You found {gold}40{white} gp and a piece of {copper}hardy bread{white}!")
                    enter()
                    gp += 40
                    inv.append('hardy bread')
                
                elif answer == "leave":
                    scrollTxt(f"You may travel {blue}north{white}, {blue}south{white}, {blue}west{white} or {blue}east{white}")
                    answer = get_input(["north", "east", "south", "west"])
                    print()
                    scrollTxt(f"You travel {red}answer{white} for a couple {blue}hours{white}")
                    if answer == "north":
                        location = "frosted cave"
                    if answer == "south": location = "goliaths burrow"
                    if answer == "east":
                        location = "sunken graveyard"
                    if answer == "west": location = "monk cliffs"
                        
                    enter()
            
            elif location == "frosted cave":
                scrollTxt(f"~[{blue}FROSTED CAVE{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap_frozite()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding the {blue}frosted cave{white} is {platinum}White bridge{white} to the {teal}south{white} a {blue}cold lake{white} to the {teal}north{white}, and the {turquoise}ocean{white} to the {teal}east{white} and {teal}west{white}.{normal}{bold}")
                    scrollTxt("")

                if "giants layer" not in triggers:
                    triggers.append("giants layer")
                    scrollTxt(
                        f"{italic}{grey}Smoke{white} rises from a {red}fire{white} inside the {teal}frozen{darkgrey} cave{white}. You smell cooked {brown}mammoth{white} although those creatures are very hard to {red}kill{white}...{normal}{bold}"
                    )

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}{grey}Smoke{white} rises from a {red}fire{white} inside the {teal}frozen{darkgrey} cave{white}. You smell cooked {brown}mammoth{white} although those creatures are very hard to {red}kill{white}...{normal}{bold}"
                    )

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {purple}Inv{white} / {darkgrey}Stats{white} / {red}Settings{white} / {silver}Save{white} | {teal}Venture into cave{white} / {platinum}Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", "venture into cave", 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "venture into cave":
                    print("")
                    scrollTxt(f"You decide to venture into the {teal}frosty cave{white}.")
                    scrollTxt(
                        f"Upon getting a close {blue}look{white} you see that there are {red}2{white} {teal}Frost{darkgrey} Giants{white}")
                    print()
                    scrollTxt(f"How do you {turquoise}procede{white}?")
                    scrollTxt(f"    * [{orange}CA{white}] - Charge and attack")
                    scrollTxt(f"    * [{blue}OBO{white}] - Take them down one by one")
                    scrollTxt(f"    * [{green}LA{white}] - Look around for other options")
                    scrollTxt(f"    * [{yellow}RL{white}] - Run and leave")

                    answer = get_input(["ca", 'obo', 'la', 'rl'])
                    print()

                    if answer == "ca":
                        scrollTxt(
                            f"You decide that the {gold}best{white} option is to {orange}charge{white} and {turquoise}take{white} on all the {copper}giants{white} at once!")
                        enter()
                        combat(["frost giant 1", 'frost giant 2'], 1.5)

                    if answer == "obo":
                        scrollTxt(
                            f"You decide that the {gold}best{white} option is to take each of the {blue}frost{darkgrey} giants{white} on {red}one{white} at a time.")
                        eleft = ['frost giant 1', 'frost giant 2']
                        while len(eleft) > 0:
                            if random.randint(1, 7) in range(1, dexterity):
                                print(
                                    f"You are {turquoise}able{white} to {lime}locate{white} and {red}corner{white} one {copper}giant{white}!")
                                enter()
                                echose = random.choice(eleft)
                                combat([echose])
                                eleft.remove(echose)
                            else:
                                print(
                                    f"You are {red}spotted{white} and the rest of the {teal}frost{darkgrey} giants{white} charge at you!")
                                enter()
                                combat(eleft)
                                eleft = []

                            print()

                        triggers.append("frost giants killed")

                    if answer == "la":
                        crollTxt(
                            "You decide that none of the other options are the best and you should look for other ways of attacking")
                        crollTxt("After doing a thorough search of the area you find 2 things")
                        crollTxt(f"[{darkgrey}ARROW{white}]     - A huge stalagmite that can fall on the frost giants")
                        crollTxt(f"[{red}FIRE{white}]     - A leather blanket that can be lit on fire")
                        print()
                        crollTxt("What would you like to do?")
                        answer = get_input(["fire", "arrow"])
                        print()

                        if answer == "fire":
                            if "firebolt" not in known_spells and "torch" not in inv:
                                crollTxt("You fail to find a way to light the leather blanket on fire")
                            else:
                                if "firebolt" in known_spells:
                                    crollTxt(f"You use {orange}FIREBOLT{white} to light the tree on fire")
                                    crollTxt("1 of the giants die before fire is put out")
                                    crollTxt(f"You charge at the remaining {teal}FROST {darkgrey}GIANTS{white}")
                                    enter()
                                    combat(["frost giant"])
                                else:
                                    inv.remove("torch")
                                    crollTxt("You throw your torch at the leather blanket and light it on fire")
                                    crollTxt("1 of the giants die before fire is put out")
                                    crollTxt(f"You charge at the remaining {teal}FROST {darkgrey}GIANTS{white}")
                                    enter()
                                    combat(["frost giant"])
                                triggers.append("giants killed")

                            enter()
                        if answer == "arow":
                            bow_check = False
                            for item in inv:
                                if "bow" in item:
                                    bow_check = True
                            if bow_check is False:
                                crollTxt("You fail to find a way to fire an arrow at the stalagmite")
                            else:
                                crollTxt("You fire an arrow hitting the stalagmite causing it to fall on one of the giants")
                                crollTxt(f"The giant takes {red}20{white} damage")
                                crollTxt(f"You charge at the rest of the {teal}FROST {darkgrey}GIANTS{white}")
                                enter()
                                combat(["frost giant 1", "frost giant 2"], enemies_damaged = [0, 20])
                                triggers.append("giants killed")

                    if answer == "rl":
                        crollTxt("You run away from the cave")
                        enter()
            

                if answer == "leave":
                    scrollTxt(f"You may travel {blue}south{white} or {blue}north{white}")
                    answer = get_input(["north", "south"])
                    print()
                    scrollTxt(f"You travel {red}answer{white} for a couple {blue}hours{white}")
                    if answer == "north":
                        location = "dead lake"
                    if answer == "south": location = "white bridge"
                    
            elif location == "goliaths burrow":
                scrollTxt(f"~[{blue}Goliaths Burrow{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap_frozite()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding the {blue}burrow{white} is {platinum}White bridge{white} to the {teal}north{white} a huge {darkgrey}colloseum{white} to the {teal}south{white}, a {red}plateau{white} to the {teal}east{white} and the {turquoise}ocean{white} to the {teal}west{white}.{normal}{bold}")
                    scrollTxt("")

                if "goliaths burrow" not in triggers:
                    triggers.append("goliaths burrow")
                    scrollTxt(
                        f"{italic}You can make a out a {darkgrey}lonely goliath{white} huddling in the {teal}cold{white}, cluched in hand is a {red}healing stone{white} but he looks very {purple}hungery{white}.{normal}{bold}"
                    )

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}You can make a out a {darkgrey}lonely goliath{white} huddling in the {teal}cold{white}, cluched in hand is a {red}healing stone{white} but he looks very {purple}hungery{white}.{normal}{bold}"
                    )

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {purple}Inv{white} / {darkgrey}Stats{white} / {red}Settings{white} / {silver}Save{white} | {teal}Go toward goliath{white} / {platinum}Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", "go towards goliath", 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "go towards goliath":
                    scrollTxt(f"You reach the {teal}go{darkgrey}liath{white}. He seems to take no {red}notice{white}")
                    commands = ["leave"]
                    if "hardy bread" in inv:
                        commands.append('hardy bread')
                        scrollTxt(f"[{brown}Give Hardy Bread{white}] ", end="", flush=True)
                    if "mammoth meat" in inv:
                        commands.append("mammoth meat")
                        scrollTxt(f"[{red}Give Mammoth Meat{white}] ", end="", flush=True)
                    if "lightning cider" in inv:
                        commands.append("lightning cider")
                        scrollTxt(f"[{yellow}Give Lightning Cider{white}]", end="", flush=True)
                    if "mushroom soup" in inv:
                        commands.append("mushroom soup")
                        scrollTxt(f"[{copper}Give Mushroom soup{white}]", end="", flush=True)
                    scrollTxt(f"[{blue}Leave{white}]")
                    if commands == ["leave"]:
                        scrollTxt(f"{italic}you need food{normal}{bold}")
                    scrollTxt(f"What would you like to {blue}do{white}?")
                    answer = get_input(commands)
                    print()
                    if answer != 'leave':
                        inv.remove(answer)
                        scrollTxt(f"You give the {darkgrey}goliath{white} a {copper}{answer}{white}")
                        if answer == "hardy bread":
                            print()
                            scrollTxt(f"The {darkgrey}goliath{white} gobbles down the {brown}warm bread{white}")
                            scrollTxt(f"He smiles {blue}gratefully{white} at you and gives his {red}healing stone{white}")
                            scrollTxt(f"+ {red}healing stone{white}")
                            inv.append("healing stone")
                        elif answer == "mammoth meat":
                            print()
                            scrollTxt(f"The {darkgrey}goliath{white} gobbles down the {brown}hardy meat{white}")
                            scrollTxt(f"He smiles {blue}gratefully{white} at you and gives his {red}healing stone{white}")
                            scrollTxt(f"+ {red}healing stone{white}")
                            inv.append("healing stone")
                        elif answer == "mushroom soup":
                            scrollTxt(f"The {darkgrey}goliath{white} slurps the {copper}mushroom soup{white}")
                            scrollTxt(f"He then {red}spits{white} it out and {orange}roars{white}!")
                            enter()
                            combat(["goliath"])
                        else:
                            scrollTxt(f"The {darkgrey}goliath{white} slips the {gold}lightning cider{white}")
                            scrollTxt(f"He jumps up as he is {red}struck{white} by a bolt of {yellow}lightning{white}!")
                            scrollTxt(f"He {orange}roars{white} and charges at you!")
                            enter()
                            combat(["goliath"])
                        enter()
                    else:
                        scrollTxt(f"You leave the {darkgrey}goliath{white}")
                        enter()


                if answer == "leave":
                    scrollTxt(f"You may travel {blue}north{white} or {blue}south{white}")
                    answer = get_input(["north", "south"])
                    if answer == "north":
                        location = "white bridge"
                    if answer == "south": location = "core-sail arena"
                    enter()

            elif location == "sunken graveyard":
                scrollTxt(f"~[{blue}SUNKEN GRAVEYARD{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap_frozite()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding the {blue}sunken graveyard{white} is {platinum}White bridge{white} to the {teal}west{white} {darkgrey}mountains{white} to the {teal}east{white}, a {red}plateau{white} to the {teal}south{white} and the {turquoise}ocean{white} to the {teal}north{white}.{normal}{bold}")
                    scrollTxt("")

                if "sunken grave" not in triggers:
                    triggers.append("sunken grave")
                    scrollTxt(
                        f"{italic}Suken into the {brown}ground{white} is a {darkgrey}lonely graveyard{white}. Graves 🪦 are {red}scattered{white} around. You can see 3 {turquoise}gh{teal}os{blue}ts{white}. {normal}{bold}"
                    )

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}Suken into the {brown}ground{white} is a {darkgrey}lonely graveyard{white}. Graves 🪦 are {red}scattered{white} around. You can see 3 {turquoise}gh{teal}os{blue}ts{white}. {normal}{bold}"
                    )

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {purple}Inv{white} / {darkgrey}Stats{white} / {red}Settings{white} / {silver}Save{white} | {teal}Go to ghosts{white} / {platinum}Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", "go to ghosts", 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "go to ghosts":
                    scrollTxt(f"You walk up to the {turquoise}gh{teal}os{blue}ts{white}.")
                    scrollTxt(f"One of them {red}rudely{white} says, '{darkgrey}WhO aRe YoU!{white}'")
                    scrollTxt(f'How do you {blue}respond{white}: {purple}None the matter to you{white} / {darkgrey}A stranger{white}')
                    answer = get_input(["none the matter to you", "a stranger"])
                    print()

                    if answer == "none the matter to you":
                        scrollTxt(f"The {turquoise}gh{teal}os{blue}ts{white} all {red}charge{white} at you!")
                        enter()
                        combat(["ghost 1", "ghost 2", "ghost 3"])
                    elif answer == "a stranger":
                        scrollTxt(f"Another {turquoise}gh{teal}os{blue}t{white} tells you, '{darkgrey}Listen youngster, and listen good, I have been around here longer that you, and I've have stories to tell unlike you!{white}'")
                        scrollTxt(f'How do you {blue}respond{white}: {purple}Ok{white} / {darkgrey}I don\'t care{white} / {red}Please tell me{white}')
                        answer = get_input(["ok", "i don't care", "please tell me"])

                        print()

                        if answer == "ok" or answer == "i don't care":
                            scrollTxt(f"'{darkgrey}How rude, not wanting to hear our stories{white}' the {turquoise}gh{teal}os{blue}ts{white} cry.")
                            scrollTxt(f"Then they all {red}attack{white} you")
                            enter()
                            combat(["ghost 1", "ghost 2", "ghost 3"])
                        elif answer == "please tell me":
                            scrollTxt(f"'{darkgrey}Well alright{white}', the {turquoise}gh{teal}os{blue}t{white} continues, '{darkgrey}I fought in many a war. I killed thousands, nay millions of soliders. I twas the top of my army. Until some coward shot me from afar{white}'")
                            scrollTxt(f'How do you {blue}respond{white}: {purple}I doubt it{white} / {darkgrey}Wow{white} / {red}Lol imagine dying{white}')
                            answer = get_input(["i doubt it", "wow", "lol imagine dying"])
                            print()
                            if answer == "i doubt it" or answer == "lol imagine dying":
                                scrollTxt(f"'{darkgrey}HOW DARE YOU!!!!!!!!!!{white}' the {turquoise}gh{teal}os{blue}ts{white} cry.")
                                scrollTxt(f"Then they all {red}attack{white} you")
                                enter()
                                combat(["ghost 1", "ghost 2", "ghost 3"])
                            elif answer == "wow":

                                scrollTxt(f"They {turquoise}gh{teal}os{blue}t{white} nods his head, '{darkgrey}looks like this one respects elders, and GHOSTS{white}'")
                                scrollTxt(f"You got {turquoise}gh{teal}os{blue}t{white} {purple}blessing{white}")
                                if "ghost blessing" not in triggers:
                                    triggers.append("ghost blessing")
                                    scrollTxt(f" + {gold}50{white} Gp")
                                    scrollTxt(f" + {red}5{white} Max Hp")
                                    max_health += 5
                                    gp += 50
                                    enter()


                if answer == "leave":
                    scrollTxt(f"{blue}Areas have not been added{white}")
                    scrollTxt(f"You may only travel {blue}west{white}")
                    enter()
                    location = "white bridge"
            
            elif location == "dead lake":
                scrollTxt(f"~[{blue}DEAD LAKE{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap_frozite()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding the {blue}dead lake{white} is open {blue}ice tundura{white} to the {teal}south{white}, a {green}forest{white} to the {teal}north{white}, more {blue}lake{white} to the {teal}east{white} and the {turquoise}ocean{white} to the {teal}west{white}.{normal}{bold}")
                    scrollTxt("")

                if "dead lake" not in triggers:
                    triggers.append("dead lake")
                    scrollTxt(
                        f"{italic}You on the {gold}beach{white} a {darkgrey}merchant{white} holding a {red}bubbling red{white} potion. The {darkgrey}merchant{white} also has a huge {purple}longbow{white} sticking out of a {silver}backpack{white}{normal}{bold}"
                    )

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}You on the {gold}beach{white} a {darkgrey}merchant{white} holding a {red}bubbling red{white} potion. The {darkgrey}merchant{white} also has a huge {purple}longbow{white} sticking out of a {silver}backpack{white}{normal}{bold}"
                    )

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {purple}Inv{white} / {darkgrey}Stats{white} / {red}Settings{white} / {silver}Save{white} | {teal}Merchant{white} / {platinum}Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", "merchant", 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "merchant":
                    scrollTxt(f"As you travel across the {gold}beach{white} a {blue}Merr{darkgrey}ow{white} ({red}fish{white} humanoid) holding a {purple}Jade Harpoon{white} jumps out of the {blue}lake{white}!")
                    enter()

                    combat(['merrow'])
                    scrollTxt(f"Finally you reach the {darkgrey}merchant{white}")
                    Shop(["potion of rage", "light shortsword", "cross-saber", "explosive bow"], [5, 40, 130, 220], f"{purple}Izle's{white} Intresting {darkgrey}Items{white}", sp = 20)


                if answer == "leave":
                    scrollTxt(f"{blue}Areas have not been added{white}")
                    scrollTxt(f"You may only travel {blue}south{white}")
                    enter()
                    location = "frosted cave"

            elif location == "monk cliffs":
                scrollTxt(f"~[{blue}Monk Cliffs{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap_frozite()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding the {blue}monk cliffs{white} is {darkgrey}white bridge{white} to the {teal}east{white}, and the vast {turquoise}ocean{white} surrounding everywhere {teal}else{white}{normal}{bold}")
                    scrollTxt("")

                if "monk cliffs" not in triggers:
                    triggers.append("monk cliffs")
                    scrollTxt(
                        f"{italic}Hidden high in the {darkgrey}mountians{white} lies a the {purple}sacred{white} temple of the {gold}monks{white}. Adorned with {red}red lanters{white} and {gold}gold tigers{white} this {darkgrey}temple{white} is kept {purple}safe{white} by over 100 {red}monks{white}{normal}{bold}"
                    )

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}Hidden high in the {darkgrey}mountians{white} lies a the {purple}sacred{white} temple of the {gold}monks{white}. Adorned with {red}red lanters{white} and {gold}gold tigers{white} this {darkgrey}temple{white} is kept {purple}safe{white} by over 100 {red}monks{white}{normal}{bold}"
                    )

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {purple}Inv{white} / {darkgrey}Stats{white} / {red}Settings{white} / {silver}Save{white} | {teal}Monks{white} / {platinum}Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", "monks", 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "monks":
                    scrollTxt(f"You walk up to one of the {gold}monks{white}")
                    scrollTxt(f"'{darkgrey}What have you come here to do?{white}' asks the {gold}Monk{white}")
                    scrollTxt(f"What do you {purple}say{white}?")
                    scrollTxt(f"[{blue}I have come to Learn{white}] [{red}I have come to Train{white}]")
                    answer = get_input(["learn", "train"])
                    print()

                    if answer == "learn":
                        scrollTxt(f"'{darkgrey}What will you learn?{white}', inquires the {gold}Monk{white}")
                        while True:
                            clear()
                            cost = {
                                "master archer": 1,
                                "quick draw": 2,
                                "cursed hand": 2,
                                "exp drain": 3,
                                "lucky dance": 3
                            }
                            print(f"You have {turquoise}{crystals}{white} Level Cystals")
                            print(f"- {purple}Master{white} Archer -  [ {teal}1 level crystal{white} ]")
                            print(f"- {turquoise}Quick{white} Draw    -  [ {teal}2 level crystal{white} ]")
                            print(f"- {darkgrey}Cursed{white} Hand   -  [ {teal}2 level crystal{white} ]")
                            print(f"- {blue}Exp{white} Drain     -  [ {teal}3 level crystal{white} ]")
                            print(f"- {gold}Lucky{white} Dance   -  [ {teal}3 level crystal{white} ]")
                            print(f"[{purple}l{white}] to leave")
                            print()
                            scrollTxt(f"What would {blue}you{white} like to learn?")
                            answer = get_input(["master archer", "quick draw", "cursed hand", "exp drain", "lucky dance", "leave"])
                            print()

                            if answer == "leave":
                                break
                                

                            else:
                                

                                if crystals >= cost[answer]:
                                    crystals -= cost[answer]
                                    if answer == "master archer":
                                        scrollTxt(f"You learned how to {gold}prep weapon{white} for a {red}reaction turn{white}!")
                                        special_moves.append("prep weapon")
                                    if answer == "quick draw":
                                        scrollTxt(f"You learned how to {gold}use item{white} for a {red}reaction turn{white}!")
                                        special_moves.append("use item")
                                    if answer == "cursed hand":
                                        scrollTxt(f"You learned how to {gold}inflict drain{white} for a {red}reaction turn{white}!")
                                        special_moves.append("cursed drain")
                                    if answer == "exp drain":
                                        scrollTxt(f"You learned how to {gold}drain exp{white} for a {red}reaction turn{white}!")
                                        special_moves.append("exp drain")
                                    if answer == "lucky dance":
                                        scrollTxt(f"You learned how to {gold}dance?{white} for a {red}reaction turn{white}!")
                                        special_moves.append("lucky dance")

                                    enter()
                                else:
                                    scrollTxt(f"You don\'t have {red}enough{white}")
                                    enter()
                    if answer == "train":
                        scrollTxt(f"How {red}difficult{white} would you like this to {blue}be{white}? [{gold}1{white}-{gold}4{white}]")
                        answer = get_input(["1", "2", "3", "4"], g=True)
                        diffi = answer
                        print()
                        scrollTxt(f"Let us {purple}fight{white}...")
                        enter()
                        combat(["monk lvl [" + answer + "]"])
                        scrollTxt(f"'{darkgrey}You have done well{white}' says the {gold}Monk{white}")
                        if diffi == "4" and "diff 4" not in triggers:
                            triggers.append("diff 4")
                            scrollTxt(f"'{darkgrey}You have beat me at my {red}highest level{darkgrey} take this {gold}Lightning Spear{white}' offers the {purple}Monk{white}")
                            scrollTxt(f"+ {gold}Lightning Spear{white} [Legend Weapon]")
                            inv.append("lightning spear")
                        enter()

                elif answer == "leave":
                    scrollTxt(f"You may only travel {blue}east{white}")
                    enter()
                    location = "white bridge"

            elif location == "core-sail arena":
                scrollTxt(f"~[{blue}Core-Sail Arena{white}]~")
                scrollTxt("")

                if settings['minimap']:
                    minimap_frozite()
                    print("")

                if settings["surroundings"]:
                    scrollTxt(
                        f"{italic}Surrounding the {blue}Core-Sail Arena{white} (CSA) is a {darkgrey}burrow{white} to the {teal}north{white} and the {turquoise}vast ocean{white} every where {teal}else{white}.{normal}{bold}")
                    scrollTxt("")

                if "coresail" not in triggers:
                    triggers.append("coresail")
                    scrollTxt(
                        f"{italic}The {red}infamous{white} {turquoise}Core{white}-{darkgrey}Sail{white} {red}Arena{white} is now open to the {gold}public{white}, although many few would try their {orange}luck{white} at this {purple}deadly sport{white}.{normal}{bold}"
                    )

                elif settings["print out des"] is True:
                    scrollTxt(
                        f"{italic}The {red}infamous{white} {turquoise}Core{white}-{darkgrey}Sail{white} {red}Arena{white} is now open to the {gold}public{white}, although many few would try their {orange}luck{white} at this {purple}deadly sport{white}.{normal}{bold}"
                    )

                scrollTxt(f"{turquoise}What would you like to do{white}?")
                scrollTxt(f"> {purple}Inv{white} / {darkgrey}Stats{white} / {red}Settings{white} / {silver}Save{white} | {teal}Arena{white} / {platinum}Leave{white}")
                answer = get_input(["inv", 'stats', 'settings', "save", "arena", 'leave'])
                scrollTxt("")

                usual_options(answer)

                if answer == "arena":
                    leaving = False
                    scrollTxt(f"You walk up the {turquoise}Core{white}-{darkgrey}Sail{white} {red}Arena{white}...")
                    time.sleep(2)

                    print()
                    scrollTxt(f"The {red}crowds{white} cheer as you {darkgrey}step{white} on the stage.")
                    scrollTxt(f"Your first {purple}opponent{white} is {lime}Muck{white} the {brown}Mutant{white}")
                    enter()

                    combat(["muck the mutant"])
                    scrollTxt(f"The {blue}crowds{white} go {gold}wild{white} as this {darkgrey}newcomer{white} at taken down {lime}Muck{white}")
                    print()
                    time.sleep(2)
                    scrollTxt(f"Your {red}prize{white} is {gold}200{white} GP")
                    gp += 200
                    print()
                    
                    while True:
                        clear()
                        scrollTxt(f"The {blue}crowds{white} go {gold}wild{white} as this {darkgrey}newcomer{white} at taken down {lime}Muck{white}")
                        print()
                        scrollTxt(f"Your {red}prize{white} is {gold}200{white} GP")
                        print()
                        scrollTxt(f"What would you like to {blue}do{white}?")
                        scrollTxt(f"{red}1.{white} Fight Next Opponent , {red}2.{white} Leave Arena , {red}3.{white} Inv")
                        answer = get_input(["1", "2", "3"])
                        print()

                        if answer == "1":
                            break
                        if answer == "2":
                            leaving = True
                            break
                        if answer == "3":
                            inventory()

                    if leaving is False:
                        scrollTxt(f"Your next {purple}opponent{white} is {darkgrey}Zanders{white} the {gold}Pirate{white}")
                        enter()

                        combat(["zanders the pirate"])
                        scrollTxt(f"The {blue}crowds{white} love you now. You are becomming a {gold}new hero{white} among the {orange}warriors{white} here.")
                        print()
                        time.sleep(2)
                        scrollTxt(f"Your {red}prize{white} is {gold}500{white} GP")
                        gp += 500
                        print()
                        
                        while True:
                            clear()
                            scrollTxt(f"The {blue}crowds{white} love you now. You are becomming a {gold}new hero{white} among the {orange}warriors{white} here.")
                            print()
                            scrollTxt(f"Your {red}prize{white} is {gold}500{white} GP")
                            print()
                            scrollTxt(f"What would you like to {blue}do{white}?")
                            scrollTxt(f"{red}1.{white} Fight Next Opponent , {red}2.{white} Leave Arena , {red}3.{white} Inv")
                            answer = get_input(["1", "2", "3"])
                            print()

                            if answer == "1":
                                break
                            if answer == "2":
                                leaving = True
                                break
                            if answer == "3":
                                inventory()

                    if leaving is False:
                        scrollTxt(f"Your next {purple}opponent{white} is The {copper}ROCK{white} {orange}GIANT{white}")
                        enter()

                        combat(["the rock giant"])
                        scrollTxt(f"The {blue}crowds{white} throw {red}flowers{white} at you. You have been a {orange}Legend{white} quick to {gold}rise{white} through the ranks.")
                        print()
                        time.sleep(2)
                        scrollTxt(f"Your {red}prize{white} is {gold}GROGS AXE OF SMASHING{white}")
                        inv.append("grogs axe of smashing")
                        print()
                        
                        while True:
                            clear()
                            scrollTxt(f"The {blue}crowds{white} throw {red}flowers{white} at you. You have been a {orange}Legend{white} quick to {gold}rise{white} through the ranks.")
                            print()
                            scrollTxt(f"Your {red}prize{white} is {gold}GROGS AXE OF SMASHING{white}")
                            print()
                            scrollTxt(f"What would you like to {blue}do{white}?")
                            scrollTxt(f"{red}1.{white} Fight Next Opponent , {red}2.{white} Leave Arena , {red}3.{white} Inv")
                            answer = get_input(["1", "2", "3"])
                            print()

                            if answer == "1":
                                break
                            if answer == "2":
                                leaving = True
                                break
                            if answer == "3":
                                inventory()

                    if leaving is False:
                        scrollTxt(f"Your next {purple}opponent{white} is The {blue}Blade{white} of the {darkgrey}North{white}")
                        enter()

                        combat(["blade of the north"])
                        scrollTxt(f"The {blue}crowds{white} chant your {red}name{white} and sing {darkgrey}songs{white} of your {orange}wins{white}.")
                        print()
                        time.sleep(2)
                        scrollTxt(f"Your {red}prize{white} is {teal}DUAL BLADES{white}")
                        inv.append("dual blade [offhand]")
                        inv.append("dual blade [weapon]")
                        print()
                        
                        while True:
                            clear()
                            scrollTxt(f"The {blue}crowds{white} chant your {red}name{white} and sing {darkgrey}songs{white} of your {orange}wins{white}.")
                            print()

                            scrollTxt(f"Your {red}prize{white} is {teal}DUAL BLADES{white}")

                            print()
                            scrollTxt(f"What would you like to {blue}do{white}?")
                            scrollTxt(f"{red}1.{white} Fight Next Opponent , {red}2.{white} Leave Arena , {red}3.{white} Inv")
                            answer = get_input(["1", "2", "3"])
                            print()

                            if answer == "1":
                                break
                            if answer == "2":
                                leaving = True
                                break
                            if answer == "3":
                                inventory()
                        
                    if leaving is False:
                            scrollTxt(f"Your next {purple}opponent{white} is The {purple}Other{white} {orange}Worlder{white}")
                            enter()

                            combat(["other worlder"])
                            scrollTxt(f"You have {blue}done{white} it, the {red}impossible{white}, {gold}winning{white} the {turquoise}Core{white}-{darkgrey}Sail{white} {red}Arena{white}")
                            print()
                            time.sleep(2)
                            scrollTxt(f"Your {red}prize{white} is {purple}WARPED{orange} SABER{white}")
                            inv.append("warped saber")
                            print()



                elif answer == "leave":
                    scrollTxt(f"You may only travel {blue}north{white}")
                    enter()
                    location = "goliaths burrow"
            
            if pre_loc != location:
                clear()
                travel_encounters = ["ambush", "ambush", "ambush", "ambush", "merchant", "merchant", "merchant", "merchant", "guardian", "chest"]
                encounter = random.choice(travel_encounters)

                if encounter == "ambush":
                    ambush_enemies = {
                        "group of giga spider": ["giga spider 1", "giga spider 2"],
                        "raging ogre": ["ogre"],
                        "cold assasin": ["assasin"],
                        "herd of wooly mammoths": ["wooly mammoth 1", "wooly mammoth 2", "wooly mammoth 3"]
                    }

                    enemy = random.choice(list(ambush_enemies.keys()))
                    scrollTxt(f"As you are {purple}traveling{white} your are {red}ambushed{white} by a {darkgrey}{enemy}{white}!")
                    enter()

                    combat(ambush_enemies[enemy])

                    scrollTxt(f"You are able to {teal}defeat{white} the {darkgrey}{enemy}{white} and you continue along the {brown}path{white}.")
                    enter()
                
                elif encounter == "guardian":
                    if lvl < 20: guardian = f"{platinum}platinum guardian{white}"
                    elif lvl > 29: guardian = f"{teal}echo {darkgrey}guardian{white}"
                    else: guardian = f"{turquoise}silence{silver} guardian{white}"

                    scrollTxt(f'You encounter a huge {guardian}!')
                    scrollTxt(f"It {red}charges{white} at you")
                    scrollTxt(f"You you {blue}RUN{white} or {orange}FIGHT{white} ?")
                    answer = get_input(["fight", "run"])
                    print()

                    if answer == "fight":
                        scrollTxt(f"You draw you {darkgrey}weapon{white} and {red}charge{white}!")
                        enter()

                        if lvl < 20: guardian = f"platinum guardian"
                        elif lvl > 29: guardian = f"echo guardian"
                        else: guardian = f"silence guardian"

                        combat([guardian], 1.5)
                        scrollTxt(f"You stagger along the {brown}path{white}, {yellow}exhausted{white}")
                        enter()

                    else:
                        scrollTxt(f"You {turquoise}narrowly{white} escape the {copper}guardain{white} but not before it {orange}strikes{white} you")
                        scrollTxt(f"- {red}5{white} Health")

                        health -= 5

                        if health < 1:
                            scrollTxt(f"This {red}kills{white} you 💀")
                            die()

                        enter()
                
                elif encounter == "merchant":
                    if random.randint(1, 3) == 1:
                        scrollTxt(f"As you are {teal}walking{white} you find a {red}joun{blue}gler{white} merchant holding some {darkgrey}WeIrD iTeMs{white}")
                        Shop(["stone on stick", "netherite shovel", "the stick to heal"], [30, 50, 100], f"{red}joun{blue}gler{white} merchant", sp = 20)
                    
                    elif random.randint(1, 2) == 1:
                        scrollTxt(f"As you are {teal}walking{white} you find a {turquoise}wand{blue}er{white} holding a glowing {lime}green{white} staff")
                        Shop(["teleportation token", "teleportation staff", "world token"], [20, 200, 200], f"The {blue}wan{turquoise}der{white}", sp = 20)
                    else:
                        scrollTxt(f"As you are {teal}walking{white} you find a {darkgrey}blacksmith{white} setting up {brown}shop{white}, hammer in hand")
                        Shop(["sharpening stone", "shrinker", "power gauntlets"], [100, 150, 180], f"The {darkgrey}Black{white}{silver}SMITH™️", sp = 20)

                elif encounter == "chest":
                    scrollTxt(f"A weird {brown}patch of dirt{white} catches your {copper}eye{white}.")
                    scrollTxt(f"Upon closer {teal}inspection{white} you find a {gold}chest{white}")
                    scrollTxt(f'Would you like to {green}try{white} to open it?')
                    answer = get_input(["yes", "no"])
                    print()

                    if answer == "yes":
                        if random.randint(1, 3) == 1:
                            scrollTxt(f"You try to open the {brown}chest{white} but it snaps it's {yellow}teeth{white} at you")
                            scrollTxt(f"It\'s a {brown}wooden {red}beast {darkgrey}mimic{white}!")
                            enter()
                            combat(["wooden beast mimic"])
                            scrollTxt(f"You are {orange}shaken up{white} but continue along the {brown}path{white}")
                            enter()
                        else:
                            if random.randint(1, 6) in range(1, strength):
                                scrollTxt(f"You are able to {green}open{white} the {gold}chest{white}")
                                scrollTxt(f"You find {gold}20{white} GP")
                                gp += 20
                                if random.randint(1, 3) == 1:
                                    scrollTxt(f"You also found a {red}hyper heal potion{white}")
                                    inv.append("hyper heal potion")
                                elif random.randint(1, 2) == 1:
                                    scrollTxt(f"You found a {green}tortoise potion{white}")
                                    inv.append("tortoise potion")
                                else:
                                    scrollTxt(f"You found a {teal}frosted potion{white}")
                                    inv.append('frosted potion')
                                print()
                                scrollTxt(f"You continue along the {brown}path{white} in a {green}good{white} mood")
                                enter()
                            else:
                                scrollTxt(f"You are {red}unable{white} to {blue}open{white} the {gold}chest{white}")
                                scrollTxt(f"You continue along the {brown}path{white} in a {red}bad{white} mood")
                                enter()
                    else:
                        scrollTxt(f"You decide it's better left {red}alone{white} and you continue along the {brown}path{white}")
                        enter()
else:
    print("[!] There has been an error in the code\nWill be fixed soon")
