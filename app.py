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

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

__END__

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colorful Page</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <h1>Welcome to Colorful Page</h1>
    </header>
    <main>
        <section class="section1">
            <h2>Section 1</h2>
            <p>This is the first section of the colorful page.</p>
        </section>
        <section class="section2">
            <h2>Section 2</h2>
            <p>This is the second section of the colorful page.</p>
        </section>
        <section class="section3">
            <h2>Section 3</h2>
            <p>This is the third section of the colorful page.</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Colorful Page. All rights reserved.</p>
    </footer>
</body>
</html>

<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }

    header {
        background-color: #3498db;
        color: #fff;
        padding: 20px;
        text-align: center;
    }

    main {
        padding: 20px;
    }

    section {
        margin-bottom: 20px;
        padding: 20px;
    }

    .section1 {
        background-color: #2ecc71;
        color: #fff;
    }

    .section2 {
        background-color: #f1c40f;
        color: #fff;
    }

    .section3 {
        background-color: #e74c3c;
        color: #fff;
    }

    footer {
        background-color: #34495e;
        color: #fff;
        text-align: center;
        padding: 10px;
    }
</style>


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
