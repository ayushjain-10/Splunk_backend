from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def displayForm():
  return render_template('form.html')

@app.route('/results', methods=['GET', 'POST'])
def form_results():

    context = {
        'realm': request.args.get('realm'),
        'token': request.args.get('token'),
        'rum': request.args.get('rum'),
        'envName': request.args.get('envName'),
    }

    return render_template('scenarios.html', **context)
  
@app.route('/test', methods=['GET', 'POST']) 
def test(): 
 	return "Hello World!!!!!" 


if __name__ == '__main__':
  app.run(debug=True, port=3000)
