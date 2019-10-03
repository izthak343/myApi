import app
import json
import unittest


class Tester(unittest.TestCase):

	#test the api - Checks the variables 
	def setUp(self):
		self.app = app.app.test_client()

	def test_sum_api(self):
		resp =self.app.post( '/mySum',data=json.dumps({'firstNum': [1,1,1],'secondNum':[4,5,6]}),content_type='application/json')
		self.assertEqual(resp.status_code,200)

	def test_sum_with_ampty_array(self):
		resp =self.app.post( '/mySum',data=json.dumps({'firstNum': [],'secondNum':[]}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/mySum',data=json.dumps({'firstNum': [1,2],'secondNum':[]}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/mySum',data=json.dumps({'firstNum': [1,3],'secondNum':[]}),content_type='application/json')
		self.assertEqual(resp.status_code,500)

	def test_sum_with_non_digit(self):
		resp =self.app.post( '/mySum',data=json.dumps({'firstNum': [1,'a'],'secondNum':[1,2]}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/mySum',data=json.dumps({'firstNum': [1,2],'secondNum':[1,'a']}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/mySum',data=json.dumps({'firstNum': ['a'],'secondNum':['a']}),content_type='application/json')
		self.assertEqual(resp.status_code,500)

	def test_sum_with_non_list(self):
		resp =self.app.post( '/mySum',data=json.dumps({'firstNum': 1,'secondNum':5}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/mySum',data=json.dumps({'firstNum': [5,4],'secondNum':5}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/mySum',data=json.dumps({'firstNum': 1,'secondNum':[5,4]}),content_type='application/json')
		self.assertEqual(resp.status_code,500)


	def test_multiply_api(self):
		resp =self.app.post( '/myMultiply',data=json.dumps({'firstNum': [1,1,1],'secondNum':[4,5,6]}),content_type='application/json')
		self.assertEqual(resp.status_code,200)

	def test_multiply_with_ampty_array(self):
		resp =self.app.post( '/myMultiply',data=json.dumps({'firstNum': [],'secondNum':[]}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/myMultiply',data=json.dumps({'firstNum': [1,2],'secondNum':[]}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/myMultiply',data=json.dumps({'firstNum': [1,3],'secondNum':[]}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		
	def test_multiply_with_non_digit(self):
		resp =self.app.post( '/myMultiply',data=json.dumps({'firstNum': [1,'a'],'secondNum':[1,2]}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/myMultiply',data=json.dumps({'firstNum': [1,2],'secondNum':[1,'a']}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/myMultiply',data=json.dumps({'firstNum': ['a'],'secondNum':['a']}),content_type='application/json')
		self.assertEqual(resp.status_code,500)

	def test_multiply_with_non_list(self):
		resp =self.app.post( '/myMultiply',data=json.dumps({'firstNum': 1,'secondNum':5}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/myMultiply',data=json.dumps({'firstNum': [5,4],'secondNum':5}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
		resp =self.app.post( '/myMultiply',data=json.dumps({'firstNum': 1,'secondNum':[5,4]}),content_type='application/json')
		self.assertEqual(resp.status_code,500)
    


if __name__ == '__main__':
    unittest.main()




