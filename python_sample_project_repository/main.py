# This is a sample Python script.
# It facilitates the example tests in test_main.py.
# In PyCharm:
# Press Shift+F10 to execute the code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Greeting:
    """
    This is a minimal class that holds a greeting comprised of a
      person's name and an adjective describing how it is to see them.
      Obviously this is a weird way to implement it, but it helps
      with the example tests in tests/test_main.py!
    """

    def __init__(self, name: str, adjective: str):
        """
        :param name: someone's name
        :param adjective: how it is to see them
        """
        self.name = name
        self.adjective = adjective

    def tostring(self) -> str:
        """
        Return a minimal greeting in the form of a string based on self.name
          and self.adjective
        """
        return f"Hi, {self.name}. It's {self.adjective} to see you."


def sayhello(name: str = "friend", adjective: str = "good") -> None:
    """
    Print a greeting for someone, including their name and how it
      is to see them, making use of the Greeting class
    :param name: someone's name
    :param adjective: how it is to see the person
    :return: None
    """
    print(Greeting(name, adjective).tostring())


# TODO: you can note items that need to be done like this
# FIXME: or like this

# Press the green button in the gutter to run the script.
# Code blocks with pragma: co cover comments won't be tested
if __name__ == "__main__":  # pragma: no cover
    print(Greeting("PyCharm", "delightful").tostring())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
