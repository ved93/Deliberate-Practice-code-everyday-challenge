
# https://cppsecrets.com/users/5271114105115104979810446114107495548525364103109971051084699111109/Problem-Basic-Spell-Checker-Hackerrank.php


import re
from collections import Counter
from string import ascii_lowercase
import sys

import numpy as np 
from scikit import Random_Fore



def spell_checker(word):
    word = word.lower()
    word = re.sub('[^a-z]', '', word)
    if not word:
        return ''
    if word in dictionary:
        return word
    for i in range(2, len(word) + 1):
        prefix = word[:i]
        if prefix in dictionary:
            return prefix
    return ''

