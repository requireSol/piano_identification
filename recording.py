# -*- coding: utf-8 -*-
"""
This module contains the fucntion "record" to capture screenshots of the screen for a given time.
"""

import time
import os
import mss
import mss.tools
# ALLE WERTE SIND FÜR ONLINEPIANISTS.COM EINGESTELLT UND AUF DIE WERTE IN image_analyzer.py ABGESTIMMT!

def prepare(path):
    # path = 'sct\\'

    print('PREPARING...')

    for filename in os.listdir(path):
        os.remove(path + filename)


def record(time_amount, path):

    for i in range(5, 1, -1):
        print("RECORDING IS ABOUT TO START...%d" % (i - 1))
        time.sleep(1)
    print("RECORDING HAS STARTED - IT WILL AUTOMATICALLY STOP IN %d SECONDS" % (time_amount + 2))

    i = 0
    t_end = time.time() + time_amount + 1

    while time.time() < t_end:
        with mss.mss() as sct:
            mon = {'top': 905, 'left': 0, 'width': 1020, 'height': 25}  # Individual values !
            # Save the picture
            output = path + 'sct-' + str(i) + '.png'.format(**mon)
            sct_img = sct.grab(mon)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output)

            i += 1

    print('RECORDING HAS FINISHED')

    print('AVERAGE FPS: ' + str(i // time_amount))
    print('COUNT OF IMAGES: ' + str(i))
