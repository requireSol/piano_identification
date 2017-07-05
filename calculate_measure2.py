def set_length2(left_measure, right_measure, length):

    compare_lengths_keys = []
    compare_lengths_pause = []
    for i in range(1, 17):
        a = 1.0 / 16.0
        compare_lengths_keys.append([str(i), round(i * a + 0.00, 4), round((i - 1) * a + 0.00, 4)])
        compare_lengths_pause.append([str(i), round(i * a + 0.035, 4), round((i - 1) * a + 0.035, 4)])

    compare_lengths_keys[4][0] = '6'
    compare_lengths_keys[6][0] = '8'
    compare_lengths_keys[10][0] = '12'
    compare_lengths_keys[14][0] = '16'


    temp_notation = []
    for line in left_measure:
        tones = []
        valuesoflines = []
        for tone in line:
            temp = (float(tone[1]) / float(length))
            if tone[0] == 'z':
                for comp in compare_lengths_pause:
                    if comp[2] <= temp <= comp[1]:
                        valuesoflines.append(int(comp[0]))
                        tones.append(tone[0])
                        break
            else:
                for comp in compare_lengths_keys:
                    if comp[2] <= temp <= comp[1]:
                        valuesoflines.append(int(comp[0]))
                        tones.append(tone[0])
                        break

        combination = combination_recursion(len(valuesoflines), valuesoflines, [[], 0])
        abc_notation = ''
        for i, combi in enumerate(combination[0]):
            abc_notation += tones[i] + str(combi) + ' '
        temp_notation.append(abc_notation)

    left_abc = '& '
    left_abc = left_abc.join(temp_notation)
    left_abc += '|\n'

    temp_notation = []
    for line in right_measure:
        tones = []
        valuesoflines = []
        for tone in line:

            temp = (float(tone[1]) / float(length))
            if tone[0] == 'z':
                for comp in compare_lengths_pause:
                    if comp[2] <= temp <= comp[1]:
                        valuesoflines.append(int(comp[0]))
                        tones.append(tone[0])
                        break

            else:
                for comp in compare_lengths_keys:
                    if comp[2] <= temp <= comp[1]:
                        valuesoflines.append(int(comp[0]))
                        tones.append(tone[0])
                        break

        combination = combination_recursion(len(valuesoflines), valuesoflines, [[], 0])
        if not (sum(combination[0])) == 16:
            print('ERROR', combination, tones)
        abc_notation = ''
        for i, combi in enumerate(combination[0]):
            abc_notation += tones[i] + str(combi) + ' '
        temp_notation.append(abc_notation)

    right_abc = '& '
    right_abc = right_abc.join(temp_notation)
    right_abc += '|\n'

    return left_abc, right_abc


def combination_recursion(condition, values, valuelist):
    """
    valuelist: [[lengthes], [priorities]]
    values: [all lengthes of tones]
    condition: start with len(values)
    """
    way1 = [[], 0]
    way2 = [[], 0]

    if condition == 1:
        way1[0] += valuelist[0] + [values[- condition]]

        if values[- condition] == 1:
            way2[0] += valuelist[0] + [values[- condition]]
        else:
            way2[0] += valuelist[0] + [values[- condition] - 1]

        way1[1] += valuelist[1] + 3
        way2[1] += valuelist[1] + 2

        if not (sum(way1[0]) == 16) and not (sum(way2[0]) == 16):
            return way1
        elif not sum(way1[0]) == 16:
            return way2
        elif not sum(way2[0]) == 16:
            return way1
        elif way1[1] == way2[1]:
            return way1
        elif way1[1] < way2[1]:
            return way1
        else:
            return way2

    else:

        way1[0] += valuelist[0] + [values[- condition]]
        if values[- condition] == 1:
            way2[0] += valuelist[0] + [values[- condition]]
        else:
            way2[0] += valuelist[0] + [values[- condition] - 1]
        way1[1] += valuelist[1] + 3
        way2[1] += valuelist[1] + 2

        way1 = combination_recursion(condition - 1, values, way1)
        way2 = combination_recursion(condition - 1, values, way2)

        if not (sum(way1[0]) == 16) and not (sum(way2[0]) == 16):
            return way1
        elif not sum(way1[0]) == 16:
            return way2
        elif not sum(way2[0]) == 16:
            return way1
        elif way1[1] == way2[1]:
            return way1
        elif way1[1] < way2[1]:
            return way1
        else:
            return way2
