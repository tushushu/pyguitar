# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-06 21:08:36
"""
import sys

from pyguitar_tasks import fretboard_identification


def main() -> None:
    args = sys.argv[1:]
    if args and args[0] == '-0':
        fretboard_identification.run()
    else:
        print("""
        Please run `pyguitar -i` instead:
        *********************************
        0 -> Fretboard identification
        *********************************
        """)
