# Cindy Zheng (partners: Julianna & Ruoshui )
# SoftDev
# K05 — Teamwork, but Better This Time: Printing a random student name from KREWES
# 2020-09-30

import random

KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', \
'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTAN\
CE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER\
', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDY', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHU\
I', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}


krew = list(KREWES.get('orpheus')) + (list(KREWES.get('rex')))+ (list(KREWES.get('endymion')))

name = random.randint(0, len(krew)-1)

print(krew[name])
