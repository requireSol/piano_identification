class Key:
    key = None
    keyboard = None

    def __init__(self, key):
        white = ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1', 'A1', 'B1', 'C2', 'D2', 'E2', 'F2',
                 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
                 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6', 'C7', 'D7', 'E7',
                 'F7', 'G7', 'A7', 'B7', 'C8']

        black_b = ['B0', 'D1', 'E1', 'G1', 'A1', 'B1', 'D2', 'E2', 'G2', 'A2', 'B2',
                   'D3', 'E3', 'G3', 'A3', 'B3', 'D4', 'E4', 'G4', 'A4', 'B4', 'D5', 'E5', 'G5', 'A5',
                   'B5', 'D6', 'E6', 'G6', 'A6', 'B6', 'D7', 'E7', 'G7', 'A7', 'B7']
        black_sharp = ['A0', 'C1', 'D1', 'F1', 'G1', 'A1', 'C2', 'D2', 'F2', 'G2', 'A2',
                       'C3', 'D3', 'F3', 'G3', 'A3', 'C4', 'D4', 'F4', 'G4', 'A4', 'C5', 'D5', 'F5', 'G5',
                       'A5', 'C6', 'D6', 'F6', 'G6', 'A6', 'C7', 'D7', 'F7', 'G7', 'A7']

        b_order = ['B', 'E', 'A', 'D', 'G']
        sharp_order = ['F', 'C', 'G', 'D', 'A']
        b_keys = ['C', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb']
        sharp_keys = ['C', 'G', 'D', 'A', 'E', 'H']

        Key.key = key

        if key in b_keys:  # B-Tonart
            b_count = b_keys.index(key)
            if b_count < 6:
                for ind, element in enumerate(white):
                    if element[0] in b_order[:b_count]:
                        white[ind] = element[0] + '=' + element[-1]
                for ind, element in enumerate(black_b):
                    if element[0] not in b_order[:b_count]:
                        black_b[ind] = element[0] + '-' + element[-1]

            else:
                for ind, element in enumerate(white):
                    if element[0] in b_order[:5]:
                        white[ind] = element[0] + '=' + element[-1]
                    if element[0] == 'B':
                        white[ind] = 'C' + '-' + element[-1]

            Key.keyboard = white + black_b + ['X']

        else: # #-Tonart
            sharp_count = sharp_keys.index(key)
            for ind, element in enumerate(white):
                if element[0] in sharp_order[:sharp_count]:
                    white[ind] = element[0] + '=' + element[-1]
            for ind, element in enumerate(black_sharp):
                if element[0] not in sharp_order[:sharp_count]:
                    black_sharp[ind] = element[0] + '+' + element[-1]

            Key.keyboard = white + black_sharp + ['X']
