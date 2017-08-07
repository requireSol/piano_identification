# -*- coding: utf-8 -*-
import data_analyzer as d_a
import calculate_measure as c_m
import image_analyzer as i_a
import numpy as np
import os


def creating_abc_notation(path):
    white_keys = ['A,,,,', 'B,,,,', 'C,,,', 'D,,,', 'E,,,', 'F,,,', 'G,,,', 'A,,,', 'B,,,', 'C,,', 'D,,', 'E,,', 'F,,',
                  'G,,', 'A,,', 'B,,', 'C,', 'D,', 'E,', 'F,', 'G,', 'A,', 'B,', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'c',
                  'd', 'e', 'f', 'g', 'a', 'b', "c'", "d'", "e'", "f'", "g'", "a'", "b'", "c''", "d''", "e''", "f''",
                  "g''", "a''", "b''", "c'''"]
    # WICHTIG: Tonart tastaturzusammenstellung mit neuer funktion
    black_keys_b = ['_B,,,,', '_D,,,', '_E,,,', '_G,,,', '_A,,,', '_B,,,', '_D,,', '_E,,', '_G,,', '_A,,', '_B,,',
                    '_D,', '_E,', '_G,', '_A,', '_B,', '_D', '_E', '_G', '_A', '_B', '_d', '_e', '_g', '_a', '_b',
                    "_d'", "_e'", "_g'", "_a'", "_b'", "_d''", "_e''", "_g''", "_a''", "_b''"]
    # Tastaturaufbau = alle weiße Tasteb+ alle schwarze Tasten
    allkeys = white_keys + black_keys_b + ['z']

    log = open('log1.txt', 'w')
    log.write('')
    log.close()
    # path = 'sct\\'

    count = len(os.listdir(path))

    temp = i_a.get_data_from_image(count, path)
    whole_data = temp[0]  # 15313
    # print(temp[1])
    # measure_number_ties = temp[1]
    # measure_number_ties = []
    whole_not_left = ''
    whole_not_right = ''
    tied_note_with_voices = [[], []]
    for index, measure in enumerate(whole_data):
        measure_number_ties = []
        y = len(measure) // 40
        if y == 0:
            y = 1
        if not index == len(whole_data) - 1:

            for z in range(88):
                if np.sum(whole_data[index][-y:, z]) == y and np.sum(whole_data[index+1][:y, z]) == y:  # 1 Linke Hand
                    # measure_number_ties += [[index, z]]  # Hand, Taktnummer, Index
                    measure_number_ties += [allkeys[z] + ' ']
                    #print(whole_data[index][-y:, z] + whole_data[index+1][:y, z])
                    #print(np.sum(whole_data[index][-y:, z]) + np.sum(whole_data[index+1][:y, z]))
                if np.sum(whole_data[index][-y:, z]) == 2*y and np.sum(whole_data[index+1][:y, z]) == y * 2:  # 2 Rechte Hand
                    # measure_number_ties += [[index, z]]
                    measure_number_ties += [allkeys[z] + ' ']
                    #print(whole_data[index][-y:, z] + whole_data[index + 1][:y, z])
                    #print(np.sum(whole_data[index][-y:, z]) + np.sum(whole_data[index + 1][:y, z]))
        # print(measure)
        temp = d_a.analyze_pressed_keys(measure)
        # print(len(measure))
        # LEFT: Index 0, RIGHT: Index 1
        # print(index)
        # print(measure_number_ties)
        # if measure_number_ties == []: measure_number_ties = [[0, 0]]
        temp = c_m.abc_both_hands(temp[0], temp[1], len(measure), measure_number_ties, tied_note_with_voices)
        # temp = c_m.set_length2(temp[0], temp[1], len(measure))
        whole_not_left += temp[0]
        whole_not_right += temp[1]
        tied_note_with_voices = temp[2]
        # print(tied_note_with_voices)
    # print(measure_number_ties)
    f = open('abc_file.txt', 'w')
    #whole_not_right = whole_not_right.replace('_E', 'E')
    #whole_not_right = whole_not_right.replace('_A', 'A')
    #whole_not_right = whole_not_right.replace('_B', 'B')
    #whole_not_right = whole_not_right.replace('_D', 'D')

    #whole_not_left = whole_not_left.replace('_E', 'E')
    #whole_not_left = whole_not_left.replace('_A', 'A')
    #whole_not_left = whole_not_left.replace('_B', 'B')
    #whole_not_left = whole_not_left.replace('_D', 'D')
    f.write('L: 1/16 \nV:1 \nK: Ab \n' + whole_not_right + 'V:2 bass \n' + whole_not_left)
