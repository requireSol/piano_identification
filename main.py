import numpy as np
import thread
import data_analyzer as d_a
import calculate_measure as c_m
import image_analyzer as i_a
import recording as rec


c = raw_input('Modus: [1] = recording | [2] = creating abc-notation\n')
if c == '1':
    print('START')
    try:
        test = thread.start_new_thread(rec.record, (252,))    # time in seconds
    except:
        "Error: unable to start thread"

    c = raw_input("Press any key to stop the recording")
elif c == '2':
    # c = raw_input("Eingabe.")
    whole_data = i_a.get_data_from_image(15116)  # 15313
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
