from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
  return 'Hello, World!!'

formData = f"""
<form action="/results" method="POST">
  Realm
  <input type="text" name="realm">
  <br>
  Token 
  <input type="password" name="token">
  <br>
  RUM Token 
  <input type="password" name="rum">
  <br>
  Environment Name
  <input type="text" name="envName">
  <br>
  <input type="button" value="Initiate"/>
</form>
"""

@app.route('/entryForm')
def requiredData():
  return formData

@app.route('/results', methods=['POST'])
def formResults():
  realm = request.form.get("realm")
  token = request.form.get("token")
  rum = request.form.get("rum")
  envName = request.form.get("envName")
  return f'{realm}{token}{rum}{envName} now working'

if __name__ == '__main__':
  app.run()