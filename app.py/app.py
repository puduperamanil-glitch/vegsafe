
from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder=r"D:\html\vegsafe",
    static_folder=r"D:\html\vegsafe\static"
)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    print("Starting VegSafe...")
    app.run(debug=True)


