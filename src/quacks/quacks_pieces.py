import matplotlib.pyplot as plt
import numpy as np
import random
import logging
from enum import Enum

logger = logging.getLogger(__name__)
# class syntax
class ChipColor(Enum):
    BOMB = 1
    ORANGE = 2
    GREEN = 3
    RED = 4
    BLUE = 5
    BLACK = 6
    YELLOW = 7
    PURPLE = 8

# Quacks of Quedlinburg probability sim
class QuacksChip:
    def __init__(self, color: ChipColor, value=0):
        self.color = color
        self.value = value

    def __str__(self):
        if self.color == ChipColor.BOMB:
            return f"bomb {self.value}-chip"
        else:
            # TODO: colors of chip
            return f"benign {self.value}-chip"


class QuacksBag:
    def __init__(self):
        self.chips = []
        self.chips_backup = []

        # Add bad chips
        self.add(ChipColor.BOMB, 3)
        self.add(ChipColor.BOMB, 2, quantity=2)
        self.add(ChipColor.BOMB, 1, quantity=4)
        self.add(ChipColor.ORANGE, 1)
        self.add(ChipColor.GREEN, 1)

    def add(self, good, value, quantity=1):
        chip = QuacksChip(good, value)
        for i in range(quantity):
            self.chips.append(chip)
        self.chips_backup = self.chips

    def draw(self):
        '''
        @brief Draw a @ref QuacksChip from the bag

        @return The drawn chip
        '''
        chip_idx = random.randint(0, len(self.chips)-1)
        return self.chips.pop(chip_idx)

    def reset(self):
        self.chips = self.chips_backup

    def num_bombs(self):
        return len([chip for chip in self.chips if chip.color == ChipColor.BOMB])

    def status(self):
        logger.info(f" Bombs/total pieces: {self.num_bombs()}/{len(self.chips)}")


class QuacksPot:
    def __init__(self):
        self.placed_chips = []
        self.bomb_count = 0
        self.limit = 7
        self.pot_count = 0

    def place(self, chip):
        '''
        @brief Draw a @ref QuacksChip from the bag

        @return True if the pot has not exploded. False if it has
        '''
        self.placed_chips.append(chip)
        self.pot_count = self.pot_count + chip.value
        if chip.color == ChipColor.BOMB:
            self.bomb_count = self.bomb_count + chip.value
        return self.bomb_count <= self.limit

class QuacksPlayer:
    def __init__(self, player_name):
        self.name = player_name
        self.bag = QuacksBag()
        self.pot = QuacksPot()
        self.unexploded = True

    def drawChip(self):
        '''
        @brief Draw a chip from a player's own bag

        @return True if the player can continue drawing after. 
                False if the player cannot (out of chips/exploded)
        '''
        chip = self.bag.draw()
        self.unexploded = self.pot.place(chip)
        self.status(chip)
        return (len(self.bag.chips) > 0 and self.unexploded)

    def ex_chance(self):
        # Calculate explosion chance for next roll
        bomb_remaining = self.pot.limit - self.pot.bomb_count
        total_chips = len(self.bag.chips)
        explode_chips = len([chip for chip in self.bag.chips
                            if chip.value > bomb_remaining 
                            and chip.color == ChipColor.BOMB])
        return explode_chips / total_chips

    def status(self, chip=None):
        if chip:
            logger.info(f" Just drew a {chip}!")
        exp_status = "" if self.unexploded else "(EXPLODED)"
        logger.info(f" {self.name}'s pot progress: {self.pot.pot_count} spaces {exp_status}")
        logger.info(f" Bomb count: {self.pot.bomb_count}/{self.pot.limit}")
        logger.info(f" Explosion chance: {round(self.ex_chance()*100, 2)}%")
        self.bag.status()
        return

