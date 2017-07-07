# -*- coding: utf-8 -*-
import numpy as np


def analyze_pressed_keys(data): #Bezieht sich auf einen Takt
    """data is an 2D numpy-array"""
    # phase 1  SUMMING UP KEYS
    # print(len(data[0]))
    # print(data)

    gesamt = [] #Hier werden die Anzahlen der auf einanderfolgenden 0,1,2 jeder Taste eines Taktes gespeichert
    for index in range(len(data[0])): #88 Durchläufe für 88 Tasten
        # print(len(data[0]))
        temp = data[:, index] #Selektieren der Typen (0,1,2) von der jeweiligen Taste
        typ = temp[0] #0: nicht gedrückt, 1: links, 2: rechts
        zaehler = 1 #Die Anzahl aufeinanderfolgender gleichbleibender Typen (rechts, links oder nicht gedrückt
        anzahl = [] #Hier werden Die aufsummierten 0,1,2 einer Taste zwischengespeichet. Format: [Typ,Annzahl] (typ gibt rechts links oder nicht gedrückt an
        for w in range(1, len(temp)):
            if temp[w] == typ:
                zaehler += 1
            else:
                anzahl.append((typ, zaehler))
                zaehler = 1
                typ = temp[w]

        anzahl.append((typ, zaehler)) #Summe gleicher aufeinanderfolgender Typen wird zur Übersicht der jeweiligen Taste in einem Takt hinzugefügt
        gesamt.append(anzahl) #Aufsummierten Werte einer Taste für einen ganzen Takt werden gespeichert
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
        # phase 2 VOICE-MERGING Es gibt momentan noch 88 "Stimmen" weil es 88 Tasten gibt. Dies wird vorerst auf 4 reduziert
    left_voices = np.asarray([[88]*len(data[:, 0])] * 4) #Array enthält vier Stimmen der linken Hand, die nacheinander gefüllt werden
    # Länge der Stimmen entspricht der Anzahl der Frames eines Takten
    right_voices = np.asarray([[88]*len(data[:, 0])] * 4) #Array enthält vier Stimmen der rechten Hand, die nacheinander gefüllt werden
    # Länge der Stimmen entspricht der Anzahl der Frames eines Takten
    for index, anzahl in enumerate(gesamt):
        if len(anzahl) == 1 and anzahl[0][0] == 0: #Wenn eine Taste nur einen Zustand hat und der nicht gedrückt ist, muss sie nicht berücksichtigt werden
            continue
        temp = 0 #"Framezeiger", zeigt die Framposition an, an der der nächste aufsummierte Block von Typen startet (wird benötigt um im nächsten Schritt auf...
        # ...Überlappungen mit anderen bereits registrierten Tasten (in vorherigen Schleifendurchläufen) zu prüfen
        #Folgendes Verfahren:
        #Sind in der ersten Stimme die Frames (Positionen), die der nächste aufsummierte Typ belegen würde, als Pause gekennzeichnet
        #  (Wert 88) wird dieser aufsummierte Typ in diese Stimme geschrieben, anonsten wird jeweils mit der zweiten (oder dritten, vierten) Stimme fortgefahren

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

    #Gleiches Verfahren wie bei linker Hand
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
    #Bezeichnungen der Tasten in ABC-Notation mit Bs
    white_keys = ['A,,,,','B,,,,','C,,,','D,,,','E,,,','F,,,','G,,,','A,,,','B,,,','C,,','D,,','E,,','F,,','G,,','A,,','B,,','C,','D,','E,','F,','G,','A,','B,','C','D','E','F','G','A','B','c','d','e','f','g','a','b',"c'","d'","e'","f'","g'","a'","b'","c''","d''","e''","f''","g''","a''","b''","c'''"]
    # WICHTIG: Tonart tastaturzusammenstellung mit neuer funktion
    black_keys_b = ['_B,,,,','_D,,,','_E,,,','_G,,,','_A,,,','_B,,,','_D,,','_E,,','_G,,','_A,,','_B,,','_D,','_E,','_G,','_A,','_B,','_D','_E','_G','_A','_B','_d','_e','_g','_a','_b',"_d'","_e'","_g'","_a'","_b'","_d''","_e''","_g''","_a''","_b''"]
    #Tastaturaufbau = alle weiße Tasteb+ alle schwarze Tasten
    allkeys = white_keys + black_keys_b + ['z']

    #Gleiches Vorgehen wie oben, diesmal müssen die gleichen aufeinanderfolgenden Töne in jeder Stimme aufsuummiert werden TODO: Auslagern in Funktion?
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
