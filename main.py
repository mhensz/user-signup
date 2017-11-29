from flask import Flask, request, redirect, render_template
import cgi

app=Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too



@app.route("/signup", methods=['POST'])
def signup():

    #get user input
    username = request.form['username']
    password = request.form['password']
    verify_pw = request.form['verify_pw']
    email = request.form['email']

    #check if username is empty
    if not username or not password or not verify_pw:
        user_error = "Field Cannot Be Blank"
        return redirect("/?field_error=" + user_error)

    #check if password is empty


@app.route("/")
def index():
    empty_error = request.args.get("field_error")
    return render_template('home.html', user_error=empty_error)
app.run()