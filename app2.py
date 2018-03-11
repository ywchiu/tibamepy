from flask import Flask,jsonify
from sklearn.externals import joblib
app=Flask(__name__)

@app.route("/<year>/")
def getSalary(year):
	clf = joblib.load('fit.pickle')
	predicted = clf.predict(int(year))
	return jsonify({'data' : predicted[0][0]})

if __name__=="__main__":
	app.run(port=9999)