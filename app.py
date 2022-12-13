from flask import Flask, request, render_template
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry import trace
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()


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
  tracer = trace.get_tracer(__name__)
  with tracer.start_as_current_span("Something") as span:
    print("Ayush")
    return "Hello World!"


if __name__ == '__main__':
  app.run()
