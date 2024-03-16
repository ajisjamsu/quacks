import matplotlib.pyplot as plt
import numpy as np
import random
import logging
import click
from quacks import quacks_pieces as qp

logger = logging.getLogger(__name__)

# Quacks of Quedlinburg probability sim
def main():
    logging.basicConfig(level=logging.INFO)
    logger.info(" Welcome to Quacks of Quedlinburg!")

    p1 = qp.QuacksPlayer("p1")
    while True:
        if click.confirm(f"{p1.name}: Draw a chip?", default=True):
            can_continue_drawing = p1.drawChip()
            if not can_continue_drawing:
                break
        else:
            break


if __name__ == "__main__":
    main()
