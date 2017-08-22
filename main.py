# -*- coding: utf-8 -*-
import recording as rec
import process_images as p_i
import report
import time

path = 'sct2\\'
c = input('Mode: [1] = recording | [2] = creating abc-notation\n')
if c == '1':
    print('START')
    rec.prepare(path)
    rec.record(266, path)    # time in seconds

elif c == '2':
    start_time = time.time()

    score_object = p_i.create_score_object(path)

    outputstr = score_object.convert_to_abc()
    f = open('abc_file.txt', 'w')
    f.write(outputstr)
    f.close()

    end_time = str(round((time.time() - start_time), 3))
    report_object = report.Report(score_object, end_time)
    report_object.create()


