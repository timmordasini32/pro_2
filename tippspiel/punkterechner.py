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
