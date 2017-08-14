# -*- coding: utf-8 -*-
import numpy as np


def summing_up(temp, with_keys):
    # Bezeichnungen der Tasten in ABC-Notation mit Bs
    white_keys = ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1', 'A1', 'B1', 'C2', 'D2', 'E2', 'F2',
                  'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
                  'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6', 'C7', 'D7', 'E7',
                  'F7', 'G7', 'A7', 'B7', 'C8']
    # WICHTIG: Tonart tastaturzusammenstellung mit neuer funktion
    black_keys_b = ['B-0', 'D-1', 'E-1', 'G-1', 'A-1', 'B-1', 'D-2', 'E-2', 'G-2', 'A-2', 'B-2',
                    'D-3', 'E-3', 'G-3', 'A-3', 'B-3', 'D-4', 'E-4', 'G-4', 'A-4', 'B-4', 'D-5', 'E-5', 'G-5', 'A-5',
                    'B-5', 'D-6', 'E-6', 'G-6', 'A-6', 'B-6', 'D-7', 'E-7', 'G-7', 'A-7', 'B-7']
    # Tastaturaufbau = alle weiße Tasteb+ alle schwarze Tasten
    allkeys = white_keys + black_keys_b + ['z']

    typ = temp[0]  # nicht gedrückt, 1: links, 2: rechts
    zaehler = 1  # Die Anzahl aufeinanderfolgender gleichbleibender Typen (rechts, links oder nicht gedrückt
    anzahl = []  # Hier werden Die aufsummierten 0,1,2 einer Taste zwischengespeichet
    #  Format: [Typ,Annzahl] (typ gibt rechts links oder nicht gedrückt an

    for w in range(1, len(temp)):
        if temp[w] == typ:
            zaehler += 1
        else:
            if with_keys == 0:
                anzahl.append((typ, zaehler))
            else:
                anzahl.append((allkeys[typ], zaehler))
            zaehler = 1
            typ = temp[w]
    if with_keys == 0:
        anzahl.append((typ, zaehler))
    else:
        anzahl.append((allkeys[typ], zaehler))

    """for index, tie in enumerate(tones_with_ties[:]):
        tones_with_ties[index] = allkeys[tie]"""

    return anzahl


def voice_merging(sumup_frames, frame_count, voice_nr):

    voices = np.asarray([[88] * frame_count] * 4)  # Länge der Stimmen entspricht der Anzahl der Frames eines Takten

    for index, anzahl in enumerate(sumup_frames):
        # Wenn eine Taste nur einen Zustand hat und der nicht gedrückt ist, muss sie nicht berücksichtigt werden
        if len(anzahl) == 1 and anzahl[0][0] == 0:
            continue
        temp = 0
        """ temp : "Framezeiger", zeigt die Framposition an, an der der nächste aufsummierte Block von Typen startet 
        (wird benötigt um im nächsten Schritt auf Überlappungen mit anderen bereits registrierten Tasten 
        (in vorherigen Schleifendurchläufen) zu prüfen Folgendes Verfahren: Sind in der ersten Stimme die 
        Frames (Positionen), die der nächste aufsummierte Typ belegen würde, als Pause gekennzeichnet (Wert 88)
        wird dieser aufsummierte Typ in diese Stimme geschrieben, anonsten wird jeweils mit 
        der zweiten (oder dritten, vierten) Stimme fortgefahren"""
        for i in anzahl:
            if i[0] == voice_nr:  # (1. Hand, 2. Tonnummer)
                if np.sum(voices[0, temp:temp + i[1]]) == i[1]*88:
                    voices[0, temp:temp + i[1]] = [index]*(i[1])
                elif np.sum(voices[1, temp:temp+i[1]]) == i[1]*88:
                    voices[1, temp:temp + i[1]] = [index]*(i[1])
                elif np.sum(voices[2, temp:temp+i[1]]) == i[1]*88:
                    voices[2, temp:temp + i[1]] = [index] * (i[1])
                elif np.sum(voices[3, temp:temp+i[1]]) == i[1]*88:
                    voices[3, temp:temp + i[1]] = [index] * (i[1])
            temp += (i[1])

    return voices


def analyze_pressed_keys(data):  # Bezieht sich auf einen Takt
    """data is an 2D numpy-array"""

    gesamt = []  # Hier werden die Anzahlen der auf einanderfolgenden 0,1,2 jeder Taste eines Taktes gespeichert
    for index in range(len(data[0])):  # 88 Durchläufe für 88 Tasten
        gesamt.append(summing_up(data[:, index], 0))  # data[:, index]: Selektieren der Typen (0,1,2) von einer Taste

    """Mit vorherigem Beispiel (4 Takte mit jeweils 8 Frames) Variable "gesamt":
        1. Takt: 
        [[(0,8)],[(1,4),(0,4)],[(0,8)],[(0,8)],[(0,4),(1,4)],[(0,8)],[(0,8)],[(0,8)]]
        2. Takt:
        [[(0,8)],[(0,8)],[(0,8)],[(0,8)],[(0,8)],[(1,4),(0,4)],[(2,4),(0,4)],[(0,4),(1,4)]]
        3. Takt:
        [[(0,7)],[(0,7)],[(0,7)],[(0,7)],[(0,7)],[(1,4),(0,3)],[(0,4),(2,3)],[(2,7)]]
        4. Takt:
        [[(0,4),(1,3)],[(1,4),(0,3)],[(0,7)],[(2,4),(0,3)],[(0,4),(2,3)],[(0,7)],[(0,7)],[(0,7)]]
        """

    left_voices = voice_merging(gesamt, len(data[:, 0]), 1)
    right_voices = voice_merging(gesamt, len(data[:, 0]), 2)

    sumup_left = []
    sumup_right = []

    for index in range(4):

        sumup_left.append(summing_up(left_voices[index], 1))
        sumup_right.append(summing_up(right_voices[index], 1))

    return sumup_left, sumup_right


def analyze_for_ties(measure1, next_measure):
    # Bezeichnungen der Tasten in ABC-Notation mit Bs
    white_keys = ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1', 'A1', 'B1', 'C2', 'D2', 'E2', 'F2',
                  'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
                  'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6', 'C7', 'D7', 'E7',
                  'F7', 'G7', 'A7', 'B7', 'C8']
    # WICHTIG: Tonart tastaturzusammenstellung mit neuer funktion
    black_keys_b = ['B-0', 'D-1', 'E-1', 'G-1', 'A-1', 'B-1', 'D-2', 'E-2', 'G-2', 'A-2', 'B-2',
                    'D-3', 'E-3', 'G-3', 'A-3', 'B-3', 'D-4', 'E-4', 'G-4', 'A-4', 'B-4', 'D-5', 'E-5', 'G-5', 'A-5',
                    'B-5', 'D-6', 'E-6', 'G-6', 'A-6', 'B-6', 'D-7', 'E-7', 'G-7', 'A-7', 'B-7']
    # Tastaturaufbau = alle weiße Tasteb+ alle schwarze Tasten
    allkeys = white_keys + black_keys_b + ['z']

    y = len(measure1) // 40
    if y == 0:
        y = 1
    measure_ties = []
    for z in range(88):
        if np.sum(measure1[-y:, z]) == y and np.sum(next_measure[:y, z]) == y:  # 1 Linke Hand
            # measure_number_ties += [[index, z]]  # Hand, Taktnummer, Index
            measure_ties += [allkeys[z]]
            # print(whole_data[index][-y:, z] + whole_data[index+1][:y, z])
            # print(np.sum(whole_data[index][-y:, z]) + np.sum(whole_data[index+1][:y, z]))
        if np.sum(measure1[-y:, z]) == 2 * y and np.sum(next_measure[:y, z]) == y * 2:  # 2 Rechte Hand
            # measure_number_ties += [[index, z]]
            measure_ties += [allkeys[z]]
            # print(whole_data[index][-y:, z] + whole_data[index + 1][:y, z])
            # print(np.sum(whole_data[index][-y:, z]) + np.sum(whole_data[index + 1][:y, z]))
    return measure_ties
