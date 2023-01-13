# Gruppenphase

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

# Spielplan Paarungen 0,1 2,3 / 0,2 1,3 / 0,3 1,2
spiele_gruppe_a = []
spiele_gruppe_b = []
spiele_gruppe_c = []
spiele_gruppe_d = []
spiele_gruppe_e = []
spiele_gruppe_f = []
spiele_gruppe_g = []
spiele_gruppe_h = []
for gruppenname, teams in wm2022.items():

    for team in teams:
        spiele = []
        spiele.append(team)
        c = 0
        if gruppenname == "Gruppe A":
            spiele_gruppe_a.append((teams[c], team))
            c += 1

        if gruppenname == "Gruppe B":
            spiele_gruppe_b.append((teams[c], team))
            c += 1
        if gruppenname == "Gruppe C":
            spiele_gruppe_c.append((teams[c], team))
            c += 1
        if gruppenname == "Gruppe D":
            spiele_gruppe_d.append((teams[c], team))
            c += 1
        if gruppenname == "Gruppe E":
            spiele_gruppe_e.append((teams[c], team))
            c += 1
        if gruppenname == "Gruppe F":
            spiele_gruppe_f.append((teams[c], team))
            c += 1
        if gruppenname == "Gruppe G":
            spiele_gruppe_g.append((teams[c], team))
            c += 1
        if gruppenname == "Gruppe H":
            spiele_gruppe_h.append((teams[c], team))
            c += 1

del spiele_gruppe_a[0]
del spiele_gruppe_b[0]
del spiele_gruppe_c[0]
del spiele_gruppe_d[0]
del spiele_gruppe_e[0]
del spiele_gruppe_f[0]
del spiele_gruppe_g[0]
del spiele_gruppe_h[0]

print(spiele_gruppe_a)
print(spiele_gruppe_b)
print(spiele_gruppe_c)
print(spiele_gruppe_d)
print(spiele_gruppe_e)
print(spiele_gruppe_f)
print(spiele_gruppe_g)
print(spiele_gruppe_h)


