from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def sub_data():
   print "Got Post Info"
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   return render_template('result.html', name=name, comment=comment, location=location, language=language)
@app.route('/result')
def go_back():
	return render_template('index.html')
	
app.run(debug=True)