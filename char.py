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

    def get_name(self):
        """Randomly pick a name for the character."""
        first = random.choice(['Bill', 'Bob', 'Betty', 'Lothar',
                               'Grog', 'Melllvar', 'Grok',
                               'Sam', 'Zyzax', 'Grep',
                               'Dirk', 'Gerion', 'Mordred',
                               'Tormund', 'Myra', 'Larona'])
        last = random.choice(['Smith', 'Jones', 'Proudsteel',
                              'Darkclaw', 'Deathbringer',
                              'Swiftfoot', 'Houlihan',
                              'Loreweaver', 'Bloodtooth',
                              'Greybeard', 'Whisperwind',
                              'Malloy', 'Giantsbane'])

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
                                    'Paladin', 'Ranger', 'Sorcerer'])

        if char_class == 'Barbarian':
            self.strength += 5

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
            self.wisdom += 5

        self.char_class = char_class

    def get_skills(self):
        """Determine skills based on character class."""
        if self.char_class == '':
            print('You must determine your character class first.')

        if self.char_class == 'Barbarian':
            self.skills = ['Endurance', 'Intimidate']

        if self.char_class == 'Bard':
            self.skills = ['Bluff', 'Diplomacy']

        if self.char_class == 'Monk':
            self.skills = ['Athletics', 'Insight']

        if self.char_class == 'Paladin':
            self.skills = ['History', 'Heal']

        if self.char_class == 'Ranger':
            self.skills = ['Nature', 'Stealth']

        if self.char_class == 'Sorcerer':
            self.skills = ['Arcana', 'Insight']


if __name__ == '__main__':
    """Generate and print a character."""
    new_char = Character()
    new_char.get_name()
    new_char.get_stats()
    new_char.get_class()
    new_char.get_skills()

    char_str = "Name: {} \n Class: {} \n".format(new_char.name,
                                                 new_char.char_class)
    stats_str = ("STR: {} \n INT: {} \n WIS: {} \n"
                 "DEX: {} \n CON: {} \n CHA: {} \n").format(new_char.strength,
                                                            new_char.intelligence,
                                                            new_char.wisdom,
                                                            new_char.dexterity,
                                                            new_char.constitution,
                                                            new_char.charisma)
    skill_str = 'Skills: {}'.format(new_char.skills)
    print(char_str, stats_str, skill_str)
