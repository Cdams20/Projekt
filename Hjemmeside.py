from flask import Flask, render_template, url_for, request, redirect, session

app = Flask(__name__)
app.secret_key = "hello"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/<user>")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

# When you run the browser, write slash login to get redirect to the site where you can type info.
# @app.route login.

# Make a key to decrypt the session data that is written. Because it is all encrypted on the server.
# app.secret_key ="write any word"

# GET is the most common way to getting or sending information to a website.
# Its and insecure way and is most commonly used.
# Post is the more secure way of doing that, and not anything can see the data info.

# Sessions is something you are gonna load in and use while the user is on the website.
# As soon as they leave it is gonna disappear.
# The sessions will collect the data of what the user was doing on that page.
# The other pages can acess the sessions from the previous pages. Because the data is stored.
# When the user leaves the page it is gonna disappear, but when going to it again it will load it
# And access/use it. They are stored on the server and not client side.
# The session we are doing will store data as a dict. If can have multiple sessions with different values
# Like Age, Condition, etc.
