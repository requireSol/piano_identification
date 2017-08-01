# -*- coding: utf-8 -*-
import data_analyzer as d_a
import calculate_measure as c_m
import image_analyzer as i_a
import numpy as np
import os


def creating_abc_notation(path):
    log = open('log1.txt', 'w')
    log.write('')
    log.close()
    # path = 'sct\\'

    count = len(os.listdir(path))

    temp = i_a.get_data_from_image(count, path)
    whole_data = temp[0]  # 15313
    # measure_number_ties = temp[1]
    measure_number_ties = []
    whole_not_left = ''
    whole_not_right = ''
    for index, measure in enumerate(whole_data):
        measure_number_ties = []
        y = len(measure) // 40
        if not index == len(whole_data) - 1:
            for z in range(88):
                if np.sum(whole_data[index][-y:, z]) + np.sum(whole_data[index+1][:y, z]) == y * 2:  # 1 Linke Hand
                    measure_number_ties += [z]  # Hand, Taktnummer, Index
                if np.sum(whole_data[index][-y:, z]) + np.sum(whole_data[index+1][:y, z]) == y * 4:  # 2 Rechte Hand
                    measure_number_ties += [z]
        # print(measure)
        temp = d_a.analyze_pressed_keys(measure, measure_number_ties)
        print(len(measure))
        # LEFT: Index 0, RIGHT: Index 1



        temp = c_m.abc_both_hands(temp[0], temp[1], len(measure), measure_number_ties)
        # temp = c_m.set_length2(temp[0], temp[1], len(measure))
        whole_not_left += temp[0]
        whole_not_right += temp[1]

    f = open('abc_file.txt', 'w')
    f.write('L: 1/16 \n' + 'V:1 \n' + whole_not_right + 'V:2 bass \n' + whole_not_left)
