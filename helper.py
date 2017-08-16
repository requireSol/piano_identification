import note
import chord
import rest
import measure
import voice
import part


class InvalidNoteError(Exception):
    """Exception wenn es sich um keine gültige Note handelt"""


class InvalidSustainError(Exception):
    """Exception wenn es sich um keine gültige Ton/Akkord/Pausenlänge handelt"""


class InvalidTieOptionError(Exception):
    """Exception wenn es sich um keine gültige Übergebundenoption handelt"""


class UnexpectedObjectError(Exception):
    """Exception wenn es sich nicht um das erwartete Object handelt"""


class DifferentListLenghtesError(Exception):
    """Exception wenn zwei Listen nicht die gleiche Länge haben"""


def is_valid_sustain(sustain):
    if not isinstance(sustain, int):
        raise UnexpectedObjectError('Expected IntObject')

    if sustain not in [1, 2, 3, 4, 6, 8, 10, 12, 14, 16]:
        raise InvalidSustainError('Invalid Value')

    return True


def is_valid_note_name(note_str):
    if not isinstance(note_str, str):
        raise UnexpectedObjectError('Expected StrObject')

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

    if note_str not in valid_note_names:
        raise InvalidNoteError('Invalid Value')

    return True


def is_valid_note_object(single_object):
    if not isinstance(single_object, note.Note):
        raise UnexpectedObjectError('Expected NoteObject')

    return True


def is_to_voice_addable_object(single_object):
    if not (isinstance(single_object, note.Note) or
            isinstance(single_object, chord.Chord) or
            isinstance(single_object, rest.Rest)):
        raise UnexpectedObjectError('Expected NoteObject, RestObject or ChordObject')

    return True


def is_valid_tie_option(tie_option):
    if not isinstance(tie_option, str):
        raise UnexpectedObjectError('Expected StrObject')

    if tie_option not in ['start', '']:
        raise InvalidTieOptionError('Invalid Value')

    return True


def is_list(notes_list):
    if not isinstance(notes_list, list):
        raise UnexpectedObjectError('Expected ListObject')

    return True


def has_same_lengthes(object1, object2):
    if not len(object1) == len(object2):
        raise DifferentListLenghtesError('Excepted ListObject with same Length')

    return True


def is_valid_measure_object(single_object):
    if not isinstance(single_object, measure.Measure):
        raise UnexpectedObjectError('Expected MeasureObject')

    return True


def is_valid_voice_object(single_object):
    if not isinstance(single_object, voice.Voice):
        raise UnexpectedObjectError('Expected VoiceObject')

    return True


def is_valid_part_object(single_object):
    if not isinstance(single_object, part.Part):
        raise UnexpectedObjectError('Expected VoiceObject')

    return True
