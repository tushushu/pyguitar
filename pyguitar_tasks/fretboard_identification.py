# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-06 20:59:02
"""
import pyguitar as pyg
from pyguitar.utils import speak


if __name__ == "__main__":
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
    while True:
        print("Press 'q' to quit the game!")
        inputs = input()
        if inputs == 'q':
            break
    speak("Quiting the game, bye!")
