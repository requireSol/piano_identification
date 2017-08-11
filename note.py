import helper


class Note:
    abc_pitches = {'0': ',,,,', '1': ',,,', '2': ',,', '3': ',', '4': '', '5': '', '6': "'", '7': "''", '8': "'''"}
    abc_accidentals = {'+': '^', '-': '_', '=': '=', '': ''}
    abc_tie = {'start': '-', '': ''}
    valid_note_names = \
        ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1', 'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3',
         'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5',
         'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6', 'C7', 'D7', 'E7', 'F7', 'G7', 'A7', 'B7', 'C8', 'B-0',
         'C-1', 'D-1', 'E-1', 'F-1', 'G-1', 'A-1', 'B-1', 'C-2', 'D-2', 'E-2', 'F-2', 'G-2', 'A-2', 'B-2', 'C-3',
         'D-3', 'E-3', 'F-3', 'G-3', 'A-3', 'B-3', 'C-4', 'D-4', 'E-4', 'F-4', 'G-4', 'A-4', 'B-4', 'C-5', 'D-5',
         'E-5', 'F-5', 'G-5', 'A-5', 'B-5', 'C-6', 'D-6', 'E-6', 'F-6', 'G-6', 'A-6', 'B-6', 'C-7', 'D-7', 'E-7',
         'F-7', 'G-7', 'A-7', 'B-7', 'C-8', 'A+0', 'B+0', 'C+1', 'D+1', 'E+1', 'F+1', 'G+1', 'A+1', 'B+1', 'C+2',
         'D+2', 'E+2', 'F+2', 'G+2', 'A+2', 'B+2', 'C+3', 'D+3', 'E+3', 'F+3', 'G+3', 'A+3', 'B+3', 'C+4', 'D+4',
         'E+4', 'F+4', 'G+4', 'A+4', 'B+4', 'C+5', 'D+5', 'E+5', 'F+5', 'G+5', 'A+5', 'B+5', 'C+6', 'D+6', 'E+6',
         'F+6', 'G+6', 'A+6', 'B+6', 'C+7', 'D+7', 'E+7', 'F+7', 'G+7', 'A+7', 'B+7']

    valid_tie_options = ['start', '']

    is_rest = False

    def __init__(self, str_note, sustain=4, tie_option=''):

        if helper.is_valid_tie_option(tie_option):
            self.tie = tie_option

        if helper.is_valid_sustain(sustain):
            self.sustain = sustain

        if helper.is_valid_note_name(str_note):
            self.str_format = str_note

            self.tone = str_note[0]

            self.pitch = str_note[-1]
            if len(str_note) == 3:
                self.accidental = str_note[1]
            else:
                self.accidental = ''  # Will be changed to '=' if necessary

        self.offset = 0 # Will be filled in after adding to a measure

        self.voice_index = None #Will be set after adding the voice with this note to a measure

    def change_sustain(self, new_sustain):

        if helper.is_valid_sustain(new_sustain):
            self.sustain = new_sustain

    def convert_to_abc(self):

        abc_format = self.abc_accidentals[self.accidental]
        if int(self.pitch) < 5:
            abc_format += self.tone
        else:
            abc_format += self.tone.lower()

        abc_format += self.abc_pitches[self.pitch] + str(self.sustain) + self.abc_tie[self.tie]

        return abc_format

