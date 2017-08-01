# -*- coding: utf-8 -*-
import creating_abc_file as c_n
import recording as rec
import time

path = 'sct2\\'
c = raw_input('Mode: [1] = recording | [2] = creating abc-notation\n')
if c == '1':
    print('START')
    rec.prepare(path)
    rec.record(224, path)    # time in seconds
    time.sleep(240)

    # c = raw_input("Press any key to stop the recording")
elif c == '2':

    c_n.creating_abc_notation(path)  # TODO über returnwert, hier zurückgeben

    """whole_data = i_a.get_data_from_image(12856)  # 15313
    whole_not_left = ''
    whole_not_right = ''
    # print(len(whole_data))
    for measure in whole_data:

        # print(len(measure))
        temp = d_a.analyze_pressed_keys(np.asarray(measure))
        # LEFT: Index 0, RIGHT: Index 1
        temp = c_m.set_length2(temp[0], temp[1], len(measure))
        whole_not_left += temp[0]
        whole_not_right += temp[1]

    f = open('abc_file.txt', 'w')
    f.write('L: 1/16 \n' + 'V:1 \n' + whole_not_right + 'V:2 bass \n' + whole_not_left)
"""