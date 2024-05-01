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

# app.py

from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)

    # Homepage route
    @app.route('/')
    def home():
        return render_template('index.html')

    # Contact form route
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            # Process the contact form submission
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            
            # In a real application, you would typically send an email or store the message in a database
            return 'Your message has been sent!'

        return render_template('contact.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
