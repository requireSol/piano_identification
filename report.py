import time


class Report:

    notifications = ''

    def __init__(self, score_object, time_needed):
        self.score_object = score_object
        self.timeneeded = time_needed

    def create(self, path='auswertung.txt'):

        stats = self.score_object.get_stats()

        report_str = """Auswertung - "%s" von "%s"
Infos:
Zeitstempel: %s
gebrauchte Zeit: %ss
**********************************
Hinweise: 
%s
**********************************
Statistiken:
Allgemein
Takte:   %dx
***********************************
Noten:   %dx
Akkorde: %dx
Pausen:  %dx
Gesamt:  %dx
***********************************
Tonlaengen
1/16: %dx
1/8:  %dx
3/16: %dx
1/4:  %dx
3/8:  %dx
1/2:  %dx
5/8:  %dx
3/4:  %dx
7/8:  %dx
1/1:  %dx
***********************************

        """ % (self.score_object.title, self.score_object.composer, time.strftime("%b %d %Y %H:%M:%S"), self.timeneeded,
               Report.notifications[:-1], stats[0], stats[1], stats[2], stats[3], stats[4], stats[5][1], stats[5][2],
               stats[5][3], stats[5][4], stats[5][6], stats[5][8], stats[5][10], stats[5][12],
               stats[5][14], stats[5][16])

        file = open(path, 'w')
        file.write(report_str)
        file.close()


