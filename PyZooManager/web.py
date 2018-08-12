from flask import Flask, render_template, redirect, url_for, request

animals = [
  {"type": "Bear", "count": 5},
  {"type": "Fox", "count": 1}
]

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def animals_page():
  if request.method == "POST":
    return redirect(url_for("animals_page"))
  return render_template("index.html", animals=animals)


if __name__ == "__main__":
  app.run(debug=True)
