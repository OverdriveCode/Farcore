import random 

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

items_all = {
        # Books
        'monster book': {
            'name': 'monster book',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A large {copper}leather bound{white} book detailing every {red}monster{white} and what they have.',
            'selling price': 5,
            'fuse': False
        },
        'map': {
            'name': 'map',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {paleyellow}scroll{white} containing the {darkgrey}map{white} of {purple}Far{blue}core{white}, divided into areas',
            'selling price': 3,
            'fuse': False
        },
        'reykrs book': {
            'name': 'reykrs book',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {copper}scroll{white} of advice written by {darkgrey}Reykr{white} 🐺.',
            'selling price': 3,
            'fuse': False
        },
        'andrew dengs book': {
            'name': 'andrew dengs book',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {copper}scroll{white} of advice written by {green}AndrewDeng3{white} 🐕.',
            'selling price': 3,
            'fuse': False
        },
        'nj wolfs book': {
            'name': 'nj wolfs book',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {copper}scroll{white} of advice written by {blue}njwolf444{white} 🤖.',
            'selling price': 3,
            'fuse': False
        },
        'shadow samurias book': {
            'name': 'shadow samurias book',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {copper}scroll{white} of advice written by {blue}shadow samuria{white} 👾.',
            'selling price': 3,
            'fuse': False
        },
        'guide': {
            'name': 'guide',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {copper}page{white} torn from a larger {brown}book{white} containing info on {purple}Far{blue}core{white}',
            'selling price': 3,
            'fuse': False
        },

        # Potions & Drinks
        'health potion': {
            'name': 'health potion',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A large triangular {silver}glass{white} bottle filled with {red}red liquid{white}, topped with a {gold}golden cap{white}',
            'selling price': 1,
            'fuse': False
        },
        'healing stone': {
            'name': 'healing stone',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A glowing {red}red{ironc}pink{white} stone. {orange}Warm{white} to the {copper}touch{white}. Said to cure any {darkgrey}illness{white}',
            'selling price': 10,
            'fuse': False
        },
        'hyper heal potion': {
            'name': 'hyper heal potion',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A small triangular {silver}glass{white} bottle filled with {ironc}pink liquid{white}, topped with a {gold}golden cap{white}',
            'selling price': 4,
            'fuse': False
        },
        'crystal potion': {
            'name': 'crystal potion',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A small vial of {blue}liquid{white} {turquoise}crystal{white}. {paleyellow}Energy{white} radiates from it. The {blue}liquid{white} inside {teal}swirls{white} forming a {purple}vortex{white}.',
            'selling price': 20,
            'fuse': False
        },
        'ember potion': {
            'name': 'ember potion',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {silver}glass{white} sphere bottle containing a {orange}orange burning liquid{white}. It has {grey}black molten rocks{white} crusted over it.',
            'selling price': 5,
            'fuse': False
        },
        'frosted potion': {
            'name': 'frosted potion',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {darkgrey}vial{white} containing a {turquoise}frosty{white} {teal}blue liquid{white}. Flowing from the potion is {blue}ice cold air{white}.',
            'selling price': 10,
            'fuse': False
        },
        'tortoise potion': {
            'name': 'tortoise potion',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {green}tortise shell{white} moldted unto a {silver}glass bottle{white}. Contains a {darkgrey}iron grey liquid{white}.',
            'selling price': 5,
            'fuse': False
        },
        'flaming dragon drink': {
            'name': 'flaming dragon drink',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {brown}wooden cup{white} filled with {orange}firey{grey} smoking{white} liquid. A specialty drink from {darkgrey}The Black Boar{white}',
            'selling price': 3,
            'fuse': False
        },
        'potion of rage': {
            'name': 'potion of rage',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A glass of {gold}bubbling{white} {red}red surup{white}. Made to bring out your {purple}inner{white} {darkgrey}beserker{white}!',
            'selling price': 3,
            'fuse': False
        },
        'lightning cider': {
            'name': 'lightning cider',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {yellow}bright yellow drink{white} {darkgrey}smoke{white} comes out of the liquid. A specialty drink from {darkgrey}Frozen Drinks{white}',
            'selling price': 3,
            'fuse': False
        },
        'spiders bite drink': {
            'name': 'spiders bite drink',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A thin {silver}glass cup{white} filled with {green}dark green{white} liquid. A specialty drink from {darkgrey}The Black Boar{white}',
            'selling price': 4,
            'fuse': False
        },
        'frost mead': {
            'name': 'frost mead',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {brown}wooden cup{white} painted {teal}light blue{white} filled with {turquoise}frosty iced{white} liquid. A specialty drink from {darkgrey}The Black Boar{white}',
            'selling price': 3,
            'fuse': False
        },
        'magi potion': {
            'name': 'magi potion',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A small square {silver}glass{white} bottle containing a {turquoise}shinning blue liquid{white}. Glows {purple}purple{white} every midnight.',
            'selling price': 2,
            'fuse': False
        },
        'potion of knowledge': {
            'name': 'potion of knowledge',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A crystal shaped {silver}bottle{white}. It has a {grey}misty grey liquid{white} inside. Its hard to make out the {blue}liquid{white}.',
            'selling price': 2,
            'fuse': False
        },
        'cove\'s concoction': {
            'name': 'cove\'s concoction',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"This {orange}concoction{white} was created by {darkgrey}Aove serderius{white} a {green}alchemist{white} known for {red}crazy{white} ideas.",
            'selling price': 5,
            'fuse': False
        },
        'awl\'s alchemy': {
            'name': 'awl\'s alchemy',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"This {orange}alchemy drink{white} was created by {darkgrey}Aove serderius{white} a {green}alchemist{white} known for {red}crazy{white} ideas.",
            'selling price': 5,
            'fuse': False
        },
        'luck potion': {
            'name': 'luck potion',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A {lime}leaf-shaped{white} glass bottle containing a {gold}golden liquid{white}. It is said to taste like {orange}fortune{white} and {yellow}happiness{white}.",
            'selling price': 10,
            'fuse': False
        },
        
        # Food
        'mushroom': {
            'name': 'mushroom',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A {brown}strangely{white} shaped {copper}mushroom{white}. For some reason you can't identify the {yellow}color{white}",
            'selling price': 0,
            'fuse': False
        },
        'hardy bread': {
            'name': 'hardy bread',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A {gold}delicious{white} smelling {copper}homemade {brown}loaf of bread{white}. Baked with {green}herbs{white} and {lime}vegtables{white}.",
            'selling price': 5,
            'fuse': False
        },
        'mammoth meat': {
            'name': 'mammoth meat',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A hardy chunk of {red}mammoth meat{white}. Little bits of {darkgrey}hair{white} and {brown}mammoth fur{white} line the meat.",
            'selling price': 20,
            'fuse': False
        },
        'mushroom soup': {
            'name': 'mushroom soup',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A unidetifiable {yellow}colored{white} soup. Has a {brown}leathery{white} texture? Served in a {darkgrey}steel bowl{white}?",
            'selling price': 2,
            'fuse': False
        },

        # Tokens
        'teleportation token': {
            'name': 'teleportation token',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"This {turquoise}futuristic{white} token allows {blue}someone{white} to transport himself/herself to another {copper}area{white}",
            'selling price': 5,
            'fuse': False
        },
        'dungeon token': {
            'name': 'dungeon token',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"This {copper}ancient{white} {darkgrey}stone{white} token allows for {red}adventure{white} to be tucked away in a {brown}pocket{white}...",
            'selling price': 10,
            'fuse': False
        },
        'world token': {
            'name': 'world token',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"This {orange}glowing{white} {purple}purple token{white}. Seems to {platinum}blurr{white} the surrounding {blue}area{white}.",
            'selling price': 20,
            'fuse': False
        },
        'teleportation staff': {
            'name': 'teleportation staff',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"This {turquoise}futuristic{white} {brown}staff{white} allows {blue}you{white} to teleport to any {copper}area{white} any amount of {green}times{white}.",
            'selling price': 50,
            'fuse': False
        },

        # Scrolls
        'aura of weakening scroll': {
            'name': 'aura of weakening scroll',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A {paleyellow}scroll{white} containing {blue}information{white} on how to preform the {darkgrey}aura of weakening{white} spell",
            'selling price': 7,
            'fuse': False
        },
        'dark chromatic orb scroll': {
            'name': 'dark chromatic orb scroll',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A {paleyellow}scroll{white} containing {blue}information{white} on how to preform the {darkgrey}dark{white} {purple}chromatic orb{white} spell",
            'selling price': 7,
            'fuse': False
        },
        'ice shards scroll': {
            'name': 'ice shards scroll',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A {paleyellow}scroll{white} containing {blue}information{white} on how to preform the {turquoise}ice shards{white} spell",
            'selling price': 7,
            'fuse': False
        },
        'dagger swarm scroll': {
            'name': 'dagger swarm scroll',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A {paleyellow}scroll{white} containing {blue}information{white} on how to preform the {grey}dagger swarm{white} spell",
            'selling price': 7,
            'fuse': False
        },
        'poison nova scroll': {
            'name': 'poison nova scroll',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A {paleyellow}scroll{white} containing {blue}information{white} on how to preform the {green}poison nova{white} spell",
            'selling price': 7,
            'fuse': False
        },
        'hyper heal scroll': {
            'name': 'hyper heal scroll',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A {paleyellow}scroll{white} containing {blue}information{white} on how to preform the {red}hyper heal{white} spell",
            'selling price': 7,
            'fuse': False
        },
        'shadow spear scroll': {
            'name': 'shadow spear scroll',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A {paleyellow}scroll{white} containing {blue}information{white} on how to preform the {darkgrey}shadow spear{white} spell",
            'selling price': 7,
            'fuse': False
        },
        'dark arrows scroll': {
            'name': 'dark arrows scroll',
            'consumable': True,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f"A {paleyellow}scroll{white} containing {blue}information{white} on how to preform the {darkgrey}dark arrows{white} spell",
            'selling price': 7,
            'fuse': False
        },

        # Weapons
        'rusty sword': {
            'name': 'rusty sword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'Made of some {yellow}unidentifiable{white} {darkgrey}metal{white}, heavily {copper}rusted{white} over.',
            'selling price': 1,
            'fuse': False
        },
        'wooden sword': {
            'name': 'wooden sword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A short and stout {brown}oaken{white} blade. Hand carved from a large {copper}tree branch{white}. Small cuts and knicks are everywhere',
            'selling price': 5,
            'fuse': False
        },
        'heart sword': {
            'name': 'heart sword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {ironc}pinkish{white}-{red}red{white} short sword. Gives off a {red}redish{white} glow.',
            'selling price': 30,
            'fuse': False
        },
        'rapier': {
            'name': 'rapier',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A thin long {silver}silvery{white} {grey}blade{white}. A beautiful {gold}golden{white} hilt lies on the end of the {grey}blade{white}.',
            'selling price': 15,
            'fuse': False
        },
        'frozen katana': {
            'name': 'frozen katana',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {blue}blue steel{white} katana with {gold}golden engravings{white}. {turquoise}Ice{white} covers the top half of the {darkgrey}blade{white}',
            'selling price': 40,
            'fuse': False
        },
        'scimitar': {
            'name': 'scimitar',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A curved {darkgrey}short sword{white} adorned with {yellow}yellow markings{white} and {red}small jewels{white}. Often used by {paleyellow}sand bandits{white}.',
            'selling price': 16,
            'fuse': False
        },
        'sun scimitar': {
            'name': 'sun scimitar',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A tall {darkgrey}curved{white} {gold}golden blade{white}. Said to {red}harness{white} the {orange}SUN\'s POWER{white}. This {darkgrey}weapon{white} is only claimed by the {red}death{white} of the owner.',
            'selling price': 30,
            'fuse': False
        },
        'kobold scimitar': {
            'name': 'kobold scimitar',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A curved {darkgrey}broad sword{white} dripping with {lime}poison{white}. Often used by {green}kobold{white}.',
            'selling price': 20,
            'fuse': False
        },
        'master scimitar': {
            'name': 'master scimitar',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A curved {darkgrey}broad sword{white} adorned with {gold}gold markings{white} and {red}large rubies{white}. Often used by {paleyellow}bandit lords{white}.',
            'selling price': 20,
            'fuse': False
        },
        'lightning spear': {
            'name': 'lightning spear',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A tall {darkgrey}dark spear{white} with a {yellow}brilliant{white} {gold}lightning bolt{white} shaped {darkgrey}spear head{white}. Summons {yellow}lightning{white} to {red}strike{white}.',
            'selling price': 50,
            'fuse': False
        },
        'note-it-downs saber': {
            'name': 'note-it-downs saber',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A thin {darkgrey}longsword{white} use by {blue}NoteitDOWN{white}. [{turquoise}CUSTOM WEAPON{white}]',
            'selling price': 15,
            'fuse': False
        },
        'cross-saber': {
            'name': 'cross-saber',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A thin {red}sharp{white} {darkgrey}longsword{white}. A interesting {gold}gold cross hilt{white} gives you good {blue}defense{white}',
            'selling price': 30,
            'fuse': False
        },
        'nathans jade claymore': {
            'name': 'nathans jade claymore',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A huge {teal}jade{white} {darkgrey}claymore{white} use by {orange}Nathan Pang{white}. [{turquoise}CUSTOM WEAPON{white}]',
            'selling price': 15,
            'fuse': False
        },
        'bronze sword': {
            'name': 'bronze sword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A dusty {copper}bronze{white} {silver}blade{white}. Used by many {brown}gladiators{white}',
            'selling price': 15,
            'fuse': False
        },
        'iron sword': {
            'name': 'iron sword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A heavy {grey}blackish grey{white} {silver}sword{white}. Favored by the {darkgrey}dark knights{white} of {brown}old{white}',
            'selling price': 25,
            'fuse': False
        },
        'warhog blade': {
            'name': 'warhog blade',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A stout {copper}warthog tooth{white} sword. Wrapped in {brown}leather{white} [{turquoise}CUSTOM WEAPON{white}]',
            'selling price': 20,
            'fuse': False
        },
        'steel sword': {
            'name': 'steel sword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A gleeming {grey}silver{white} {silver}blade{white}. A true symbol of a {darkgrey}knight{white}',
            'selling price': 40,
            'fuse': False
        },
        'steel broadsword': {
            'name': 'steel broadsword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A tall {darkgrey}blade{white} inbetween a {silver}sword{white} and a {teal}longsword{white}. Shines {gold}bright{white} ready to take on {red}enemies{white}',
            'selling price': 40,
            'fuse': False
        },
        'jungle blade': {
            'name': 'jungle blade',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A sword made out of {copper}renforced{white} {purple}enchanted{white} {brown}wood{white}. Pulsing {red}vines{white} cover the blade.',
            'selling price': 50,
            'fuse': False
        },
        'sword of looting': {
            'name': 'sword of looting',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A completely {gold}golden sword{white} tall and {purple}strong{white}. Its {gold}shiny{white} appearence makes {copper}enemies{white} distracted.',
            'selling price': 50,
            'fuse': False
        },
        'double bladed sword': {
            'name': 'double bladed sword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {blue}dark blue{white} leather hilt with {grey}steel blades{white} coming out from both {red}ends{white}',
            'selling price': 50,
            'fuse': False
        },
        'flameblade': {
            'name': 'flameblade',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {red}flamming silver{white} blade with a {darkgrey}black hilt{white}. {orange}Glowing orange{white} runes are echted onto the {darkgrey}blade{white}.',
            'selling price': 50,
            'fuse': False
        },
        'flamebane': {
            'name': 'flameblane',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {red}flamming silver{white} axe with a {darkgrey}black handle{white}. {orange}Glowing orange{white} runes are echted onto the {darkgrey}axe{white}.',
            'selling price': 50,
            'fuse': False
        },
        'vorpal sword': {
            'name': 'vorpal sword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {red}blood red{white} blade with {darkgrey}darkgrey markings{white} and a {darkgrey}dark hilt{white}. Strikes {yellow}fear{white} into the heart of the {gold}bravest{white} heroes.',
            'selling price': 100,
            'fuse': False
        },
        'light shortsword': {
            'name': 'light shortsword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A very {darkgrey}small{white} dagger-like {gold}sword{white}. Often used in the {red}left hand{white} as an {brown}second{white} weapon.',
            'selling price': 20,
            'fuse': False
        },
        'magic sword': {
            'name': 'magic sword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'The {blue}glowing blue{white} {darkgrey}blade{white} has been by {orange}heros{white} for ages. It has many {darkgrey}names{white}; {turquoise}The Master Sword{white}, {blue}Dimond Sword{white}, {purple}Lightsaber{white}.',
            'selling price': 50,
            'fuse': False
        },
        'trident': {
            'name': 'trident',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A long {gold}golden trident{white}. {silver}Sharp{white} and {green}agile{white}.',
            'selling price': 40,
            'fuse': False
        },
        'dual blade [offhand]': {
            'name': 'dual blade [offhand]',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A short thin {teal}teal blade{white} perfectly shaped for the {green}left hand{white}.',
            'selling price': 20,
            'fuse': False
        },
        'dual blade [weapon]': {
            'name': 'dual blade [weapon]',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A short thin {teal}teal blade{white} perfectly shaped for the {orange}right hand{white}.',
            'selling price': 20,
            'fuse': False
        },
        'jade scythe': {
            'name': 'jade scythe',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A tall {brown}wooden{white} staff with a {red}deadly{white} {turquoise}jade{white} {darkgrey}scythe head{white}. The {grey}material{white} seems to {purple}drain{white} the {red}life{white} out of things.',
            'selling price': 35,
            'fuse': False
        },
        'dagger': {
            'name': 'dagger',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A thin {silver}silver{white} blade atop a {copper}sturdy{white} {brown}leather{white} hilt.',
            'selling price': 5,
            'fuse': False
        },
        'netherite shovel': {
            'name': 'netherite shovel',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A shovel made out of a {darkgrey}dark black metal{white} with a {brown}wooden handle{white} with {darkgrey}netherite bracing{white}',
            'selling price': 20,
            'fuse': False
        },
        'stone on stick': {
            'name': 'stone on stick',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {darkgrey}stone{white} on a {brown}stick{white}.',
            'selling price': 1,
            'fuse': False
        },
        'grim dagger': {
            'name': 'grim dagger',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A large {darkgrey}darkgrey{white} blade with {red}dark red markings{white}. Makes you feel {paleyellow}uneasy{white}, used by {orange}Hollow Soliders{white}.',
            'selling price': 20,
            'fuse': False
        },
        'warped saber': {
            'name': 'warped saber',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {orange}glowing{white} {purple}purple{ironc}pink{white} saber. Rays of {yellow}energy{white} fly out of the {darkgrey}blade{white}.',
            'selling price': 50,
            'fuse': False
        },
        'feather dagger': {
            'name': 'feather dagger',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A triangle shaped {darkgrey}blade{white} with a small {gold}golden hilt{white}. Small birds are {red}engraven{white} on the dagger.',
            'selling price': 20,
            'fuse': False
        },
        'dagger of stealing': {
            'name': 'dagger of stealing',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {darkgrey}large knife{white} like one of those used for {red}combat{white}. This one {yellow}shimmers{white} {gold}gold{white} from time to time.',
            'selling price': 30,
            'fuse': False
        },
        'spear': {
            'name': 'spear',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A tall {brown}wooden shaft{white} with a {orange}sharp{white} {darkgrey}iron spear head{white} attached to the top. Good for {orange}attacking{white} many {copper}enemies{white}',
            'selling price': 7,
            'fuse': False
        },
        'wooden club': {
            'name': 'wooden club',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A large crude {brown}wooden{white} stick. Used by many {green}goblins{white}',
            'selling price': 1,
            'fuse': False
        },
        'ice spikes club': {
            'name': 'ice spikes club',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {brown}thick wooden stick{white}, covered in {teal}icicles{white} and {silver}snow{white}',
            'selling price': 5,
            'fuse': False
        },
        'claymore': {
            'name': 'claymore',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A large {silver}iron{white} {darkgrey}claymore{white}. This blade is {brown}6{white}ft long!',
            'selling price': 10,
            'fuse': False
        },
        'dragon scale claymore': {
            'name': 'dragon scale claymore',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A gargauntuan {red}dragon scale{white} {darkgrey}claymore{white}. The {orange}redish orange{white} {silver}scales{white} spit out a {paleyellow}white-hot flame{white}.',
            'selling price': 50,
            'fuse': False
        },
        'frosted longsword': {
            'name': 'frosted longsword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {turquoise}icy blue{white} {darkgrey}longsword{white}. The tip of the {grey}blade{white} is competely covered in {teal}ice{white}. The handle is {green}extremely{white} {blue}cold{white}.',
            'selling price': 35,
            'fuse': False
        },
        'dark claymore': {
            'name': 'dark claymore',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A huge {darkgrey}iron{white} {silver}claymore{white}, it is {orange}slanted{white} at the end. The top part is completely {darkgrey}black{white} and made of {darkgrey}DARK STEEL{white}.',
            'selling price': 30,
            'fuse': False
        },
        'curved claymore': {
            'name': 'curved claymore',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {teal}teal{white} large curved {darkgrey}claymore{white}. It is extremely {red}sharp{white} made from {purple}renforced steel{white}.',
            'selling price': 30,
            'fuse': False
        },
        'great axe': {
            'name': 'great axe',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A huge {darkgrey}metal axe{white} with {gold}gold{white} highlights. Made for extreme {orange}durability{white} and {paleyellow}bone-crushing{white} power!',
            'selling price': 20,
            'fuse': False
        },
        'bugbear axe': {
            'name': 'bugbear axe',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {darkgrey}huge iron axe{white} used by {brown}Bugbears{white}. Covered in {copper}animal hide{white} and {brown}leather{white}.',
            'selling price': 10,
            'fuse': False
        },
        'great sword': {
            'name': 'great sword',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A large {darkgrey}metal sword{white} with {gold}gold{white} highlights. Made for extreme {orange}durability{white} and {red}high{white} power!',
            'selling price': 20,
            'fuse': False
        },
        'axe': {
            'name': 'axe',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A short {grey}iron{white} axe. Used to cut down {brown}trees{white}.',
            'selling price': 6,
            'fuse': False
        },
        'jade harpoon': {
            'name': 'jade harpoon',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A deadly {purple}purple{white} {darkgrey}weapon{white} of the sea. Used by {blue}Merr{purple}ows{white} this item is considered {red}CURSED{white}.',
            'selling price': 40,
            'fuse': False
        },
        'grogs axe of smashing': {
            'name': 'grogs axe of smashing',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A double sided {darkgrey}metal axe{white}, made by Gorg the {orange}barbarian{white}. Great for dealing lots of {red}damage{white}.',
            'selling price': 20,
            'fuse': False
        },
        'cursed axe': {
            'name': 'cursed axe',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'This {darkgrey}battle axe{white} is surrounded by a {purple}cloud of evil{white}. It {darkgrey}drains{white} both the {blue}user{white} and the {orange}victim{white} of life.',
            'selling price': 40,
            'fuse': False
        },
        'cursed dagger': {
            'name': 'cursed dagger',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'This {darkgrey}dagger{white} was unlucky enough to be {purple}cursed{white} by the {red}dreadwood{white}. It radiates an {paleyellow}unholy light{white}...',
            'selling price': 40,
            'fuse': False
        },
        'cursed bow': {
            'name': 'cursed bow',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'This {darkgrey}bow{white} was corrupted by its {orange}master{white} leading it to become much more {red}powerful{white} but it seems to {purple}drain{white} the user.',
            'selling price': 40,
            'fuse': False
        },
        'explosive bow': {
            'name': 'explosive bow',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {darkgrey}steel longbow{white} with {red}TNT{white} 💣 tipped {silver}arrows{white}. Highly {orange}dangerous{white} to both you and your {darkgrey}enemies{white}.',
            'selling price': 80,
            'fuse': False
        },
        'combo gloves': {
            'name': 'combo gloves',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A pair of {red}red{white} {darkgrey}gloves{white}. They have great {yellow}speed{white} and can take on many {copper}enemies{white} at once.',
            'selling price': 20,
            'fuse': False
        },
        'power gauntlets': {
            'name': 'power gauntlets',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A pair of {orange}orange gauntlets{white}, they {red}amplify{white} you actual {orange}strength{white} and {darkgrey}dexterity{white}. Made of a {gold}rare metal{white}.',
            'selling price': 40,
            'fuse': False
        },
        'tazer': {
            'name': 'tazer',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A small {darkgrey}black box{white} with a {red}red button{white}, when your press the {red}button{white} the device spits out {blue}blue electricity{white}.',
            'selling price': 10,
            'fuse': False
        },
        'the stick to rule them all': {
            'name': 'the stick to rule them all',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {brown}stick{white}.',
            'selling price': 1,
            'fuse': False
        },
        'crystal dagger': {
            'name': 'crystal dagger',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A small {darkgrey}dagger{white} make out of {turquoise}pure crystal{white}. Holds {red}immense{white} {gold}power{white}',
            'selling price': 10,
            'fuse': False
        },
        
        # Bows
        'short bow': {
            'name': 'short bow',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A small {brown}wooden{white} bow. Curved {copper}oak{white} tips with a {ironc}leather{white} handle.',
            'selling price': 10,
            'fuse': False
        },
        'longbow': {
            'name': 'longbow',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A tall {brown}wooden{white} bow. Curved {darkgrey}iron{white} tips with a {brown}renforced leather{white} handle.',
            'selling price': 15,
            'fuse': False
        },
        'crossbow': {
            'name': 'crossbow',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A small {silver}steel{white} & {brown}wood{white} bow. Straight {silver}steel{white} tips. Full of {darkgrey}chains{white} and {grey}latches{white}.',
            'selling price': 30,
            'fuse': False
        },
        'cursed bow': {
            'name': 'cursed bow',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'This {darkgrey}bow{white} was corrupted by its {orange}master{white} leading it to become much more {red}powerful{white} but it seems to {purple}drain{white} the user.',
            'selling price': 40,
            'fuse': False
        },
        'explosive bow': {
            'name': 'explosive bow',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': False,
            'description':
            f'A {darkgrey}steel longbow{white} with {red}TNT{white} 💣 tipped {silver}arrows{white}. Highly {orange}dangerous{white} to both you and your {darkgrey}enemies{white}.',
            'selling price': 80,
            'fuse': False
        },
        
        # Shields
        'goblin shield': {
            'name': 'goblin shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A small triangular {brown}wood{white} shield. Has small {grey}metal spikes{white} stickings out from the edges. Smells of {green}goblin{white}.',
            'selling price': 1,
            'fuse': False
        },
        'wooden shield': {
            'name': 'wooden shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A worn down circular {brown}wooden{white} shield. With {ironc}leather straps{white} on the back and a {gold}gold tip{white} in the front',
            'selling price': 3,
            'fuse': False
        },
        'bronze shield': {
            'name': 'bronze shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A shiny triangular {copper}bronze{white} shield. With {grey}dark leather straps{white} on the back and a {gold}gold tip{white} in the front',
            'selling price': 15,
            'fuse': False
        },
        'iron shield': {
            'name': 'iron shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A large square {grey}dark{white} shield. Bound by {darkgrey}black leather{white}. Holds a sharp {grey}metal{white} tip on the front.',
            'selling price': 25,
            'fuse': False
        },
        'steel shield': {
            'name': 'steel shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A gleeming oval {silver}steel{white} shield. Worn with {gold}pride{white} by the highest {grey}knights{white}',
            'selling price': 40,
            'fuse': False
        },
        'platinum shield': {
            'name': 'steel shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A heater shaped {darkgrey}shield{white} made out of a {gold}shiny{white} {silver}white{white} metal. This {darkgrey}metal{white} called {gold}pla{silver}tnium{white} has recently been {blue}discovered{white}',
            'selling price': 50,
            'fuse': False
        },
        'guardian shield': {
            'name': 'guardian shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A {darkgrey}shield{white} that towers over all other {copper}shields{white}. Made of pure {grey}heavy iron{white} gives it unparalled {orange}defense{white}.',
            'selling price': 45,
            'fuse': False
        },
        'kinetic shield [0]': {
            'name': 'kinetic shield [0]',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A {blue}large{white} round shield, covered in a {darkgrey}dark material{white} that feels like {orange}rubber{white}, when it takes a hit it {purple}shimmers purple{white}.\nAbsorbed {purple}0{white} energy',
            'selling price': 70,
            'fuse': False
        },
        'shield of blocking': {
            'name': 'shield of blocking',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A glowing {orange}orange magic{white} {darkgrey}shield{white}. Said to be the most {red}powerful{white} shield but the {gold}creator{white} died when the shield was only {yellow}75%{white} done.',
            'selling price': 70,
            'fuse': False
        },
        'plate shield': {
            'name': 'plate shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A large {darkgrey}metal shield{white} with {gold}gold{white} highlights. Made for {orange}extreme durability{white} and great {blue}defense{white}',
            'selling price': 20,
            'fuse': False
        },
        'grim shield': {
            'name': 'grim shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A {darkgrey}darkgrey{white} shield with menacing {red}red markings{white}. Used by the {orange}Hollow Solider{white}.',
            'selling price': 40,
            'fuse': False
        },
        'scale shield': {
            'name': 'scale shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A {yellow}light-weight{white} shield that moves {silver}swiftly{white} to {orange}defend{white} oncomming {red}attacks{white}.',
            'selling price': 30,
            'fuse': False
        },
        'rune shield': {
            'name': 'rune shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A small {blue}diamond{white} shaped {darkgrey}shield{white}. Engraved in the shield a {orange}glowing orange{white} {copper}runes{white}.',
            'selling price': 55,
            'fuse': False
        },
        'phoenix shield': {
            'name': 'phoenix shield',
            'consumable': False,
            'weapon': False,
            'shield': True,
            'staff': False,
            'description':
            f'A {orange}blazing{white} {gold}crested{white} shield. A large {red}red phoenix{white} is painted in the center.',
            'selling price': 60,
            'fuse': False
        },
        
        # Staffs
        'citrine staff': {
            'name': 'citrine staff',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': True,
            'description':
            f'A tall knobbly {brown}staff{white}. At the tip is a {yellow}yellowish{white} {lime}lime{white} crystal. {paleyellow}Crackels{white} on {blue}rainly{white} days.',
            'selling price': 90,
            'fuse': False
        },
        'earth staff': {
            'name': 'earth staff',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': True,
            'description':
            f'A thick short {brown}wooden staff{white}. A {lime}glowing green{white} crystal tops the {brown}staff{white}. {red}Birds{white} perch on the {brown}staff{white} from time to time.',
            'selling price': 100,
            'fuse': False
        },
        'gold staff': {
            'name': 'gold staff',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': True,
            'description':
            f'A strong {gold}golden staff{white} with a {darkgrey}hammer-like{white} top. A ring of {yellow}pure energy{white} swarms around the {darkgrey}staff{white}.',
            'selling price': 200,
            'fuse': False
        },
        'dread staff': {
            'name': 'dread staff',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': True,
            'description':
            f'A {darkgrey}cruel black staff{white} with a horrible {silver}skull{white} atop. {darkgrey}Bones{white} from a ribcage line the {silver}staff{white}. Gives off a {lime}light green glow{white}.',
            'selling price': 200,
            'fuse': False
        },
        'frost staff': {
            'name': 'frost staff',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': True,
            'description':
            f'A tall {teal}darkblue staff{white} with tons of {turquoise}icicles{white} jutting out from the top. Very {blue}cold{white} to the touch. Can {turquoise}freeze{white} water.',
            'selling price': 130,
            'fuse': False
        },
        'ruby staff': {
            'name': 'sapphire staff',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': True,
            'description':
            f'A thick sout {brown}staff{white}. At the tip is a {orange}fiery{white} {brown}red{white} crystal. {brown}Flares{white} randomly every {yellow}hour{white}.',
            'selling price': 50,
            'fuse': False
        },
        'sapphire staff': {
            'name': 'sapphire staff',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': True,
            'description':
            f'A smooth {darkgrey}black{white} {brown}staff{white}. At the tip is a {blue}swirling{white} {turquoise}teal{white} crystal. Grows {paleyellow}brighter{white} the closer it is to {teal}water{white}.',
            'selling price': 30,
            'fuse': False
        },
        'quartz staff': {
            'name': 'quartz staff',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': True,
            'description':
            f'A thin white {brown}staff{white}. At the tip is a {silver}clear{white} crystal. Whisles like wind when waved around',
            'selling price': 20,
            'fuse': False
        },
        'cotopia staff': {
            'name': 'coptopia staff',
            'consumable': False,
            'weapon': True,
            'shield': False,
            'staff': True,
            'description':
            f'A tall thin {green}green{white} {brown}staff{white}. Used by the {purple}wizard{white} {darkgrey}Cotopia{white}. [{turquoise}CUSTOM STAFF{white}]',
            'selling price': 25,
            'fuse': False
        },
        
        # Gear
        'torch': {
            'name': 'torch',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A piece {darkgrey}coal{white} tied to a long {brown}wooden stick{white} with {copper}rope{white}.',
            'selling price': 2,
            'fuse': False
        },
        'metal scrap': {
            'name': 'metal scrap',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A small piece of {darkgrey}metal{white}.',
            'selling price': 1,
            'fuse': False
        },
        'water bottle': {
            'name': 'water bottle',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {silver}clear{white} bottle of {blue}water{white}. Very {platinum}simple{white}',
            'selling price': 2,
            'fuse': False
        },
        'mirror': {
            'name': 'mirror',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A small hand-held {silver}mirror{white}, lined with {gold}gold{white} on the sides.',
            'selling price': 4,
            'fuse': False
        },
        'rope': {
            'name': 'rope',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'{green}50{white}ft of renforced {brown}leather{white} rope.',
            'selling price': 4,
            'fuse': False
        },
        'climbing gear': {
            'name': 'climbing gear',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {copper}leather{white} suit with {brown}rope{white} and {darkgrey}hooks{white}.',
            'selling price': 8,
            'fuse': False
        },
        'totem of undying': {
            'name': 'totem of undying',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {gold}golden statue{white} {lime}green emrald{white} eyes line the statue.',
            'selling price': 30,
            'fuse': False
        },

        # Trophies
        'copper trophy': {
            'name': 'copper trophy',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {turquoise}rare{white} item that is {gold}rewarded{white} for {brown}killing{white} many {teal}enemies{white}. Made of {brown}copper{white}. [{green}2{white}%] drop',
            'selling price': 25,
            'fuse': False
        },
        'bronze trophy': {
            'name': 'bronze trophy',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {turquoise}very rare{white} item that is {gold}rewarded{white} for {brown}killing{white} many {teal}enemies{white}. Made of {copper}bronze{white}. [{green}1{white}%] drop',
            'selling price': 50,
            'fuse': False
        },
        'silver trophy': {
            'name': 'silver trophy',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {turquoise}extremely rare{white} item that is {gold}rewarded{white} for {brown}killing{white} many {teal}enemies{white}. Made of {silver}silver{white}. [{green}0.5{white}%] drop',
            'selling price': 100,
            'fuse': False
        },
        'gold trophy': {
            'name': 'gold trophy',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {darkgrey}[{turquoise}h{darkgrey}]{turquoise}yper rare{white} item that is {gold}rewarded{white} for {brown}killing{white} many {teal}enemies{white}. Made of {gold}gold{white}. [{green}0.2{white}%] drop',
            'selling price': 250,
            'fuse': False
        },
        "overdrive's trophy": {
            'name': 'gold trophy',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {darkgrey}[{turquoise}g{darkgrey}]{turquoise}host rare{white} item that is {gold}rewarded{white} for {brown}killing{white} many {teal}enemies{white}. Made of {darkgrey}meteorite{white} and {orange}dragon scales{white}. [{green}0.1{white}%] drop',
            'selling price': 500,
            'fuse': False
        },
    
        # Monster parts
        'troll heart': {
            'name': 'troll heart',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {turquoise}glowing{white} {blue}blueish{white}{green}green{white} beating {red}heart{white}...',
            'selling price': 4,
            'fuse': True
        },
        'goblin horn': {
            'name': 'goblin horn',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {copper}coffee brown{white} {silver}horn{white} that is {paleyellow}hollow{white} inside.',
            'selling price': 2,
            'fuse': True
        },
        'orc tooth': {
            'name': 'orc tooth',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A large {darkgrey}grey tooth{white}. {red}Razor{white} sharp and {orange}serrated{white}.',
            'selling price': 3,
            'fuse': True
        },
        'ogre nail': {
            'name': 'ogre nail',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A huge {yellow}yellowish{white} {darkgrey}silver{white} nail. Large enought to be used as a {blue}Shield{white}.',
            'selling price': 5,
            'fuse': True
        },
        'yeti eye': {
            'name': 'yeti eye',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {turquoise}glowing{white} {teal}icy blue{white} {darkgrey}eye{white}. Gives you {blue}frostbite{white} if you hold it to long.',
            'selling price': 8,
            'fuse': True
        },
        'sharpening stone': {
            'name': 'sharpening stone',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A firm block of {darkgrey}iron{white} used to {gold}sharpen{white} tools.',
            'selling price': 10,
            'fuse': True
        },
        'shrinker': {
            'name': 'shrinker',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A stranger {lime}glowing orb{white} that seems to {orange}wa{purple}rp{white} reality...',
            'selling price': 30,
            'fuse': True
        },
        'lightning stone': {
            'name': 'lightning stone',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {yellow}yellow stone{white} that {paleyellow}crackles{white} and spits out small {yellow}shock{white} {darkgrey}waves{white}.',
            'selling price': 9,
            'fuse': True
        },
        'jade': {
            'name': 'jade',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A small piece of {turquoise}jade{white} has {purple}strange{white} {red}life-altertering{white} properties.',
            'selling price': 10,
            'fuse': True
        },
        'dragon scale': {
            'name': 'dragon scale',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A shiny {orange}burning{white} {darkgrey}scale{white}. Dropped from many types of {red}dragons{white}.',
            'selling price': 10,
            'fuse': True
        },
        'skull': {
            'name': 'skull',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A horrible looking {silver}skull{white}, rattles from {red}time{white} to {red}time{white}',
            'selling price': 5,
            'fuse': True
        },
        'master ruby': {
            'name': 'master ruby',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A huge {red}shiny ruby{white} turns {ironc}pink{white} when exposed to extreme {orange}heat{white}.',
            'selling price': 20,
            'fuse': True
        },
        'mutant jaguar tooth': {
            'name': 'mutant jaguar tooth',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A {brown}rotting{white} tooth from a {orange}huge jaguar{white}, makes you feel {red}STRONG{white}.',
            'selling price': 10,
            'fuse': True
        },
        'acid goo': {
            'name': 'mutant goo',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A mass of {lime}radoactive goo{white} that {orange}burns{white} you if you {darkgrey}touch{white} it.',
            'selling price': 5,
            'fuse': True
        },
        'rock core': {
            'name': 'rock core',
            'consumable': False,
            'weapon': False,
            'shield': False,
            'staff': False,
            'description':
            f'A lump of {darkgrey}hardened{white} {orange}magma{white} rock. Gives off a lot of {red}heat{white} and is very {purple}heavy{white}',
            'selling price': 10,
            'fuse': True
        },
    }
    
weapons_all = {
        # Swords
        'rusty sword': {'hit': -1, 'damage': 2, 'special': False, "special text": "", "speed": 10, "sweep": 1.2,
                            "durability": 50, "reload": 0, "two handed": False, "req": {}},
        'wooden sword': {'hit': 2, 'damage': 5, 'special': False, "special text": "", "speed": 5, "sweep": 0.7,
                            "durability": 15, "reload": 0, "two handed": False, "req": {}},
        'bronze sword': {'hit': 2, 'damage': 7, 'special': False, "special text": "", "speed": 10, "sweep": 0.8,
                            "durability": 20, "reload": 0, "two handed": False, "req": {}},
        'iron sword': {'hit': -1, 'damage': 10, 'special': "bleed",
                        "special text": f"A large {red}gash{white} appears", "speed": 15, "sweep": 0.9,
                        "durability": 25, "reload": 0, "two handed": False, "req": {"str": 4}, 'crit': 1},
        'steel sword': {'hit': 3, 'damage': 10, 'special': False, "special text": "", "speed": 6, "sweep": 1,
                        "durability": 30, "reload": 0, "two handed": False, "req": {}, "crit": 1},
        'vorpal sword': {'hit': 5, 'damage': 12, 'special': False, "special text": "", "speed": 6, "sweep": 1.5,
                        "durability": 30, "reload": 0, "two handed": False, "req": {},},
        'dual blade [weapon]': {'hit': 5, 'damage': 9, 'special': False, "special text": "", "speed": 6, "sweep": 1,
                        "durability": 30, "reload": 0, "two handed": False, "req": {}, "crit": 0},
        'dual blade [offhand]': {'hit': 5, 'damage': 9, 'special': False, "special text": "", "speed": 6, "sweep": 1,
                        "durability": 30, "reload": 0, "two handed": False, "req": {}, "crit": 0},
        'steel broadsword': {'hit': 1, 'damage': 15, 'special': False, "special text": "", "speed": 10, "sweep": 1.5,
                        "durability": 30, "reload": 0, "two handed": False, "req": {}, "crit": 2},
        'frozen katana': {'hit': 2, 'damage': 11, 'special': "hyper freeze", "special text": f"{turquoise}Ice{white} instantly covers the {red}enemies{white} body. Keeping it in a {teal}frosted{white} prison", "speed": 7, "sweep": 0.9,
                        "durability": 20, "reload": 0, "two handed": False, "req": {}, "crit": 3},
        'sword of looting': {'hit': 1, 'damage': 10, 'special': False, "special text": "", "speed": 10, "sweep": 1,
                        "durability": 20, "reload": 0, "two handed": False, "req": {}, "crit": 2},
        'heart sword': {'hit': 2, 'damage': 7, 'special': False, "special text": "", "speed": 10, "sweep": 1,
                        "durability": 20, "reload": 0, "two handed": False, "req": {}, "crit": 0},
        'light shortsword': {'hit': 2, 'damage': 8, 'special': False, "special text": "", "speed": 9, "sweep": 0.9,
                        "durability": 20, "reload": 0, "two handed": False, "req": {}, "crit": 1},
        'jungle blade': {'hit': 5, 'damage': 8, 'special': "poison", "special text": f"Ugly {green}green{white} blood {lime}oozes{white} out of their {red}wound{white}", "speed": 6, "sweep": 1,
                        "durability": 20, "reload": 0, "two handed": False, "req": {}, "crit": 1}, 
        'double bladed sword': {'hit': -1, 'damage': 10, 'special': False, "special text": "", "speed": 6000000000, "sweep": 1,
                        "durability": 30, "reload": 0, "two handed": True, "req": {}, "crit": 1}, 
        'flameblade': {'hit': 3, 'damage': 12, 'special': "burn", "special text": f"Your {red}target{white} bursts into {orange}firey flames{white}", "speed": 6, "sweep": 1,
                        "durability": 20, "reload": 0, "two handed": False, "req": {}, "crit": 2},
        'great sword': {'hit': -1, 'damage': 12, 'special': False, "special text": "", "speed": 8, "sweep": 1.3,
                        "durability": 50, "reload": 0, "two handed": True, "req": {"str": 4}, "crit": 2},
        'magic sword': {'hit': 5, 'damage': 12, 'special': False, "special text": "", "speed": 6, "sweep": 1.2,
                        "durability": 30, "reload": 0, "two handed": False, "req": {}, "crit": 1}, 
        'frosted longsword': {'hit': -1, 'damage': 12, 'special': "freeze", "special text": f"The {red}enemies{white} body slightly {turquoise}frosts{white} over. Leaving it {blue}blueish{white}.", "speed": 10, "sweep": 1.7,
                        "durability": 20, "reload": 0, "two handed": True, "req": {}, "crit": 1}, 
        'warhog blade': {'hit': 0, 'damage': 8, 'special': "crunch",
                        "special text": f"The {red}target{white} falls back {darkgrey}crushed{white} by your {orange}blow{white}", "speed": 15, "sweep": 0.9,
                        "durability": 25, "reload": 0, "two handed": False, "req": {}, 'crit': 1},

        # Axes
        'great axe': {'hit': -2, 'damage': 14, 'special': False, "special text": "", "speed": 10, "sweep": 1.7,
                        "durability": 50, "reload": 0, "two handed": True, "req": {"str": 4}, "crit": 3},
        'cursed axe': {'hit': -1, 'damage': 14, 'special': "drain", "special text": f"The {red}target{white} wound turns {darkgrey}grey{white} and {purple}shrivels{white}",
                "speed": 15, "sweep": 1.5, "durability": 15, "reload": 0, "two handed": True, "req": {"str": 4}, 'crit': 3},
        'grogs axe of smashing': {'hit': -2, 'damage': 18, 'special': "crunch", "special text": f"The {red}target{white} falls back {darkgrey}crushed{white} by your {orange}blow{white}",
                "speed": 15, "sweep": 1.2, "durability": 15, "reload": 0, "two handed": True, "req": {"str": 6}, "crit": 3},
        'bugbear axe': {'hit': -1, 'damage': 13, 'special': "bleed", "special text": f"A large {red}gash{white} appears",
                "speed": 15, "sweep": 1.2, "durability": 15, "reload": 0, "two handed": True, "req": {"str": 6}, "crit": 4},
        'axe': {'hit': -1, 'damage': 7, 'special': "bleed", "special text": f"A large {red}gash{white} appears",
                "speed": 15, "sweep": 1, "durability": 15, "reload": 0, "two handed": False, "req": {"str": 3}, "crit": 2},
        'flamebane': {'hit': -1, 'damage': 12, 'special': "burn", "special text": f"Your {red}target{white} bursts into {orange}firey flames{white}", "speed": 29, "sweep": 1.5,
                        "durability": 20, "reload": 0, "two handed": True, "req": {}, "crit": 5},

        # Bows
        'short bow': {'hit': 2, 'damage': 11, 'special': False, "special text": "", "speed": 20, "sweep": 2,
                            "durability": 15, "reload": 1, "two handed": True, "req": {}, "crit": 3},
        'longbow': {'hit': 3, 'damage': 40, 'special': False, "special text": "", "speed": 40, "sweep": 2,
                            "durability": 25, "reload": 2, "two handed": True, "req": {"str": 5}, 'crit': 3},
        'crossbow': {'hit': 2, 'damage': 25, 'special': False, "special text": "", "speed": 20, "sweep": 1.5,
                            "durability": 30, "reload": 1, "two handed": False, "req": {}, "crit": 1},
        'cursed bow': {'hit': 1, 'damage': 20, 'special': "drain", "special text": f"The {red}target{white} wound turns {darkgrey}grey{white} and {purple}shrivels{white}",
                "speed": 25, "sweep": 1.5, "durability": 15, "reload": 1, "two handed": True, "req": {"str": 4}, 'crit': 2},
        'explosive bow': {'hit': 3, 'damage': 60, 'special': "burn", "special text": f"Your {red}target{white} bursts into {orange}firey flames{white}",
                "speed": 25, "sweep": 1.5, "durability": 15, "reload": 1, "two handed": True, "req": {"str": 4}, 'crit': 2},

        # Staffs
        'citrine staff': {'hit': 0, 'damage': 3, 'special': False, "special text": "", "speed": 5, "sweep": 1,
                            "durability": 50, "reload": 0, "two handed": False, "req": {"class": "mage"}},
        'ruby staff': {'hit': -2, 'damage': 4, 'special': False, "special text": "", "speed": 20, "sweep": 0.7,
                        "durability": 50, "reload": 0, "two handed": False, "req": {"class": "mage"}},
        'earth staff': {'hit': -2, 'damage': 6, 'special': False, "special text": "", "speed": 20, "sweep": 0.7,
                        "durability": 50, "reload": 0, "two handed": False, "req": {"class": "mage"}},
        'gold staff': {'hit': -1, 'damage': 8, 'special': False, "special text": "", "speed": 20, "sweep": 1,
                        "durability": 50, "reload": 0, "two handed": False, "req": {"class": "mage"}, "crit": 2},
        'sapphire staff': {'hit': 2, 'damage': 2, 'special': False, "special text": "", "speed": 5, "sweep": 0.8,
                            "durability": 50, "reload": 0, "two handed": False, "req": {"class": "mage"}},
        'frost staff': {'hit': 2, 'damage': 4, 'special': False, "special text": "", "speed": 5, "sweep": 1.2,
                            "durability": 50, "reload": 0, "two handed": False, "req": {"class": "mage"}},
        'dread staff': {'hit': 1, 'damage': 6, 'special': False, "special text": "", "speed": 10, "sweep": 1,
                            "durability": 50, "reload": 0, "two handed": False, "req": {"class": "mage"}},
        'quartz staff': {'hit': 3, 'damage': 1, 'special': False, "special text": "", "speed": 5, "sweep": 0.5,
                            "durability": 50, "reload": 0, "two handed": False, "req": {"class": "mage"}},
        'cotopia staff': {'hit': 2, 'damage': 1, 'special': False, "special text": "", "speed": 5, "sweep": 0.5,
                            "durability": 50, "reload": 0, "two handed": False, "req": {"class": "mage"}},

        # Claymores
        'claymore': {'hit': -2, 'damage': 9, 'special': "bleed",
                        "special text": f"A large {red}gash{white} appears", "speed": 20, "sweep": 1,
                        "durability": 20, "reload": 0, "two handed": False, "req": {"str": 4}, "crit": 1},
        'curved claymore': {'hit': -3, 'damage': 20, 'special': "crunch",
                        "special text": f"The {red}target{white} falls back {darkgrey}crushed{white} by your {orange}blow{white}", "speed": 20, "sweep": 1,
                        "durability": 20, "reload": 0, "two handed": True, "req": {"str": 4}, "crit": 2},
        'dark claymore': {'hit': -2, 'damage': 15, 'special': "bleed",
                            "special text": f"You cause a {red}wound{white} gushing with {red}blood{white}", "speed": 30,
                            "sweep": 1.7, "durability": 20, "reload": 0, "two handed": True, "req": {"str": 5}, "crit": 2},
        'nathans jade claymore': {'hit': -1, 'damage': 12, 'special': "life steal",
                        "special text": f"The {red}enemy{white} turns a {darkgrey}shadowly grey{white} as it\'s {red}lifeforce{white} is being {purple}drained{white}", "speed": 20, "sweep": 1,
                        "durability": 20, "reload": 0, "two handed": True, "req": {"str": 2}, "crit": 1},
        'dragon scale claymore': {'hit': -2, 'damage': 40, 'special': "dragon burn",
                            "special text": f"The {copper}enemy{white} ignites on {red}fire{white}. {paleyellow}White hot flames{white} ingulf everything.", "speed": 30,
                            "sweep": 2, "durability": 20, "reload": 1, "two handed": True, "req": {"str": 6}, 'crit': 3},
        
        # Scimitars
        'kobold scimitar': {'hit': 4, 'damage': 8, 'special': "poison", "special text": f"Ugly {green}green{white} blood {lime}oozes{white} out of their {red}wound{white}", "speed": 5, "sweep": 1,
                    "durability": 20, "reload": 0, "two handed": False, "req": {}},
        'master scimitar': {'hit': 2, 'damage': 8, 'special': "shock", "special text": f"The {red}enemies{white} body {paleyellow}crackles{white} with {yellow}electricity{white}.", "speed": 5, "sweep": 1.5,
                    "durability": 25, "reload": 0, "two handed": False, "req": {"dex": 5}},
        'sun scimitar': {'hit': 3, 'damage': 12, 'special': "burn", "special text": f"The {red}enemies{white} body is {red}lit{white} up in {orange}fiery flames{white}", "speed": 5, "sweep": 1.5,
                    "durability": 30, "reload": 0, "two handed": False, "req": {"dex": 5}},
        'scimitar': {'hit': 4, 'damage': 6, 'special': False, "special text": "", "speed": 4, "sweep": 1,
                    "durability": 25, "reload": 0, "two handed": False, "req": {"dex": 5}},

        # Daggers
        'cursed dagger': {'hit': 3, 'damage': 6, 'special': "drain", "special text": f"The {red}target{white} wound turns {darkgrey}grey{white} and {purple}shrivels{white}",
                "speed": 4, "sweep": 0.8, "durability": 15, "reload": 0, "two handed": False, "req": {"dex": 4}},
        'dagger': {'hit': 4, 'damage': 3, 'special': "bleed",
                    "special text": f"A large {red}gash{white} appears", "speed": 3, "sweep": 0.5,
                    "durability": 20, "reload": 0, "two handed": False, "req": {}},
        'grim dagger': {'hit': 3, 'damage': 3, 'special': ["hyper bleed", "hyper bleed", "hyper bleed"],
                    "special text": [f"{darkgrey}You draw lots of {red}blood{darkgrey} as a gaping {red}wound{darkgrey} opens{white}", f"{darkgrey}You draw lots of {red}blood{darkgrey} as a gaping {red}wound{darkgrey} opens{white}", f"{darkgrey}You draw lots of {red}blood{darkgrey} as a gaping {red}wound{darkgrey} opens{white}"], "speed": 10, "sweep": 1,
                    "durability": 20, "reload": 0, "two handed": False, "req": {}},
        'feather dagger': {'hit': 5, 'damage': 5, 'special': "bleed",
                    "special text": f"A large {red}gash{white} appears", "speed": 3, "sweep": 0.6,
                    "durability": 20, "reload": 0, "two handed": False, "req": {"dex": 5}},
        'dagger of stealing': {'hit': 3, 'damage': 5, 'special': "bleed",
                    "special text": f"A large {red}gash{white} appears", "speed": 4, "sweep": 0.6,
                    "durability": 20, "reload": 0, "two handed": False, "req": {"dex": 6}},
        'crystal dagger': {'hit': 10, 'damage': 30, 'special': False, "special text": "", "speed": 100, "sweep": 1.5,
                        "durability": 1, "reload": 0, "two handed": False, "req": {}},

        # Light Weapons
        'rapier': {'hit': 6, 'damage': 4, 'special': False, "special text": "", "speed": 3, "sweep": 0.8,
                    "durability": 25, "reload": 0, "two handed": False, "req": {"dex": 4}},
        'note-it-downs saber': {'hit': 4, 'damage': 6, 'special': "drain", "special text": f"The {red}target{white} wound turns {darkgrey}grey{white} and {purple}shrivels{white}", "speed": 5, "sweep": 1.5,
                    "durability": 20, "reload": 0, "two handed": False, "req": {}},
        'cross-saber': {'hit': 4, 'damage': 8, 'special': "bleed", "special text": f"A large {red}gash{white} appears", "speed": 5, "sweep": 1.5,
                    "durability": 20, "reload": 0, "two handed": True, "req": {"dex": 6}},
        'warped saber': {'hit': 4, 'damage': 16, 'special': "acid", "special text": f"{lime}Radoactive{white} goo covered the {red}enemy{white} causing a {orange}deadly burn{white}.", "speed": 5, "sweep": 1.5,
                    "durability": 30, "reload": 0, "two handed": True, "req": {"dex": 6}, "damage to all": 8},
        'trident': {'hit': 6, 'damage': 8, 'special': False, "special text": "", "speed": 3, "sweep": 1,
                    "durability": 30, "reload": 0, "two handed": False, "req": {}, "crit": 1},

        # Other
        'wooden club': {'hit': -1, 'damage': 6, 'special': "bleed",
                        "special text": f"A large {red}gash{white} appears", "speed": 12, "sweep": 0.8,
                        "durability": 5, "reload": 0, "two handed": False, "req": {}, "crit": 2},
        'stone on stick': {'hit': -5, 'damage': 100, 'special': "bleed",
                        "special text": f"A large {red}gash{white} appears", "speed": 20, "sweep": 2,
                        "durability": 2, "reload": 0, "two handed": True, "req": {}, "crit": 5},
        'ice spikes club': {'hit': -1, 'damage': 10, 'special': "hyper freeze",
                        "special text": f"{turquoise}Ice{white} instantly covers the {red}enemies{white} body. Keeping it in a {teal}frosted{white} prison", "speed": 12, "sweep": 0.9,
                        "durability": 9, "reload": 0, "two handed": False, "req": {}, "crit": 3},  
        'jade scythe': {'hit': 0, 'damage': 15, 'special': "life steal", "special text": f"The {red}enemy{white} turns a {darkgrey}shadowly grey{white} as it\'s {red}lifeforce{white} is being {purple}drained{white}", "speed": 10, "sweep": 2,
                        "durability": 20, "reload": 0, "two handed": True, "req": {}},   
        'jade harpoon': {'hit': 1, 'damage': 16, 'special': ["life steal", "life steal", "life steal"], "special text": [f"The {red}enemy{white} turns a {darkgrey}shadowly grey{white} as it\'s {red}lifeforce{white} is being {purple}drained{white}",f"The {red}enemy{white} turns a {darkgrey}shadowly grey{white} as it\'s {red}lifeforce{white} is being {purple}drained{white}", f"The {red}enemy{white} turns a {darkgrey}shadowly grey{white} as it\'s {red}lifeforce{white} is being {purple}drained{white}"], "speed": 13, "sweep": 1.3,
                        "durability": 20, "reload": 0, "two handed": True, "req": {"str": 5, "dex": 5}},   
        'spear': {'hit': 1, 'damage': 6, 'special': False, "special text": "", "speed": 5, "sweep": 2.2,
                            "durability": 20, "reload": 0, "two handed": True, "req": {}},
        'lightning spear': {'hit': 5, 'damage': 8, 'special': "lightning", "special text": f"A {gold}lightning bolt{white} from the {darkgrey}cloudy{white} sky {red}strikes{white} the {copper}enemy{white}", "speed": 5, "sweep": 2.2,
                            "durability": 20, "reload": 0, "two handed": False, "req": {}},
        'tazer': {'hit': 5, 'damage': 1, 'special': "shock", "special text": f"The {red}enemies{white} body {paleyellow}crackles{white} with {turquoise}electricity{white}.", "speed": 5, "sweep": 0.5,
                            "durability": 20, "reload": 0, "two handed": False, "req": {}},
        'netherite shovel': {'hit': 1, 'damage': 5, 'special': "dirtify", "special text": f"The {red}enemy{white} turns into {brown}dirt{white}?", "speed": 10, "sweep": 1,
                            "durability": 2031, "reload": 0, "two handed": False, "req": {}},
        'the stick to rule them all': {'hit': 5, 'damage': 100, 'special': False, "special text": "", "speed": 5, "sweep": 1,
                            "durability": 1, "reload": 0, "two handed": False, "req": {"str": 100}},
        'power gauntlets': {'hit': 0, 'damage': 0, 'special': False,
                    "special text": "", "speed": 5, "sweep": 2,
                    "durability": 20, "reload": 0, "two handed": False, "req": {}},
        'combo gloves': {'hit': 10, 'damage': 4, 'special': False,
                    "special text": "", "speed": 2, "sweep": 2,
                    "durability": 20, "reload": 0, "two handed": True, "req": {}},

    }
    
shield_all = {
        "wooden shield": {'block': 3, "guard": 7, 'damage': 3, "break": 9},
        "bronze shield": {'block': 4, "guard": 8, 'damage': 4, "break": 12},
        "iron shield": {'block': 5, "guard": 5, 'damage': 6, "break": 15},
        "steel shield": {'block': 5, "guard": 9, 'damage': 5, "break": 20},
        "platinum shield": {'block': 6, "guard": 11, 'damage': 6, "break": 25},

        "phoenix shield": {"block": 5, "guard": 10, "damage": 8, "break": 25},
        "guardian shield": {"block": 7, "guard": 5, "damage": 2, "break": 30},
        "plate shield": {"block": 5, "guard": 10, "damage": 3, "break": 50},
        "scale shield": {"block": 3, "guard": 14, "damage": 4, "break": 15},
        "rune shield": {"block": 5, "guard": 12, "damage": 6, "break": 9},
        "goblin shield": {'block': 3, "guard": 6, 'damage': 5, "break": 8},
        "kinetic shield [0]": {"block": 0, "guard": 8, "damage": 5, "break": 20},
        "shield of blocking": {"block": "80", "guard": 5, "damage": 4, "break": 15},
        "grim shield": {"block": 7, "guard": 10, "damage": 7, "break": 20},
    }
    
staffs_all = {
        'citrine staff': {'hit': 2, 'damage': 15, 'norm': "lightning",
                            "norm text": f"You shoot a {paleyellow}orb{white} of {paleyellow}lightning{white} at your {red}target{white}",
                            "multi": False, "hit bonus": 5, "damage bonus": 9},
        'ruby staff': {'hit': 2, 'damage': 12, 'norm': "flame",
                        "norm text": f"You cast a {red}torrent{white} of {orange}flames{white} at your {darkgrey}targets{white}",
                        "multi": True, "hit bonus": 3, "damage bonus": 9},
        'sapphire staff': {'hit': 4, 'damage': 9, 'norm': "waves",
                            "norm text": f"You shoot a {blue}gush{white} of {turquoise}waves{white} at your {darkgrey}targets{white}",
                            "multi": True, "hit bonus": 6, "damage bonus": 7},
        'quartz staff': {'hit': 6, 'damage': 8, 'norm': "wind",
                            "norm text": f"You shoot a {silver}gust{white} of {grey}wind{white} at your {red}target{white}",
                            'multi': False, "hit bonus": 5, "damage bonus": 6},
        "cotopia staff": {'hit': 2, 'damage': 8, 'norm': "leaf",
                            "norm text": f"You {orange}fire{white} out a {darkgrey}swarm{white} of {red}razor sharp{white} {lime}leafs{white} at your {red}targets{white}.",
                            'multi': True, "hit bonus": 1, "damage bonus": 7},
        "earth staff": {'hit': 3, 'damage': 20, 'norm': "earthquake",
                            "norm text": f"You slam your {green}earth staff{white} into the ground causing huge {darkgrey}stone spike{white} to erupt out of the {brown}ground{white}",
                            'multi': False, "hit bonus": 4, "damage bonus": 10},
        "frost staff": {'hit': 10, 'damage': 10, 'norm': "frost wind",
                            "norm text": f"You wave your {turquoise}frost staff{white} causing a huge {teal}ice blast{white} to emit from your {brown}staff{white} freezing all enemies.",
                            'multi': True, "hit bonus": 8, "damage bonus": 9}, 
        "gold staff": {'hit': 4, 'damage': 25, 'norm': "gold slam",
                            "norm text": f"You hammer your {gold}golden staff{white} into the {red}enemy{white} sending a flash of {gold}golden light{white} and causing the {red}enemy{white} to fly back",
                            'multi': False, "hit bonus": 4, "damage bonus": 12},
        "dread staff": {'hit': 9, 'damage': 15, 'norm': "frost wind",
                            "norm text": f"Your eyes glow {lime}green{white} as you send a army of {darkgrey}skeletons{white} to attack all the {red}enemies{white}. ",
                            'multi': True, "hit bonus": 6, "damage bonus": 15}, 

}

enemies_all = {
        # Basic Enemies
        "goblin": {
            "attack": "The " + green + "goblin" + white + " jumps up and slams down a " +
                    copper + "Wooden Club" + white + " at you",
            'health': 10,
            'damage': 3,
            "elemental": 'none',
            "armor": 5,
            'drop': {'wooden club': 10, 'goblin shield': 20, "goblin horn": 10},
            "dex": 0,
            "str": 5,
            "gold": 2,
            "exp": 10,
            "death": f"The goblin falls to the ground in {red}blood{white}, {grey}dead{white}"
        },
        "skeleton soldier": {
            "attack": f"The {silver}skeleton soldier{white} swings a {darkgrey}broadsword{white} at you",
            'health': 15,
            'damage': 5,
            "elemental": 'bleed',
            "armor": 8,
            'drop': {'iron sword': 10},
            "dex": 1,
            "str": 6,
            "gold": 10,
            "exp": 30,
            "death": f"The {silver}skeleton soldier{white} collapses into a pile of {paleyellow}bones{white}."
        },
        "skeleton": {
            "attack": f"The {silver}skeleton{white} rambles towards you and {red}claws{white} at your face!",
            'health': 10,
            'damage': 2,
            "elemental": 'drain',
            "armor": 6,
            'drop': {'skull': 10},
            "dex": 2,
            "str": 5,
            "gold": 10,
            "exp": 20,
            "death": f"The {silver}skeleton{white} bursts into a pile of {paleyellow}bones{white}."
        },
        "zombie": {
            "attack": f"The {green}zombie{white} lumbers towards you and throws a {red}punch{white}",
            'health': 20,
            'damage': 1,
            "elemental": 'poison',
            "armor": 6,
            'drop': {},
            "dex": 0,
            "str": 7,
            "gold": 10,
            "exp": 20,
            "death": f"The {green}zombies{white} head falls off, its body soon {red}follows{white}, falling to the floor."
        },
        "ghost": {
            "attack": f"The {turquoise}gh{blue}os{teal}st{white} drains your {purple}life{white} through {darkgrey}dark magic{white}",
            'health': 10,
            'damage': 5,
            "elemental": 'drain',
            "armor": 19,
            'drop': {"claymore": 50, "iron sword": 50, "steel sword": 50, "flame blade": 100, "longbow": 50, "iron shield": 50, "steel shield": 50, "platinum shield": 50, "curved claymore": 50, "double bladed sword": 50,},
            "dex": 20,
            "str": 0,
            "gold": 30,
            "exp": 50,
            "death": f"The {turquoise}gh{blue}os{teal}st{white} disapates fadeing into the {darkgrey}air{white}."
        },
        "rust monster": {
            "attack": f"The {copper}rust monster{white} snaps its {copper}rusty claws{white} at you!",
            'health': 15,
            'damage': 4,
            "elemental": 'rust',
            "armor": 12,
            'drop': {'rusty sword': 10, "sharpening stone": 10},
            "dex": 3,
            "str": 3,
            "gold": 10,
            "exp": 20,
            "death": f"The {copper} monster{white} screeches and flips over, {darkgrey}dead{white}"
        },
        "chest mimic": {
            "attack": f"The {brown}chest mimic{white} bites you!",
            'health': 7,
            'damage': 3,
            "elemental": 'none',
            "armor": 8,
            'drop': {}, 
            "dex": 1,
            "str": 3,
            "gold": 5,
            "exp": 5,
            "death": f"The {darkgrey}mimic{white} rolls over dropping all it's {gold}coins{white}"
        },
        "giant rat": {
            "attack": f"The {darkgrey}giant rat{white} throws itself at you and {paleyellow}nashes{white} it's {red}teeth{white}",
            'health': 5,
            'damage': 3,
            "elemental": 'poison',
            "armor": 5,
            'drop': {}, 
            "dex": 1,
            "str": 2,
            "gold": 5,
            "exp": 5,
            "death": f"The {darkgrey}giant rat{white} falls to the {brown}ground{white} with a thud"
        },
        "bandit": {
            "attack": [f"The {copper}bandit{white} slashes at you with a {darkgrey}scimitar{white}", f"The {copper}bandit{white} steals some {gold}gold{white} from you"],
            'health': 12,
            'damage': [5, "steal"],
            "elemental": ['none', "none"],
            "armor": 8,
            'drop': {"scimitar": 10},
            "dex": [3, 10],
            "str": 5,
            "gold": 10,
            "exp": 20,
            "death": f"The {copper}bandit{white} coughs, {red}staggers{white} and falls to the {brown}ground{white}"
        },
        "kobold": {
            "attack": f"The {lime}kobold{white} slashes at you with a {green}poison scimitar{white}",
            'health': 25,
            'damage': 10,
            "elemental": "poison",
            "armor": 8,
            'drop': {"kobold scimitar": 10},
            "dex": 4,
            "str": 5,
            "gold": 20,
            "exp": 40,
            "death": f"The {lime}kobold{white} hisses, as it {red}falls{white} to the ground."
        },
        "snow minion": {
            "attack": f"The {teal}snow minion{white} hurls itself at you",
            'health': 5,
            'damage': 2,
            "elemental": 'none',
            "armor": 3,
            'drop': {},
            "dex": 5,
            "str": 1,
            "gold": 1,
            "exp": 5,
            "death": f"The {teal}snow minion{white} explodes in a pile of {silver}snow{white}"
        },
        "jade minion": {
            "attack": f"The {teal}jade minion{white} hurls itself at you",
            'health': 7,
            'damage': 3,
            "elemental": 'force drain',
            "armor": 5,
            'drop': {"jade": 25},
            "dex": 5,
            "str": 1,
            "gold": 3,
            "exp": 10,
            "death": f"The {teal}jade minion{white} shattters into {teal}jade{white}."
        },
        "noble": {
            "attack": "The " + gold + "noble" + white + " parries and thrust a " +
                        silver + "rapier" + white + " at you",
            'health': 10,
            'damage': 2,
            "elemental": 'none',
            "armor": 10,
            'drop': {"rapier": 5},
            "dex": 5,
            "str": 2,
            "gold": 9,
            "exp": 15,
            "death": f"The noble collapses, {red}dead{white}"
        },
        "warrior": {
            "attack": "The " + orange + "warrior" + white + " slams a " +
                        darkgrey + "broadsword" + white + " down upon you",
            'health': 15,
            'damage': 3,
            "elemental": 'none',
            "armor": 6,
            'drop': {"bronze sword": 10, 'bronze shield': 10},
            "dex": 2,
            "str": 5,
            "gold": 7,
            "exp": 20,
            "death": f"The warrior falls, {red}dead{white}"
        },
        "troll": {
            "attack": "The " + green + "troll" + white + " screams and slash its " +
                        grey + "nails" + white + " at you",
            'health': 15,
            'damage': 5,
            "elemental": 'none',
            "armor": 5,
            'drop': {"troll heart": 5},
            "dex": 4,
            "str": 6,
            "gold": 5,
            "exp": 30,
            "death": f"The troll falls to the ground in {blue}blue blood{white}, {grey}dead{white}"
        },
        "dragon worshiper": {
            "attack": f"The {darkgrey}dragon worshiper{white} sends {purple}shadow spear{white} hurling directly at {blue}you{white}",
            'health': 15,
            'damage': 7,
            "elemental": 'drain',
            "armor": 10,
            'drop': {"shadow spear scroll": 10},
            "dex": 1,
            "str": 4,
            "gold": 10,
            "exp": 35,
            "death": f"The {red}dragon worshiper{white} seems to {orange}melt{white} into the {green}forest ground{white}."
        },
        "orc": {
            "attack": f"The {green}orc{white} charges and cleaves its {grey}claymore{white} at you",
            'health': 20,
            'damage': 4,
            "elemental": 'none',
            "armor": 8,
            'drop': {"claymore": 7, "orc tooth": 10},
            "dex": -1,
            "str": 6,
            "gold": 10,
            "exp": 30,
            "death": f"The {green}orc{white} falls in {grey}battle{white}, dead."
        },
        "ogre": {
            "attack": f"The {brown}og{copper}re{white} slams a massive {green}tree{brown} branch{white} at you",
            'health': 55,
            'damage': 15,
            "elemental": 'confusion',
            "armor": 6,
            'drop': {"ogre nail": 10},
            "dex": -1,
            "str": 10,
            "gold": 40,
            "exp": 60,
            "death": f"The {brown}og{copper}re{white} wobbles around before falling off a {darkgrey}cliff{white} !"
        },
        "spike gang runt": {
            "attack": f"The {darkgrey}spike gang{white} {copper}runt{white} slams its {turquoise}ice spikes{white} {brown}club{white} at you",
            'health': 20,
            'damage': 5,
            "elemental": 'freeze',
            "armor": 8,
            'drop': {"ice spikes club": 10},
            "dex": 0,
            "str": 5,
            "gold": 20,
            "exp": 30,
            "death": f"The {darkgrey}spike gang{white} {copper}runt{white} tries to {blue}flee{white} but is {red}mortaly wounded{white}"
        },
        "spike gang leader": {
            "attack": [f"The {darkgrey}spike gang{white} {copper}leader{white} slams its {turquoise}ice spikes{white} {brown}club{white} at you",
                       f"The {darkgrey}spike gang{white} {copper}leader{white} throws a {yellow}rapid{white} set of {brown}punches{white} at you"],
            'health': 30,
            'damage': [5, 4],
            "elemental": ['freeze', "confusion"],
            "armor": 8,
            'drop': {"ice spikes club": 5},
            "dex":[1, 4],
            "str": 8,
            "gold": 30,
            "exp": 45,
            "death": f"The {darkgrey}spike gang{white} {copper}leader{white} gnashes his {yellow}teeth{white} at you at he falls {red}dead{white}."
        },
        "bugbear": {
            "attack": f"The {brown}bugbear{white} thunders toward you and swings its {darkgrey}axe{white}",
            'health': 40,
            'damage': 10,
            "elemental": 'bleed',
            "armor": 5,
            'drop': {"bugbear axe": 5},
            "dex": -1,
            "str": 6,
            "gold": 20,
            "exp": 50,
            "death": f"The {brown}bugbear{white} collapses to the {darkgrey}ground{white} in a deafening {orange}thud{white}."
        },
        "goliath": {
            "attack": f"The {teal}gol{darkgrey}iath{white} swings a {red}massive{white} {purple}curved claymore{white} at you",
            'health': 80,
            'damage': 20,
            "elemental": 'bleed',
            "armor": 8,
            'drop': {"curved claymore": 5, "healing stone": 1},
            "dex": -1,
            "str": 10,
            "gold": 40,
            "exp": 60,
            "death": f"The {teal}gol{darkgrey}iath{white} screams out {red}curses{white}, dying."
        },
        "wooly mammoth": {
            "attack": f"The {brown}wooly{blue} mammoth{white} rams into you!",
            'health': 40,
            'damage': 5,
            "elemental": 'confusion',
            "armor": 5,
            'drop': {"mammoth meat": 5},
            "dex": -2,
            "str": 10,
            "gold": 20,
            "exp": 30,
            "death": f"The {brown}wooly{blue} mammoth{white} staggers around and {red}falls{white} to the floor."
        },
        "assasin": {
            "attack": [f"The {darkgrey}assasin{white} stabs you with a {gold}feather dagger{white}",
                        f"The {darkgrey}assasin{white} uses {red}heal wounds{white}",
                        f"The {darkgrey}assasin{white} fires a {lime}poison tipped{white} {darkgrey}bolt{white} from a {brown}crossbow{white}"],
            'health': 20,
            'damage': [7, "heal", 6],
            "elemental": ["bleed", "none", "bleed"],
            "armor": 15,
            'drop': {"feather dagger": 5, "crossbow": 5},
            "dex": [4, 10, 5],
            "str": 3,
            "gold": 40,
            "exp": 50,
            "death": f"The {darkgrey}assasin{white} takes a {green}posion pill{white} insuring that no {blue}secrets{white} would be spilled..."
        },
        "merrow": {
            "attack": [f"The {purple}Merr{blue}ow{white} throws its {darkgrey}harpoon{white} at you",
                        f"The {purple}Merr{blue}ow{white} jabs its {darkgrey}harpoon{white} at you",
                        f"The {purple}Merr{blue}ow{white} shoots a {blue}blast{white} of {turquoise}water{white} at you"],
            'health': 50,
            'damage': [20, 15, 8],
            "elemental": ["life steal", "life steal", "confusion"],
            "armor": 10,
            'drop': {"jade harpoon": 5},
            "dex": [1, 3, 10],
            "str": 5,
            "gold": 50,
            "exp": 50,
            "death": f"The {purple}Merr{blue}or{white} utters a {red}cry{white} at it jumps back into the {turquoise}water{white} never to be seen again..."
        },
        "monk lvl [1]": {
            "attack": [f"The {gold}Monk{white} punches and {red}jabs{white} at you",
                        f"The {gold}Monk{white} {blue}meditates{white}",],
            'health': 30,
            'damage': [10, "dam buff"],
            "elemental": ["confusion", "none"],
            "armor": 9,
            'drop': {},
            "dex": [5, 10],
            "str": 5,
            "gold": 30,
            "exp": 20,
            "death": f"The {gold}Monk{white} bows and tells you the {red}battle{white} is {purple}over{white}"
        },
        "monk lvl [2]": {
            "attack": [f"The {gold}Monk{white} punches and {red}jabs{white} at you",
                        f"The {gold}Monk{white} {blue}meditates{white}",
                        f"The {gold}Monk{white} throws a {darkgrey}spear{white} at you"],
            'health': 40,
            'damage': [10, "dam buff", 15],
            "elemental": ["confusion", "none", "bleed"],
            "armor": 10,
            'drop': {"spear": 10},
            "dex": [6, 10, 3],
            "str": 7,
            "gold": 40,
            "exp": 40,
            "death": f"The {gold}Monk{white} bows and tells you the {red}battle{white} is {purple}over{white}"
        },
        "monk lvl [3]": {
            "attack": [f"The {gold}Monk{white} punches and {red}jabs{white} at you",
                        f"The {gold}Monk{white} {blue}meditates{white}",
                        f"The {gold}Monk{white} throws a {darkgrey}spear{white} at you",
                        f'The {gold}Monk{white} shoots a blast of {orange}CHI{white} at you'],
            'health': 60,
            'damage': [10, "dam buff", 15, 15],
            "elemental": ["confusion", "none", "bleed", "drain"],
            "armor": 11,
            'drop': {"spear": 10},
            "dex": [8, 10, 5, 9],
            "str": 9,
            "gold": 60,
            "exp": 60,
            "death": f"The {gold}Monk{white} bows and tells you the {red}battle{white} is {purple}over{white}"
        },
        "monk lvl [4]": {
            "attack": [f"The {gold}Monk{white} punches and {red}jabs{white} at you",
                        f"The {gold}Monk{white} {blue}meditates{white}",
                        f"The {gold}Monk{white} throws a {darkgrey}spear{white} at you",
                        f'The {gold}Monk{white} shoots a blast of {orange}CHI{white} at you',
                        f"The {gold}Monk{white} sends a {red}fire{white} {darkgrey}kick{white} at you"],
            'health': 80,
            'damage': [10, "dam buff", 15, 15, 25],
            "elemental": ["confusion", "none", "bleed", "drain", "burn"],
            "armor": 12,
            'drop': {"spear": 10},
            "dex": [10, 10, 7, 12, 5],
            "str": 10,
            "gold": 80,
            "exp": 80,
            "death": f"The {gold}Monk{white} bows and tells you the {red}battle{white} is {purple}over{white}"
        },
        "you": {
            "attack": f'{purple}You{white} {red}attack{white} yourself using your {darkgrey}weapon{white}',
            'health': 123,
            'damage': 123,
            "elemental": "none",
            "armor": 123,
            'drop': {"totem of undying": 1},
            "dex": 123,
            "str": 123,
            "gold": 123,
            "exp": 123,
            "death": f"You {red}die{white}, the other {purple}you{white}"
        },
        
        #Core-sail Enemies
        "muck the mutant": { 
            "attack": [f"{lime}Muck{white} the {darkgrey}mutant{white} bleches out {orange}burning acid{white} at you", 
                       f"{lime}Muck{white} the {darkgrey}mutant{white} regenerates more {orange}goo{white}"],
            'health': 60,
            'damage': [10, "heal"],
            "elemental": ['acid', "none"],
            "armor": 6,
            'drop': {"acid goo": 3},
            "dex": [3, 10],
            "str": 5,
            "gold": 20,
            "exp": 30,
            "death": f"{lime}Muck{white} the {darkgrey}mutant{white} has been {red}Eliminated{white} from the {blue}Core-sail{white} Arena"
        },
        "zanders the pirate": { 
            "attack": [f"{darkgrey}Zanders{white} slashes at you with a {orange}sun scimitar{white}", 
                       f"{darkgrey}Zanders{white} throws a {red}knife{white} at you"],
            'health': 60,
            'damage': [15, 10],
            "elemental": ['burn', "none"],
            "armor": 11,
            'drop': {"sun scimitar": 5},
            "dex": [2, 5],
            "str": 5,
            "gold": 40,
            "exp": 50,
            "death": f"{darkgrey}Zanders{white} the {gold}Pirate{white} has been {red}Eliminated{white} from the {blue}Core-sail{white} Arena"
        },
        "the rock giant": { 
            "attack": [f"The {copper}Rock{darkgrey} Giant{white} throws a {red}massive{brown} stone{white} at you", 
                       f"The {copper}Rock{darkgrey} Giant{white} slams its {red}hands{white} together {yellow}crushing{white} you",
                       f"The {copper}Rock{darkgrey} Giant{white} stomps on you"],
            'health': 120,
            'damage': [20, 15, 30],
            "elemental": ['none', "confusion", "none"],
            "armor": 8,
            'drop': {"rock core": 5},
            "dex": [-1, 3, 1],
            "str": 12,
            "gold": 70,
            "exp": 70,
            "death": f"The {copper}Rock{darkgrey} Giant{white} has been {red}Eliminated{white} from the {blue}Core-sail{white} Arena"
        },
        "blade of the north": { 
            "attack": [f"The {darkgrey}Blade{white} of the {blue}North{white} jumps up and {red}slashes{white} you!", 
                       f"The {darkgrey}Blade{white} of the {blue}North{white} starts {purple}spinning{white} with {red}streaking{white} blades.",
                       f"The {darkgrey}Blade{white} of the {blue}North{white} shield {red}bashes{white} you"],
            'health': 100,
            'damage': [30, 40, 20],
            "elemental": ['bleed', "bleed", "confusion"],
            "armor": 12,
            'drop': {"shield of blocking": 5},
            "dex": [4, 2, 6],
            "str": 8,
            "gold": 100,
            "exp": 100,
            "death": f"The {darkgrey}Blade{white} of the {blue}North{white} has been {red}Eliminated{white} from the {blue}Core-sail{white} Arena"
        },
        "other worlder": { 
            "attack": [f"The {purple}Other{orange} Worlder{white} beams you with a {lime}gamma{white} ray.", 
                       f"The {purple}Other{orange} Worlder{white} fire a {turquoise}hyper{white} {darkgrey}cannon{white}",
                       f"The {purple}Other{orange} Worlder{white} slashes you with a {red}warped{gold} saber{white}"],
            'health': 200,
            'damage': [30, 70, 50],
            "elemental": ['acid', "confusion", "drain"],
            "armor": 9,
            'drop': {"world token": 5},
            "dex": [8, -1, 5],
            "str": 8,
            "gold": 200,
            "exp": 200,
            "death": f"The {purple}Other{orange} Worlder{white} has been {red}Eliminated{white} from the {blue}Core-sail{white} Arena"
        },

        # Monster Enemies
        "drowned monstrosity": { 
            "attack": [f"The {green}drowned monstrosity{white} rolls towards you, many {darkgrey}hands{white} claw at you", f"The {green}drowned monstrosity{white} grows more {orange}body parts{white}"],
            'health': 20,
            'damage': [8, "heal"],
            "elemental": ['none', "none"],
            "armor": 5,
            'drop': {},
            "dex": [-1, 10],
            "str": 5,
            "gold": 10,
            "exp": 30,
            "death": f"The {green}drowned monstrosity{white} screams (it sounds weiredly like a {yellow}human{white}) as it falls back into the {turquoise}pool{white}"
        },
        "forest horror": { 
            "attack": [f"The {green}forrest horror{white} opens its {darkgrey}jaws{white} slaming massive {silver}razor sharp{white} {paleyellow}teeth{white} at you!", f"The {green}forest horror{white} {red}ROARS{white} calling upon {copper}ancient strength{white}!"],
            'health': 20,
            'damage': [9, "dam buff"],
            "elemental": ['none', "none"],
            "armor": 5,
            'drop': {},
            "dex": [-2, 10],
            "str": 5,
            "gold": 10,
            "exp": 40,
            "death": f"The {green}forest horror{white} sinks back into the {brown}forest ground{white}..."
        },
        "huge python": { 
            "attack": f"The {lime}huge python{white} hisses and snaps its {darkgrey}fangs{white} at you!",
            'health': 35,
            'damage': 9,
            "elemental": "poison",
            "armor": 5,
            'drop': {},
            "dex": 5,
            "str": 2,
            "gold": 10,
            "exp": 40,
            "death": f"The {lime}huge python{white}\'s head falls to the {brown}ground{white} its body going {yellow}limp{white}"
        },
        "giga spider": { 
            "attack": f"The {darkgrey}giga spider{white} lunges at you and {red}bites{white} you with its {lime}fangs{white}",
            'health': 30,
            'damage': 5,
            "elemental": "poison",
            "armor": 10,
            'drop': {},
            "dex": 3,
            "str": 2,
            "gold": 20,
            "exp": 30,
            "death": f"The {darkgrey}giga spider{white} hisses at you as it {red}dies{white}."
        }, 
        "gelatinous cube": { 
            "attack": [f"The {lime}gelatinous cube{white} spits out {green}poisonous jelly{white} at you", f"The {lime}gelatianous cube{white} attempts to {darkgrey}swallow{white} you!"],
            'health': 25,
            'damage': [5, 50],
            "elemental": ['poison', "none"],
            "armor": 5,
            'drop': {},
            "dex": [1, -10],
            "str": 3,
            "gold": 10,
            "exp": 30,
            "death": f"The {lime}gelatinous cube{white} melts into the {darkgrey}dungeon floor{white} turning into a pile of {orange}ooze{white}"
        },
        "fungi monster": {
            "attack": f"The {green}fungi monster{white} slams both fists at you spreading {lime}spores{white} everywhere",
            'health': 35,
            'damage': 7,
            "elemental": "poison",
            "armor": 5,
            'drop': {"mushroom": 1, "mushroom": 1, "mushroom": 2, "mushroom": 3, "poison nova scroll": 5},
            "dex": 2,
            "str": 5,
            "gold": 5,
            "exp": 40,
            "death": f"The {green}fungi monster{white} screams out and before {orange}disolving{white} into the {brown}dirt{white}."
        },
        "mutant jaguar": {
            "attack": f"The {lime}mutant jaguar{white} charges at you with {red}massive razor-sharp{white} {darkgrey}claws{white}",
            'health': 50,
            'damage': 12,
            "elemental": "poison",
            "armor": 10,
            'drop': {"mutant jaguar tooth": 1, "mutant jaguar tooth": 3, "mutant jaguar tooth": 5},
            "dex": 1,
            "str": 5,
            "gold": 20,
            "exp": 60,
            "death": f"The {lime}mutant jaguar{white} roars for the last {green}time{white} then falls to the {brown}ground{white}"
        },
        "wooden beast mimic": {
            "attack": f"The {brown}wooden{red} beast{darkgrey} mimic{white} throws a huge {brown}wooden chest{white} at you!",
            'health': 50,
            'damage': 10,
            "elemental": "confusion",
            "armor": 10,
            'drop': {"hyper heal potion": 3, "frosted potion": 3, "tortoise potion": 3},
            "dex": -1,
            "str": 5,
            "gold": 20,
            "exp": 30,
            "death": f"The {brown}wooden{red} beast{darkgrey} mimic{white} falters its {darkgrey}mouth{white} opening like a {gold}chest{white}"
        },

        # Mini-Bosses
        "jade knight": {
            "attack": [f"The {turquoise}Jade Knight{white} slashes its {teal}jade sword{white} at you!",
                        f"The {turquoise}Jade Knight{white} casts a {purple}spell{white} causing {blue}ice shards{white} to rain down at you!",
                        f"The {turquoise}Jade Knight{white} casts a {copper}ancient{red} healing spell{white}!"],
            'health': 30,
            'damage': [6, 8, "heal"],
            "elemental": ['force drain', "freeze", "none"],
            "armor": 8,
            'drop': {"ice shards scroll": 5, "jade": 10},
            "dex": [2, 1, 10],
            "str": 6,
            "gold": 20,
            "exp": 60,
            "death": f"The {turquoise}Jade Knight{white} falls to {orange}one knee{white}, its {darkgrey}blade{white} turns to {platinum}mist{white} as it also turns to {platinum}mist{white}."
        },
        "death knight": {
            "attack": [f"The {darkgrey}Death Knight{white} slashes a {purple}shadowy blade{white} at you!",
                        f"The {darkgrey}Death Knight{white} drives the {purple}shadow blade{white} into the ground causing an {red}earthquake{white}",
                        f"The {darkgrey}Death Knight{white} bashes his {darkgrey}iron shield{white} at you"],
            'health': 50,
            'damage': [10, 7, 9],
            "elemental": ['drain', "confusion", "none"],
            "armor": 8,
            'drop': {"iron shield": 5},
            "dex": [1, 5, -1],
            "str": 5,
            "gold": 20,
            "exp": 70,
            "death": f"The {darkgrey}Death Knight{white} falls to {purple}one knee{white}, its {darkgrey}blade{white} turns to {platinum}mist{white} as he also turns to {platinum}mist{white}."
        },
        "lich": {
            "attack": [f"The {purple}lich{white} fires a {darkgrey}shadow spear{white} at you",
                        f"The {purple}lich{white} cast a {darkgrey}shadow bullet{white} spell at you",
                        f"The {purple}lich{white} shoots a {darkgrey}dark chromatic orb{white} at you"],
            'health': 30,
            'damage': [10, 7, 7],
            "elemental": ['none', "drain", "life steal"],
            "armor": 8,
            'drop': {"dark chromatic orb scroll": 5},
            "dex": [-1, 3, 3],
            "str": 2,
            "gold": 20,
            "exp": 60,
            "death": f"The {purple}lich{white} dies then it is ingulfed in {blue}blue flames{white}"
        },
        "dragon lord": {
            "attack": f"The {red}dragon lord{white} attempts to slash the {orange}DRAGON SCALE CLAYMORE{white}",
            'health': 15,
            'damage': 1,
            "elemental": 'none',
            "armor": 10,
            'drop': {"dragon scale claymore": 15},
            "dex": -10,
            "str": 1,
            "gold": 10,
            "exp": 1,
            "death": f"The {red}dragon lord{white} coughs out {red}blood{white}..."
        },

        # Bosses
        "the stranger": {
            "attack": [f"The {purple}stranger{white} swings a {silver}silver{white} {grey}blade{white} at you",
                        f"The {purple}stranger{white} cast a {darkgrey}shadow bullet{white} spell at you",
                        f"The {purple}stranger{white} swings a {silver}silver{white} {grey}blade{white} at you",
                        f"The {purple}stranger{white} cast a {darkgrey}shadow bullet{white} spell at you",
                        f"The {purple}stranger{white} {red}heals{white} himself"
            ],
            'health': 20,
            'damage': [6, 3, 6, 3, "heal"],
            "elemental": ['none', "drain", "none", "drain", "none"],
            "armor": 10,
            'drop': {"hyper heal scroll": 5},
            "dex": [5, 2, 5, 2, 10],
            "str": 1,
            "gold": 12,
            "exp": 40,
            "death": f"The {purple}stranger{white} disappears {platinum}in mist{white}."
        }, 
        "bandit lord": {
            "attack": [f"The {yellow}BANDIT LORD{white} slash a {red}master{white} {paleyellow}scimtar{white} at you",
                        f"The {yellow}BANDIT LORD{white} steals some {gold}gold{white} from you",
                        f"The {yellow}BANDIT LORD{white} thows a {darkgrey}dagger{white} at you"],
            'health': 20,
            'damage': [6, "steal", 4],
            "elemental": ["shock", "none", "none"],
            "armor": 14,
            'drop': {"master scimitar": 5, "lightning stone": 10, "dagger": 12, "dagger swarm scroll": 5},
            "dex": [2, 10, 5],
            "str": 4,
            "gold": 20,
            "exp": 80,
            "death": f"The {yellow}Bandit Lord{white} falls to the {brown}ground{white}, {paleyellow}scimtar{white} in hand"
        },  
        "orc warlord": {
            "attack": [f"The {green}ORC WARLORD{white} hurls a {grey}boulder{white} at you!",
                        f"The {green}ORC WARLORD{white} slashes the {darkgrey}DARK-CLAYMORE{white} at you!",
                        f"The {green}ORC WARLORD{white} {red}ROARS{white}!"],
            'health': 25,
            'damage': [5, 7, "dam buff"],
            "elemental": ['none', "none", "none"],
            "armor": 10,
            'drop': {"dark claymore": 5},
            "dex": [2, -1, 10],
            "str": 7,
            "gold": 15,
            "exp": 70,
            "death": f"The {green}ORC WARLORD{white} staggers and falls, {red}breathing{white} no-more."
        },
        "necromancer": {
            "attack": [f"The {purple}Necromancer{white} casts out a {turquoise}ghosty blue hand{white} that grabs you",
                        f"The {purple}Necromancer{white} sends a volley of {darkgrey}dark arrows{white} flying at you",
                        f"The {purple}Necromancer{white} summons a {yellow}skeleton{white} to join the battle"],
            'health': 60,
            'damage': [17, 15, "summon"],
            "elemental": ['life steal', "drain", "skeleton"],
            "armor": 8,
            'drop': {"dark arrows scroll": 5},
            "dex": [-1, 5, 10],
            "str": 2,
            "gold": 30,
            "exp": 100,
            "death": f"The {purple}necromancer{white} screams as its {darkgrey}body{white} unwinds turn into just a {red}corpse{white}..."
        },
        "jade guardian": {
            "attack": [f"The {turquoise}JADE GUARDIAN{white} slashes its {purple}life {gold}steal{darkgrey} scythe{white} at you!",
                        f"The {turquoise}JADE GUARDIAN{white} swings its {teal}jade fists{white} in a {darkgrey}windmill{white} motion and {orange}charges{white} at you!",
                        f"The {turquoise}JADE GUARDIAN{white} {teal}charges{white} up"],
            'health': 40,
            'damage': [8, 12, "dam buff"],
            "elemental": ['force drain', "none", "none"],
            "armor": 10,
            'drop': {"jade scythe": 5, "jade": 10},
            "dex": [3, 0, 10],
            "str": 5,
            "gold": 30,
            "exp": 100,
            "death": f"The {turquoise}jade guardian{white} spins around {orange}sparks{white} flying everywhere,"
        },
        "guardian of the jungle": {
            "attack": [f"The {purple}GUARDIAN{white} OF THE {green}JUNGLE{white} rams into you with at full {red}force{white}",
                        f"The {purple}GUARDIAN{white} OF THE {green}JUNGLE{white} punches you with a {darkgrey}mossy stone fist{white}",
                        f"The {purple}GUARDIAN{white} OF THE {green}JUNGLE{white} jumps up and falls down {orange}body slamming{white} you"],
            'health': 100,
            'damage': [15, 18, 25],
            "elemental": ['confusion', "confusion", "confusion"],
            "armor": 10,
            'drop': {"jungle blade": 1},
            "dex": [3, -1, -2],
            "str": 8,
            "gold": 50,
            "exp": 150,
            "death": f"The {purple}GUARDIAN{white} OF THE {green}JUNGLE{white} staggers around {orange}sparks{white} and {brown}wood chips{white} flying everywhere,"
        },
        
        "yeti": {
            "attack": [f"The {turquoise}YETI{white} picks up an {teal}icicle{white} and hurls it at you!",
                        f"The {turquoise}YETI{white} {red}heals{white} itself",
                        f"The {turquoise}YETI{white} slams a {red}massive{white} {darkgrey}fist{white} at you!",
                        f"The {turquoise}YETI{white} roars and exhales a {teal}icy blue wind{white} on you!",
                        f"The {turquoise}YETI{white} rolls up into a {darkgrey}ball{white} and {orange}propels{white} itself at you!",
                        f"The {turquoise}YETI{white} picks up an {teal}icicle{white} and hurls it at you!",
                        f"The {turquoise}YETI{white} slams a {red}massive{white} {darkgrey}fist{white} at you!",
                        f"The {turquoise}YETI{white} roars and exhales a {teal}icy blue wind{white} on you!",
                        f"The {turquoise}YETI{white} rolls up into a {darkgrey}ball{white} and {orange}propels{white} itself at you!"],
            'health': 40,
            'damage': [5, "heal", 8, 2, 12, 5, 8, 2, 12],
            "elemental": ["freeze", "none", "none", "freeze", "none", "freeze", "none", "freeze", "none"],
            "armor": 8,
            'drop': {"yeti eye": 1, "yeti eye": 2, "frosted longsword": 1, "aura of weakening scroll": 5},
            "dex": [2, 10, -1, 10, -2, 2, -1, 10, -2],
            "str": 8,
            "gold": 25,
            "exp": 100,
            "death": f"The {turquoise}YETI{white} wobbles around, {red}bleeding{white} everywhere. Finally {blue}seeing{white} that it is going to {red}die{white} it jumps off the {purple}mountain{white}."
        },
        "the dreadwood": {
            "attack": [f"The {brown}DREADWOOD{white} shoots out a volley of {copper}razor sharp branches{white}",
                        f"The {brown}DREADWOOD{white} grows more {brown}branches{white}, {red}healing{white} itself",
                        f"The {brown}DREADWOOD{white}\'s eyes glow {purple}purple{white} as it {darkgrey}drains{white} you",
                        f"The {brown}DREADWOOD{white} lifts up its massive {brown}oaken foot{white} as it {darkgrey}stomps{white} on you!",
            ],
            'health': 60,
            'damage': [7, "heal", 5, 15],
            "elemental": ["bleed", "none", "drain", "none"],
            "armor": 10,
            'drop': {},
            "dex": [5, 10, 10, -1],
            "str": 7,
            "gold": 30,
            "exp": 120,
            "death": f"The {brown}DREADWOOD{white} {orange}roars{white} in anguish as it {darkgrey}disolves{white} into the ground"
        },
        "frost giant": {
            "attack": [f"The {teal}FROST{darkgrey} GIANT{white} slams his huge {brown}foot{white} down at you!",
                        f"The {teal}FROST{darkgrey} GIANT{white} roars filling the air with {turquoise}cold frost{white}",
                        f"The {teal}FROST{darkgrey} GIANT{white} swings a {red}firey axe{white} upon you!",
                        f"The {teal}FROST{darkgrey} GIANT{white} throws a {darkgrey}boulder{white} covered in {teal}snow{white} at you",
            ],
            'health': 180,
            'damage': [11, 5, 14, 16],
            "elemental": ["confusion", "freeze", "burn", "confusion"],
            "armor": 11,
            'drop': {"flamebane": 10},
            "dex": [1, 10, 1, -1],
            "str": 7,
            "gold": 40,
            "exp": 150,
            "death": f"The {teal}FROST{darkgrey} GIANT{white} curses you as he {red}dies{white}."
        },
        "the dark dragon": {
            "attack": [f"The {darkgrey}DARK{white}{purple} DRAGON{white} roars, breathing out a {orange}torrent{white} of {red}flames{white}",
                        f"The {darkgrey}DARK{white}{purple} DRAGON{white} roars, breathing out a {blue}wave{white} of {darkgrey}dark energy{white}",
                        f"The {darkgrey}DARK{white}{purple} DRAGON{white} swings its {orange}gargantuan tail{white} down at you",
                        f"The {darkgrey}DARK{white}{purple} DRAGON{white} slams its {darkgrey}claws{white} down at you",
                        f"The {darkgrey}DARK{white}{purple} DRAGON{white} inhales {darkgrey}dark air{white} its eyes glow {purple}purple{white}",
            ],
            'health': 80,
            'damage': [7, 7, 20, 15, "dam buff"],
            "elemental": ["dragon burn", "life steal", "none", "bleed", "none"],
            "armor": 10,
            'drop': {"dragon scale claymore": 5, "dragon scale": 2},
            "dex": [6, 6, -1, 0, 10],
            "str": 8,
            "gold": 50,
            "exp": 130,
            "death": f"The {darkgrey}DARK{white}{purple} DRAGON{white} bellows a {orange}roar{white} of pure {red}rage{white}, {red}blood{white} gushes from a {gold}hundred{white} wounds. Finally it {darkgrey}collapses{white} on the {brown}floor{white}. "
        },
        
        # Guardians
        "copper guardian": {
            "attack": f"The {copper}copper guardian{white} slams a giant {darkgrey}fist{white} at you",
            'health': 30,
            'damage': 8,
            "elemental": 'none',
            "armor": 12,
            'drop': {},
            "dex": -1,
            "str": 7,
            "gold": 30,
            "exp": 70,
            "death": f"The {copper}copper guardian{white} starts to {red}malfunction{white} and it collapses on the {brown}ground{white}"
        },
        "silver guardian": {
            "attack": f"The {silver}silver guardian{white} shoots out a {red}missle{white} directly at you!",
            'health': 35,
            'damage': 5,
            "elemental": 'none',
            "armor": 14,
            'drop': {},
            "dex": 10,
            "str": 5,
            "gold": 35,
            "exp": 80,
            "death": f"The {silver}silver guardian{white} starts to {red}malfunction{white} and it collapses on the {brown}ground{white}"
        },
        "iron guardian": {
            "attack": f"The {darkgrey}iron guardian{white} shoots out a slams its {darkgrey}dark claymore{white} down upon you",
            'health': 40,
            'damage': 10,
            "elemental": 'none',
            "armor": 9,
            'drop': {"dark claymore": 5},
            "dex": -3,
            "str": 10,
            "gold": 40,
            "exp": 90,
            "death": f"The {darkgrey}iron guardian{white} starts to {red}malfunction{white} and it collapses on the {brown}ground{white}"
        },
        "steel guardian": {
            "attack": f"The {grey}steel guardian{white} swings its {darkgrey}huge broadsword{white} at you",
            'health': 45,
            'damage': 10,
            "elemental": 'none',
            "armor": 13,
            'drop': {"steel sword": 5},
            "dex": 1,
            "str": 10,
            "gold": 45,
            "exp": 100,
            "death": f"The {grey}steel guardian{white} starts to {red}malfunction{white} and it collapses on the {brown}ground{white}"
        },
        "platinum guardian": {
            "attack": f"The {grey}platinum guardian{white} slashes it's {platinum}greatsword{white} in deadly arcs",
            'health': 60,
            'damage': 15,
            "elemental": 'none',
            "armor": 12,
            'drop': {"platinum shield": 5},
            "dex": 2,
            "str": 10,
            "gold": 60,
            "exp": 120,
            "death": f"The {platinum}steel guardian{white} starts to {red}malfunction{white} and it collapses on the {brown}ground{white}"
        },
        "silence guardian": {
            "attack": f"The {turquoise}silence {silver}guardian{white} slams the {darkgrey}ground{white} causing waves of {turquoise}energy{white} release.",
            'health': 100,
            'damage': 15,
            "elemental": 'silence waves',
            "armor": 12,
            'drop': {},
            "dex": 10,
            "str": 10,
            "gold": 70,
            "exp": 120,
            "death": f"The {turquoise}silence {silver}guardian{white} starts to {red}malfunction{white} and it collapses on the {brown}ground{white}"
        },
        "echo guardian": {
            "attack": f"The {teal}echo {darkgrey}guardian{white} blasts a ray of {blue}echo waves{white} from its {darkgrey}core{white}",
            'health': 150,
            'damage': 25,
            "elemental": 'echo blast',
            "armor": 12,
            'drop': {},
            "dex": 10,
            "str": 10,
            "gold": 100,
            "exp": 150,
            "death": f"The {teal}echo {darkgrey}guardian{white} starts to {red}malfunction{white} and it collapses on the {brown}ground{white}"
        },
        
    }
