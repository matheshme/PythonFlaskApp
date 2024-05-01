# # app.py

# from flask import Flask 
# from urllib.parse import quote 

# def create_app():
#     app = Flask(__name__)

#     @app.route('/')
#     def home():
#         return 'Final Testing'

#     return app
# if __name__ == '__main__':
#     app = create_app()
#     app.run(host='0.0.0.0', port=80, debug=True)

from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import quote 

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Final Testing'

    @app.route('/hello/<name>')
    def hello(name):
        return f'Hello, {name}!'

    @app.route('/search')
    def search():
        query = request.args.get('query')
        if query:
            encoded_query = quote(query)
            return redirect(url_for('search_results', query=encoded_query))
        return render_template('search.html')

    @app.route('/search_results/<query>')
    def search_results(query):
        decoded_query = quote(query)
        # Perform search using decoded_query
        # Dummy result for demonstration
        results = ['result1', 'result2', 'result3']
        return render_template('search_results.html', query=query, results=results)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
