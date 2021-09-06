# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-04 15:11:14


References:
[1] https://en.wikipedia.org/wiki/Musical_note
[2] https://en.wikipedia.org/wiki/Pitch_class
[3] https://en.wikipedia.org/wiki/Accidental_(music)
"""


from enum import IntEnum


_MAP_SHARP = {
    1: "C",
    2: "C_SHARP",
    3: "D",
    4: "D_SHARP",
    5: "E",
    6: "F",
    7: "F_SHARP",
    8: "G",
    9: "G_SHARP",
    10: "A",
    11: "A_SHARP",
    12: "B",
}

_MAP_FLAT = {
    1: "C",
    2: "D_FLAT",
    3: "D",
    4: "E_FLAT",
    5: "E",
    6: "F",
    7: "G_FLAT",
    8: "G",
    9: "A_FLAT",
    10: "A",
    11: "B_FLAT",
    12: "B",
}


class NoteName(IntEnum):
    """
    In European music theory, most countries use the solfège naming convention
    do–re–mi–fa–sol–la–si. However, in English- and Dutch-speaking regions,
    pitch classes are typically represented by the first seven letters of the
    Latin alphabet (A, B, C, D, E, F and G).

    Letter names are modified by the accidentals. The sharp sign ♯ raises a
    note by a semitone or half-step, and a flat ♭ lowers it by the same amount.
    The accidentals are written after the note name: so, for example, F♯
    represents F-sharp, B♭ is B-flat, and C♮ is C natural (or C).
    """
    C = 1
    C_SHARP = 2
    D_FLAT = 2
    D = 3
    D_SHARP = 4
    E_FLAT = 4
    E = 5
    F = 6
    F_SHARP = 7
    G_FLAT = 7
    G = 8
    G_SHARP = 9
    A_FLAT = 9
    A = 10
    A_SHARP = 11
    B_FLAT = 11
    B = 12

    @classmethod
    def _num2note(cls, val: int, accidental: str) -> str:
        if accidental == "sharp":
            note_name = _MAP_SHARP[val]
        elif accidental == "flat":
            note_name = _MAP_FLAT[val]
        else:
            raise ValueError("Parameter `accidental` should be either" +
                             "'sharp' or 'flat'")
        return note_name

    @classmethod
    def add(cls, note: "NoteName", num: int, accidental: str) -> "NoteName":
        val = (note.value + num) % 12
        if val == 0:
            val = 12
        note_name = cls._num2note(val, accidental)
        return getattr(cls, note_name)

    @classmethod
    def sub(cls, note: "NoteName", num: int, accidental: str) -> "NoteName":
        return cls.add(note, -num, accidental)
