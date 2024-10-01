from flask import Flask,jsonify,request
import ipl


app = Flask(__name__)

@app.route('/')
def index():
    return 'hello mf hi world'

@app.route('/api/teams/')
def teams():
    Teams = ipl.Teams_API()
    return jsonify(Teams)

@app.route('/api/teamvsteam')
def TeamVsTeam():
    Team1 = request.args.get('team1')
    Team2 = request.args.get('team2')
    response = ipl.Versus_API(Team1,Team2)
    print(response)
    return jsonify(response)
app.run(debug=True)