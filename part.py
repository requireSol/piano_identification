import helper


class Part:

    def __init__(self, clef='treble'):
        self.measures = []
        self.clef = clef

    def add(self, measure_objects):
        if isinstance(measure_objects, list):
            for single_object in measure_objects:
                if helper.is_valid_voice_object(single_object):
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





