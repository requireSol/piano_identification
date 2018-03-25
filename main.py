# -*- coding: utf-8 -*-
import recording as rec
import process_images as p_i
import report
import time

path = 'sct2\\'
c = input('Mode: [1] = recording | [2] = creating abc-notation from recorded images | [3] creating abc_notation from datafile\n')
if c == '1':
    length = input('Length in seconds: ')
    if length.isnumeric():
        rec.prepare(path)
        rec.record(length, path)    # time in seconds
    else:
        print('expected int')

elif c == '2' or c == '3':
    title = input("Enter the title: ")
    composer = input("Enter the composer: ")

    start_time = time.time()
    # In Process_Images auswählen, ob man Bilder einlesen möchte oder nicht.

    score_object = p_i.create_score_object(path, use_images=c == '2', title=title, composer=composer)

    outputstr = score_object.convert_to_abc()
    f = open('abc_file.txt', 'w')
    f.write(outputstr)
    f.close()

    end_time = str(round((time.time() - start_time), 3))
    report_object = report.Report(score_object, end_time)
    report_object.create()
