# -*- coding: utf-8 -*-
import correct_rhythm as c_r
import measure
import note
import rest
import voice


def voices_generator(measure1, measure_length, tied_tones):

    cons_pause_threshold = 0.07
    cons_note_threshold = 0.01
    notes = ((1, 0.01, 0.07),
             (2, 0.07, 0.13),
             (3, 0.13, 0.19),
             (4, 0.19, 0.26),
             (6, 0.26, 0.39),
             (8, 0.39, 0.52),
             (10, 0.52, 0.64),
             (12, 0.64, 0.77),
             (14, 0.77, 0.88),
             (16, 0.88, 1.00))
    rests = ((1, 0.07, 0.012),
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

    for voice1 in measure1:
        voice_object = voice.Voice()
        tones_of_voice = []
        note_values_of_voice = []
        for tone in voice1:
            temp = (float(tone[1]) / float(measure_length))  # (Prozentwert)
            if temp > cons_pause_threshold and tone[0] == 'z':
                log.write('z: ' + str(temp) + '\n')
                for value, min_v, max_v in rests:
                    if min_v < temp <= max_v:
                        rest_object = rest.Rest(value)
                        voice_object.add(rest_object)

                        note_values_of_voice.append(value)
                        tones_of_voice.append(tone[0] + '%beam')

            elif temp > cons_note_threshold and not tone[0] == 'z':
                log.write(tone[0] + ': ' + str(temp) + '\n')
                for value, min_v, max_v in notes:
                    if min_v < temp <= max_v:
                        note_object = note.Note(tone[0], value)
                        voice_object.add(note_object)

                        note_values_of_voice.append(value)
                        tones_of_voice.append(tone[0] + '%beam')
        log.write(str(measure_length) + '---------------------voice-------------\n')

        if sum(note_values_of_voice) == 16:
            # print('YEAH' + str(note_values_of_voice) + str(tones_of_voice))
            note_values_of_voice = c_r.improve_valid_rhythm(note_values_of_voice, tones_of_voice)
            # print(str(sum(note_values_of_voice)) + ': ' + str(note_values_of_voice))

        else:
            # print('BUHH' + str(note_values_of_voice) + str(tones_of_voice))
            note_values_of_voice = c_r.correct_invalid_rhythm(note_values_of_voice, tones_of_voice)
            # print(str(sum(note_values_of_voice)) + ': ' + str(note_values_of_voice))

        for tone in tied_tones:
            if tone == voice_object.notes_chords_rests[-1].str_format:
                voice_object.notes_chords_rests[-1].tie = 'start'

        voice_object.improve_rhythm()

        yield voice_object

    log.write('---------------------measure-------------\n')
    log.close()


def abc(measure1, measure_length, tied_notes, previous_measure):

    abc_notation_all_voices_list = []
    # voices_generator(measure, measure_length, tied_notes)
    new_tied_notes_with_voices = []  # 0: tied_note, 1: voice_nr

    voices = list(voices_generator(measure1, measure_length, tied_notes))  # enthält 4 stimmen

    measure_object = measure.Measure(previous_measure)

    measure_object.add(voices)

    measure_object.arrange_voices_for_ties()

    measure_object.merge_voices_to_chords()

    return measure_object


def abc_both_hands(left_measure, right_measure, length, tied_notes, previous_measures):

    left_measure_object = abc(left_measure, length, tied_notes, previous_measures[0])

    right_measure_object = abc(right_measure, length, tied_notes, previous_measures[1])

    return left_measure_object, right_measure_object
