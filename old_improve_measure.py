# -*- coding: utf-8 -*-
def merge_pause_and_note(valuesofline, tones):
    for index, value in enumerate(valuesofline[:]):
        if value % 2 == 1 and tones[index] == 'z':
            possible_values = []
            for ind, val in enumerate(valuesofline[:]):
                if val % 2 == 1 and not tones[ind] == 'z':
                    # 1. Value | 2. Index | 3. distance to pause
                    possible_values.append((val, ind, abs(index - ind)))
            if len(possible_values) > 0:
                merge_partner = possible_values[0]
                for i in range(1, len(possible_values)):
                    if possible_values[i][2] < merge_partner[2]:
                        merge_partner = possible_values[i]
                valuesofline[index] -= 1
                valuesofline[merge_partner[1]] += 1

    return valuesofline
