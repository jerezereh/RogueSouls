from collections import namedtuple


# File for all dictionaries used in main file, such as items, timings, skills, etc.
SMAPW = 20
SMAPH = 20

SkillNode = namedtuple('SkillNode', ['description', 'effect', 'taken'])
WeaponDamageTypes = namedtuple('typeName', ['l_att', 'h_att'])
Weapon = namedtuple('weaponName', ['wep_type', 'damage', 'l_time', 'h_time'])
Fix = namedtuple('fix', ['bonus', 'stat', 'special_text', 'rarity'])

items = []

skills = {
    'skill1': SkillNode('Your skin hardens.', '+1 END', False),
    'skill2': SkillNode('Your moves grow quicker.', '+1 AGI', False),
    'skill3': SkillNode('Your mind sharpens.', '+1 PER', False),
    'skill4': SkillNode('Your faith strengthens.', '+1 FAI', False)
}

skillgraph = {
    'skill1': ['skill2', 'skill3'],
    'skill2': ['skill1', 'skill3'],
    'skill3': ['skill4'],
    'skill4': []
}

# damage types: basic: slash, blunt, pierce
# complex: thrust (slash/piercing), bludgeoning (blunt/piercing), chop (slash/blunt)
# weapon styles have
weapon_styles = {
    # fist weapons: punch, smash
    'fist': WeaponDamageTypes('blunt', 'blunt'),

    # small swords: underhanded swing, short thrust
    'small_sword': WeaponDamageTypes('slash', 'pierce'),

    # bastard swords: one-handed slash, overhead chop
    'bastard_sword': WeaponDamageTypes('slash', 'chop'),

    # long swords: two-handed slash, two-handed
    'long_swords': WeaponDamageTypes('thrust', 'slash')
}

weapons = {
    'Unarmed': Weapon('fist', '4', '7', '12'),
    'Broken Sword': Weapon('small_sword', '6', '10', '10'),
    'Short Sword': Weapon('small_sword', '15', '10', '12')
}

weapon_prefix = {
    '': '',
    'Hardened': Fix('+1', 'dmg', '', 'mag'),
    'Battered': Fix('-1', 'dmg', '', 'low'),
    'Tiered': Fix()
}

weapon_affix = {
    '': '',
    'Of the Moon': Fix('', '', 'Upon each successful hit, add an amount of SP to your pool equal to the damage the hit'
                               'dealt.', 'uni'),
    'of Storms': Fix(['+2', '-1'], ['int', 'vig'], '', 'rare')
}

armor_prefix = {

}

armor_affix = {

}

acc_prefix = {

}

acc_affix = {

}

consumables = {

}

# AI Notation:
# Right-hand attack: R
# Left-hand attack: L
# Two-hand attack: T
# Block: B
# Dodge: D
# Wait: W
# Repeat pattern: +
# Attack Modifier (Heavy): H

# If AI attempts to attack with one-hand when wielding two-handed weapon, consume two one-handed inputs for each two-
#   handed attack. E.g. if pattern is RLRR+ and creature only has two-handed weapon, pattern is converted to TT+.
# If an attack modifier is present, the attack changes accordingly. If an attack is being consumed to become a two-
# handed, it gains all modifiers of the individual attacks, if applicable (each modifier can only be applied once).
AI = {
    'basic': {
        'def': ['R', 'B', '+'],
        'dual': ['R', 'L', 'R', 'L', 'D', 'D', '+'],
        'th': ['T', 'T', 'B', 'B', '+']
    },

    'aggressive': {
        'def': ['R', 'R', 'R', 'R', 'W', '+'],
        'dual': ['R', 'L', 'R', 'L', 'R', 'L', 'W', '+'],
        'th': ['T', '+']
    }
}

