import helper
import chord
import rest
import note
import copy


class Measure:

    def __init__(self, prev_measure):
        self.voices = []
        self.previous_measure = prev_measure

    def add(self, voice_objects):
        if isinstance(voice_objects, list):
            for single_object in voice_objects:
                if helper.is_valid_voice_object(single_object):
                    self.voices.append(single_object)

        elif helper.is_valid_voice_object(voice_objects):
            self.voices.append(voice_objects)

        self.update_voice_index_of_notes()

    def get_voices(self):
        return self.voices

    def get_unique_offsets_with_sustains(self):

        unique_offsets_with_sustains = set([])
        for voice in self.voices:
            offsets = voice.get_offsets()
            sustains = voice.get_sustains()
            for i in range(len(offsets)):
                unique_offsets_with_sustains.update([(sustains[i], offsets[i])])
                print(unique_offsets_with_sustains)

        return unique_offsets_with_sustains

    def merge_voices_to_chords(self):
        unique_offsets_with_sustains = self.get_unique_offsets_with_sustains()
        # all_valid_chords = []
        print(unique_offsets_with_sustains)
        for sustain, offset in unique_offsets_with_sustains:
            possible_chord = []
            for ind_voice, voice1 in enumerate(self.voices):
                for ind_note, note1 in enumerate(voice1.notes_chords_rests):
                    if note1.sustain == sustain and note1.offset == offset and note1.tie == '' and isinstance(note1, note.Note) and not(ind_note == 0 and self.previous_measure.voices[ind_voice].notes_chords_rests[-1].tie == 'start'):
                        possible_chord.append(note1)
                        if len(possible_chord) == 1:
                            swap_index = (ind_voice, ind_note)
                        elif len(possible_chord) > 1:
                            voice1.notes_chords_rests[ind_note] = rest.Rest(sustain)
            if len(possible_chord) > 1:
                merged_chord = chord.Chord(possible_chord, sustain)
                self.voices[swap_index[0]].notes_chords_rests[swap_index[1]] = merged_chord

    def get_notes_with_ties_of_previous_measure(self):
        notes_with_ties_of_previous_measure = []
        if not self.previous_measure:
            return notes_with_ties_of_previous_measure
        else:
            for voice in self.previous_measure.voices:
                if voice.notes_chords_rests[-1] == 'start':
                    notes_with_ties_of_previous_measure.append(voice.notes_chords_rests[-1]) #Eventuell DeepCopy

            return notes_with_ties_of_previous_measure

    def get_first_note_str_format_of_voices(self):
        first_note_str_format_of_voices = []
        for voice in self.voices:
            first_note_str_format_of_voices.append(voice.notes_chords_rests[0].str_format)

        return first_note_str_format_of_voices

    def arrange_voices_for_ties(self):
        for j in range(len(self.voices)):
            notes_with_ties_of_previous_measure = self.get_notes_with_ties_of_previous_measure()
            first_note_str_format_of_voices = self.get_first_note_str_format_of_voices()
            for note_with_tie in notes_with_ties_of_previous_measure:
                cmp_voice_index = note_with_tie.voice_index
                if not note_with_tie.str_format == first_note_str_format_of_voices[cmp_voice_index]:
                    swap_index = 0
                    for i in range(len(first_note_str_format_of_voices)):
                        if note_with_tie.str_format == first_note_str_format_of_voices[i]:
                            swap_index = i
                temp = self.voices[swap_index]
                self.voices[swap_index] = self.voices[note_with_tie.voice_index]
                self.voices[note_with_tie.voice_index] = temp
                break
            self.update_voice_index_of_notes()

    def update_voice_index_of_notes(self):
        for ind, voice in enumerate(self.voices):
            for single_object in voice.notes_chords_rests:
                single_object.voice_index = ind
