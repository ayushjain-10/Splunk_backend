from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def displayForm():
  return render_template('form.html')

@app.route('/results', methods=['GET'])
def form_results():

    context = {
        'realm': request.args.get('realm'),
        'token': request.args.get('token'),
        'rum': request.args.get('rum'),
        'envName': request.args.get('envName'),
    }

    return render_template('scenarios.html', **context)

# create a route with hello world
@app.route('/frontend')
def hello_world():
  # redirect to button.html
  return render_template('button.html')




if __name__ == '__main__':
  app.run(debug=True, port=3000)
