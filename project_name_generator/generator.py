# coding=utf-8

import random
import string

from .adjectives import ADJECTIVES
from .nouns import NOUNS


def generate(words=2, number=False, alliterative=False):
    if alliterative is True:
        alliterative = random.choice(string.ascii_letters)

    raw = []

    for _ in range(words - 1):
        word = _random_word(ADJECTIVES)
        raw.append(word)

    word = _random_word(NOUNS)
    raw.append(word)

    if number:
        word = str(random.randint(1, 9999))
        raw.append(word)

    return {
        'raw': raw,
        'dashed': '-'.join(raw),
        'spaced': ' '.join(raw),
    }


def _random_word(choices, alliterative):
    while True:
        word = random.choice(choices)
        if not alliterative or word[0].lower() == alliterative.lower():
            break
    return word
