import json
from flask import Flask,request,jsonify
from functions.myFunctions import multiply,sum

app = Flask(__name__)





def checkInput(jsonAll):
	#check if the valur of the parm  match the requirements
	if 'firstNum' not in jsonAll.keys() or 'secondNum' not in jsonAll.keys():
		return {'failed': True ,'massege' : 'mast pass firstNum and secondNum' , 'status': 500} 
	firstNum=jsonAll["firstNum"]
	secondNum=jsonAll["secondNum"]
	if ( (not isinstance(firstNum, list)) or (not isinstance(secondNum, list )) ):
		return {'failed': True ,'massege' : 'mast pass a list' , 'status': 500}

	if( firstNum == [] or secondNum == []):
		return {'failed': True ,'massege' : 'Ampty array is prohibited' , 'status': 500}
	for digit in firstNum:
		if not isinstance(digit, int):
			return {'failed': True ,'massege' : 'There is a non-digit character' , 'status': 500}
	for digit in secondNum:
		if not isinstance(digit, int):
			return {'failed': True ,'massege' : 'There is a non-digit character' , 'status': 500}

	return {'failed': False,'firstNum':firstNum,'secondNum':secondNum}

@app.route('/mySum',methods=['POST'])
def mySum():
	if request.method == 'POST':
		jsonAll=request.get_json()
		check = checkInput(jsonAll)
		if(check['failed']):
			return json.dumps({'FAILED': check['massege']}), check['status'], {'ContentType':'application/json'}
		firstNum=check["firstNum"]
		secondNum=check["secondNum"]
		ans = sum(firstNum,secondNum)
		return json.dumps({'success': ans}), 200, {'ContentType':'application/json'}

@app.route('/myMultiply',methods=['POST'])
def myMultiply():
	if request.method == 'POST':
		jsonAll=request.get_json()
		check = checkInput(jsonAll)
		if(check['failed']):
			return json.dumps({'FAILED': check['massege']}), check['status'], {'ContentType':'application/json'}
		firstNum=check["firstNum"]
		secondNum=check["secondNum"]

		ans = multiply(firstNum,secondNum)
		return json.dumps({'success': ans}), 200, {'ContentType':'application/json'}






		


if __name__ == '__main__':
    app.run( debug=True,host=('0.0.0.0'))


