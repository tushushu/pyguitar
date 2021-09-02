# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-02 21:11:03
"""
from enum import Enum


class Pitch(Enum):
    C = 1
    D = 2
    E = 3
    F = 4
    G = 5
    A = 6
    B = 7


class String:
    def __init__(self, pitch: Pitch) -> None:
        self.pitch = pitch

    def __str__(self) -> str:
        return f"String with {self.pitch}"

    def press_down(self, position: int) -> Pitch:
        # TODO
        pass
