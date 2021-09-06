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
        for string in strings:
            assert isinstance(string, String)
        self._strings = strings[::-1]

    def __str__(self) -> str:
        tuning = []
        for string in self._strings:
            tuning.append(string.name)
        return "****<Fretboard object>****\n" + \
            f"----Number of strings -> {len(self._strings)}\n" + \
            f"----Tuning -> {''.join(tuning[::-1])}"

    def press_down_string(self, string_num: int, fret_num: int) -> str:
        assert 0 < string_num < len(self._strings) + 1
        return self._strings[string_num - 1].press_down(fret_num)
