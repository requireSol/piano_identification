class InvalidNoteError(Exception):
    """Exception if given note does not match with possible notes"""


class InvalidSustainError(Exception):
    """Exception if sustain is smaller than 0"""


class InvalidTieOptionError(Exception):
    """Exception"""


class InvalidNoteObject(Exception):
    """Exception for other classes"""


class Note:
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

    valid_tie_options = ['start', 'end', 'continue', '']

    def __init__(self, str_note, sustain_sixteenth=4, tie_option=''):

        if tie_option not in self.valid_tie_options:
            raise InvalidTieOptionError
        else:
            self.tie = tie_option

        if not isinstance(sustain_sixteenth, int) and 1 > sustain_sixteenth > 17:  #Eventuell ganze Note abfangen
            raise InvalidSustainError()
        else:
            self.sustain_in_sixteenth = sustain_sixteenth
            self.sustain_in_quarter = round(sustain_sixteenth // 4.0, 2) # vlt weg

        if not isinstance(str_note, str) and str_note not in self.valid_note_names:
            raise InvalidNoteError(str_note)

        else:
            self.tone = str_note[0]

            self.pitch = str_note[-1]
            if len(str_note) == 3:
                self.accidental = str_note[1]
            else:
                self.accidental = '='

        self.offset = 0 # Will be filled in after adding to a measure

    """def change_note(self, new_note):

        if not isinstance(new_note, str) and new_note not in self.valid_note_names:
            raise InvalidNoteError(new_note)

        else:
            self.tone = new_note[0]

            self.pitch = new_note[-1]
            if len(new_note) == 3:
                self.accidental = new_note[1]
            else:
                self.accidental = '='"""

    def change_sustain(self, new_sustain_sixteenth):

        if not isinstance(new_sustain_sixteenth, int) and 1 > new_sustain_sixteenth > 17:  # Eventuell ganze Note abfangen
            raise InvalidSustainError()
        else:
            self.sustain_in_sixteenth = new_sustain_sixteenth
            self.sustain_in_quarter = round(new_sustain_sixteenth // 4.0, 2) # vlt weg