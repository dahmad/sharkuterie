from glob import glob
from random import randint, shuffle
from itertools import product


def get_possible_patterns():
    return list(product('QE', repeat=4))

def get_random_pattern():
    patterns = get_possible_patterns()
    shuffle(patterns)
    return patterns[0]

def get_q(segment, beat_length):
    start = randint(0, int(len(segment) - beat_length))
    end = int(start + beat_length)
    return start, end

def get_e(segment, beat_length):
    return get_q(segment, beat_length / 2)

def get_clips(source_filepath):
    matcher = source_filepath.split('.')[0] + '--'
    return sorted(glob('{0}*mp3'.format(matcher)))