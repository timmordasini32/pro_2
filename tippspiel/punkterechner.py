# Der Punkteberechner liest die Tipps des Spielers aus und vergleicht sie mit den effektiven Resultaten. Die Verteilung der Punkte kann dem untenstehenden Code entnommen werden.

def punkterechner(resultat_spiel1_team1, resultat_spiel1_team2, player1_spiel1_team1, player1_spiel1_team2):
    total_player1 = 0
# Deklarierung, welche Mannschaft das Spiel gewonnen hat oder ob es sich um ein Unentschieden handelt.
    if player1_spiel1_team1 != 'Null' and player1_spiel1_team2 != 'Null':
        if resultat_spiel1_team1 > resultat_spiel1_team2:
            resultat_winner = "team1"
        elif resultat_spiel1_team1 < resultat_spiel1_team2:
            resultat_winner = "team2"
        else:
            resultat_winner = "unentschieden"

        if player1_spiel1_team1 > player1_spiel1_team2:
            player1_winner = "team1"
        elif player1_spiel1_team1 < player1_spiel1_team2:
            player1_winner = "team2"
        else:
            player1_winner = "unentschieden"

# Wurde der richtige Sieger (oder Unentschieden) gewählt, erhält der Nutzer 5 Punkte.
        if resultat_winner == player1_winner:
            total_player1 += 5

# Wurde auf die richtige Tordifferenz getippt, erhält der Nutzer 3 Punkte.
        if resultat_spiel1_team1 - resultat_spiel1_team2 == player1_spiel1_team1 - player1_spiel1_team2:
            total_player1 += 3

# Wurde auf die richtige Anzahl Tore der Heim- oder Auswärtsmannschaft getippt, erhält der Nutzer einen Punkt.
        if player1_spiel1_team1 == resultat_spiel1_team1:
            total_player1 += 1
        if player1_spiel1_team2 == resultat_spiel1_team2:
            total_player1 += 1

        return total_player1
    else:
        return total_player1

