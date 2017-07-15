# -*- coding: utf-8 -*-
"""
This module contains the fucntion "record" to capture screenshots of the screen for a given time.
"""

import time
import os
from mss import mss


def prepare():
    path = 'sct2\\'

    print('PREPARING...')

    for filename in os.listdir(path):
        os.remove(path + filename)
# sdagjkl

def record(time_amount):

    for i in range(5)[::-1]:
        print("RECORDING IS ABOUT TO START...%d" % (i + 1))
        time.sleep(1)
    print("RECORDING HAS STARTED - IT WILL AUTOMATICALLY STOP IN %d SECONDS" % (time_amount + 2))

    i = 0
    t_end = time.time() + time_amount + 1

    while time.time() < t_end:
        with mss() as sct:
            mon = {'top': 905, 'left': 0, 'width': 1020, 'height': 25}
            # Save the picture
            output = 'sct2\\sct-' + str(i) + '.png'.format(**mon)
            sct.to_png(sct.get_pixels(mon), output)
            i += 1

    print('RECORDING HAS FINISHED')

    print(i // time_amount)
    print(i)
