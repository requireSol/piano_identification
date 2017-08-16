import helper


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
