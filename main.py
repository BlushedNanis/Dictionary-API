from flask import Flask, render_template
from pandas import read_csv

app = Flask(__name__)

df = read_csv("dictionary.csv")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def api(word):
    definition = df.loc[df["word"] == word.lower()]["definition"].squeeze()
    if type(definition) == str:
        dictionary_result = {"definition": definition, "word": word}
        return dictionary_result
    else:
        return "Please, provide a valid word."

if __name__ == "__main__":
    app.run(debug=True)