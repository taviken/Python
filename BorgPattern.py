"""Demonstration of the Borg pattern. Alternative solution to the singleton Pattern."""


class Hive:
    """Base Class. Contains a shared dict which all subclasses have access to."""
    _shared_dict = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_dict


class Drone(Hive):
    """Subclass that can consume other objects that have the '__dict__' attribute."""

    def get(self, item: str, default: object = None) -> object:
        """Retrieves object from shared dict, returns None if not found, or a default value that can be passed in."""
        return self.__dict__.get(item, default)

    def set(self, key: str, value: object) -> None:
        """Sets a key value pair within the shared dict. Overwrites previous values of equal key."""
        self.__dict__[key] = value

    def assimilate(self, other: object, designation: str) -> None:
        """Copies the '__dict__' of an object passed in if the object contains said attribute. Ignores otherwise"""
        if hasattr(other, "__dict__"):
            self.set(designation, other.__dict__)

    def __init__(self) -> None:
        super().__init__()
        self.__dict__ = self._shared_dict

    def __iter__(self) -> tuple:
        """Yields key value tuple of the shared dict"""
        for k, v in self.__dict__.items():
            yield k, v


def main():
    class Human:
        """Test object for demonstration purposes."""

        def __init__(self, name, rank):
            """Creates an instance of a Human object. Requires 'name','rank' parameters"""
            self.name = name
            self.rank = rank

    picard = Human('picard', 'captain')

    seven_of_nine = Drone()
    seven_of_nine.assimilate(picard, 'Locutus')

    hue = Drone()
    print(f'Hue knows the following:\n {list(hue)}')


if __name__ == '__main__':
    main()
