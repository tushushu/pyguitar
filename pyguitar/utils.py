# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-11 15:51:41
"""
import os
from enum import Enum


def speak(text: str, print_text: bool = True) -> None:
    if print_text:
        print(text)
    os.system(f"say '{text}'")


class Color(str, Enum):
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

    @classmethod
    def _print(cls, text: str, color: 'Color') -> None:
        print(color + text + cls.RESET)

    @classmethod
    def print_red(cls, text: str) -> None:
        cls._print(text, cls.RED)

    @classmethod
    def print_green(cls, text: str) -> None:
        cls._print(text, cls.GREEN)
