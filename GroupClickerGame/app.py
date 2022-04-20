from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

    # Load current count
    f = open("count.txt", "r")
    count = (f.read())
    f.close()

    # Render HTML with count variable
    return render_template("index.html", count=count)

@app.route("/", methods=["POST"])
def getvalue():
    f = open("count.txt", "r")
    count = (f.read())
    count -= 1
    f = open("coount.txt","w")
    f.write(str(count))
    f.close

    return render_template("index.html", count=count)

if __name__ == "__main__":
    app.run()
