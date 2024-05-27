from flask import Flask, render_template
from pandas import read_csv

# Set Flask instance
app = Flask(__name__)

# Load dictionary data into the data frame
df = read_csv("dictionary.csv")


# Set home route
@app.route("/")
def home():
    return render_template("home.html")


# Set word route
@app.route("/api/v1/<word>")
def api(word):
    definition = df.loc[df["word"] == word.lower()]["definition"].squeeze()
    if type(definition) == str:
        # Return definition if the word exists in dictionary data
        dictionary_result = {"definition": definition, "word": word}
        return dictionary_result
    else:
        return "Please, provide a valid word."


if __name__ == "__main__":
    app.run(debug=True)