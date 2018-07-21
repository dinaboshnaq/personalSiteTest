from flask import Flask, render_template
from random import randint

app=Flask(__name__)
@app.route('/intro')
def loadPage():
	return render_template('intro.html')


@app.route('/intro2')
def loadPage2():
	return render_template('intro2.html')


if __name__=='__main__':
	app.run(debug=True, port=1616)