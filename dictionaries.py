from collections import namedtuple


# File for all dictionaries used in main file, such as items, timings, skills, etc.
SMAPW = 20
SMAPH = 20

SkillNode = namedtuple('SkillNode', ['description', 'effect', 'taken'])
WeaponDamageTypes = namedtuple('typeName', ['l_att', 'h_att'])
Weapon = namedtuple('weaponName', ['wep_type', 'damage', 'l_time', 'h_time'])

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
    'long_swords': WeaponDamageTypes('', '')
}

weapons = {
    'Unarmed': Weapon('fist', '4', '7', '12'),
    'Broken Sword': Weapon('small_sword', '6', '10', '10'),
    'Short Sword': Weapon('small_sword', '15', '10', '12')
}

