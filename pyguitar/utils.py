# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-09-11 15:51:41
"""
import os


def speak(text: str, print_text: bool = True) -> None:
    if print_text:
        print(text)
    os.system(f"say '{text}'")
