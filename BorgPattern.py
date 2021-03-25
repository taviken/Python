class Hive:
    _shared_dict = {}


class Drone(Hive):
    def get(self, item, default=None):
        return self._shared_dict.get(item, default)

    def set(self, key, value):
        self._shared_dict[key] = value

    def assimilate(self, other):
        if hasattr(other, "__dict__"):
            self._shared_dict.update(other.__dict__)


def main():
    class Human:
        def __init__(self, name, rank):
            self.name = name
            self.rank = rank

    picard = Human('picard', 'captain')

    seven_of_nine = Drone()
    seven_of_nine.assimilate(picard)

    hue = Drone()
    print(f'Hue knows this {hue._shared_dict}')


if __name__ == '__main__':
    main()
