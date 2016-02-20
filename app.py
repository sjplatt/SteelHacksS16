from flask import Flask, render_template, request, redirect, url_for, abort, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';
app.config['id'] = 0
app.config['USERNAME'] = 'test'
app.config['PASSWORD'] = 'test'

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "at") as f:
        f.write(contents)

# import googlemaps

# def distance(firstLocation, secondLocation):
#     """Uses google maps API to return distance"""
#     gmaps = googlemaps.Client(key="AIzaSyBDIfU8m6p93dfOUEB8S1b_PHEQ3JRg-go")
#     matrix = gmaps.distance_matrix(firstLocation, secondLocation)
#     return matrix['rows'][0]['elements'][0]['duration']['text']

@app.route('/')
def home():
    return render_template('maps.html')

@app.route('/maps')
def maps():
    locations = ["ABC","PQR","Name"]
    return render_template('maps.html', locations)

if __name__ == '__main__':
    app.run(debug=True)