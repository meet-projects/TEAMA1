from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
#from database_setup import Base Person <--- Import your tables here!!
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#engine = create_engine('sqlite:///crudlab.db')
#Base.metadata.bind = engine
#DBSession = sessionmaker(bind=engine)
#session = DBSession()


#YOUR WEB APP CODE GOES HERE
@app.route('/')
def gotofrontpage():
    return render_template('front_page.html')



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
		#age=request.form["year","month","day"]
		








if __name__ == '__main__':
    app.run(debug=True)
