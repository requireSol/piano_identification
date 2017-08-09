# -*- coding: utf-8 -*-


def without_pauses(diff_value, new_rhythm, value_3_notes, value_1_notes):
    if diff_value > 0:  # and len(value_3_notes + value_1_notes) > 0:
        for index in value_1_notes:
            new_rhythm[index] = 2
        for index in value_3_notes:
            new_rhythm[index] = 4

        diff_value -= len(value_3_notes + value_1_notes)

        if diff_value == 0:
            return new_rhythm

        if diff_value > 0:
            new_rhythm[0] += diff_value
            return new_rhythm

        if diff_value < 0:
            max_value = max(new_rhythm)
            index_of_max = new_rhythm.index(max_value)
            new_rhythm[index_of_max] += diff_value
            return new_rhythm

    elif diff_value < 0:
        if len(value_1_notes) % 2 == 1:
            new_rhythm[value_1_notes[0]] = 2
            diff_value -= 1

        for index in value_3_notes:
            new_rhythm[index] -= 1
            diff_value += 1
            if diff_value == 0:
                break

        if diff_value == 0:
            return new_rhythm

        if diff_value < 0:
            max_value = max(new_rhythm)
            index_of_max = new_rhythm.index(max_value)
            new_rhythm[index_of_max] += diff_value
            return new_rhythm


def filling_pauses(diff_value, pauses, new_rhythm, sum_pauses):
    pause_percent_values = []
    for pause_value in pauses:
        pause_percent_values.append(pause_value[0] // sum_pauses)

    dummy_percent = 2 / diff_value
    for i in range(diff_value // 2):
        index_of_max = pause_percent_values.index(max(pause_percent_values))
        pause_percent_values[index_of_max] -= dummy_percent
        new_rhythm[pauses[index_of_max][0]] += 2

    return new_rhythm


def correct_invalid_rhythm(old_rhythm, tones):

    new_rhythm = old_rhythm[:]
    voice_length = sum(old_rhythm)
    pauses = []
    sum_pauses = 0
    value_1_notes = []
    value_3_notes = []
    for index, is_rest in enumerate(tones):
        if is_rest:  # (Index of a pause | Length of a pause
            pauses.append((index, old_rhythm[index]))
            sum_pauses += old_rhythm[index]
            new_rhythm[index] = 0
        else:  # (Index of a tone (with odd length) | Length of a tone)
            if old_rhythm[index] == 1:
                value_1_notes.append(index)
            elif old_rhythm[index] == 3:
                value_3_notes.append(index)

    #Trivialcheck
    diff_value = 16 - voice_length

    if len(value_1_notes + value_3_notes) == diff_value:
        for index in value_1_notes:
            old_rhythm[index] = 2
        for index in value_3_notes:
            old_rhythm[index] = 4
        return old_rhythm

    diff_value = 16 - voice_length + sum_pauses

    if len(pauses) > 0:

        if diff_value == 0:
            return new_rhythm

        if diff_value < 0:  # Springe zum Verfahren, als ob ein Takt keine Pause hätte und zu lang wäre
            new_rhythm = without_pauses(diff_value, new_rhythm, value_3_notes, value_1_notes)

            return new_rhythm

        # decrease_odd_value_count = len(odd_note_values) - diff_value
        if diff_value > 0 and len(value_3_notes + value_1_notes) > 0:
            for index in value_1_notes:
                new_rhythm[index] = 2
            for index in value_3_notes:
                new_rhythm[index] = 4

            diff_value -= len(value_3_notes + value_1_notes)

            if diff_value == 0:
                return new_rhythm

            if diff_value > 0:  # Pausen wieder auffüllen
                new_rhythm = filling_pauses(diff_value, pauses, new_rhythm, sum_pauses)

                return new_rhythm

            if diff_value < 0:  # Springe zum Verfahren, als ob ein Takt keine pause hätte und zu lang wäre
                new_rhythm = without_pauses(diff_value, new_rhythm, value_3_notes, value_1_notes)

                return new_rhythm

        elif diff_value > 0 and len(value_3_notes + value_1_notes) == 0:
            new_rhythm = filling_pauses(diff_value, pauses, new_rhythm, sum_pauses)

            return new_rhythm
            # Pause wieder auffüllen
    elif len(pauses) == 0:
        new_rhythm = without_pauses(diff_value, new_rhythm, value_3_notes, value_1_notes)

        return new_rhythm


def improve_valid_rhythm(old_rhythm, tones):
    new_rhythm = old_rhythm[:]
    voice_length = sum(old_rhythm)
    pauses = []
    sum_pauses = 0
    value_1_notes = []
    value_3_notes = []
    for index, is_rest in enumerate(tones):
        if is_rest:  # (Index of a pause | Length of a pause
            pauses.append((index, old_rhythm[index]))
            sum_pauses += old_rhythm[index]
            new_rhythm[index] = 0
        elif not is_rest:  # (Index of a tone (with odd length) | Length of a tone)
            if old_rhythm[index] == 1:
                value_1_notes.append(index)
            elif old_rhythm[index] == 3:
                value_3_notes.append(index)

    if len(value_1_notes) == 0 and len(value_3_notes) == 0:
        return old_rhythm

    diff_value = 16 - voice_length + sum_pauses

    if len(pauses) == 0:
        if len(value_1_notes) < len(value_3_notes):
            for i in range(len(value_1_notes)):
                new_rhythm[value_1_notes[i]] = 2
                new_rhythm[value_3_notes[i]] = 2
        else:
            for i in range(len(value_3_notes)):
                new_rhythm[value_1_notes[i]] = 2
                new_rhythm[value_3_notes[i]] = 2
        return new_rhythm

    else:
        for index in value_3_notes + value_1_notes:
            new_rhythm[index] += 1
            diff_value -= 1
            if diff_value == 0:
                break

        if diff_value > 0:
            new_rhythm = filling_pauses(diff_value, pauses, new_rhythm, sum_pauses)
            return new_rhythm
        else:
            return new_rhythm
