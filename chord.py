import note


class InvalidNoteError(Exception):
    """Exception if given note does not match with possible notes"""


class InvalidNotesListError(Exception):
    """if given param isnt list"""


class InvalidSustainError(Exception):
    """Exception if sustain is smaller than 0"""


class Chord:

    def __init__(self, list_note_objects, sustain_sixteenth=4):
        self.tones = []
        self.pitches = []
        self.accidentals = []

        if not isinstance(sustain_sixteenth, int) and 1 > sustain_sixteenth > 17:
            raise InvalidSustainError()
        else:
            self.sustain_in_sixteenth = sustain_sixteenth
            self.sustain_in_quarter = round(sustain_sixteenth // 4.0, 2) # vlt weg

        if not isinstance(list_note_objects, list):
            raise InvalidNotesListError()
        else:
            for note_object in list_note_objects:

                if not isinstance(note_object, note.Note):
                    raise note.InvalidNoteObject()

                else:
                    self.tones.append(note_object.tone)

                    self.pitches.append(note_object.pitch)

                    self.accidentals.append(note_object.accidental)

    def change_sustain(self, new_sustain_sixteenth):

        if not isinstance(new_sustain_sixteenth, int) and 1 > new_sustain_sixteenth > 17:
            raise InvalidSustainError()
        else:
            self.sustain_in_sixteenth = new_sustain_sixteenth
            self.sustain_in_quarter = round(new_sustain_sixteenth // 4.0, 2) #vlt weg