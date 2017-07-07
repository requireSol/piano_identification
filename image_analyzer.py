# -*- coding: utf-8 -*-
import numpy as np
from scipy import misc


def get_data_from_image(image_count):
    white_keys_x = [int(round(10 + 19.32 * x)) for x in range(52)] #Referenzpixel für die weißen Tasten

    black_keys_x = [20] #Referenzpixel für die schwarzen Tasten
    z = 20
    for i in range(7):
        for j in [40, 20, 35, 20, 20]:
            z += j
            black_keys_x.append(z)
    keys = white_keys_x + black_keys_x

    f = open("output.txt", 'w')
    whole_data = [] # Es werden dort alle Takte in einer Liste gespeichert, die jeweils eine Liste über den Status aller Tasten eines Frames enthalten (1 /2 gedrückt, 0 nicht gedrückt
    """Beispiel: Diese(im Beispiel gibt es statt 88 Tasten nur 8, weshalb eine Frameliste die Länge von 8 hat)
    [[[0 1 0 0 0 0 0 0] [0 1 0 0 0 0 0 0] [0 1 0 0 0 0 0 0] [0 1 0 0 0 0 0 0] [0 0 0 0 1 0 0 0] [0 0 0 0 1 0 0 0] [0 0 0 0 1 0 0 0] [0 0 0 0 1 0 0 0]], #1. Takt besteht aus 8 Frames
     [[0 0 0 0 0 1 2 0] [0 0 0 0 0 1 2 0] [0 0 0 0 0 1 2 0] [0 0 0 0 0 1 2 0] [0 0 0 0 0 0 0 1] [0 0 0 0 0 0 0 1] [0 0 0 0 0 0 0 1] [0 0 0 0 0 0 0 1]], #2. Takt besteht aus 8 Frames
     [[0 0 0 0 0 1 0 2] [0 0 0 0 0 1 0 2] [0 0 0 0 0 1 0 2] [0 0 0 0 0 1 0 2] [0 1 0 0 0 0 2 2] [0 1 0 0 0 0 2 2] [0 1 0 0 0 0 2 2]],                   #3. Takt besteht aus 7 Frames
     [[0 1 0 2 0 0 0 0] [0 1 0 2 0 0 0 0] [0 1 0 2 0 0 0 0] [0 1 0 2 0 0 0 0] [1 0 0 0 2 0 0 0] [1 0 0 0 2 0 0 0] [1 0 0 0 2 0 0 0]]]                   #4. Takt besteht aus 7 Frames
    """
    count = 0
    taktende_gesetzt = 0  # Wenn ein Taktende erkannt worden ist, wird das hier vermerkt (0 kein Taktende gesetzt, 1 Taktende gesetzt)
    measure = []  # Hier wird ein Takt zwischengespeichert, bevor er zu den gesamten Daten ergänzt wird
    for i in range(image_count):
        image_asarray = misc.imread('sct2\\sct-' + str(i) + '.png')
        # image_asarray = get_image_asarray('sct2\\sct-' + str(i) + '.png')

        data = []
        # check the keys
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
            measure.append(data) #Frame wird zum Takt hinzugefügt
            count += 1 # Counter für mögliche Taktende Frames inkrementieren
            if np.sum(np.asarray(data) == 0) and (taktende_gesetzt == 0): #Wenn gerade keine Tasten gedrückt werden Taktende noch nicht gesetzt worden ist, wird es jetzt gesetzt
                # End of measure
                whole_data.append(np.asarray(measure)) #Takt zu den gesamten Daten hinzufügen
                measure = [] #Neuer Takt wird dann erstellt
                taktende_gesetzt = 1 #
        else:
            measure.append(data) #Frame wird zum Takt hinzugefügt ###TODO Übergebunden Flag oder sowas
            if taktende_gesetzt == 0 and count > 0: #Falls oben kein Taktende gesetzt wurde, weil es keinen Frame gab, der hellgraue Pixel entält und in dem keine Tasten gedrückt waren
                temp1 = (count // 2) * (-1) + 1 #In diesem Fall der Mittlere der Frames genommen, der graue Pixel für ein Taktende entählt
                whole_data.append(np.asarray(measure[:temp1])) #Dementsprechend wird dieser Teil als Takt zu den gesamten Daten hinzugefügt
                measure = measure[temp1:] #Der neue Takt enthält bereits die restlichen Frames, die nicht mehr zum vorherigen Takt gehören
            count = 0 #Zähler für mögliche Taktstriche wird zurückgesetzt, da neuer Takt anfängt
            taktende_gesetzt = 0 #Neuer Takt hat angefangen, es muss noch ein Taktende irgendwann gesetzt werden

        f.write('\n')

    whole_data.append(np.asarray(measure)) #Rest nach dem Taktende des vorletzten Takt wird hinzugefügt, auch wenn es kein extra Taktende gibt

    f.close()
    return whole_data
