import time
from mss import mss


def record(time_amount):
    i = 0
    t_end = time.time() + time_amount + 3
    while time.time() < t_end:
        with mss() as sct:
            # The screen part to capture
            mon = {'top': 905, 'left': 0, 'width': 1020, 'height': 25}

            # Save the picture
            output = 'sct2\\sct-' + str(i) + '.png'.format(**mon)
            sct.to_png(sct.get_pixels(mon), output)
            i += 1
    print(i)
    print('RECORDING HAS FINISHED')
    print(i)
