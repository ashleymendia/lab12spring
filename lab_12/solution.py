from random import randrange, random
from copy import deepcopy

UPPER_CRITICAL_HIT_LIMIT = 256
ATTACK_FIRST_THRESHOLD = 0.7
NAME_IDX, NICKNAME_IDX, LEVEL_IDX, TYPE1_IDX, TYPE2_IDX, HP_IDX, ATTACK_IDX, SPEED_IDX = 0, 1, 2, 3, 4, 6, 7, 8

"""
PROBLEM 1
"""
class Pokemon:
    def __init__(self, pokemon_name, nickname, level, type1, type2, hp, attack, speed):
        """
        The constructor of the Pokemon class.

        :param pokemon_name: A string containing the Pokemon's name.
        :param nickname: A string containing the Pokemon's name.
        :param level: An int containing the Pokemon's level.
        :param type1: A string containing the Pokemon's first type.
        :param type2: A string containing the Pokemon's second type.
        :param hp: An int containing the Pokemon's health points.
        :param attack: An int containing the Pokemon's attack power.
        :param speed: An int containing the Pokemon's speed.
        """
        self.pokemon_name = pokemon_name
        self.nickname = nickname
        self.level = level
        if type2 == "":
            type2 = None
        self.types = (type1, type2)
        self.hp = hp
        self.stats = {
            "attack": attack,
            "speed": speed
        }

        self.critical_hit_multiplier = ((2 * self.level + 5) / (self.level + 5))

    def attack(self):
        """
        Using "helper" method will_land_critical_hit, returns attack value of Pokemon based on the critical hit chances
        explained by the README.

        Critical hit multiplier = (2L + 5) / (L + 5), where L is the Pokemon's level attribute.

        :return: Either the Pokemon's attack stat or the attack stat multiplied by the critical hit multiplier.
        """
        print("{} attacks!".format(self.nickname))
        if self._will_land_critical_hit():
            print("{} lands a critical hit!".format(self.nickname))
            return self.stats["attack"] * self.critical_hit_multiplier

        return self.stats["attack"]

    def _will_land_critical_hit(self):
        """
        A "helper" method that determines whether a Pokemon will land a critical hit.

        :return: True/False
        """
        random_byte = randrange(0, UPPER_CRITICAL_HIT_LIMIT)
        threshold_value = self.stats["speed"] / 2

        return random_byte < threshold_value

    def __str__(self):
        """
        Creates and returns a string representation of the Pokemon object.

        :return: A string.
        """
        type_string = "/".join(list(self.types)) if self.types[1] else self.types[0]

        return "{} Pokemon object '{}' of type(s) {}, level {}".format(
            self.pokemon_name,
            self.nickname,
            type_string,
            self.level
        )

    def __gt__(self, other):
        """
        Compares the "speed" stat against other's "speed" stat and returns True if it is larger. Otherwise returns
        False.

        :param other:
        :return: None.
        """
        if not isinstance(other, Pokemon):
            return False

        return self.stats["speed"] > other.stats["speed"]


"""
PROBLEM 2
"""
class ProfessorTrainer:
    def __init__(self, trainer_name, filepath):
        """
        The initializer method of the ProfessorTrainer class.

        :param trainer_name: A string containing the name of the professor.
        :param filepath: A string denoting the file path and name containing the professor's Pokemon's information.
        """
        self.professor_name = trainer_name
        self.party = []
        self._load_pokemon(filepath)

    def _load_pokemon(self, filepath):
        """
        A "helper" method that reads a file and populates the ProfessorTrainer's party attribute with Pokemon objects
        created from the information in the file.

        :param filepath: The path of the file to be read, in string form.
        :return: None.
        """
        try:
            save_file = open(filepath, 'r')
        except FileNotFoundError:
            print("ERROR: FILE {} NOT FOUND!".format(filepath))
            return

        save_file.readline()  # header

        for line in save_file:
            line = line.strip().split(",")
            name, nickname, level, type1, type2 = line[NAME_IDX], line[NICKNAME_IDX], int(line[LEVEL_IDX]), \
                                                  line[TYPE1_IDX], line[TYPE2_IDX]
            hp = int(line[HP_IDX])
            attack, speed = int(line[ATTACK_IDX]), int(line[SPEED_IDX])

            new_pokemon = Pokemon(name, nickname, level, type1, type2, hp, attack, speed)

            self.party.append(new_pokemon)

        save_file.close()

    def __str__(self):
        """
        Creates and returns a string representation of the Professor object.

        :return: A string.
        """
        list_representation = ["ProfessorTrainer object '{}' and contains the following Pokemon objects:"
                                   .format(self.professor_name)]

        # For list comprehension!
        pokemon_string_list = ["{}, called {} {}".format(pokemon.pokemon_name, pokemon.nickname, pokemon.types) for pokemon in self.party]

        list_representation.extend(pokemon_string_list)

        return "\n".join(list_representation)


"""
PROBLEM 3
(Note: see function ultimate_showdown() before looking at move())
"""
def move(first_attacking_trainer, first_attacking_pokemon, second_attacking_trainer, second_attacking_pokemon):
    """
    Performs a single move where Pokemon A attacks Pokemon B. It then checks whether Pokemon B's health is 0 or below.
    If so, it returns the name of the winner (Trainer A's 'professor_name' attribute). It then repeats the same process
    but with Pokemon B attacking Pokemon A and checking whether Pokemon A's health has dropped to zero or below.

    If neither Pokemon fainted, returns a NEXT_TURN_FLAG, which is not really necessary, but it adds clarity to the
    fact that another move will be starting.

    :param first_attacking_trainer: The ProfessorTrainer object whose Pokemon is attacking first.
    :param first_attacking_pokemon: The Pokemon object that is attacking first.
    :param second_attacking_trainer: The ProfessorTrainer object whose Pokemon is attacking second.
    :param second_attacking_pokemon: The Pokemon object that is attacking second.
    :return: Either NEXT_TURN_FLAG or the professor_name attribute of the winning ProfessorTrainer object (a str).
    """
    # First Pokemon attacks
    second_attacking_pokemon.hp -= first_attacking_pokemon.attack()

    # We check if the defending Pokemon has fainted (i.e. health is 0 or below)
    if second_attacking_pokemon.hp <= 0:
        # If so, return the name of the attacking ProfessorTrainer
        print("Professor {}'s Pokemon {} wins!".format(first_attacking_trainer.professor_name,
                                                       first_attacking_pokemon.nickname))

        return first_attacking_trainer.professor_name

    # Second Pokemon attacks
    first_attacking_pokemon.hp -= second_attacking_pokemon.attack()

    # We check if the defending Pokemon has fainted (i.e. health is 0 or below)
    if first_attacking_pokemon.hp <= 0:
        # If so, return the name of the attacking ProfessorTrainer
        print("Professor {}'s Pokemon {} wins!".format(second_attacking_trainer.professor_name,
                                                       second_attacking_pokemon.nickname))

        return second_attacking_trainer.professor_name

    # If neither Pokemon fainted, we don't do anything. We can just let the function end since Winner has a starting
    # value in ultimate_showdown().


def ultimate_showdown(trainer, challenger):
    """
    Creates a deep copy of a random Pokemon object from both ProfessorTrainer object parties, and haves them duke it
    out in the ring as per the instructions in the README. Returns the name of the winning ProfessorTrainer object.

    :param trainer: A ProfessorTrainer object.
    :param challenger: Another ProfessorTrainer object.
    :return: A string.
    """
    # Choose a random Pokemon from both professors and make a copy of it so as to not affect the original.
    trainer_pokemon = deepcopy(trainer.party[randrange(0, len(trainer.party))])
    challender_pokemon = deepcopy(challenger.party[randrange(0, len(challenger.party))])

    print("Professor {} sends out a {} called '{}'!".format(trainer.professor_name, trainer_pokemon.pokemon_name,
                                                            trainer_pokemon.nickname))
    print("Professor {} sends out a {} called '{}'!".format(challenger.professor_name, challender_pokemon.pokemon_name,
                                                            challender_pokemon.nickname), end="\n\n")
    winner = "Nobody"  # starting value for the winner; will be changed below

    # While neither Pokemon's health is 0 or below...
    while trainer_pokemon.hp > 0 and challender_pokemon.hp > 0:
        if trainer_pokemon > challender_pokemon:
            """
            I defined a helper function, move(), so that my code wouldn't be too cluttered. But you didn't have to do 
            this.
            """
            winner = move(trainer, trainer_pokemon, challenger, challender_pokemon)
        elif challender_pokemon > trainer_pokemon:
            winner = move(challenger, challender_pokemon, trainer, trainer_pokemon)
        else:
            # coin toss since they both have the same strength
            if round(random()):
                winner = move(trainer, trainer_pokemon, challenger, challender_pokemon)
            else:
                winner = move(challenger, challender_pokemon, trainer, trainer_pokemon)

    return winner


def main():
    """
    As usual, just some sample behavior. Feel free to try your own. Man, I'll miss you all.
    """
    your_professor = ProfessorTrainer("Darryl Reeves", "save_file_1.csv")
    their_professor = ProfessorTrainer("Gary Oak", "save_file_2.csv")

    winner = ultimate_showdown(your_professor, their_professor)
    print("Professor {} wins the ultimate showdown!".format(winner))


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
