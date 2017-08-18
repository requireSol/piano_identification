import os
import image_analyzer as i_a
import file_analyzer as f_a
import data_analyzer as d_a
import calculate_measure as c_m
import score
import part
import key


def create_score_object(path):
    count = len(os.listdir(path))

    i_a.convert_images_to_textfile(count, path)

    measure_arrays = f_a.get_data_from_file()
    #measure_arrays = i_a.get_data_from_images(count, path) # Import image_analyzer2 then

    d_a.search_for_incorrect_measures(measure_arrays)

    key1 = (d_a.get_key(measure_arrays))

    key.Key(key1)

    score_object = score.Score(key1)
    bass_part_object = part.Part('bass')
    treble_part_object = part.Part('treble')

    previous_measures = [None, None]  # 0: Left, 1: Right

    for index, measure in enumerate(measure_arrays):
        print(str(index) + ': ' + str(len(measure)))
        if index == len(measure_arrays) - 1:
            tied_notes = []
        else:
            tied_notes = d_a.analyze_for_ties(measure, measure_arrays[index+1])

        temp = d_a.analyze_pressed_keys(measure)
        bass_measure_part = temp[0]
        treble_measure_part = temp[1]

        temp = c_m.abc_both_hands(bass_measure_part, treble_measure_part, len(measure), tied_notes, previous_measures)
        bass_measure_object = temp[0]
        treble_measure_object = temp[1]

        bass_part_object.add(bass_measure_object)
        treble_part_object.add(treble_measure_object)

        previous_measures = [bass_measure_object, treble_measure_object]  # 0: Left, 1: Right

    score_object.add([treble_part_object, bass_part_object])

    return score_object
