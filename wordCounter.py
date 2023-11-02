import re
#1. Text lesen, bei jedem Leerzeichen neuen Array Punkt erstellen

text = "Hallo, das hier ist ein Text. Ich will schauen, ob ich die Worte in diesem Text lesen und dann zählen kann."

wordArray = text.split()
finalWordArray = []
for i in range (0, len(wordArray)):
    finalWordArray.append(re.sub(r"[^a-zA-Z0-9 äöüÄÖÜ]", "", wordArray[i]))

# 2. Matrix erstellen, in der je die Zahl und dann das Wort steht. Bei jedem hinzufügen eines Wortes wird geschaut, ob dieses schon in der Matrix ist.
#  a) schon in der Matrix
#     Das Wort wird gefunden und die Zahl wird um 1 erhöht
#  b) noch nicht in der Matrix
#     Das Wort wird der Matrix hinzugefügt und die Zahl wird auf 1 gesetzt

