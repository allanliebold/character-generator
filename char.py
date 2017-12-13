"""Character generator for a role-playing game."""
import random


class Character(object):
    """Definition of Character class object."""

    def __init__(self):
        """Initialization of character."""
        self.name = ''
        self.strength = 0
        self.intelligence = 0
        self.wisdom = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.char_class = ''
        self.abilities = []
        self.alignment = ''

    def get_name(self):
        """Randomly pick a name for the character."""
        first = random.choice(['Bill', 'Bob', 'Betty', 'Lothar',
                               'Grog', 'Melllvar', 'Grok',
                               'Sam', 'Zyzax', 'Grep', 'Lars',
                               'Dirk', 'Gerion', 'Mordred',
                               'Tormund', 'Myra', 'Larona', 'Mim',
                               'Desra', 'Veryl', 'Quarr', 'Arfur',
                               'Brosephus', 'Guymon', 'Cyril',
                               'Klarg', 'Vik', 'Draia'])
        last = random.choice(['Smith', 'Jones', 'Proudsteel',
                              'Darkclaw', 'Deathbringer', 'the Merciless',
                              'Swiftfoot', 'Houlihan', 'Viletongue',
                              'Loreweaver', 'Bloodtooth', 'the Eternal',
                              'Greybeard', 'Whisperwind', 'Warhammer',
                              'Malloy', 'Giantsbane', 'Coldheart',
                              'Highloft', 'Wormfeed', 'Seaborn',
                              'Farseer', 'McGillicutty', 'Laserbeak',
                              'Gardner', 'Drakeslayer'])

        self.name = '{} {}'.format(first, last)

    def get_stats(self):
        """Randomly determine a base stat."""
        self.strength = random.randint(1, 20)
        self.intelligence = random.randint(1, 20)
        self.wisdom = random.randint(1, 20)
        self.dexterity = random.randint(1, 20)
        self.constitution = random.randint(1, 20)
        self.charisma = random.randint(1, 20)

    def get_class(self):
        """Randomly select a character class."""
        char_class = random.choice(['Barbarian', 'Bard', 'Monk',
                                    'Paladin', 'Ranger', 'Sorcerer',
                                    'Rogue'])

        if char_class == 'Barbarian':
            self.strength += 5
            self.intelligence -= 2
            if self.intelligence < 1:
                self.intelligence = 1

        if char_class == 'Bard':
            self.charisma += 5

        if char_class == 'Monk':
            self.dexterity += 2
            self.constitution += 3

        if char_class == 'Paladin':
            self.wisdom += 2
            self.strength += 3

        if char_class == 'Ranger':
            self.dexterity += 5

        if char_class == 'Sorcerer':
            self.wisdom += 3
            self.intelligence += 2
            self.strength -= 2
            if self.strength < 1:
                self.strength = 1

        if char_class == 'Rogue':
            self.dexterity += 3
            self.charisma += 2

        self.char_class = char_class

    def get_skills(self):
        """Determine skills based on character class."""
        if self.char_class == '':
            print('You must determine your character class first.')

        if self.char_class == 'Barbarian':
            self.skills = ['Endurance', 'Intimidate']

        if self.char_class == 'Bard':
            self.skills = random.sample(['Bluff', 'Diplomacy',
                                         'Streetwise'], 2)

        if self.char_class == 'Monk':
            self.skills = random.sample(['Athletics', 'Insight',
                                         'Streetwise'], 2)

        if self.char_class == 'Paladin':
            self.skills = random.sample(['History', 'Religion',
                                         'Endurance'], 2)

        if self.char_class == 'Ranger':
            self.skills = random.sample(['Nature', 'Dungeoneering',
                                         'Perception'], 2)

        if self.char_class == 'Sorcerer':
            self.skills = random.sample(['Arcana', 'Insight', 'History'], 2)

        if self.char_class == 'Rogue':
            self.skills = random.sample(['Stealth', 'Thievery',
                                         'Streetwise'], 2)

    def get_alignment(self):
        """Determine character's alignment."""
        law_chaos = random.choice(['Lawful', 'Neutral', 'Chaotic'])
        good_evil = random.choice(['Good', 'Neutral', 'Evil'])

        if law_chaos == 'Neutral' and good_evil == 'Neutral':
            law_chaos = 'True'

        self.alignment = '{} {}'.format(law_chaos, good_evil)

if __name__ == '__main__':
    """Generate and print a character."""
    new_char = Character()
    new_char.get_name()
    new_char.get_stats()
    new_char.get_class()
    new_char.get_skills()
    new_char.get_alignment()

    char_str = " Name: {} \n Class: {} \n".format(new_char.name,
                                                  new_char.char_class)
    align_str = 'Alignment: {} \n'.format(new_char.alignment)
    stats_str = ("STR: {} \n INT: {} \n WIS: {} \n"
                 " DEX: {} \n CON: {} \n"
                 " CHA: {} \n").format(new_char.strength,
                                       new_char.intelligence,
                                       new_char.wisdom,
                                       new_char.dexterity,
                                       new_char.constitution,
                                       new_char.charisma)
    skill_str = 'Skills: {}'.format(new_char.skills)
    print(char_str, align_str, stats_str, skill_str)
