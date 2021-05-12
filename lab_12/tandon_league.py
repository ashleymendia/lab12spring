class Pokemon:
    def __init__(self):
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
        pass

    def attack(self):
        """
        Using "helper" method _will_land_critical_hit, returns attack value of Pokemon based on the critical hit chances
        explained by the README.

        Critical hit multiplier = (2L + 5) / (L + 5), where L is the Pokemon's level attribute.

        :return: Either the Pokemon's attack stat or the attack stat multiplied by the critical hit multiplier.
        """
        pass

    def _will_land_critical_hit(self):
        """
        A "helper" method that determines whether a Pokemon will land a critical hit.

        :return: True/False
        """
        pass

    def __str__(self):
        """
        Creates and returns a string representation of the Pokemon object.

        :return: A string.
        """
        pass

    def __gt__(self):
        pass


class ProfessorTrainer:
    def __init__(self):
        """
        The constructor of the ProfessorTrainer class.

        :param professor_name: A string containing the name of the professor.
        :param filepath: A string denoting the file path and name containing the professor's Pokemon's information.
        """
        pass

    def _load_pokemon(self):
        """
        A "helper" method that reads a file and populates the ProfessorTrainer's party attribute with Pokemon objects
        created from the information in the file.

        :param filepath: The path of the file to be read, in string form.
        :return: None.
        """
        pass

    def __str__(self):
        """
        Creates and returns a string representation of the Professor object.

        :return: A string.
        """
        pass


def ultimate_showdown():
    """
    Creates a deep copy of a random Pokemon object from both ProfessorTrainer object parties, and haves them duke it
    out in the ring as per the instructions in the README. Returns the name of the winning ProfessorTrainer object.

    :param trainer: A ProfessorTrainer object.
    :param challenger: Another ProfessorTrainer object.
    :return: A string.
    """
    pass


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
