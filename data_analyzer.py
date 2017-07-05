import numpy as np


def analyze_pressed_keys(data):
    # phase 1  SUMMING UP KEYS
    gesamt = []
    for index in range(len(data[0])-1):
        temp = data[:, index]
        typ = temp[0]
        zaehler = 1
        anzahl = []
        for w in range(1, len(temp)):
            if temp[w] == typ:
                zaehler += 1
            else:
                anzahl.append([typ, zaehler])
                zaehler = 1
                typ = temp[w]
        anzahl.append([typ, zaehler])
        gesamt.append(anzahl)

        # phase 2 VOICE-MERGING (hardcoded) dynamic coding possible
    left_voices = np.asarray([[88]*len(data[:, 0])] * 4)
    right_voices = np.asarray([[88]*len(data[:, 0])] * 4)
    for index, anzahl in enumerate(gesamt):
        if len(anzahl) == 1:
            continue
        temp = 0
        for i in anzahl:
            if i[0] == 1:  # (1. Hand, 2. Tonnummer)
                if np.sum(left_voices[0, temp:temp+i[1]]) == i[1]*88:
                    left_voices[0, temp:temp + i[1]] = [index]*(i[1])
                elif np.sum(left_voices[1, temp:temp + i[1]]) == i[1]*88:
                    left_voices[1, temp:temp + i[1]] = [index]*(i[1])
                elif np.sum(left_voices[2, temp:temp + i[1]]) == i[1]*88:
                    left_voices[2, temp:temp + i[1]] = [index] * (i[1])
                elif np.sum(left_voices[3, temp:temp + i[1]]) == i[1]*88:
                    left_voices[3, temp:temp + i[1]] = [index] * (i[1])
            temp += (i[1])

    for index, anzahl in enumerate(gesamt):
        if len(anzahl) == 1:
            continue
        temp = 0
        for i in anzahl:
            if i[0] == 2:  # (1. Hand, 2. Tonnummer)
                if np.sum(right_voices[0, temp:temp + i[1]]) == i[1]*88:
                    right_voices[0, temp:temp + i[1]] = [index]*(i[1])
                elif np.sum(right_voices[1, temp:temp+i[1]]) == i[1]*88:
                    right_voices[1, temp:temp + i[1]] = [index]*(i[1])
                elif np.sum(right_voices[2, temp:temp+i[1]]) == i[1]*88:
                    right_voices[2, temp:temp + i[1]] = [index] * (i[1])
                elif np.sum(right_voices[3, temp:temp+i[1]]) == i[1]*88:
                    right_voices[3, temp:temp + i[1]] = [index] * (i[1])
            temp += (i[1])

    white_keys = ['A,,,,','B,,,,','C,,,','D,,,','E,,,','F,,,','G,,,','A,,,','B,,,','C,,','D,,','E,,','F,,','G,,','A,,','B,,','C,','D,','E,','F,','G,','A,','B,','C','D','E','F','G','A','B','c','d','e','f','g','a','b',"c'","d'","e'","f'","g'","a'","b'","c''","d''","e''","f''","g''","a''","b''","c'''"]
    # WICHTIG: Tonart tastaturzusammenstellung mit neuer funktion
    black_keys_b = ['_B,,,,','_D,,,','_E,,,','_G,,,','_A,,,','_B,,,','_D,,','_E,,','_G,,','_A,,','_B,,','_D,','_E,','_G,','_A,','_B,','_D','_E','_G','_A','_B','_d','_e','_g','_a','_b',"_d'","_e'","_g'","_a'","_b'","_d''","_e''","_g''","_a''","_b''"]

    allkeys = white_keys + black_keys_b + ['z']

    sumup_left = []
    for index in range(4):
        temp = left_voices[index]
        typ = temp[0]
        zaehler = 1
        anzahl = []
        for w in range(1, len(temp)):
            if temp[w] == typ:
                zaehler += 1
            else:
                anzahl.append((allkeys[typ], zaehler))
                zaehler = 1
                typ = temp[w]
        anzahl.append((allkeys[typ], zaehler))
        sumup_left.append(anzahl)

    sumup_right = []
    for index in range(4):
        temp = right_voices[index]
        typ = temp[0]
        zaehler = 1
        anzahl = []
        for w in range(1, len(temp)):
            if temp[w] == typ:
                zaehler += 1
            else:
                anzahl.append((allkeys[typ], zaehler))
                zaehler = 1
                typ = temp[w]
        anzahl.append((allkeys[typ], zaehler))
        sumup_right.append(anzahl)

    return sumup_left, sumup_right
