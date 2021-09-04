# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-02 21:11:03
"""
from .pitch import Pitch


class String:
    def __init__(self, pitch: Pitch) -> None:
        self.pitch = pitch

    def __str__(self) -> str:
        return f"String with {self.pitch}"

    def press_down(self, position: int) -> Pitch:
        # TODO
        pass
