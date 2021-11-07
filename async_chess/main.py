import asyncio
import random
import itertools

grand_master_sayings = (
    'Hasta la vista, baby',
    'if rooks could kill',
    'your mother',
    'you hang more pawns than a the spanish inquisition!',
    'i sunk your battleship',
    'nobody expects the spanish inquisition',
)

# make moves, just for fun
grid = itertools.product(
    ('Pawn', 'Bishop', 'Knight', 'Rook', 'King', 'Queen'),  # pieces
    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'),  # files
    (1, 2, 3, 4, 5, 6, 7, 8)  # ranks
)
grid_string = list(map(lambda x: f'{x[0]} to {x[1]}{x[2]}', grid))
# note the above string is actually incorrect, pawns cannot ever be rank 1, but this is just for sillyness so perfect


class Player:
    def __init__(self, name: str, skill: int):
        self.name = name
        self.skill = skill
        self.simulated_moves_until_beaten = random.randint(0, skill)

    async def engage_grandmaster(self, grandmaster_damage_inflicted: int):
        # in this demo, a player will play a grand master. the grand master
        # will always win, and the simulated moves is just how many moves before
        # the player is beaten.
        wait_time = 2.0 + random.random() * self.skill
        await asyncio.sleep(wait_time)
        phrase = random.choice(grand_master_sayings)
        print(phrase)  # just for fun!
        self.simulated_moves_until_beaten -= grandmaster_damage_inflicted
        return self.simulated_moves_until_beaten


def main():
    # create players
    bill = Player('Bill', 2)
    joe = Player('Joe', 4)
    bob = Player('Bob', 8)
    ringer = Player('Dvorak', 10)
