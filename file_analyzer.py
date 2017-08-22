import numpy as np
import helper


def get_data_from_file(path='output.txt'):
    file = open(path, 'r')

    if verify_file(path):

        measure_arrays = []
        is_barline_found = False
        measure = []

        for line in file:
            if len(line) >= 89:
                data_one_line = []

                for status in line[:88]:

                    data_one_line.append(int(status))

                if line[88] == '4':
                    measure.append(data_one_line)

                    if not is_barline_found:
                        if len(measure) > 10:
                            measure_arrays.append(np.asarray(measure))
                            measure = []
                            is_barline_found = True

                else:
                    measure.append(data_one_line)

                    is_barline_found = False

        measure_arrays.append(np.asarray(measure))
        file.close()

        return measure_arrays
    else:
        file.close()


def verify_file(path):
    file = open(path, 'r')
    is_valid_file = True
    for ind, line in enumerate(file):
        if len(line) >= 89:
            for i in range(88):
                if not (line[i] == '0' or line[i] == '1' or line[i] == '2'):
                    raise helper.InvalidFormatError('Invalid Format: Line: ' + str(ind) + ', Index: ' + str(i) + ', Character: ' + line[i])
            if not (line[88] == '3' or line[88] == '4'):
                raise helper.InvalidFormatError('Invalid Format: Line: ' + str(ind) + ', Index: ' + str(88) + ', Character: ' + line[88])

    file.close()
    return is_valid_file
