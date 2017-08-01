# -*- coding: utf-8 -*-
import correct_rhythm as c_r


def new_version(measure, measure_length):

    cons_pause_threshold = 0.07
    cons_note_threshold = 0.01
    note = ((1, 0.01, 0.07),
            (2, 0.07, 0.13),
            (3, 0.13, 0.19),
            (4, 0.19, 0.26),
            (6, 0.26, 0.39),
            (8, 0.39, 0.52),
            (10, 0.52, 0.64),
            (12, 0.64, 0.77),
            (14, 0.77, 0.88),
            (16, 0.88, 1.00))

    pause = ((1, 0.07, 0.012),
             (2, 0.012, 0.18),
             (3, 0.18, 0.24),
             (4, 0.24, 0.31),
             (6, 0.31, 0.44),
             (8, 0.44, 0.57),
             (10, 0.57, 0.69),
             (12, 0.69, 0.82),
             (14, 0.82, 0.93),
             (16, 0.93, 1.00))
    log = open('log1.txt', 'a')
    for voice in measure:
        tones_of_voice = []
        note_values_of_voice = []
        for tone in voice:
            temp = (float(tone[1]) / float(measure_length))  # (Ton, Prozentwert)
            if temp > cons_pause_threshold and tone[0] == 'z':
                log.write('z: ' + str(temp) + '\n')
                for value, min_v, max_v in pause:
                    if min_v < temp <= max_v:
                        note_values_of_voice.append(value)
                        tones_of_voice.append(tone[0])

            elif temp > cons_note_threshold and not tone[0] == 'z':
                log.write(tone[0] + ': ' + str(temp) + '\n')
                for value, min_v, max_v in note:
                    if min_v < temp <= max_v:
                        note_values_of_voice.append(value)
                        tones_of_voice.append(tone[0])
        log.write(str(measure_length) + '---------------------voice-------------\n')

        if sum(note_values_of_voice) == 16:
            # print('YEAH' + str(note_values_of_voice) + str(tones_of_voice))
            note_values_of_voice = c_r.improve_valid_rhythm(note_values_of_voice, tones_of_voice)
            # print(str(sum(note_values_of_voice)) + ': ' + str(note_values_of_voice))

        else:
            # print('BUHH' + str(note_values_of_voice) + str(tones_of_voice))
            note_values_of_voice = c_r.correct_invalid_rhythm(note_values_of_voice, tones_of_voice)
            # print(str(sum(note_values_of_voice)) + ': ' + str(note_values_of_voice))

        yield note_values_of_voice, tones_of_voice

    log.write('---------------------measure-------------\n')
    log.close()


def abc(measure, measure_length):
    abc_notation_all_voices_list = []
    voices_generator = new_version(measure, measure_length)
    for voice in voices_generator:
        note_values_of_voice = voice[0]
        tones_of_voice = voice[1]

        abc_notation_one_voice = ''
        for i, combi in enumerate(note_values_of_voice):
            if not combi == 0 and not (combi == 16 and tones_of_voice[i] == 'z'):
                abc_notation_one_voice += tones_of_voice[i] + str(combi) + ' '
        if not abc_notation_one_voice == '':
            abc_notation_all_voices_list.append(abc_notation_one_voice)

    if len(abc_notation_all_voices_list) == 0:
        abc_notation_all_voices_list = ['z16 ']

    """for tie in tones_with_ties:
        if allkeys[tie] in abc_notation_all_voices_list[-1]:
            abc_notation_all_voices_list[-1] = abc_notation_all_voices_list[-1][:-1] + '- '"""

    abc_notation_all_voices = '& '
    abc_notation_all_voices = abc_notation_all_voices.join(abc_notation_all_voices_list)
    abc_notation_all_voices += '|\n'
    return abc_notation_all_voices


def abc_both_hands(left_measure, right_measure, length):
    left_hand_abc = abc(left_measure, length)
    right_hand_abc = abc(right_measure, length)

    return left_hand_abc, right_hand_abc
