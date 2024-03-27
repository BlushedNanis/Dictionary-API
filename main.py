from flask import Flask, render_template
from pandas import read_csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def api(word):
    df = read_csv("dictionary.csv")
    definition = df.loc[df["word"] == word.lower()]["definition"].squeeze()
    print(type(definition))
    if type(definition) == str:
        return {"definition": definition,
                "word": word}
    else:
        return "Please, provide a valid word."

if __name__ == "__main__":
    app.run(debug=True)