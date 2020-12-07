'''auteur = elisa
date = 30 novembre 3 decembre 6 décembre
to do = partie graphique'''

import fonctionspendu

partie = 0
ScoreMax = 0

while fonctionspendu.fJouer()[1] == 'y' :
    if partie == 0 :
        ScoreMax = fonctionspendu.fJouer()[0]
        partie += 1
    else :
        if fonctionspendu.fJouer()[0] > ScoreMax :
            ScoreMax = fonctionspendu.fJouer()[0]
        else :
            ScoreMax = ScoreMax
    print('Score max : ', ScoreMax)
    print('partie finie')