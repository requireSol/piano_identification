# -*- coding: utf-8 -*-
import correct_rhythm as c_r


def voices_generator(measure, measure_length, tied_tones):
    white_keys = ['A,,,,', 'B,,,,', 'C,,,', 'D,,,', 'E,,,', 'F,,,', 'G,,,', 'A,,,', 'B,,,', 'C,,', 'D,,', 'E,,', 'F,,',
                  'G,,', 'A,,', 'B,,', 'C,', 'D,', 'E,', 'F,', 'G,', 'A,', 'B,', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'c',
                  'd', 'e', 'f', 'g', 'a', 'b', "c'", "d'", "e'", "f'", "g'", "a'", "b'", "c''", "d''", "e''", "f''",
                  "g''", "a''", "b''", "c'''"]
    # WICHTIG: Tonart tastaturzusammenstellung mit neuer funktion
    black_keys_b = ['_B,,,,', '_D,,,', '_E,,,', '_G,,,', '_A,,,', '_B,,,', '_D,,', '_E,,', '_G,,', '_A,,', '_B,,',
                    '_D,', '_E,', '_G,', '_A,', '_B,', '_D', '_E', '_G', '_A', '_B', '_d', '_e', '_g', '_a', '_b',
                    "_d'", "_e'", "_g'", "_a'", "_b'", "_d''", "_e''", "_g''", "_a''", "_b''"]
    # Tastaturaufbau = alle weiße Tasteb+ alle schwarze Tasten
    allkeys = white_keys + black_keys_b + ['z']

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
            temp = (float(tone[1]) / float(measure_length))  # (Prozentwert)
            if temp > cons_pause_threshold and tone[0] == 'z':
                log.write('z: ' + str(temp) + '\n')
                for value, min_v, max_v in pause:
                    if min_v < temp <= max_v:
                        note_values_of_voice.append(value)
                        tones_of_voice.append(tone[0] + ' ')

            elif temp > cons_note_threshold and not tone[0] == 'z':
                log.write(tone[0] + ': ' + str(temp) + '\n')
                for value, min_v, max_v in note:
                    if min_v < temp <= max_v:
                        note_values_of_voice.append(value)
                        tones_of_voice.append(tone[0] + ' ')
        log.write(str(measure_length) + '---------------------voice-------------\n')

        if sum(note_values_of_voice) == 16:
            # print('YEAH' + str(note_values_of_voice) + str(tones_of_voice))
            note_values_of_voice = c_r.improve_valid_rhythm(note_values_of_voice, tones_of_voice)
            # print(str(sum(note_values_of_voice)) + ': ' + str(note_values_of_voice))

        else:
            # print('BUHH' + str(note_values_of_voice) + str(tones_of_voice))
            note_values_of_voice = c_r.correct_invalid_rhythm(note_values_of_voice, tones_of_voice)
            # print(str(sum(note_values_of_voice)) + ': ' + str(note_values_of_voice))

            #TODO merge tones to chords

        for tone in tied_tones:
            if allkeys[tone] + ' ' == tones_of_voice[-1]:
                pass
                tones_of_voice[-1] += '-'

        count = 0
        for index, value in enumerate(note_values_of_voice[:]):
            note_values_of_voice[index] = (value, count)
            count += value


        # print(note_values_of_voice)

        yield note_values_of_voice, tones_of_voice

    log.write('---------------------measure-------------\n')
    log.close()


def abc(measure, measure_length, tied_notes):
    abc_notation_all_voices_list = []
    # voices_generator(measure, measure_length, tied_notes)

    voices = list(voices_generator(measure, measure_length, tied_notes)) # enthält 4 stimmen
    voices_unique_elements = set([])
    for voice in voices: # Voice hat zwei Elemente: 0: Notenwerte, 1: Töne
        voices_unique_elements.update(set(voice[0]))

    # print(voices_unique_elements)

    same_elements_with_tie = []
    same_elements_without_tie = []
    for element in voices_unique_elements:
        temp_with_tie = []
        temp_without_tie = []
        for ind1, voice in enumerate(voices):
            if element in voice[0]:
                if not voice[1][voice[0].index(element)][0] == 'z':
                    if not voice[1][voice[0].index(element)][-1] == '-':
                        temp_without_tie.append((ind1, voice[0].index(element)))  # 0: voice_nr, 1: element_nr
                    if voice[1][voice[0].index(element)][-1] == '-':
                        temp_with_tie.append((ind1, voice[0].index(element)))  # 0: voice_nr, 1: element_nr

                            # print(temp)
        if len(temp_without_tie) > 1:
            same_elements_without_tie.append(temp_without_tie)
        if len(temp_with_tie) > 1:
            same_elements_with_tie.append(temp_with_tie)

    # print(same_elements)

    for chord in same_elements_without_tie:
        main_voice_index, main_index_to_be_changed = chord[0][0], chord[0][1]
        voices[main_voice_index][1][main_index_to_be_changed] = '[' + voices[main_voice_index][1][main_index_to_be_changed]
        for voice_index, index_to_be_changed in chord[1:]:
            voices[main_voice_index][1][main_index_to_be_changed] += voices[voice_index][1][index_to_be_changed]
            voices[voice_index][1][index_to_be_changed] = 'z '
        voices[main_voice_index][1][main_index_to_be_changed] += ']'

    for chord in same_elements_with_tie:
        main_voice_index, main_index_to_be_changed = chord[0][0], chord[0][1]
        voices[main_voice_index][1][main_index_to_be_changed] = '[' + voices[main_voice_index][1][main_index_to_be_changed]
        for voice_index, index_to_be_changed in chord[1:]:
            voices[main_voice_index][1][main_index_to_be_changed] += voices[voice_index][1][index_to_be_changed]
            voices[voice_index][1][index_to_be_changed] = 'z '
        voices[main_voice_index][1][main_index_to_be_changed] += ']-'

    print('JAAAA')
    print(voices)









    for voice in voices_generator(measure, measure_length, tied_notes):
        note_values_of_voice = voice[0]
        tones_of_voice = voice[1]

        abc_notation_one_voice = ''
        for i, combi in enumerate(note_values_of_voice):
            if not combi == 0 and not (combi == 16 and tones_of_voice[i] == 'z '):
                abc_notation_one_voice += tones_of_voice[i].replace(' ', str(combi)) + ' '
                # abc_notation_one_voice += tones_of_voice[i] + str(combi) + ' '
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


def abc_both_hands(left_measure, right_measure, length, tied_notes):
    left_hand_abc = abc(left_measure, length, tied_notes)
    right_hand_abc = abc(right_measure, length, tied_notes)

    return left_hand_abc, right_hand_abc
