from flask import Flask
from flask import render_template
from flask import request
from datenbank import to_csv
import pandas as pd   # Quelle *1*
from tippspiel2 import *
from punkterechner import *

app = Flask("Tippspiel")

@app.route("/readme")
def home():
    return render_template("readme.html")


#Quelle *2*
@app.route("/")
def start():
    df = pd.read_csv('database.csv')
    print(df)
    neue_liste = []
    sno = 1
    for index, row in df.iterrows():
        neue_liste.append([sno, row[0], row[1], row[2], row[3]])
        sno = sno + 1

    return render_template("indexTS.html", liste=neue_liste)


@app.route("/add", methods=["GET", "POST"])
def add_new_todo():
    if request.method == "GET":

        s_tag_1 = spiele_spieltag_1
        s_tag_2 = spiele_spieltag_2
        s_tag_3 = spiele_spieltag_3
        spiele_spieltage = [s_tag_1, s_tag_2, s_tag_3]

        return render_template("todo_form.html", spiele_spieltage=spiele_spieltage)

    if request.method == "POST":
        vorname = request.form['Vorname']
        nachname = request.form['Nachname']

        tag1_t1_tipps = request.form.getlist('tag1_t1')
        tag1_t2_tipps = request.form.getlist('tag1_t2')
        tag2_t1_tipps = request.form.getlist('tag2_t1')
        tag2_t2_tipps = request.form.getlist('tag2_t2')
        tag3_t1_tipps = request.form.getlist('tag3_t1')
        tag3_t2_tipps = request.form.getlist('tag3_t2')

        getippte_spiele = 0

        for tag1_t1_tipp, tag1_t2_tipp in zip(tag1_t1_tipps, tag1_t2_tipps):
            if tag1_t1_tipp != '' and tag1_t2_tipp != '':
                getippte_spiele = getippte_spiele + 1

        for tag2_t1_tipp, tag2_t2_tipp in zip(tag2_t1_tipps, tag2_t2_tipps):
            if tag2_t1_tipp != '' and tag2_t2_tipp != '':
                getippte_spiele = getippte_spiele + 1

        for tag3_t1_tipp, tag3_t2_tipp in zip(tag3_t1_tipps, tag3_t2_tipps):
            if tag3_t1_tipp != '' and tag3_t2_tipp != '':
                getippte_spiele = getippte_spiele + 1

        tag1_t1_tipps = ['Null' if x == '' else int(x) for x in tag1_t1_tipps]
        tag1_t2_tipps = ['Null' if x == '' else int(x) for x in tag1_t2_tipps]
        tag2_t1_tipps = ['Null' if x == '' else int(x) for x in tag2_t1_tipps]
        tag2_t2_tipps = ['Null' if x == '' else int(x) for x in tag2_t2_tipps]
        tag3_t1_tipps = ['Null' if x == '' else int(x) for x in tag3_t1_tipps]
        tag3_t2_tipps = ['Null' if x == '' else int(x) for x in tag3_t2_tipps]

        tag1_t1_resultat = [0, 0, 6, 1, 1, 0, 4, 0, 7, 1, 1, 0, 2, 1, 3, 0]
        tag1_t2_resultat = [2, 2, 2, 1, 2, 0, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0]
        tag2_t1_resultat = [1, 1, 0, 2, 2, 0, 2, 1, 1, 1, 0, 1, 1, 3, 2, 3]
        tag2_t2_resultat = [3, 1, 0, 0, 0, 2, 1, 0, 1, 0, 2, 4, 0, 3, 0, 2]
        tag3_t1_resultat = [0, 2, 3, 0, 2, 1, 0, 1, 1, 2, 0, 1, 0, 2, 1, 0]
        tag3_t2_resultat = [2, 1, 0, 1, 0, 2, 1, 0, 2, 4, 0, 2, 1, 3, 2, 2]

        punktetotal = 0

        for tag1_t1_resultat, tag1_t2_resultat, tag1_t1_tipp, tag1_t2_tipp in zip(tag1_t1_resultat, tag1_t2_resultat, tag1_t1_tipps, tag1_t2_tipps):
            punktetotal = punktetotal + punkterechner(tag1_t1_resultat, tag1_t2_resultat, tag1_t1_tipp, tag1_t2_tipp)

        for tag2_t1_resultat, tag2_t2_resultat, tag2_t1_tipp, tag2_t2_tipp in zip(tag2_t1_resultat, tag2_t2_resultat, tag2_t1_tipps, tag2_t2_tipps):
            punktetotal = punktetotal + punkterechner(tag2_t1_resultat, tag2_t2_resultat, tag2_t1_tipp, tag2_t2_tipp)

        for tag3_t1_resultat, tag3_t2_resultat, tag3_t1_tipp, tag3_t2_tipp in zip(tag3_t1_resultat, tag3_t2_resultat, tag3_t1_tipps, tag3_t2_tipps):
            punktetotal = punktetotal + punkterechner(tag3_t1_resultat, tag3_t2_resultat, tag3_t1_tipp, tag3_t2_tipp)

        print("Punktetotal:", punktetotal)

        punkteprognose = (63 * punktetotal) / getippte_spiele
        to_csv([str(vorname), str(nachname), punktetotal, round(punkteprognose, 2)])

        return "hät funktioniert"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
