# -*- coding: utf-8 -*-
import data_analyzer as d_a
import calculate_measure as c_m
import image_analyzer as i_a
import numpy as np
import os
import score
import part


def creating_abc_notation(path):
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

    count = len(os.listdir(path))

    temp = i_a.get_data_from_image(count, path)
    whole_data = temp[0]  # 15313
    score_object = score.Score()
    left_part_object = part.Part('bass')
    right_part_object = part.Part('treble')

    previous_measures = (None, None)

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

        measure_objects = c_m.abc_both_hands(temp[0], temp[1], len(measure), measure_number_ties, previous_measures)
        previous_measures = measure_objects

        left_part_object.add(measure_objects[0])

        right_part_object.add(measure_objects[1])

    score_object.add([right_part_object, left_part_object,])

    outputstr = score_object.convert_to_abc()
    f = open('abc_file.txt', 'w')

    f.write(outputstr)
