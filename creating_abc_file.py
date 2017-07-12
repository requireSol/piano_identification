# -*- coding: utf-8 -*-
import data_analyzer as d_a
import calculate_measure2 as c_m
import image_analyzer as i_a


def creating_abc_notation():
    log = open('log.txt', 'w')
    log.write('')
    log.close()

    whole_data = i_a.get_data_from_image(12856)  # 15313
    whole_not_left = ''
    whole_not_right = ''
    for measure in whole_data:

        # print(measure)
        temp = d_a.analyze_pressed_keys(measure)
        # print(len(measure))
        # LEFT: Index 0, RIGHT: Index 1
        temp = c_m.abc_both_hands(temp[0], temp[1], len(measure))
        # temp = c_m.set_length2(temp[0], temp[1], len(measure))
        whole_not_left += temp[0]
        whole_not_right += temp[1]

    f = open('abc_file.txt', 'w')
    f.write('L: 1/16 \n' + 'V:1 \n' + whole_not_right + 'V:2 bass \n' + whole_not_left)
