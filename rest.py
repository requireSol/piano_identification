import helper


class InvalidSustainError(Exception):
    """Exception if sustain is smaller than 0"""


class Rest:

    is_rest = True

    def __init__(self, sustain=4):

        if helper.is_valid_sustain(sustain):
            self.sustain = sustain

        self.pause_visibility = True

        self.str_format = 'X'

        self.offset = 0

        self.tie = ''

    def change_sustain(self, new_sustain):

        if helper.is_valid_sustain(new_sustain):
            self.sustain = new_sustain
