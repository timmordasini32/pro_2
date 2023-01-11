# Gruppen

gruppeneinteilung = {1: ["Katar", "Ecuador", "Senegal", "Niederlande"],
                     2: ["England", "Iran", "USA", "Wales"],
                     ...}

gruppe1_teams = ["Katar", "Ecuador", "Senegal", "Niederlande"]
gruppe2_teams = ["England", "Iran", "USA", "Wales"]
gruppe3_teams = ["Argentinien", "Saudi-Arabien", "Mexiko", "Polen"]
gruppe4_teams = ["Frankreich", "Australien", "Dänemark", "Tunesien"]
gruppe5_teams = ["Spanien", "Costa Rica", "Deutschland", "Japan"]
gruppe6_teams = ["Belgien", "Kanada", "Marokko", "Kroatien"]
gruppe7_teams = ["Brasilien", "Serbien", "Schweiz", "Kamerun"]
gruppe8_teams = ["Portugal", "Ghana", "Uruguay", "Südkorea"]

spielplan = {1: [(0,1), (2,3)], 2: [(), ()]}

def get_spieltag(tag):
    for group_nr, countries in grupeneinteilung.items():
        einteilung = spielplan.get(tag)
        spiele = {}
        spiele.update({f"{countries[einteilung[0][0]]_countries[einteilung[0][1]]}": {'tip': None, 'true': None},
                       {f"{countries[einteilung[1][0]]_countries[einteilung[1][1]]}": {'tip': None, 'true': None}
                       )
    return spiele
    
1. SPielt
Dictionary  

# 1. Runde Gruppenphase
n_g1_s1_t1 = gruppe1_teams[0]
n_g1_s1_t2 = gruppe1_teams[1]
n_g1_s2_t1 = gruppe1_teams[2]
n_g1_s2_t2 = gruppe1_teams[3]
n_g2_s1_t1 = gruppe2_teams[0]
n_g2_s1_t2 = gruppe2_teams[1]
n_g2_s2_t1 = gruppe2_teams[2]
n_g2_s2_t2 = gruppe2_teams[3]
n_g3_s1_t1 = gruppe3_teams[0]
n_g3_s1_t2 = gruppe3_teams[1]
n_g3_s2_t1 = gruppe3_teams[2]
n_g3_s2_t2 = gruppe3_teams[3]
n_g4_s1_t1 = gruppe4_teams[0]
n_g4_s1_t2 = gruppe4_teams[1]
n_g4_s2_t1 = gruppe4_teams[2]
n_g4_s2_t2 = gruppe4_teams[3]
n_g5_s1_t1 = gruppe5_teams[0]
n_g5_s1_t2 = gruppe5_teams[1]
n_g5_s2_t1 = gruppe5_teams[2]
n_g5_s2_t2 = gruppe5_teams[3]
n_g6_s1_t1 = gruppe6_teams[0]
n_g6_s1_t2 = gruppe6_teams[1]
n_g6_s2_t1 = gruppe6_teams[2]
n_g6_s2_t2 = gruppe6_teams[3]
n_g7_s1_t1 = gruppe7_teams[0]
n_g7_s1_t2 = gruppe7_teams[1]
n_g7_s2_t1 = gruppe7_teams[2]
n_g7_s2_t2 = gruppe7_teams[3]
n_g8_s1_t1 = gruppe8_teams[0]
n_g8_s1_t2 = gruppe8_teams[1]
n_g8_s2_t1 = gruppe8_teams[2]
n_g8_s2_t2 = gruppe8_teams[3]

# 2. Runde Gruppenphase
n_g1_s3_t1 = gruppe1_teams[0]
n_g1_s3_t2 = gruppe1_teams[2]
n_g1_s4_t1 = gruppe1_teams[1]
n_g1_s4_t2 = gruppe1_teams[3]
n_g2_s3_t1 = gruppe2_teams[0]
n_g2_s3_t2 = gruppe2_teams[2]
n_g2_s4_t1 = gruppe2_teams[1]
n_g2_s4_t2 = gruppe2_teams[3]
n_g3_s3_t1 = gruppe3_teams[0]
n_g3_s3_t2 = gruppe3_teams[2]
n_g3_s4_t1 = gruppe3_teams[1]
n_g3_s4_t2 = gruppe3_teams[3]
n_g4_s3_t1 = gruppe4_teams[0]
n_g4_s3_t2 = gruppe4_teams[2]
n_g4_s4_t1 = gruppe4_teams[1]
n_g4_s4_t2 = gruppe4_teams[3]
n_g5_s3_t1 = gruppe5_teams[0]
n_g5_s3_t2 = gruppe5_teams[2]
n_g5_s4_t1 = gruppe5_teams[1]
n_g5_s4_t2 = gruppe5_teams[3]
n_g6_s3_t1 = gruppe6_teams[0]
n_g6_s3_t2 = gruppe6_teams[2]
n_g6_s4_t1 = gruppe6_teams[1]
n_g6_s4_t2 = gruppe6_teams[3]
n_g7_s3_t1 = gruppe7_teams[0]
n_g7_s3_t2 = gruppe7_teams[2]
n_g7_s4_t1 = gruppe7_teams[1]
n_g7_s4_t2 = gruppe7_teams[3]
n_g8_s3_t1 = gruppe8_teams[0]
n_g8_s3_t2 = gruppe8_teams[2]
n_g8_s4_t1 = gruppe8_teams[1]
n_g8_s4_t2 = gruppe8_teams[3]

# 3. Runde Gruppenphase
n_g1_s5_t1 = gruppe1_teams[0]
n_g1_s5_t2 = gruppe1_teams[3]
n_g1_s6_t1 = gruppe1_teams[1]
n_g1_s6_t2 = gruppe1_teams[2]
n_g2_s5_t1 = gruppe2_teams[0]
n_g2_s5_t2 = gruppe2_teams[3]
n_g2_s6_t1 = gruppe2_teams[1]
n_g2_s6_t2 = gruppe2_teams[2]
n_g3_s5_t1 = gruppe3_teams[0]
n_g3_s5_t2 = gruppe3_teams[3]
n_g3_s6_t1 = gruppe3_teams[1]
n_g3_s6_t2 = gruppe3_teams[2]
n_g4_s5_t1 = gruppe4_teams[0]
n_g4_s5_t2 = gruppe4_teams[3]
n_g4_s6_t1 = gruppe4_teams[1]
n_g4_s6_t2 = gruppe4_teams[2]
n_g5_s5_t1 = gruppe5_teams[0]
n_g5_s5_t2 = gruppe5_teams[3]
n_g5_s6_t1 = gruppe5_teams[1]
n_g5_s6_t2 = gruppe5_teams[2]
n_g6_s5_t1 = gruppe6_teams[0]
n_g6_s5_t2 = gruppe6_teams[3]
n_g6_s6_t1 = gruppe6_teams[1]
n_g6_s6_t2 = gruppe6_teams[2]
n_g7_s5_t1 = gruppe7_teams[0]
n_g7_s5_t2 = gruppe7_teams[3]
n_g7_s6_t1 = gruppe7_teams[1]
n_g7_s6_t2 = gruppe7_teams[2]
n_g8_s5_t1 = gruppe8_teams[0]
n_g8_s5_t2 = gruppe8_teams[3]
n_g8_s6_t1 = gruppe8_teams[1]
n_g8_s6_t2 = gruppe8_teams[2]





# 1. Runde Gruppenphase Resultateingabe Admin
r_g1_s1_t1 = 0
r_g1_s1_t2 = 1
r_g1_s2_t1 = 0
r_g1_s2_t2 = 2
r_g2_s1_t1 = 6
r_g2_s1_t2 = 2
r_g2_s2_t1 = 1
r_g2_s2_t2 = 1
r_g3_s1_t1 = 1
r_g3_s1_t2 = 2
r_g3_s2_t1 = 0
r_g3_s2_t2 = 0
r_g4_s1_t1 = 4
r_g4_s1_t2 = 1
r_g4_s2_t1 = 0
r_g4_s2_t2 = 0
r_g5_s1_t1 = 7
r_g5_s1_t2 = 0
r_g5_s2_t1 = 1
r_g5_s2_t2 = 2
r_g6_s1_t1 = 1
r_g6_s1_t2 = 0
r_g6_s2_t1 = 0
r_g6_s2_t2 = 0
r_g7_s1_t1 = 2
r_g7_s1_t2 = 0
r_g7_s2_t1 = 1
r_g7_s2_t2 = 0
r_g8_s1_t1 = 3
r_g8_s1_t2 = 2
r_g8_s2_t1 = 0
r_g8_s2_t2 = 0

# 2. Runde Gruppenphase Resultateingabe Admin
r_g1_s3_t1 = 1
r_g1_s3_t2 = 3
r_g1_s4_t1 = 1
r_g1_s4_t2 = 1
r_g2_s3_t1 = 2
r_g2_s3_t2 = 0
r_g2_s4_t1 = 0
r_g2_s4_t2 = 0
r_g3_s3_t1 = 2
r_g3_s3_t2 = 0
r_g3_s4_t1 = 0
r_g3_s4_t2 = 2
r_g4_s3_t1 = 2
r_g4_s3_t2 = 1
r_g4_s4_t1 = 1
r_g4_s4_t2 = 0
r_g5_s3_t1 = 1
r_g5_s3_t2 = 1
r_g5_s4_t1 = 1
r_g5_s4_t2 = 0
r_g6_s3_t1 = 0
r_g6_s3_t2 = 2
r_g6_s4_t1 = 1
r_g6_s4_t2 = 4
r_g7_s3_t1 = 1
r_g7_s3_t2 = 0
r_g7_s4_t1 = 3
r_g7_s4_t2 = 3
r_g8_s3_t1 = 2
r_g8_s3_t2 = 0
r_g8_s4_t1 = 3
r_g8_s4_t2 = 2

# 3. Runde Gruppenphase Resultateingabe Admin
r_g1_s5_t1 = 0
r_g1_s5_t2 = 2
r_g1_s6_t1 = 1
r_g1_s6_t2 = 2
r_g2_s5_t1 = 3
r_g2_s5_t2 = 0
r_g2_s6_t1 = 0
r_g2_s6_t2 = 1
r_g3_s5_t1 = 2
r_g3_s5_t2 = 0
r_g3_s6_t1 = 1
r_g3_s6_t2 = 2
r_g4_s5_t1 = 0
r_g4_s5_t2 = 1
r_g4_s6_t1 = 1
r_g4_s6_t2 = 0
r_g5_s5_t1 = 1
r_g5_s5_t2 = 2
r_g5_s6_t1 = 2
r_g5_s6_t2 = 4
r_g6_s5_t1 = 0
r_g6_s5_t2 = 0
r_g6_s6_t1 = 1
r_g6_s6_t2 = 2
r_g7_s5_t1 = 0
r_g7_s5_t2 = 1
r_g7_s6_t1 = 2
r_g7_s6_t2 = 3
r_g8_s5_t1 = 1
r_g8_s5_t2 = 2
r_g8_s6_t1 = 0
r_g8_s6_t2 = 2

def spiel():
    print(n_g1_s1_t1 + " vs. " + n_g1_s1_t2)

# Spieler
name_player1 = str(input("Bitte Name eingeben: "))
total_player1 = 0
print(name_player1 + " hat " + str(total_player1) + " Punkte.")

# Resultateingabe Spieler
    player1_spiel1_team1 = 0
    player1_spiel1_team2 = 0

# Punktesystem
def richtiger_gewinner(resultat_spiel1_team1, resultat_spiel1_team2, player1_spiel1_team1, player1_spiel1_team2):
    total_player1 = 0
    if resultat_spiel1_team1 > resultat_spiel1_team2:
        resultat_winner = "team1"
    elif player1_spiel1_team1 < player1_spiel1_team2:
        resultat_winner = "team2"
    else:
        resultat_winner = "unentschieden"

    if player1_spiel1_team1 > player1_spiel1_team2:
        player1_winner = "team1"
    elif player1_spiel1_team1 < player1_spiel1_team2:
        player1_winner = "team2"
    else:
        player1_winner = "unentschieden"
        
    if resultat_winner == player1_winner:
        total_player1 += 5
        
        
    return total_player1

def tordifferenz():
    if resultat_spiel1_team1 - resultat_spiel1_team2 == player1_spiel1_team1 - player1_spiel1_team2:
        total_player1 += 3

def anzahl_tore():
    if player1_spiel1_team1 == resultat_spiel1_team1:
        total_player1 += 1

    if player1_spiel1_team2 == resultat_spiel1_team2:
        total_player1 += 1


def punktevergabe():
    player1_punkte = 0
    total_player1 = richtiger_gewinner(...)
    player1_punkte += total_player1
    punkte = tordifferenz(..)
    player1_punkte += punkte
    
    
print(total_player1)