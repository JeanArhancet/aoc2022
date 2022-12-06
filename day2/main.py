from enum import Enum
from typing import List


class RockPaperOpponent(str, Enum):
    ROCK = ("A",)
    PAPER = ("B",)
    SCISSORS = ("C",)


class RockPaperMe(str, Enum):
    ROCK = ("X",)
    PAPER = ("Y",)
    SCISSORS = ("Z",)


class RockPaperStatus(str, Enum):
    LOOSE = ("X",)
    TIE = ("Y",)
    WIN = ("Z",)


class RockPaperValue(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


WIN = 6
LOOSE = 0
TIE = 3


def day2_1():
    score = 0
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            opponent, me = line.split()
            me_rock_paper = RockPaperMe(me)
            opponent_rock_paper = RockPaperOpponent(opponent)
            if (
                (
                    me_rock_paper == RockPaperMe.ROCK
                    and opponent_rock_paper == RockPaperOpponent.ROCK
                )
                or (
                    me_rock_paper == RockPaperMe.PAPER
                    and opponent_rock_paper == RockPaperOpponent.PAPER
                )
                or (
                    me_rock_paper == RockPaperMe.SCISSORS
                    and opponent_rock_paper == RockPaperOpponent.SCISSORS
                )
            ):
                score += TIE + RockPaperValue[me_rock_paper.name].value
            elif (
                (
                    me_rock_paper == RockPaperMe.ROCK
                    and opponent_rock_paper == RockPaperOpponent.SCISSORS
                )
                or (
                    me_rock_paper == RockPaperMe.SCISSORS
                    and opponent_rock_paper == RockPaperOpponent.PAPER
                )
                or (
                    me_rock_paper == RockPaperMe.PAPER
                    and opponent_rock_paper == RockPaperOpponent.ROCK
                )
            ):
                score += WIN + RockPaperValue[me_rock_paper.name].value
            else:
                score += RockPaperValue[me_rock_paper.name].value
    return score


def day2_2():
    score = 0
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            opponent, me = line.split()
            me_rock_paper = RockPaperMe(me)
            opponent_rock_paper = RockPaperOpponent(opponent)
            if RockPaperStatus(me) == RockPaperStatus.TIE:
                score += TIE + RockPaperValue[opponent_rock_paper.name].value
            elif RockPaperStatus(me) == RockPaperStatus.WIN:
                if opponent_rock_paper == RockPaperOpponent.PAPER:
                    me_rock_paper = RockPaperMe.SCISSORS
                elif opponent_rock_paper == RockPaperOpponent.ROCK:
                    me_rock_paper = RockPaperMe.PAPER
                else:
                    me_rock_paper = RockPaperMe.ROCK
                score += WIN + RockPaperValue[me_rock_paper.name].value
            else:
                if opponent_rock_paper == RockPaperOpponent.PAPER:
                    me_rock_paper = RockPaperMe.ROCK
                elif opponent_rock_paper == RockPaperOpponent.ROCK:
                    me_rock_paper = RockPaperMe.SCISSORS
                else:
                    me_rock_paper = RockPaperMe.PAPER
                score += RockPaperValue[me_rock_paper.name].value
    return score


if __name__ == "__main__":
    print(day2_1())
    print(day2_2())
