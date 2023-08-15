from flask import Flask, render_template, request
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/bincomphptest'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# code to question 1

class announced_pu_results(db.Model):
    __tablename__ = "announced_pu_results"
    result_id = db.Column(db.Integer, primary_key=True)
    polling_unit_uniqueid = db.Column(db.String)
    party_abbreviation = db.Column(db.String(4))
    party_score = db.Column(db.Integer)
    entered_by_user = db.Column(db.String)
    date_entered = db.Column(db.DateTime)
    user_ip_address = db.Column(db.String(50))
    
    def __init__(self, polling_unit_uniqueid, result_id, party_abbreviation, party_score ):
        self.polling_unit_uniqueid = polling_unit_uniqueid
        self.result_id = result_id
        self.party_abbreviation = party_abbreviation
        self.party_score = party_score
        
@app.route('/announced_pu_results/<int:result_id>')
def announced_pu(result_id):
    results = announced_pu_results.query.filter_by(polling_unit_uniqueid=result_id).all()
    return render_template('announce_pu_result.html', results=results)

# Code to question 2
class lgas(db.Model):
    __tablename__ = "lga"
    uniqueid = db.Column(db.Integer, primary_key=True, auto_increment=True)
    lga_id = db.Column(db.Integer)
    lga_name = db.Column(db.String(4))
    state_id = db.Column(db.Integer)
    lga_description = db.Column(db.Text)
    entered_by_user = db.Column(db.String)
    date_entered = db.Column(db.DateTime)
    user_ip_address = db.Column(db.String(50))
    
class polls(db.Model):
    __tablename__ = "polling_unit"
    uniqueid = db.Column(db.Integer, primary_key=True, auto_increment=True)
    polling_unit_id = db.Column(db.Integer)
    ward_id = db.Column(db.Integer)
    lga_id = db.Column(db.Integer)
    uniquewardid = db.Column(db.Integer)
    polling_unit_number = db.Column(db.String)
    polling_unit_name = db.Column(db.String)
    polling_unit_description = db.Column(db.Text)
    lat = db.Column(db.String)
    date_entered = db.Column(db.DateTime)
    user_ip_address = db.Column(db.String(50))
    
@app.route('/lga')
def all_lgas():
    results = lgas.query.all()
    print(results[0].lga_name)
    return render_template('lga.html', results=results)


@app.route('/lgad', methods=["POST"])
def all_lga():
    v = request.form.get("hello")
    print(v)
    results = polls.query.filter_by(lga_id=v).all()
    print(results)
    return announced_pu_results.query.filter_by(polling_unit_uniqueid=results[0].result_id).all()


# code to Question 3

class stored_res(db.Model):
    __tablename__ = "collect_result"
    party_name = db.Column(db.String)
    polling_unit_id = db.Column(db.Integer)
    party_score = db.Column(db.Integer)
    
@app.route('/store_results', methods = ['POST'])
def store_results():
    polling_unit_id = request.form.get('polling_unit_id')
    party_name = request.form.get('party_name')
    party_score = request.form.get('party_score')
    return "Result successfully stored!!"
 
 
 #first tst   
class announced_lga_results(db.Model):
    __tablename__ = "announced_lga_results"
    result_id = db.Column(db.Integer, primary_key=True)
    lga_name = db.Column(db.String(50))
    party_abbreviation = db.Column(db.String(4))
    party_score = db.Column(db.Integer)
    entered_by_user	= db.Column(db.String(50))
    date_entered = db.Column(db.DateTime)
    user_ip_address = db.Column(db.String(50))
    
    def __init__(self, result_id, party_abbreviation, party_score):
        self.result_id = result_id
        self.party_abbreviation = party_abbreviation
        self.party_score = party_score

@app.route('/announced_lga_results/<int:result_id>')
def announced_lga(result_id):
    results = announced_lga_results.query.filter_by(result_id=result_id).all()
    return render_template('announce_lga_result.html', results=results)
     

@app.route('/')

def home():
    return 'Welcome to Polling-Results!'
if __name__ == '__main__':
    app.run(debug=True)
