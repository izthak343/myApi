# myApi
#run with docker

  docker build -t <name>.
  docker run -p 5000:5000 <name>
  
#run the api with python
  python app.py

#run the test with python
  python test_api.py
  python test_functions.py
  
#post to the api
  localhost:5000/myMultiply
  localhost:5000/mySum
