import numpy as np
from scipy import misc


def get_image_asarray(path):
    image_asarray = misc.imread(path)
    return image_asarray


def get_data_from_image(image_count):
    white_keys_x = [int(round(10 + 19.32 * x)) for x in range(52)]

    black_keys_x = [20]
    z = 20
    for i in range(7):
        for j in [40, 20, 35, 20, 20]:
            z += j
            black_keys_x.append(z)
    keys = white_keys_x + black_keys_x

    f = open("output.txt", 'w')
    whole_data = []
    count = 0
    taktende_gesetzt = 0
    measure = []
    for i in range(image_count):

        image_asarray = get_image_asarray('sct2\\sct-' + str(i) + '.png')

        data = []
        # check the keys
        y = 14
        for x in keys:
            temp = image_asarray[y, x]

            if (25 <= temp[0] <= 100) and (120 <= temp[1] <= 240) and (100 <= temp[2] <= 180):
                data.append(1)
            elif (50 <= temp[0] <= 130) and (120 <= temp[1] <= 200) and (170 <= temp[2] <= 255):
                data.append(2)
            else:
                data.append(0)

        # check for end of measure
        if np.sum(image_asarray[0:8, 30]) > 20:
            measure.append(data)
            count += 1
            if np.sum(np.asarray(data) == 0) and (taktende_gesetzt == 0):
                # End of measure
                whole_data.append(measure)
                measure = []
            taktende_gesetzt = 1
        else:
            measure.append(data)
            if taktende_gesetzt == 0 and count > 0:
                temp1 = (count // 2) * (-1) + 1
                whole_data.append(measure[:temp1])
                measure = measure[temp1:]
            count = 0
            taktende_gesetzt = 0

        f.write(str(data) + '\n')

    whole_data.append(measure)

    f.close()
    return whole_data
