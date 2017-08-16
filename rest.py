import helper


class Rest:
    abc_rest_visibility = {True: 'z', False: 'x'}

    is_rest = True

    def __init__(self, sustain=4):

        if helper.is_valid_sustain(sustain):
            self.sustain = sustain

        self.visibility = True

        self.str_format = 'X'

        self.offset = 0

        self.tie = ''

    def change_sustain(self, new_sustain):
        """'Ändert die Pausenlänge"""

        if helper.is_valid_sustain(new_sustain):
            self.sustain = new_sustain

    def convert_to_abc(self):
        """Gibt das Rest-Object als ABC-Notation zurück"""

        abc_format = self.abc_rest_visibility[self.visibility]
        abc_format += str(self.sustain)

        return abc_format
