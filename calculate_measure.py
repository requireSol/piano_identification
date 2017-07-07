import improve_measure as i_m


def set_length2(left_measure, right_measure, length):
    compare_lengths_keys = []
    compare_lengths_pause = []
    for i in range(1, 17):
        a = 1.0 / 16.0
        compare_lengths_keys.append([str(i), round(i * a - 0.00, 4), round((i - 1) * a - 0.00, 4)])
        compare_lengths_pause.append([str(i), round(i * a + 0.05, 4), round((i - 1) * a + 0.05, 4)])

    compare_lengths_keys[4][0] = '6'
    compare_lengths_keys[6][0] = '8'
    compare_lengths_keys[8][0] = '10'
    compare_lengths_keys[10][0] = '12'
    compare_lengths_keys[12][0] = '14'
    compare_lengths_keys[14][0] = '16'

    compare_lengths_pause[4][0] = '6'
    compare_lengths_pause[6][0] = '8'
    compare_lengths_pause[8][0] = '10'
    compare_lengths_pause[10][0] = '12'
    compare_lengths_pause[12][0] = '14'
    compare_lengths_pause[14][0] = '16'

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
        # print(3 ** len(valuesoflines))
        combination = combination_recursion(len(valuesoflines), valuesoflines, [], tones)
        combination = i_m.merge_pause_and_note(combination, tones)
        abc_notation = ''
        for i, combi in enumerate(combination):
            if not combi == 0 and not (combi == 16 and tones[i] == 'z'):
                abc_notation += tones[i] + str(combi) + ' '
        if not abc_notation == '':
            temp_notation.append(abc_notation)
    if len(temp_notation) == 0:
        temp_notation = ['z16 ']
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
        # print(3 ** len(valuesoflines))
        combination = combination_recursion(len(valuesoflines), valuesoflines, [], tones)
        combination = i_m.merge_pause_and_note(combination, tones)
        if not (sum(combination)) == 16:
            print('ERROR', combination, tones)
        abc_notation = ''
        for i, combi in enumerate(combination):
            if not combi == 0 and not (combi == 16 and tones[i] == 'z'):
                abc_notation += tones[i] + str(combi) + ' '
        if not abc_notation == '':
            temp_notation.append(abc_notation)
    if len(temp_notation) == 0:
        temp_notation = ['z16 ']
    right_abc = '& '
    right_abc = right_abc.join(temp_notation)
    right_abc += '|\n'

    return left_abc, right_abc


def measure_evaluation(way, tones):
    evaluation = 0

    if sum(way) == 16:
        evaluation += 100

    for index, element in enumerate(way):
        if (element == 1 or element == 3) and tones[index] == 'z':
            evaluation -= 1
        if tones[index] == 'z':
            evaluation -= element
        else:
            evaluation += element

    return evaluation


def combination_recursion(condition, values, new_valuelist, toneslist):
    """
    tones: [alle tones]
    new_valuelist: [lengthes]
    values: [all lengthes of tones]
    condition: start with len(values)
    """
    way1 = []
    way2 = []
    way3 = []

    if condition == 1:

        way1 += new_valuelist + [values[- condition]]

        if 1 <= values[- condition] <= 4:
            way2 += new_valuelist + [values[- condition] - 1]
        elif 6 <= values[- condition] <= 16:
            way2 += new_valuelist + [values[- condition] - 2]
        else:
            way2 += new_valuelist + [values[- condition]]
        if 1 <= values[- condition] <= 3:
            way3 += new_valuelist + [values[- condition] + 1]
        elif 4 <= values[- condition] <= 14:
            way3 += new_valuelist + [values[- condition] + 2]
        else:
            way3 += new_valuelist + [values[- condition]]

        evaluation_way1 = measure_evaluation(way1, toneslist)
        evaluation_way2 = measure_evaluation(way2, toneslist)
        evaluation_way3 = measure_evaluation(way3, toneslist)

        if evaluation_way1 >= evaluation_way2 and evaluation_way1 >= evaluation_way3:
            return way1
        elif evaluation_way2 >= evaluation_way1 and evaluation_way2 >= evaluation_way3:
            return way2
        elif evaluation_way3 >= evaluation_way1 and evaluation_way3 >= evaluation_way2:
            return way3

    else:

        way1 += new_valuelist + [values[- condition]]
        way1 = combination_recursion(condition - 1, values, way1, toneslist)
        evaluation_way1 = measure_evaluation(way1, toneslist)

        if 1 <= values[- condition] <= 4:
            way2 += new_valuelist + [values[- condition] - 1]
            way2 = combination_recursion(condition - 1, values, way2, toneslist)
            evaluation_way2 = measure_evaluation(way2, toneslist)

        elif 6 <= values[- condition] <= 16:
            way2 += new_valuelist + [values[- condition] - 2]
            way2 = combination_recursion(condition - 1, values, way2, toneslist)
            evaluation_way2 = measure_evaluation(way2, toneslist)

        else:
            evaluation_way2 = 0

        if 1 <= values[- condition] <= 3:
            way3 += new_valuelist + [values[- condition] + 1]
            way3 = combination_recursion(condition - 1, values, way3, toneslist)
            evaluation_way3 = measure_evaluation(way3, toneslist)

        elif 4 <= values[- condition] <= 14:
            way3 += new_valuelist + [values[- condition] + 2]
            way3 = combination_recursion(condition - 1, values, way3, toneslist)
            evaluation_way3 = measure_evaluation(way3, toneslist)

        else:
            evaluation_way3 = 0

        if evaluation_way1 >= evaluation_way2 and evaluation_way1 >= evaluation_way3:
            return way1
        elif evaluation_way2 >= evaluation_way1 and evaluation_way2 >= evaluation_way3:
            return way2
        elif evaluation_way3 >= evaluation_way1 and evaluation_way3 >= evaluation_way2:
            return way3
