import correct_rhythm
import helper


class Voice:

    def __init__(self):
        self.notes_chords_rests = []
        self.length = 0

    def add(self, note_chord_rest_objects):

        if isinstance(note_chord_rest_objects, list):
            for single_object in note_chord_rest_objects:
                if helper.is_to_voice_addable_object(single_object):
                    self.notes_chords_rests.append(single_object)

                    self.length += single_object.sustain

        elif helper.is_to_voice_addable_object(note_chord_rest_objects):
            self.notes_chords_rests.append(note_chord_rest_objects)

            self.length += note_chord_rest_objects.sustain

        self.update_offsets()

    def check_for_valid_length(self):
        if self.length == 16:
            return True
        else:
            return False

    def change_sustains(self, new_sustains):
        if helper.has_same_lengthes(new_sustains, self.notes_chords_rests):

            for ind in list(range(0, len(new_sustains)))[::-1]:
                if new_sustains[ind] == 0: # Sonderregelung !!!!!!!! Wenn durch Rythmuskorrektur eine Note zur Länge Null wird, wird sie aus dem Takt entfernt
                    del self.notes_chords_rests[ind]
                else:
                    self.notes_chords_rests[ind].change_sustain(new_sustains[ind])

            self.update_offsets()

            self.update_length()

    def get_sustains(self):
        all_sustains = []

        for single_object in self.notes_chords_rests:
            all_sustains.append(single_object.sustain)

        return all_sustains

    def get_offsets(self):
        all_offsets = []

        for single_object in self.notes_chords_rests:
            all_offsets.append(single_object.offset)

        return all_offsets

    def get_types(self): #note/chord or rest
        all_is_rest = []

        for single_object in self.notes_chords_rests:
            all_is_rest.append(single_object.is_rest)

        return all_is_rest

    def get_tones_str(self):
        all_tones_str = []

        for single_object in self.notes_chords_rests:
            all_tones_str.append(single_object.str_format)

        return all_tones_str

    def improve_rhythm(self):

        all_sustains = self.get_sustains()

        all_is_rest = self.get_types()

        if self.check_for_valid_length():
            new_all_sustains = correct_rhythm.improve_valid_rhythm(all_sustains, all_is_rest)
        else:
            new_all_sustains = correct_rhythm.correct_invalid_rhythm(all_sustains, all_is_rest)

        self.change_sustains(new_all_sustains)

    def update_offsets(self):
        count = 0
        for single_object in self.notes_chords_rests:
            single_object.offset = count
            count += single_object.sustain

    def update_length(self):
        self.length = 0

        for single_object in self.notes_chords_rests:
            self.length += single_object.sustain


