from flask import Flask,jsonify
from sklearn.externals import joblib
app=Flask(__name__)

@app.route("/<year>")
def getSalary(year):
	clf = joblib.load('salary_prediction.pkl')
	predicted = clf.predict(int(year))
	return jsonify({'data' : predicted[0]})

if __name__=="__main__":
	app.run()