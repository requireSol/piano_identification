import helper


class Chord:

    is_rest = False

    def __init__(self, list_note_objects, sustain=4):
        self.str_format = []
        self.tones = []
        self.pitches = []
        self.accidentals = []

        if helper.is_valid_sustain(sustain):
            self.sustain = sustain

        if helper.is_list(list_note_objects):
            for note_object in list_note_objects:

                if helper.is_valid_note_object(note_object):
                    self.str_format.append(note_object.str_format)

                    self.tones.append(note_object.tone)

                    self.pitches.append(note_object.pitch)

                    self.accidentals.append(note_object.accidental)

        self.offset = 0

        self.tie = ''

    def change_sustain(self, new_sustain):

        if helper.is_valid_sustain(new_sustain):
            self.sustain = new_sustain
