from random import randint
from collections import Counter
from datetime import datetime as dt

DEBUG = 1


class Player():
    def __init__(self, name: str, score: int = 0):
        self.name = name
        self.score = score
        self.current_roll = []


class Game():
    def __init__(self, players: int, npcs: int, turnorder: list = []):
        self.players = players
        self.npcs = npcs
        self.turnorder = turnorder


def log(msg: str):
    if DEBUG == 1:
        print(f'{dt.now().isoformat()}: {msg}')


def roll(roll: int, special: bool = False):
    if roll is not None and roll in range(1,7):
        if roll == 1:
            # 10 points
            log('Roll: 10')
        if roll == 2:
            # 2 stars
            log('Roll: 2-stars')
        if roll == 3:
            # 3 triangles or wild sun if special
            log('Roll: Wild Sun' if special else 'Roll: 3-stars')
            roll = 0 if special else 3
        if roll == 4:
            # 4 lighting bolts
            log('Roll: 4-lightingbolts')
        if roll == 5:
            # 5 points
            log('Roll: 5')
        if roll == 6:
            # 6 stars
            log('Roll: 6-stars')
    else:
        raise Exception('func::roll: Roll was not within 1-6')
    
    return roll


def find_duplicates(roll: list):
    counts = Counter(roll)
    return [(count, item) for item, count in counts.items() if count > 1]


def interpret_roll(roll: list):
    if len(roll) < 1 or len(roll) > 5:
        raise Exception('func::interpret_roll: Roll is out of bounds')
    if len(roll) != len(set(roll)):
        dupes = find_duplicates(roll)
        log(f'Duplicates Found in current roll - {dupes}')


def main():
    player_rolls = []
    current_roll = []
    dice_to_roll = 5
    
    for i in range(1,dice_to_roll+1):
        current_roll.append(roll(randint(1,6)))
    
    player_rolls.append(current_roll)
    interpret_roll(current_roll)

    log(f'Player Rolls: {player_rolls}')

if __name__ == '__main__':
    main()
