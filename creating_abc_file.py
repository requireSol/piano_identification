# -*- coding: utf-8 -*-
import data_analyzer as d_a
import calculate_measure as c_m
import image_analyzer as i_a
import os


def creating_abc_notation():
    log = open('log1.txt', 'w')
    log.write('')
    log.close()
    path = 'sct2\\'

    count = len(os.listdir(path))
    whole_data = i_a.get_data_from_image(count)
    # whole_data = temp[0]  # 15313
    # measure_number_of_ties = temp[1]
    whole_not_left = ''
    whole_not_right = ''
    for index, measure in enumerate(whole_data):

        # print(measure)
        temp = d_a.analyze_pressed_keys(measure)
        print(len(measure))
        # LEFT: Index 0, RIGHT: Index 1
        temp = c_m.abc_both_hands(temp[0], temp[1], len(measure))

        # temp = c_m.create_abc_notation_of_both_hands(temp[0], temp[1], len(measure))
        whole_not_left += temp[0]
        whole_not_right += temp[1]

    f = open('abc_file.txt', 'w')
    f.write('L: 1/16 \n' + 'V:1 \n' + whole_not_right + 'V:2 bass \n' + whole_not_left)



