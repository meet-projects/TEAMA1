from flask import Flask , render_template , request , url_for , redirect
app = Flask(__name__)

import datetime
# SQLAlchemy stuff
from database_setup import Base,User,Photos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE
@app.route('/')
def gotofrontpage():
    return render_template('front_page.html')

@app.route('/register')
def gotoregister():
    return render_template('register.html')


@app.route('/signin')
def gotosignin():
    return render_template('signin.html')


@app.route('/main')
def mainpage():		
    	return render_template('main_page.html')

@app.route('/newuser')
def sumbit():
		
    	return render_template('main_page.html')


@app.route('/register', methods=['GET', 'POST'])
def registration():
	if request.method == 'GET':
		return render_template('register.html')
	else:
		firstname= request.form["firstname"]
		lastname= request.form["lastname"]
		email=request.form["email"]
		gender=request.form["gender"]
		status=request.form["stereotype"]
		age = datetime.datetime(int(request.form["year"]), int(request.form["month"]), int(request.form["day"]))
		newuser=User(first_name=firstname,last_name=lastname,gender=gender,email=email,status=status,birthdate=age)
		session.add(newuser)
		session.commit()
		return redirect(url_for("mainpage"))
		
		








if __name__ == '__main__':
    app.run(debug=True)
