from flask import Flask, render_template
from data import data

app = Flask(__name__)

data_instance = data()
data_instance.initialiseer()
data_instance.stemproces()

stembus = data_instance.stembus

@app.route('/')
def index():
    resultaten_lijst = stembus.verwerking_stemmen_lijstem()
    resultaten_kandidaten = stembus.verwerking_stemmen_kandidaten()                                                                             #moeilekheden gehad om dit te kunnen doen had een beetje hulp nodig van ai om dit te kunnen vertaan en doen 
                                                                                                                                                    
    partijen = [{'naam': partij, 'keuze': aantal, 'zetels': round(aantal/120)} for partij, aantal in resultaten_lijst.items()]                      #moeilijkheden gehad om de resultaten mee tegeven aan deze codes
    kandidaten = [{'naam': kandidaat, 'keuze': aantal} for kandidaat, aantal in resultaten_kandidaten.items()]                                 #formule nog aanpassen om de zetels te berekenen

    return render_template("index.html", partijen=partijen, kandidaten=kandidaten)

if __name__ == '__main__':
    app.run(debug=True)


#http://127.0.0.1:5000/ ::  om de resultaten te zien