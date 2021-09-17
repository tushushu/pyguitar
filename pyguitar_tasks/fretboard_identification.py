# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-06 20:59:02
"""
from random import randint
from time import sleep
from typing import Optional

import pyguitar as pyg
from pyguitar.utils import Color, speak

_QUIT = False
_SCORE = [0, 0]


class _GameLoop:
    def __init__(self, text: str, kwargs: Optional[dict] = None) -> None:
        self.text = text
        self.kwargs = kwargs if kwargs else dict()

    def parse(self, inputs: str):
        return inputs

    def run(self):
        global _QUIT
        while not _QUIT:
            speak(self.text)
            inputs = input()
            if inputs == 'q':
                _QUIT = True
                break
            else:
                try:
                    return self.parse(inputs, **self.kwargs)
                except:  # noqa
                    speak("Invalid input.")
        return None


class _LowestPosition(_GameLoop):
    def parse(self, inputs: str) -> int:
        low_pos = int(inputs)
        assert 0 <= low_pos <= 12
        return low_pos


class _HighestPosition(_GameLoop):
    def parse(self, inputs: str, low_pos: int) -> int:  # type: ignore
        high_pos = int(inputs)
        assert low_pos <= high_pos <= 12
        return high_pos


class _FretboardIdentification(_GameLoop):
    def parse(self, inputs: str):
        note = pyg.NoteName.name2note(inputs)
        assert hasattr(pyg.NoteName, note)
        return inputs


if __name__ == "__main__":
    # Initialization.
    speak("Welcome to fretboard identification!")
    speak("Initializing guitar fretboard...")
    fretboard = pyg.Fretboard(
        [
            pyg.String(pyg.NoteName.E),
            pyg.String(pyg.NoteName.A),
            pyg.String(pyg.NoteName.D),
            pyg.String(pyg.NoteName.G),
            pyg.String(pyg.NoteName.B),
            pyg.String(pyg.NoteName.E),
        ]
    )

    speak("The guitar tuning is as below:")
    print(fretboard)
    sleep(1.5)
    speak("Input 'q' to quit the game!")

    # Setting.
    speak("Please set the guitar fretboard positions.")
    low_pos: int = _LowestPosition(
        text="Please input the lowest position (0 to 12): ",
    ).run()
    high_pos: int = _HighestPosition(
        text=f"Please input the highest position ({low_pos} to 12): ",
        kwargs={"low_pos": low_pos},
    ).run()

    if not _QUIT:
        speak(
            "Your guitar fretboard position range is from " +
            f"{low_pos} to {high_pos}!"
        )

    # Game.
    if not _QUIT:
        speak("Now let us enjoy the game!")
    while not _QUIT:
        string_num = randint(1, 6)
        fret_num = randint(low_pos, high_pos)
        note_name = _FretboardIdentification(
            text=f"String {string_num} and position {fret_num}: ",
        ).run()

        if _QUIT:
            break

        expected_sharp = fretboard.press_down_string(string_num, fret_num)
        expected_flat = fretboard.press_down_string(
            string_num, fret_num, accidental="flat")
        _SCORE[1] += 1
        if note_name == expected_sharp or note_name == expected_flat:
            Color.speak_green("Correct!")
            _SCORE[0] += 1
        else:
            Color.speak_red("Wrong!")
            if expected_sharp != expected_flat:
                print(
                    f"The correct answer should be {expected_sharp} " +
                    f"or {expected_flat}!"
                )
            else:
                print(f"The correct answer should be {expected_sharp}!")
    if _SCORE[1] != 0:
        speak(f"Your score is {_SCORE[0]} of {_SCORE[1]}!")
    speak("Quitting the game, bye!")
