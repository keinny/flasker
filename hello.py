from flask import Flask,render_template


#create an instance
app=Flask(__name__)

#create a route decorater
@app.route("/")

#def index():
#    return "<h1> hello world !!!</h1>"

def index():
    first_name = "Kenneth"
    favourite_piza= ["pepperoni","cheese","fish","mushrooms"]
    return render_template("index.html",
                            first_name = first_name,
                            favourite_piza=favourite_piza)

#127.0.0.1:5000/user/john
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

#custom error pages

#invalid url

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500


if __name__=='__main__':

    app.debug=True
    app.run()