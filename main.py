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

    known_spells = ["firebolt", "magic missile", "shield of the magi", "tornado burst"]
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
        "dirtify": 3
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
        "frosted cave": "frosted cave"
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

    multimove = ["the stranger", "orc warlord", "bandit", "yeti", "bandit lord", "jade guardian", "jade knight", "drowned monstrosity", "the dreadwood", "forest horror", "lich", "gelatinous cube", "the dark dragon", "death knight", "necromancer", "guardian of the jungle", "spike gang leader", "frost giant", 'assasin']
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
        "explosive bow": 20
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
                effects[effect_n] = [effects[effect_n][0] + effect_a , effects[effect_n][1]]
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

                    if item == "goblin horn":
                        wstats["hit"] += 1
                        scrollTxt(f"+ {green}1{white} accuracy")
                    if item == "orc tooth":
                        wstats["damage"] += 1
                        scrollTxt(f"+ {red}1{white} damage")
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
