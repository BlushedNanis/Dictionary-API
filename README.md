# Dictionary REST API (Flask)

REST API created using Flask. Any term that appears in the dictionary data (csv file) will have its definition returned by the API. A basic example of using the API is provided on the webpage, and if you make a request, you will receive a dictionary with the word and its description as keys.

### Example:

URL: [127.0.0.1:5000/api/v1/sun](http://127.0.0.1:5000/api/v1/sun)

Response: {
    "definition": "1. Any star, especially when seen as the centre of any single solar system.\n2. The particular star at the centre of our solar system, from which the Earth gets light and heat.\n",
    "word": "sun"
}
