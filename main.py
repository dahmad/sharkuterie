from itertools import product
from random import randint, shuffle
from pydub import AudioSegment
from pydub.playback import play
from glob import glob
import argparse
from lib import *


parser = argparse.ArgumentParser(description='')
parser.add_argument('-i', '--input')
parser.add_argument('-b', '--beat_length', type=int, default=800)

args = parser.parse_args()
print(args)

if __name__ == '__main__':
    source_filepath = args.input
    f = AudioSegment.from_file(source_filepath, frame_rate=44100)

    beat_length = args.beat_length # ms

    clips = get_clips(source_filepath)

    while len(clips) < 100:
        try:
            pattern = get_random_pattern()
            s = ''
            segment = AudioSegment.empty()

            for note in pattern:
                if note == 'Q':
                    start, end = get_q(f, beat_length)
                    s += '{0}_{1}-{2}__'.format(note, start, end)
                    segment += f[start:end]
                else:
                    start, end = get_e(f, beat_length)
                    s += '{0}_{1}-{2}__'.format(note, start, end)
                    segment += f[start:end]
                    start, end = get_e(f, beat_length)
                    s += '{0}_{1}-{2}__'.format(note, start, end)
                    segment += f[start:end]

            print('\n{0}\n'.format(s))
            play(segment * 4)

            evaluation = input()
            if evaluation == '1':
                AudioSegment.export(segment, '{0}--{1}.mp3'.format(source_filepath.split('.')[0], s))

            clips = get_clips(source_filepath)
        except:
            pass

