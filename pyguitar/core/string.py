# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-02 21:11:03
"""
from .note_name import NoteName


class String:
    def __init__(self, note_name: str) -> None:
        try:
            self._note_name = getattr(NoteName, note_name)
        except AttributeError:
            raise ValueError(
                f"The parameter `note_name` {note_name} is " +
                "invalid, please use 'C', 'D_FLAT', 'F_SHARP'..."
            )

    def __str__(self) -> str:
        return f"{self._note_name.name} string."

    def press_down(self, position: int) -> str:
        return NoteName.add(self._note_name, position).name
