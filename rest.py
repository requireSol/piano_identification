

class InvalidSustainError(Exception):
    """Exception if sustain is smaller than 0"""


class Rest:
    def __init__(self, sustain_sixteenth):

        if not isinstance(sustain_sixteenth, int) and 1 > sustain_sixteenth > 17:  # Eventuell ganze Note abfangen
            raise InvalidSustainError()
        else:
            self.sustain_in_sixteenth = sustain_sixteenth
            self.sustain_in_quarter = round(sustain_sixteenth // 4.0, 2) # vlt weg

        self.pause_visibility = True #Will be changed to 'x' if invisible

    def change_sustain(self, new_sustain_sixteenth):

        if not isinstance(new_sustain_sixteenth, int) and 1 > new_sustain_sixteenth > 17:  # Eventuell ganze Note abfangen
            raise InvalidSustainError()
        else:
            self.sustain_in_sixteenth = new_sustain_sixteenth
            self.sustain_in_quarter = round(new_sustain_sixteenth // 4.0, 2) # vlt weg