from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/movie', methods=['POST'])
def movie():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	try:
		name = request.form['name']
		year = request.form['year']
		cursor.execute('INSERT INTO movie (name, releaseyear) VALUES (?,?)', 
			(name, year))
		connection.commit()
		message = 'Record successfully added'
	except:
		connection.rollback()
		message = 'Error in insert operation'
	finally:
		return render_template('result.html', message = message)
		connection.close()

@app.route('/movies', methods=['GET'])
def movies():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	tablename = 'foods'
	column_to_retrieve = 'name'
	print("Got to the search route")
	try:
		print("Got to the 'try' statement within the search route")
		# Different way b/c this is a 'GET' request
		# http://ampersandacademy.com/tutorials/flask-framework/flask-framework-form-values
		# http://stackoverflow.com/questions/10434599/how-to-get-data-recieved-in-flask-request
		value_to_retrieve = request.args.get('name')
		print ("The value to retrieve is: %s" % value_to_retrieve)
	 	# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html#querying-the-database---selecting-rows
	 	# https://docs.python.org/2/library/sqlite3.html
		t = (value_to_retrieve,)
		cursor.execute('SELECT * FROM foods WHERE name = ?', t)
		allrows = cursor.fetchall()
		#print(allrows)
		message = allrows
	except:
		message = 'this food was not found in the table'
	finally:
		return jsonify(message)
		connection.close()

app.run(debug=True)