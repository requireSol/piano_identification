import helper
import note
import chord
import rest


class Score:

    def __init__(self, key='C', composer='unknown', title='noname'):
        """Initialisiert das Note-Object mit den übergebenen Parametern"""
        self.composer = composer
        self.title = title
        self.parts = []
        self.key = key

    def add(self, part_objects):
        """Fügt zum Score-Object ein oder mehrere Part-Objects hinzu"""
        if isinstance(part_objects, list):
            for single_object in part_objects:
                if helper.is_valid_part_object(single_object):
                    self.parts.append(single_object)

        elif helper.is_valid_part_object(part_objects):
            self.parts.append(part_objects)

    def convert_to_abc(self):
        """Gibt das Score-Object als ABC-Notation zurück"""
        header = 'L:1/16\nK:' + self.key + '\nM:4/4\nC:' + self.composer + '\nT:' + self.title + '\n'
        body = ''
        score_instruction = '%%score {'
        for part in self.parts:
            temp = part.convert_to_abc()
            score_instruction += temp[1]
            for voice in temp[0]:
                body += voice + '\n'

        score_instruction = score_instruction[:-1] + ' }'
        header += score_instruction + '\n'

        return header + body

    def get_stats(self):
        measure_count = 0
        count_general = 0
        rests_count = 0
        chords_count = 0
        notes_count = 0
        sustain_stats_general = {1: 0, 2: 0, 3: 0, 4: 0, 6: 0, 8: 0, 10: 0, 12: 0, 14: 0, 16: 0}

        for part in self.parts:
            for measure in part.measures:
                measure_count += 1
                for voice in measure.voices:
                    for note_chord_rest_object in voice.notes_chords_rests:
                        count_general += 1
                        if isinstance(note_chord_rest_object, note.Note):
                            notes_count += 1
                            sustain_stats_general[note_chord_rest_object.sustain] += 1
                        elif isinstance(note_chord_rest_object, rest.Rest):
                            rests_count += 1
                        elif isinstance(note_chord_rest_object, chord.Chord):
                            chords_count += 1
                            sustain_stats_general[note_chord_rest_object.sustain] += 1

        return measure_count // len(self.parts), notes_count, chords_count, rests_count, count_general, sustain_stats_general
