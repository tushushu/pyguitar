# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-05 17:03:25
"""
from typing import List
from .string import String


class Fretboard:
    def __init__(self, strings: List[String]) -> None:
        """Set the number of strings and pitch of the guitar fretboard.

        Args:
            strings (List[String]): Note name the last to the first string.
        """
        self._strings = strings[::-1]

    def __str__(self) -> str:
        tuning = []
        for string in self._strings:
            tuning.append(string.name)
        return f"{len(self._strings)} strings, tuning is {''.join(tuning)}"

    def press_down_string(self, string_num: int, fret_num: int) -> str:
        return self._strings[string_num - 1].press_down(fret_num)
