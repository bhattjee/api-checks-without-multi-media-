from flask import Flask, render_template
import requests
import logging

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    # Fetch book data from the API
    try:
        response = requests.get('https://freetestapi.com/api/v1/books')
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        books = data
        logging.debug(f"Books data: {books}")
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        books = []
    except ValueError as e:
        logging.error(f"JSON decoding failed: {e}")
        books = []

    # Render the HTML template with the book data
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
