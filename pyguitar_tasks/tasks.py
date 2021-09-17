# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-06 21:08:36
"""
from typing import List
from typing import Optional

from pyguitar_tasks import fretboard_identification


def main(argv: Optional[List[str]] = None) -> None:
    if argv is not None and argv[0] == '-0':
        fretboard_identification.run()
    else:
        print("""
        Please run `pyguitar -i` instead:
        *********************************
        0 -> Fretboard identification
        *********************************
        """)
