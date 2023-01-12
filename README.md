***
# Fussball Tippspiel 4 friends
***
## Projektidee
Diese Anwendung soll es Nutzern ermöglichen, Tipps auf die Ergebnisse der Fußball-Weltmeisterschaft abzugeben und gegen Freunde zu tippen. Dabei ist kein Login möglich. Es kann lediglich der Vor- und Nachname sowie all die Resultattipps eingegeben werden. Anschliessend werden die Tipps des Nutzers mit dem effektiven Endstand des Spiels verglichen und es erfolgt eine Punktevergabe. In der Rangliste ist die Einsicht des Namens, der Gesamtpunkte jedes Spielers und der Wahrscheinlichkeit, dass der Spieler das Tippturnier gewinnt, dargestellt.
***
## Problemstellung
Die Tipps können lediglich am Ende des Turniers abgegeben werden, da die effektiven Endresultat der Spiele bereits zu Beginn eingetragen werden müssen. Die Anwendung wäre somit erweiterbar, indem die User die Resultat zu Beginn eines Turniers tippen und der Admin die Resultate nach jedem erfolgtem Spiel eintragen kann. Ein weiteres Problem ist, dass kein Login vorhanden ist, wodurch der Nutzer seine Eingaben nicht speichern oder anpassen kann. Zudem können Namen mehrfach verwendet werden, wodurch die Abgabe von mehreren Tippsrunden nicht verhindert werden kann.
***
## Workflow
![](venv/Bilder/Workflow_Diagramm.png)

* Eintragung von Name und  Tipps durch User
* Vergleich des getippten Resultat und dem effektiven Endresultat
* Automatische Punktevergabe 
* Aktualisierung der Rangliste
* Berechnung der Wahrscheinlichkeit, dass der Nutzer das Turnier am Ende gewinnen wird.
***
