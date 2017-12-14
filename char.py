"""Character generator for a role-playing game."""
import random


class Character(object):
    """Definition of Character class object."""

    def __init__(self):
        """Initialization of character."""
        self.name = ''
        self.stats = {'STR': 0, 'INT': 0, 'WIS': 0,
                      'DEX': 0, 'CON': 0, 'CHA': 0}
        self.char_class = ''
        self.skills = []
        self.alignment = ''

    def get_name(self):
        """Randomly pick a name for the character."""
        first = random.choice(['Bill', 'Bob', 'Betty', 'Lothar',
                               'Grog', 'Melllvar', 'Grok', 'Elmo',
                               'Sam', 'Zyzax', 'Grep', 'Lars',
                               'Dirk', 'Gerion', 'Mordred', 'Yorick',
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
                              'Highloft', 'Wormfeed', 'Seaborn', 'Brown',
                              'Farseer', 'McGillicutty', 'Laserbeak',
                              'Gardner', 'Drakeslayer', 'the Wise'])

        self.name = '{} {}'.format(first, last)

    def get_stats(self):
        """Randomly determine base stats."""
        if self.char_class == '':
            print('You must determine your character class first.')
            return

        for key in self.stats:
            self.stats[key] = d20()

    def get_class(self):
        """Randomly select a character class."""
        char_class = random.choice(['Barbarian', 'Bard', 'Monk',
                                    'Paladin', 'Ranger', 'Sorcerer',
                                    'Rogue'])

        if char_class == 'Barbarian':
            self.stats['STR'] += 5
            self.stats['INT'] -= 2
            if self.stats['INT'] < 1:
                self.stats['INT'] = 1

        if char_class == 'Bard':
            self.stats['CHA'] += 5

        if char_class == 'Monk':
            self.stats['DEX'] += 2
            self.stats['CON'] += 3

        if char_class == 'Paladin':
            self.stats['WIS'] += 2
            self.stats['STR'] += 3

        if char_class == 'Ranger':
            self.stats['DEX'] += 5

        if char_class == 'Sorcerer':
            self.stats['WIS'] += 3
            self.stats['INT'] += 2
            self.stats['STR'] -= 2
            if self.stats['STR'] < 1:
                self.stats['STR'] = 1

        if char_class == 'Rogue':
            self.stats['DEX'] += 3
            self.stats['CHA'] += 2

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


def d20():
    """Roll a D20."""
    return random.randint(1, 20)


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
    stats_str = 'Abilities: {} \n'.format(new_char.stats)
    skill_str = 'Skills: {}'.format(new_char.skills)
    print('\n' + ('*' * 50) + '\n')
    print(char_str, align_str, stats_str, skill_str)
    print('\n' + ('*' * 50) + '\n')
