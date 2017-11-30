from flask import Flask, request, redirect, render_template
import cgi

app=Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

def is_valid(entry, min, max):
    if len(entry)<min or len(entry)>max or entry=="" or (" ") in entry:
        return False
    else:
        return True

def valid_email(email,min,max):
    # check to see if the email is valid to username standards
    # then check to see if it contains only 1 "@" and "."
    if not is_valid(email,min,max):
        return False
    elif email.count("@") !=1 or email.count(".") != 1:
        return False
    else:
        return True 



@app.route("/signup", methods=['POST'])
def signup():

    #get user input
    username = request.form['username']
    password = request.form['password']
    verify_pw = request.form['verify_pw']
    email = request.form['email']

    error="/?"
    #check if username and password are valid, passwords match, and email valid
    if not is_valid(username,3,20):
        user_error = "Not a valid username"
        error += "user_error="+ user_error
    if not is_valid(password,3,20):
        pw_error = "Not a valid password"
        error += "&pw_error=" + pw_error
    if verify_pw != password or verify_pw=="":
        verify_error = "Passwords don't match"
        error += "&verify_error=" + verify_error
    if email:
        if not valid_email(email,3,100):
            email_error = "Not a valid email"
            error += "&email_error=" + email_error
        else:
            email_error=""
        
    
    #if error redirect to same page, otherwise direct to welcome page
    if len(error) >2:
        error += "&username="+username
        error +="&email="+email
        return redirect(error)
    else:
        return render_template('welcome.html', username=username)


    #check if password is empty


@app.route("/")
def index():
    #get error messages
    user_error = request.args.get("user_error")
    pw_error = request.args.get("pw_error")
    verify_error = request.args.get("verify_error")
    email_error = request.args.get("email_error")

    #get username and email
    username = request.args.get("username")
    email = request.args.get("email")

    return render_template('home.html', user_error=user_error,
        pw_error=pw_error, 
        verify_error=verify_error,
        email_error=email_error,
        username=username,
        email = email)
app.run()