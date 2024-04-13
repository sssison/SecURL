import flask
from flask import request, jsonify
from random import randint
from model import predict_maliciousness
from time import time
from lexical_generator import lexical_generator
from rf_scoretime import rf_predict_maliciousness, xgb_predict_maliciousness


app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Create some test data for our catalog in the form of a list of dictionaries.

"""books = [
    {
        "id": 1,
        "isbn":"9781593279509",
        "title":"Eloquent JavaScript, Third Edition",
        "subtitle":"A Modern Introduction to Programming",
        "author":"Marijn Haverbeke",
        "published":"2018-12-04T00:00:00.000Z",
        "publisher":"No Starch Press",
        "pages":472,
        "description":"JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
        "website":"http://eloquentjavascript.net/"
    },
    {
        "id": 2,
        "isbn":"9781491943533",
        "title":"Practical Modern JavaScript",
        "subtitle":"Dive into ES6 and the Future of JavaScript",
        "author":"Nicolás Bevacqua",
        "published":"2017-07-16T00:00:00.000Z",
        "publisher":"O'Reilly Media",
        "pages":334,
        "description":"To get the most out of modern JavaScript, you need learn the latest features of its parent specification, ECMAScript 6 (ES6). This book provides a highly practical look at ES6, without getting lost in the specification or its implementation details.",
        "website":"https://github.com/mjavascript/practical-modern-javascript"
    }
]
@app.route('/', methods=['GET'])
def home():
    return '''<h1>SecURL API Framework</h1>
                <p>A flask api implementation for SecURL.   </p>'''

@app.route('/api/v1/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)
            return jsonify(results)
        
@app.route("/api/v1/books",  methods = ['POST'])
def api_insert():
    book = request.get_json()
    books.append(book)
    return "Success: Book information has been added."

@app.route("/api/v1/books/<id>", methods=["DELETE"])
def api_delete(id):
    for book in books:
        if book['id'] == int(id):
            books.remove(book)
    return "Success: Book information has been deleted."""

@app.route('/', methods=['GET'])
def home():
    return '''<h1>SecURL API Framework</h1>
                <p>A flask api implementation for SecURL.   </p>'''

@app.route('/securl', methods=['GET'])
def check_url():
    """
    Analyzes the URL and checks whether it is malicious or not, based on the result of the trained classifiers
    """
    inp_url = "(example url)"
    is_secure = False
    
    if 'inp_url' in request.args:
        inp_url = request.args['inp_url']
    
    if 'is_secure' in request.args:
        is_secure = (request.args['is_secure']=='enabled')

    # check time and select the algorithm
    # TODO: replace the algorithms below with lexical-based and content-based detection
    # TEMPORARY: XGB for basic security (is_secure==False), RF for enhanced security (is_secure==True) 
    time_start = time()
    prediction = xgb_predict_maliciousness(inp_url,2) if is_secure else rf_predict_maliciousness(inp_url,2)
    
    # prediction = rf_predict_maliciousness(inp_url,2)
    time_end = time()
    random_score = randint(0,100)
    return dict(
        status=200,
        score=random_score,
        safety=(random_score>60),
        url=inp_url,
        time=(time_end-time_start),
        message=prediction
    )
    """
    Future reference:
    - for obtaining domain only:
        from urllib.parse import urlparse
        domain = urlparse('http://www.example.test.co.uk/foo/bar').netloc
        print(domain) //// outputs www.example.test.co.uk
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)