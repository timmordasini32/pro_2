# Gruppen

wm2022 = {
    'Gruppe A': ["Katar", "Ecuador", "Senegal", "Niederlande"],
    'Gruppe B': ["England", "Iran", "USA", "Wales"],
    'Gruppe C': ["Argentinien", "Saudi-Arabien", "Mexiko", "Polen"],
    'Gruppe D': ["Frankreich", "Australien", "Dänemark", "Tunesien"],
    'Gruppe E': ["Spanien", "Costa Rica", "Deutschland", "Japan"],
    'Gruppe F': ["Belgien", "Kanada", "Marokko", "Kroatien"],
    'Gruppe G': ["Brasilien", "Serbien", "Schweiz", "Kamerun"],
    'Gruppe H': ["Portugal", "Ghana", "Uruguay", "Südkorea"]
}


# Spielpaarungen 0,1 2,3 / 0,2 1,3 / 0,3 1,2
spiele_spieltag_1 = []
spiele_spieltag_2 = []
spiele_spieltag_3 = []

for key, value in wm2022.items():
    spiele_spieltag_1.append((value[0], value[1]))
    spiele_spieltag_1.append((value[2], value[3]))

for key, value in wm2022.items():
    spiele_spieltag_2.append((value[0], value[2]))
    spiele_spieltag_2.append((value[1], value[3]))

for key, value in wm2022.items():
    spiele_spieltag_3.append((value[0], value[3]))
    spiele_spieltag_3.append((value[1], value[2]))
