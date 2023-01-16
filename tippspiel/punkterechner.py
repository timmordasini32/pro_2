def punkte(resultat_spiel1_team1, resultat_spiel1_team2, player1_spiel1_team1, player1_spiel1_team2):
    total_player1 = 0
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

        if resultat_winner == player1_winner:
            total_player1 += 5

        if resultat_spiel1_team1 - resultat_spiel1_team2 == player1_spiel1_team1 - player1_spiel1_team2:
            total_player1 += 3

        if player1_spiel1_team1 == resultat_spiel1_team1:
            total_player1 += 1
        if player1_spiel1_team2 == resultat_spiel1_team2:
            total_player1 += 1

        return total_player1
    else:
        return total_player1

print(punkte(2,2,2,2))
print(punkte(2,3,4,5))
print(punkte(2,2,3,2))
print(punkte('','','',''))

