import helper


class Chord:
    abc_pitches = {'0': ',,,,', '1': ',,,', '2': ',,', '3': ',', '4': '', '5': '', '6': "'", '7': "''", '8': "'''"}
    abc_accidentals = {'+': '^', '-': '_', '=': '=', '': ''}
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

    def convert_to_abc(self):
        abc_format = '['
        for i in range(len(self.tones)):
            abc_format_single = self.abc_accidentals[self.accidentals[i]]
            if int(self.pitches[i]) < 5:
                abc_format_single += self.tones[i]
            else:
                abc_format_single += self.tones[i].lower()

            abc_format_single += self.abc_pitches[self.pitches[i]] + str(self.sustain)

            abc_format += abc_format_single

        abc_format += ']'
        # print(abc_format)
        return abc_format
