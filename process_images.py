import os
import image_analyzer as i_a
import data_analyzer as d_a
import calculate_measure as c_m
import score
import part


def create_score_object(path):
    count = len(os.listdir(path))
    measure_arrays = i_a.get_data_from_images(count, path)

    score_object = score.Score()
    bass_part_object = part.Part('bass')
    treble_part_object = part.Part('treble')

    previous_measures = [None, None]  # 0: Left, 1: Right

    for index, measure in enumerate(measure_arrays):
        if index == len(measure_arrays) - 1:
            tied_notes = []
        else:
            tied_notes = d_a.analyze_for_ties(measure, measure_arrays[index+1])

        #TODO Tonart bestimmen und Tastatur dementsprechend zusammenbauen

        temp = d_a.analyze_pressed_keys(measure)
        bass_measure_part = temp[0]
        treble_measure_part = temp[0]

        temp = c_m.abc_both_hands(bass_measure_part, treble_measure_part, len(measure), tied_notes, previous_measures)
        bass_measure_object = temp[0]
        treble_measure_object = temp[1]

        bass_part_object.add(bass_measure_object)
        treble_part_object.add(treble_measure_object)

        previous_measures = [bass_measure_object, treble_measure_object]  # 0: Left, 1: Right

    score_object.add([treble_part_object, bass_part_object])

    return score_object
