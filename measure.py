import note
import chord
import rest


class DifferentListLenghtesError(Exception):
    """if Listlenghtes are different"""


class InvalidObject(Exception):
    """Other object was exspected"""


class Measure:

    def __init__(self):
        self.clef = 'treble'
        self.time_signature = '4/4'
        self.notes_chords_rests = []
        self.valid_length = False
        self.length = 0

    def add(self, note_chord_rest_objects):
        if isinstance(note_chord_rest_objects, list):
            for single_object in note_chord_rest_objects:
                if not (isinstance(single_object, note.Note) or isinstance(single_object, chord.Chord) or isinstance(single_object, rest.Rest)):
                    raise InvalidObject()
                else:
                    self.notes_chords_rests.append(single_object)

                    self.length += single_object.sustain_in_sixteenth
        elif not (isinstance(note_chord_rest_objects, note.Note) or
                  isinstance(note_chord_rest_objects, chord.Chord) or
                  isinstance(note_chord_rest_objects, rest.Rest)):
            raise InvalidObject()
        else:
            self.notes_chords_rests.append(note_chord_rest_objects)

            self.length += note_chord_rest_objects.sustain_in_sixteenth

    def check_for_valid_length(self):
        if self.length == 16:
            self.valid_length = True
        else:
            self.valid_length = False

    def change_sustains(self, new_sustains_sixteenth):
        if not len(new_sustains_sixteenth) == len(self.notes_chords_rests):
            raise DifferentListLenghtesError()

        for ind in list(range(0, len(new_sustains_sixteenth)))[::-1]:
            if not (isinstance(self.notes_chords_rests[ind], note.Note) or isinstance(self.notes_chords_rests[ind], chord.Chord) or isinstance(
                    self.notes_chords_rests[ind], rest.Rest)):
                raise InvalidObject()
            if new_sustains_sixteenth[ind] == 0: # Sonderregelung !!!!!!!! Wenn durch Rythmuskorrektur eine Note zur Länge Null wird, wird sie aus dem Takt entfernt
                del self.notes_chords_rests[ind]
                self.notes_chords_rests[ind].change_sustain(new_sustains_sixteenth[ind])



