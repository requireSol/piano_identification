import numpy as np


def get_data_from_file(path='output.txt'):
    file = open(path, 'r')

    measure_arrays = []
    is_barline_found = False
    count = 0
    measure = []

    for line in file:
        data_one_line = []

        if line.find('3') > -1:
            index = line.find('3')
        else:
            index = line.find('4')

        for status in line[:index]:

            data_one_line.append(int(status))

        if line[index] == '4':
            measure.append(data_one_line)
            count += 1

            if not is_barline_found:
                if len(measure) > 10:
                    measure_arrays.append(np.asarray(measure))
                    measure = []
                    is_barline_found = True

        else:
            measure.append(data_one_line)
            count = 0
            is_barline_found = False

    measure_arrays.append(np.asarray(measure))

    file.close()

    return measure_arrays
