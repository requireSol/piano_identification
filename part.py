import helper


class Part:
    voice_id_counter = 0

    abc_clefs = {'treble': 'treble', 'bass' : 'bass'}

    def __init__(self, clef='treble'):
        self.measures = []
        self.clef = clef
        self.voices_id = [i for i in range(self.voice_id_counter, self.voice_id_counter+4)]
        Part.voice_id_counter += 4

    def add(self, measure_objects):
        if isinstance(measure_objects, list):
            for single_object in measure_objects:
                if helper.is_valid_measure_object(single_object):
                    self.measures.append(single_object)

        elif helper.is_valid_measure_object(measure_objects):
            self.measures.append(measure_objects)

    def check_voices_for_same_measure_count(self):
        if len(self.measures) > 1:
            cmp_measures_list = self.measures[0].measures
            for voice in self.measures[1:]:
                if not len(cmp_measures_list) == len(voice.measures):
                    return False

            return True

    def convert_to_abc(self):
        all_measures_of_voices = []
        score_instruction = ' ( '
        for ind, voice in enumerate(self.measures[0].convert_to_abc()):
            temp = 'V:' + str(self.voices_id[ind]) + ' ' + self.abc_clefs[self.clef] + '\n' + voice
            all_measures_of_voices.append(temp)
            score_instruction += str(self.voices_id[ind]) + ' '
        score_instruction += ') |'

        for measure in self.measures[1:]:
            voices_of_one_measure = measure.convert_to_abc()
            for i in range(len(voices_of_one_measure)):
                all_measures_of_voices[i] += voices_of_one_measure[i]

        return all_measures_of_voices, score_instruction



