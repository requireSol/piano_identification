# -*- coding: utf-8 -*-
import recording as rec
import process_images as p_i

path = 'sct\\'
c = input('Mode: [1] = recording | [2] = creating abc-notation\n')
if c == '1':
    print('START')
    rec.prepare(path)
    rec.record(216, path)    # time in seconds

elif c == '2':

    score_object = p_i.create_score_object(path)

    outputstr = score_object.convert_to_abc()
    f = open('abc_file.txt', 'w')

    f.write(outputstr)
