from flask import Flask
from flask import render_template
from flask import request

from tippspiel.datenbank import abspeichern, auslesen

app = Flask("todo")

@app.route("/")
def start():
    todos = auslesen()
    # todos.html = todos.replace("\n", "<br>")
    todo_liste = todos.split("\n")
    neue_liste = []
    for eintrag in todo_liste:
        aufgabe, deadline = eintrag.split(",")
        neue_liste.append([aufgabe, deadline])
        print(neue_liste)
    return render_template("indexTS.html", liste=neue_liste)

@app.route("/add", methods=["GET", "POST"])
def add_new_todo():
    if request.method == "GET":
        return render_template("todo_form.html")

    if request.method == "POST":
        name_spiel1_team1 = request.form['name_spiel1_team1']
        name_spiel1_team2 = request.form['name_spiel1_team2']
        print(f"Request Form name_spiel1_team1: {name_spiel1_team1}")
        print(f"Request Form name_spiel1_team2: {name_spiel1_team2}")
        abspeichern(name_spiel1_team1, name_spiel1_team2)
        return "hät funktioniert"



if __name__ == "__main__":
    app.run(debug=True, port=5001)


