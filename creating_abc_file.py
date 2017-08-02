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
    # print(temp[1])
    # measure_number_ties = temp[1]
    # measure_number_ties = []
    whole_not_left = ''
    whole_not_right = ''
    for index, measure in enumerate(whole_data):
        measure_number_ties = []
        y = len(measure) // 40
        if y == 0:
            y = 1
        if not index == len(whole_data) - 1:

            for z in range(88):
                if np.sum(whole_data[index][-y:, z]) == y and np.sum(whole_data[index+1][:y, z]) == y:  # 1 Linke Hand
                    # measure_number_ties += [[index, z]]  # Hand, Taktnummer, Index
                    measure_number_ties += [z]
                    #print(whole_data[index][-y:, z] + whole_data[index+1][:y, z])
                    #print(np.sum(whole_data[index][-y:, z]) + np.sum(whole_data[index+1][:y, z]))
                if np.sum(whole_data[index][-y:, z]) == 2*y and np.sum(whole_data[index+1][:y, z]) == y * 2:  # 2 Rechte Hand
                    # measure_number_ties += [[index, z]]
                    measure_number_ties += [z]
                    #print(whole_data[index][-y:, z] + whole_data[index + 1][:y, z])
                    #print(np.sum(whole_data[index][-y:, z]) + np.sum(whole_data[index + 1][:y, z]))
        # print(measure)
        temp = d_a.analyze_pressed_keys(measure)
        print(len(measure))
        # LEFT: Index 0, RIGHT: Index 1
        # print(index)
        # print(measure_number_ties)
        # if measure_number_ties == []: measure_number_ties = [[0, 0]]
        temp = c_m.abc_both_hands(temp[0], temp[1], len(measure), measure_number_ties)
        # temp = c_m.set_length2(temp[0], temp[1], len(measure))
        whole_not_left += temp[0]
        whole_not_right += temp[1]
    # print(measure_number_ties)
    f = open('abc_file.txt', 'w')
    f.write('L: 1/16 \n' + 'V:1 \n' + whole_not_right + 'V:2 bass \n' + whole_not_left)
