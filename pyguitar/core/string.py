# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-02 21:11:03
"""
from .note_name import NoteName


class String:
    def __init__(self, note_name: NoteName, accidental: str = "sharp") -> None:
        self._note_name = note_name
        self._accidental = accidental

    def __str__(self) -> str:
        return f"{self._note_name.name} string."

    def press_down(self, position: int) -> str:
        name = NoteName.add(self._note_name, position, self._accidental).name
        return self._format_name(name)

    @property
    def name(self) -> str:
        name = self._note_name.name
        return self._format_name(name)

    def _format_name(self, name: str) -> str:
        return name.replace("_FLAT", "♭").replace("_SHARP", "#")
