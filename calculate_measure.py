import improve_measure as i_m


def frame_count_to_percentage(measure, measure_length):

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

    for voice in measure:
        tones_of_voice = []
        note_values_of_voice = []
        for tone in voice:
            temp = (float(tone[1]) / float(measure_length))
            if tone[0] == 'z':
                for comp in compare_lengths_pause:
                    if comp[2] <= temp <= comp[1]:
                        note_values_of_voice.append(int(comp[0]))
                        tones_of_voice.append(tone[0])
                        break
            else:
                for comp in compare_lengths_keys:
                    if comp[2] <= temp <= comp[1]:
                        note_values_of_voice.append(int(comp[0]))
                        tones_of_voice.append(tone[0])
                        break
        yield note_values_of_voice, tones_of_voice


def percentage_to_note_value(measure, measure_length):

    abc_notation_all_voices_list = []
    voices_generator = frame_count_to_percentage(measure, measure_length)
    for voice in voices_generator:
        note_values_of_voice = voice[0]
        tones_of_voice = voice[1]
        combination = combination_recursion(len(note_values_of_voice), note_values_of_voice, [], tones_of_voice)
        combination = i_m.merge_pause_and_note(combination, tones_of_voice)
        abc_notation_one_voice = ''
        for i, combi in enumerate(combination):
            if not combi == 0 and not (combi == 16 and tones_of_voice[i] == 'z'):
                abc_notation_one_voice += tones_of_voice[i] + str(combi) + ' '
        if not abc_notation_one_voice == '':
            abc_notation_all_voices_list.append(abc_notation_one_voice)
    if len(abc_notation_all_voices_list) == 0:
        abc_notation_all_voices_list = ['z16 ']
    abc_notation_all_voices = '& '
    abc_notation_all_voices = abc_notation_all_voices.join(abc_notation_all_voices_list)
    abc_notation_all_voices += '|\n'
    return abc_notation_all_voices


def create_abc_notation_of_both_hands(left_measure, right_measure, length):

    left_hand_abc = percentage_to_note_value(left_measure, length)
    right_hand_abc = percentage_to_note_value(right_measure, length)

    return left_hand_abc, right_hand_abc


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
