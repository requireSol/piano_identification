from scipy import misc
import numpy as np


def convert_images_to_textfile(image_count, path):
    white_keys_x = [int(round(10 + 19.32 * x)) for x in range(52)] #Referenzpixel für die weißen Tasten

    black_keys_x = [20] #Referenzpixel für die schwarzen Tasten
    z = 20
    for i in range(7):
        for j in [40, 20, 35, 20, 20]:
            z += j
            black_keys_x.append(z)
    keys = white_keys_x + black_keys_x

    f = open("output.txt", 'w')

    for i in range(image_count):
        image_asarray = misc.imread(path + 'sct-' + str(i) + '.png')
        # image_asarray = get_image_asarray('sct2\\sct-' + str(i) + '.png')

        data = []
        # check the keys
        if image_asarray[17, 4][0] < 100 and image_asarray[11, 4][1] < 100 and image_asarray[11, 4][2] < 100:
            continue
        y = 14
        for x in keys: # Den Status jeder Taste anhand eines Pixels jeder Taste überprüfen
            temp = image_asarray[y, x]

            if (25 <= temp[0] <= 100) and (120 <= temp[1] <= 240) and (100 <= temp[2] <= 180):
                data.append(1) #Taste in der linken Hand
            elif (50 <= temp[0] <= 130) and (120 <= temp[1] <= 200) and (170 <= temp[2] <= 255):
                data.append(2) #Taste in der rechten Hand
            else:
                data.append(0) #Taste nicht gedrückt

            f.write(str(data[-1]))
        # check for end of measure
        if np.sum(image_asarray[0:8, 30]) > 20: #Wenn an dieser Stelle graue Pixel snstatt schwarzen Pixel sind, kann es sich um ein Taktende handeln
            f.write('4')
        else:
            f.write('3')

        f.write('\n')

